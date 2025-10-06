// TECHGUIDE - Vanilla JS: simple auth, client-side routing, quiz, modal

// State
const state = {
  isAuthed: false,
  quizQuestions: [
    {
      id: 'q1',
      question: 'Which data structure uses First-In-First-Out (FIFO)?',
      options: ['Stack', 'Queue', 'Tree', 'Graph'],
      answerIndex: 1,
    },
    {
      id: 'q2',
      question: 'What does HTTP stand for?',
      options: [
        'Hyper Text Transfer Protocol',
        'Hyperlink Transfer Text Protocol',
        'High Transfer Text Protocol',
        'Hyper Transfer Type Protocol',
      ],
      answerIndex: 0,
    },
    {
      id: 'q3',
      question: 'Which keyword declares a constant in JavaScript?',
      options: ['var', 'let', 'const', 'static'],
      answerIndex: 2,
    },
    {
      id: 'q4',
      question: 'Big-O of binary search on a sorted array?',
      options: ['O(n)', 'O(n log n)', 'O(log n)', 'O(1)'],
      answerIndex: 2,
    },
    {
      id: 'q5',
      question: 'Which SQL command is used to extract data?',
      options: ['INSERT', 'UPDATE', 'SELECT', 'DELETE'],
      answerIndex: 2,
    },
  ],
};

// Elements
const sections = {
  login: document.getElementById('login-section'),
  home: document.getElementById('home-section'),
  quiz: document.getElementById('quiz-section'),
  roadmap: document.getElementById('roadmap-section'),
};
const headerEl = document.getElementById('main-header');
const navToggle = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');
const logoutLink = document.getElementById('logout-link');

// Modal
const modal = document.getElementById('modal');
const modalOverlay = document.getElementById('modal-overlay');
const modalClose = document.getElementById('modal-close');
const modalTitle = document.getElementById('modal-title');
const modalBody = document.getElementById('modal-body');

// Auth form
const loginForm = document.getElementById('login-form');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const emailHint = document.getElementById('email-hint');
const passwordHint = document.getElementById('password-hint');
const loginAlert = document.getElementById('login-alert');

// Quiz
const quizContainer = document.getElementById('quiz-container');
const submitQuizBtn = document.getElementById('submit-quiz');
const resetQuizBtn = document.getElementById('reset-quiz');
const quizResult = document.getElementById('quiz-result');

// Helpers
function showSection(name) {
  Object.keys(sections).forEach((key) => {
    const section = sections[key];
    const isTarget = key === name;
    section.classList.toggle('is-hidden', !isTarget);
    section.setAttribute('aria-hidden', String(!isTarget));
  });
}

function updateHeaderVisibility() {
  headerEl.classList.toggle('is-hidden', !state.isAuthed);
  headerEl.setAttribute('aria-hidden', String(!state.isAuthed));
}

function navigate(route) {
  if (!state.isAuthed && route !== 'login') {
    window.location.hash = '#login';
    route = 'login';
  }

  switch (route) {
    case 'home':
      showSection('home');
      break;
    case 'quiz':
      renderQuiz();
      showSection('quiz');
      break;
    case 'roadmap':
      showSection('roadmap');
      break;
    case 'login':
    default:
      showSection('login');
      break;
  }
}

function getRouteFromHash() {
  const hash = window.location.hash.replace('#', '');
  if (!hash) return state.isAuthed ? 'home' : 'login';
  return hash;
}

// Auth - simple client-only demo
function validateEmail(value) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(String(value).toLowerCase());
}

function validatePassword(value) {
  return String(value).trim().length >= 6;
}

function attemptLogin(email, password) {
  const isEmailValid = validateEmail(email);
  const isPasswordValid = validatePassword(password);

  emailHint.textContent = isEmailValid ? '' : 'Enter a valid email address';
  passwordHint.textContent = isPasswordValid ? '' : 'Minimum 6 characters';

  if (!isEmailValid || !isPasswordValid) {
    loginAlert.textContent = 'Please fix the errors above.';
    return false;
  }

  // Demo auth: accept any valid-looking email & password
  state.isAuthed = true;
  localStorage.setItem('tg_authed', '1');
  loginAlert.textContent = '';
  return true;
}

function logout() {
  state.isAuthed = false;
  localStorage.removeItem('tg_authed');
  updateHeaderVisibility();
  navigate('login');
}

// Quiz rendering & scoring
function renderQuiz() {
  quizContainer.innerHTML = '';
  state.quizQuestions.forEach((q, idx) => {
    const card = document.createElement('div');
    card.className = 'question-card';

    const title = document.createElement('p');
    title.className = 'question-title';
    title.textContent = `${idx + 1}. ${q.question}`;
    card.appendChild(title);

    const options = document.createElement('div');
    options.className = 'options';

    q.options.forEach((opt, i) => {
      const id = `${q.id}_${i}`;

      const label = document.createElement('label');
      label.className = 'option';
      label.setAttribute('for', id);

      const input = document.createElement('input');
      input.type = 'radio';
      input.name = q.id;
      input.value = String(i);
      input.id = id;

      const span = document.createElement('span');
      span.textContent = opt;

      label.appendChild(input);
      label.appendChild(span);
      options.appendChild(label);
    });

    card.appendChild(options);
    quizContainer.appendChild(card);
  });

  quizResult.textContent = '';
}

function scoreQuiz() {
  let score = 0;
  let total = state.quizQuestions.length;

  state.quizQuestions.forEach((q) => {
    const chosen = document.querySelector(`input[name="${q.id}"]:checked`);
    if (chosen && Number(chosen.value) === q.answerIndex) {
      score += 1;
    }
  });

  const percent = Math.round((score / total) * 100);
  let message = '';
  if (percent === 100) message = 'Outstanding! You are on fire!';
  else if (percent >= 80) message = 'Great job! Keep pushing!';
  else if (percent >= 50) message = 'Nice start! Keep practicing.';
  else message = 'Every expert was once a beginner. Try again!';

  quizResult.textContent = `Score: ${score}/${total} (${percent}%). ${message}`;
}

function resetQuiz() {
  renderQuiz();
}

// Modal helpers
function openModal(title, body) {
  modalTitle.textContent = title;
  modalBody.textContent = body;
  modal.classList.remove('is-hidden');
  modal.setAttribute('aria-hidden', 'false');
}
function closeModal() {
  modal.classList.add('is-hidden');
  modal.setAttribute('aria-hidden', 'true');
}

// Event listeners
window.addEventListener('DOMContentLoaded', () => {
  // Restore auth
  state.isAuthed = localStorage.getItem('tg_authed') === '1';
  updateHeaderVisibility();

  // Initial route
  navigate(getRouteFromHash());
});

window.addEventListener('hashchange', () => {
  navigate(getRouteFromHash());
});

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
  });
}

if (logoutLink) {
  logoutLink.addEventListener('click', (e) => {
    e.preventDefault();
    logout();
  });
}

if (loginForm) {
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = emailInput.value;
    const password = passwordInput.value;

    const ok = attemptLogin(email, password);
    if (ok) {
      updateHeaderVisibility();
      window.location.hash = '#home';
    }
  });

  emailInput.addEventListener('input', () => {
    emailHint.textContent = validateEmail(emailInput.value) ? '' : 'Enter a valid email address';
  });
  passwordInput.addEventListener('input', () => {
    passwordHint.textContent = validatePassword(passwordInput.value) ? '' : 'Minimum 6 characters';
  });
}

// Quiz interactions
if (submitQuizBtn) submitQuizBtn.addEventListener('click', scoreQuiz);
if (resetQuizBtn) resetQuizBtn.addEventListener('click', resetQuiz);

// Roadmap interactions
const cards = document.querySelectorAll('.roadmap-card');
cards.forEach((card) => {
  card.addEventListener('click', () => {
    const title = card.getAttribute('data-title') || 'Stage';
    const detail = card.getAttribute('data-detail') || '';
    openModal(title, detail);
  });
  card.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      const title = card.getAttribute('data-title') || 'Stage';
      const detail = card.getAttribute('data-detail') || '';
      openModal(title, detail);
    }
  });
});

if (modalOverlay) modalOverlay.addEventListener('click', closeModal);
if (modalClose) modalClose.addEventListener('click', closeModal);
window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});
