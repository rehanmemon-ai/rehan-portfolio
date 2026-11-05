const root = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');

function setTheme(isDark) {
  root.classList.toggle('dark', isDark);
  const nextTheme = isDark ? 'light' : 'dark';
  themeIcon.textContent = nextTheme === 'light' ? 'Light' : 'Dark';
  themeToggle.setAttribute('aria-label', `Switch to ${nextTheme} theme`);
}
let savedTheme = null;
try { savedTheme = localStorage.getItem('theme'); } catch { /* Storage may be disabled. */ }
const prefersDark = matchMedia('(prefers-color-scheme: dark)').matches;
setTheme(savedTheme ? savedTheme === 'dark' : prefersDark);
themeToggle.addEventListener('click', () => {
  const isDark = !root.classList.contains('dark');
  setTheme(isDark);
  try { localStorage.setItem('theme', isDark ? 'dark' : 'light'); } catch { /* Keep the in-page state. */ }
});

function setMenuOpen(open) {
  mobileMenu.hidden = !open;
  mobileMenuBtn.setAttribute('aria-expanded', String(open));
  mobileMenuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
}
mobileMenuBtn.addEventListener('click', () => setMenuOpen(mobileMenu.hidden));
mobileMenu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenuOpen(false)));
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !mobileMenu.hidden) {
    setMenuOpen(false);
    mobileMenuBtn.focus();
  }
});

const filterList = document.querySelector('[data-filter-list]');
if (filterList) {
  const cards = [...filterList.querySelectorAll('[data-filter-card]')];
  const controls = [...document.querySelectorAll('[data-filter-search],[data-filter-category],[data-filter-type],[data-filter-issuer],[data-filter-subject]')];
  const count = document.querySelector('[data-filter-count]');
  const noResults = document.querySelector('[data-no-results]');
  function updateFilters() {
    const value = (name) => document.querySelector(`[data-filter-${name}]`)?.value.trim().toLowerCase() || '';
    const query = value('search');
    let shown = 0;
    cards.forEach((card) => {
      const searchable = (card.dataset.search || card.textContent).toLowerCase();
      const matches = (!query || searchable.includes(query)) &&
        (!value('category') || card.dataset.category?.toLowerCase() === value('category')) &&
        (!value('type') || card.dataset.type?.toLowerCase() === value('type')) &&
        (!value('issuer') || card.dataset.issuer?.toLowerCase() === value('issuer')) &&
        (!value('subject') || card.dataset.subject?.toLowerCase() === value('subject'));
      card.hidden = !matches;
      if (matches) shown += 1;
    });
    count.textContent = `${shown} ${shown === 1 ? 'record' : 'records'} shown`;
    noResults.hidden = shown !== 0;
  }
  controls.forEach((control) => control.addEventListener(control.tagName === 'INPUT' ? 'input' : 'change', updateFilters));
  updateFilters();
}
