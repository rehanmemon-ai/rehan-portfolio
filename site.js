const root = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');

function setTheme(isDark) {
  root.classList.toggle('dark', isDark);
  root.classList.toggle('light', !isDark);
  const metaTheme = document.querySelector('meta[name="theme-color"]');
  if (metaTheme) metaTheme.setAttribute('content', isDark ? '#0d171c' : '#f7f7f2');
  const nextTheme = isDark ? 'light' : 'dark';
  if (themeIcon) themeIcon.textContent = nextTheme === 'light' ? 'Light' : 'Dark';
  if (themeToggle) themeToggle.setAttribute('aria-label', `Switch to ${nextTheme} theme`);
}
let savedTheme = null;
try { savedTheme = localStorage.getItem('theme'); } catch { /* Storage may be disabled. */ }
const isDark = savedTheme ? savedTheme === 'dark' : true;
setTheme(isDark);
if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    const nextDark = !root.classList.contains('dark');
    setTheme(nextDark);
    try { localStorage.setItem('theme', nextDark ? 'dark' : 'light'); } catch { /* Keep the in-page state. */ }
  });
}

function setMenuOpen(open) {
  if (!mobileMenu || !mobileMenuBtn) return;
  mobileMenu.hidden = !open;
  mobileMenuBtn.setAttribute('aria-expanded', String(open));
  mobileMenuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
}
if (mobileMenuBtn) {
  mobileMenuBtn.addEventListener('click', () => setMenuOpen(mobileMenu.hidden));
}
if (mobileMenu) {
  const siteHeader = document.querySelector('.site-header');
  mobileMenu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenuOpen(false)));
  if (siteHeader) {
    siteHeader.addEventListener('focusout', (event) => {
      if (!mobileMenu.hidden && (!event.relatedTarget || !siteHeader.contains(event.relatedTarget))) {
        setMenuOpen(false);
      }
    });
  }
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !mobileMenu.hidden) {
      setMenuOpen(false);
      if (mobileMenuBtn) mobileMenuBtn.focus();
    }
  });
}

const filterList = document.querySelector('[data-filter-list]');
if (filterList) {
  const cards = [...filterList.querySelectorAll('[data-filter-card]')];
  const controls = [...document.querySelectorAll('[data-filter-search],[data-filter-pillar],[data-filter-type],[data-filter-subject]')];
  const projectPillar = document.querySelector('[data-filter-pillar]');
  const pillarButtons = [...document.querySelectorAll('[data-filter-pillar-button]')];
  const pills = [...document.querySelectorAll('.filter-pill[data-filter-domain]')];
  const count = document.querySelector('[data-filter-count]');
  const noResults = document.querySelector('[data-no-results]');
  const nounSingular = filterList.dataset.nounSingular || 'project';
  const nounPlural = filterList.dataset.nounPlural || 'projects';
  let activeDomain = '';

  function syncPillarButtons() {
    pillarButtons.forEach((button) => {
      const target = button.dataset.filterPillarButton || '';
      const current = projectPillar?.value || '';
      const active = target === current;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    });
  }

  pillarButtons.forEach((button) => {
    button.addEventListener('click', () => {
      if (!projectPillar) return;
      projectPillar.value = button.dataset.filterPillarButton || '';
      updateFilters();
    });
  });

  if (projectPillar) {
    projectPillar.addEventListener('change', syncPillarButtons);
  }

  pills.forEach((pill) => {
    pill.addEventListener('click', () => {
      activeDomain = (pill.dataset.filterDomain || '').trim().toLowerCase();
      updateFilters();
    });
  });

  function updateFilters() {
    syncPillarButtons();
    pills.forEach((pill) => {
      const selected = (pill.dataset.filterDomain || '').trim().toLowerCase() === (activeDomain || 'all');
      pill.classList.toggle('active', selected);
      pill.setAttribute('aria-pressed', String(selected));
    });
    const value = (name) => document.querySelector(`[data-filter-${name}]`)?.value.trim().toLowerCase() || '';
    const query = value('search');
    let shown = 0;
    cards.forEach((card) => {
      const searchable = (card.dataset.search || card.textContent).toLowerCase();
      const cardDomain = (card.dataset.domain || '').toLowerCase();
      const matches = (!query || searchable.includes(query)) &&
        (!activeDomain || cardDomain === activeDomain || (activeDomain === 'all')) &&
        (!value('pillar') || card.dataset.pillar?.toLowerCase() === value('pillar')) &&
        (!value('type') || card.dataset.type?.toLowerCase() === value('type')) &&
        (!value('subject') || card.dataset.subject?.toLowerCase() === value('subject'));
      card.hidden = !matches;
      if (matches) shown += 1;
    });
    const sections = filterList.querySelectorAll('[data-pillar-section]');
    sections.forEach((sec) => {
      const secCards = sec.querySelectorAll('[data-filter-card]');
      if (secCards.length > 0) {
        const hasVisible = [...secCards].some((c) => !c.hidden);
        sec.hidden = !hasVisible;
      }
    });
    if (count) {
      const nextCount = `${shown} ${shown === 1 ? nounSingular : nounPlural} shown`;
      if (count.textContent.trim() !== nextCount) {
        count.textContent = nextCount;
      }
    }
    if (noResults) {
      noResults.hidden = shown !== 0;
    }
  }

  controls.forEach((control) => control.addEventListener(control.tagName === 'INPUT' ? 'input' : 'change', updateFilters));
  updateFilters();
}

// Diagram & Evidence Screenshot Lightbox Modal
const zoomableFigures = document.querySelectorAll('.diagram, .evidence-figure');
if (zoomableFigures.length > 0) {
  let modal = document.getElementById('diagramModal');
  if (!modal) {
    modal = document.createElement('div');
    modal.id = 'diagramModal';
    modal.className = 'modal-backdrop';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Image preview');
    modal.innerHTML = `
      <div class="modal-content">
        <button type="button" class="modal-close" aria-label="Close image preview">&times;</button>
        <img alt="" hidden>
        <p class="modal-caption"></p>
      </div>
    `;
    document.body.appendChild(modal);

    const closeBtn = modal.querySelector('.modal-close');
    const modalImg = modal.querySelector('img');
    const modalCaption = modal.querySelector('.modal-caption');
    let triggerElement = null;
    const priorInertStates = new Map();
    let priorBodyOverflow = null;

    function setBackgroundInert(isInert) {
      Array.from(document.body.children).forEach((el) => {
        if (el !== modal) {
          if (isInert) {
            priorInertStates.set(el, {
              ariaHidden: el.getAttribute('aria-hidden'),
              inert: 'inert' in el ? el.inert : undefined
            });
            el.setAttribute('aria-hidden', 'true');
            if ('inert' in el) el.inert = true;
          } else {
            const prior = priorInertStates.get(el);
            if (prior) {
              if (prior.ariaHidden !== null) {
                el.setAttribute('aria-hidden', prior.ariaHidden);
              } else {
                el.removeAttribute('aria-hidden');
              }
              if ('inert' in el && prior.inert !== undefined) {
                el.inert = prior.inert;
              }
            } else {
              el.removeAttribute('aria-hidden');
              if ('inert' in el) el.inert = false;
            }
          }
        }
      });
      if (!isInert) {
        priorInertStates.clear();
      }
    }

    function closeModal() {
      modal.classList.remove('open');
      if (priorBodyOverflow !== null) {
        document.body.style.overflow = priorBodyOverflow;
        priorBodyOverflow = null;
      } else {
        document.body.style.overflow = '';
      }
      setBackgroundInert(false);
      modalImg.removeAttribute('src');
      modalImg.alt = '';
      modalImg.hidden = true;
      modalCaption.textContent = '';
      if (triggerElement) {
        triggerElement.focus();
        triggerElement = null;
      }
    }

    const FOCUSABLE_SELECTOR = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';

    modal.addEventListener('keydown', (e) => {
      if (e.key === 'Tab') {
        const focusables = Array.from(modal.querySelectorAll(FOCUSABLE_SELECTOR))
          .filter((el) => !el.hasAttribute('disabled') && el.offsetParent !== null);
        if (focusables.length === 0) {
          e.preventDefault();
          return;
        }
        const first = focusables[0];
        const last = focusables[focusables.length - 1];
        if (e.shiftKey) {
          if (document.activeElement === first || !modal.contains(document.activeElement)) {
            e.preventDefault();
            last.focus();
          }
        } else {
          if (document.activeElement === last || !modal.contains(document.activeElement)) {
            e.preventDefault();
            first.focus();
          }
        }
      }
    });

    closeBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('open')) {
        closeModal();
      }
    });

    zoomableFigures.forEach((fig) => {
      const trigger = fig.querySelector('.image-zoom-trigger') || fig.querySelector('img');
      const img = fig.querySelector('img');
      const caption = fig.querySelector('figcaption') || fig.querySelector('.evidence-caption');
      if (!img || !trigger) return;

      if (!fig.querySelector('.image-zoom-trigger')) {
        img.setAttribute('tabindex', '0');
        img.setAttribute('role', 'button');
        img.setAttribute('aria-haspopup', 'dialog');
        img.setAttribute('aria-label', `Enlarge preview: ${img.alt || 'Detailed visual'}`);
      }

      function openModal(invoker) {
        triggerElement = invoker || trigger || img;
        modalImg.src = img.src;
        modalImg.alt = img.alt;
        modalImg.hidden = false;

        const captionText = caption ? caption.textContent.trim() : img.alt;
        modalCaption.textContent = captionText;

        setBackgroundInert(true);
        modal.classList.add('open');
        priorBodyOverflow = document.body.style.overflow;
        document.body.style.overflow = 'hidden';
        closeBtn.focus({ preventScroll: true });
      }

      trigger.addEventListener('click', () => openModal(trigger));
      if (trigger.tagName !== 'BUTTON') {
        trigger.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            openModal(trigger);
          }
        });
      }
    });
  }
}

// DEC-13: Email Copy Action with Robust Fallback, Timer Safety, and Accessible Live Status
function copyTextToClipboard(text) {
  if (navigator.clipboard && window.isSecureContext) {
    return navigator.clipboard.writeText(text);
  }
  return new Promise((resolve, reject) => {
    const prevFocus = document.activeElement;
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    textArea.style.top = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus({ preventScroll: true });
    textArea.select();
    try {
      const successful = document.execCommand('copy');
      document.body.removeChild(textArea);
      if (prevFocus && typeof prevFocus.focus === 'function') {
        prevFocus.focus({ preventScroll: true });
      }
      if (successful) {
        resolve();
      } else {
        reject(new Error('execCommand copy returned false'));
      }
    } catch (err) {
      document.body.removeChild(textArea);
      if (prevFocus && typeof prevFocus.focus === 'function') {
        prevFocus.focus({ preventScroll: true });
      }
      reject(err);
    }
  });
}

document.querySelectorAll('.copy-email-btn').forEach((btn) => {
  const defaultHtml = btn.innerHTML;
  const defaultAriaLabel = btn.getAttribute('aria-label') || 'Copy email address to clipboard';
  const statusEl = btn.closest('.copy-email-box')?.querySelector('.copy-email-status') || null;
  let resetTimerId = null;

  function scheduleReset(delayMs) {
    if (resetTimerId !== null) {
      clearTimeout(resetTimerId);
    }
    resetTimerId = setTimeout(() => {
      btn.innerHTML = defaultHtml;
      btn.classList.remove('copied', 'copy-failed');
      btn.setAttribute('aria-label', defaultAriaLabel);
      if (statusEl) statusEl.textContent = '';
      resetTimerId = null;
    }, delayMs);
  }

  btn.addEventListener('click', () => {
    const text = btn.getAttribute('data-copy');
    if (!text) return;
    copyTextToClipboard(text).then(() => {
      btn.classList.remove('copy-failed');
      btn.textContent = 'Copied! ✓';
      btn.classList.add('copied');
      btn.setAttribute('aria-label', 'Copied: email address copied to clipboard');
      if (statusEl) statusEl.textContent = `Copied ${text} to clipboard.`;
      scheduleReset(2000);
    }).catch(() => {
      btn.classList.remove('copied');
      btn.textContent = 'Copy failed ✗';
      btn.classList.add('copy-failed');
      btn.setAttribute('aria-label', 'Copy failed: unable to copy email address to clipboard');
      if (statusEl) statusEl.textContent = `Copy failed. Email address is ${text}.`;
      scheduleReset(2500);
    });
  });
});
