const root = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');
const typingLine = document.getElementById('typingLine');
const terminalOutput = document.getElementById('terminalOutput');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

const setTheme = (isDark) => {
  root.classList.toggle('dark', isDark);
  const nextTheme = isDark ? 'light' : 'dark';
  themeIcon.textContent = nextTheme === 'light' ? 'Light' : 'Dark';
  themeToggle.setAttribute('aria-label', `Switch to ${nextTheme} theme`);
};

const initTheme = () => {
  let saved = null;
  try {
    saved = localStorage.getItem('theme');
  } catch {
    // Browsers may block storage; the system preference remains available.
  }
  const prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
  const useLight = saved ? saved === 'light' : prefersLight;
  setTheme(!useLight);
};

const toggleTheme = () => {
  const isDark = !root.classList.contains('dark');
  setTheme(isDark);
  try {
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  } catch {
    // The selected theme still works for this page view.
  }
};

themeToggle.addEventListener('click', toggleTheme);
initTheme();

const setMenuOpen = (open) => {
  mobileMenu.classList.toggle('hidden', !open);
  mobileMenuBtn.setAttribute('aria-expanded', String(open));
  mobileMenuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
};

mobileMenuBtn.addEventListener('click', () => {
  setMenuOpen(mobileMenu.classList.contains('hidden'));
});
document.querySelectorAll('.mobile-link').forEach((link) => {
  link.addEventListener('click', () => setMenuOpen(false));
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {
    setMenuOpen(false);
    mobileMenuBtn.focus();
  }
});

const cmdSet = [
  { cmd: 'whoami', out: 'Rehan Memon - AI + Software Builder' },
  { cmd: 'cat mission.txt', out: 'Turning complex AI ideas into shipped products.' },
  { cmd: 'ls strengths/', out: 'ML-engineering  backend-systems  product-thinking' },
  { cmd: 'status', out: 'Open to internships and high-impact opportunities.' }
];

let cmdIndex = 0;
let charIndex = 0;
function runTerminal() {
  const current = cmdSet[cmdIndex];
  if (charIndex < current.cmd.length) {
    typingLine.textContent += current.cmd[charIndex++];
    setTimeout(runTerminal, 70);
    return;
  }

  const line = document.createElement('p');
  line.innerHTML = `<span class="text-emerald-500">$</span> ${current.cmd}`;
  const out = document.createElement('p');
  out.textContent = current.out;
  terminalOutput.append(line, out);

  typingLine.textContent = '';
  charIndex = 0;
  cmdIndex = (cmdIndex + 1) % cmdSet.length;
  if (terminalOutput.children.length > 8) terminalOutput.innerHTML = '';
  setTimeout(runTerminal, 900);
}
if (reducedMotion.matches) {
  typingLine.textContent = cmdSet[0].cmd;
  terminalOutput.textContent = cmdSet[0].out;
} else {
  setTimeout(runTerminal, 650);
}

// Premium hover interaction: 3D tilt
const tiltCards = document.querySelectorAll('[data-tilt]');
if (!reducedMotion.matches) tiltCards.forEach((card) => {
  card.addEventListener('mousemove', (e) => {
    const r = card.getBoundingClientRect();
    const x = e.clientX - r.left;
    const y = e.clientY - r.top;
    const rotateX = ((y / r.height) - 0.5) * -7;
    const rotateY = ((x / r.width) - 0.5) * 7;
    card.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'perspective(900px) rotateX(0deg) rotateY(0deg) translateY(0)';
  });
});

// Live GitHub stats integration
async function loadGitHubStats() {
  const container = document.getElementById('githubStats');
  const username = 'rehanmemon-ai';
  try {
    const res = await fetch(`https://api.github.com/users/${username}`);
    if (!res.ok) throw new Error('GitHub API unavailable');
    const data = await res.json();
    const fields = [
      ['Followers', data.followers ?? 0],
      ['Public Repos', data.public_repos ?? 0],
      ['Following', data.following ?? 0]
    ];
    container.replaceChildren();
    fields.forEach(([label, value]) => {
      const card = document.createElement('div');
      card.className = 'stat';
      const caption = document.createElement('p');
      caption.className = 'text-xs text-slate-500';
      caption.textContent = label;
      const number = document.createElement('p');
      number.className = 'mt-1 text-2xl font-bold';
      number.textContent = String(value);
      card.append(caption, number);
      container.append(card);
    });
  } catch {
    container.textContent = 'GitHub stats could not be loaded right now.';
  }
}
loadGitHubStats();
