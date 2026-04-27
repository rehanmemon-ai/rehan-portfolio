const root = document.documentElement;
const themeToggle = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');
const form = document.getElementById('contactForm');
const formNote = document.getElementById('formNote');
const typingLine = document.getElementById('typingLine');
const terminalOutput = document.getElementById('terminalOutput');

const initTheme = () => {
  const saved = localStorage.getItem('theme');
  const prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
  const useLight = saved ? saved === 'light' : prefersLight;
  root.classList.toggle('dark', !useLight);
  themeIcon.textContent = useLight ? '??' : '??';
};

const toggleTheme = () => {
  const isDark = root.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
  themeIcon.textContent = isDark ? '??' : '??';
};

themeToggle.addEventListener('click', toggleTheme);
initTheme();

mobileMenuBtn.addEventListener('click', () => {
  mobileMenu.classList.toggle('hidden');
});
document.querySelectorAll('.mobile-link').forEach((link) => {
  link.addEventListener('click', () => mobileMenu.classList.add('hidden'));
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
setTimeout(runTerminal, 650);

const counterObserver = new IntersectionObserver((entries, obs) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    entry.target.querySelectorAll('[data-counter]').forEach((el) => {
      const target = Number(el.dataset.counter);
      gsap.fromTo(el, { innerText: 0 }, {
        innerText: target,
        duration: 1.4,
        snap: { innerText: 1 },
        ease: 'power2.out'
      });
    });
    obs.unobserve(entry.target);
  });
});
counterObserver.observe(document.getElementById('hero'));

if (window.gsap) {
  gsap.registerPlugin(ScrollTrigger);

  gsap.from('header', { y: -80, opacity: 0, duration: 0.8, ease: 'power3.out' });

  gsap.utils.toArray('.reveal').forEach((el, i) => {
    gsap.to(el, {
      opacity: 1,
      y: 0,
      duration: 0.8,
      delay: i * 0.02,
      ease: 'power2.out',
      scrollTrigger: {
        trigger: el,
        start: 'top 88%'
      }
    });
  });

  // Smooth page transitions feel
  gsap.from('main', { opacity: 0, duration: 0.7, ease: 'power1.out' });

  // Text reveal for hero heading
  gsap.from('#hero h1', { y: 30, opacity: 0, duration: 1, ease: 'power4.out' });
}

// Premium hover interaction: 3D tilt
const tiltCards = document.querySelectorAll('[data-tilt]');
tiltCards.forEach((card) => {
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
  const username = 'rehanmemon';
  try {
    const res = await fetch(`https://api.github.com/users/${username}`);
    if (!res.ok) throw new Error('GitHub API unavailable');
    const data = await res.json();
    const fields = [
      ['Followers', data.followers ?? 0],
      ['Public Repos', data.public_repos ?? 0],
      ['Following', data.following ?? 0]
    ];
    container.innerHTML = fields.map(([label, value]) => `
      <div class="stat">
        <p class="text-xs text-slate-500">${label}</p>
        <p class="mt-1 text-2xl font-bold">${value}</p>
      </div>
    `).join('');
  } catch {
    container.innerHTML = '<p class="text-sm text-rose-400">GitHub stats could not be loaded right now.</p>';
  }
}
loadGitHubStats();

form.addEventListener('submit', (e) => {
  e.preventDefault();
  formNote.textContent = 'Thanks. Your message is captured in this demo UI. Connect Formspree/Web3Forms to make it live.';
  form.reset();
});
