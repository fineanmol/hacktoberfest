<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="description" content="Responsive portfolio template - customizable and forkable" />
  <title>Your Name — Portfolio</title>
  <style>
    /* -----------------------------
       CSS Variables & Reset
       -----------------------------*/
    :root{
      --bg: #0f1724;
      --card: #111827;
      --muted: #9ca3af;
      --text: #e6eef8;
      --accent: #7c3aed;
      --glass: rgba(255,255,255,0.03);
      --radius: 14px;
      --container: 1100px;
    }

    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background: linear-gradient(180deg,var(--bg) 0%, #071026 100%);
      color:var(--text);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      line-height:1.5;
      padding:24px 20px;
    }

    /* Container */
    .wrap{max-width:var(--container);margin:0 auto}

    /* NAV */
    header{
      display:flex;align-items:center;justify-content:space-between;gap:16px;margin-bottom:28px
    }
    .brand{display:flex;align-items:center;gap:12px}
    .logo{width:44px;height:44px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#06b6d4);display:flex;align-items:center;justify-content:center;font-weight:700}
    nav{display:flex;gap:14px;align-items:center}
    nav a{color:var(--muted);text-decoration:none;padding:8px;border-radius:8px}
    nav a:hover{color:var(--text);background:var(--glass)}
    .cta{background:var(--accent);color:white;padding:8px 12px;border-radius:10px;text-decoration:none}

    /* mobile nav */
    .hamburger{display:none;background:none;border:1px solid rgba(255,255,255,0.06);padding:8px;border-radius:8px}

    /* HERO */
    .hero{display:grid;grid-template-columns:1fr 360px;gap:28px;align-items:center;margin-bottom:32px}
    .hero-card{background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent);padding:26px;border-radius:var(--radius);box-shadow:0 6px 30px rgba(2,6,23,0.6)}
    h1{margin:0;font-size:28px}
    p.lead{color:var(--muted);margin-top:12px}
    .socials{display:flex;gap:10px;margin-top:16px}
    .socials a{color:var(--muted);text-decoration:none}

    /* avatar */
    .avatar{width:140px;height:140px;border-radius:12px;overflow:hidden;border:4px solid rgba(255,255,255,0.03)}
    .avatar img{width:100%;height:100%;object-fit:cover;display:block}

    /* SECTIONS */
    section{margin-bottom:28px}
    .section-title{display:flex;align-items:center;gap:12px;margin-bottom:14px}
    .section-title h2{margin:0;font-size:18px}
    .grid{display:grid;gap:16px}

    /* Projects */
    .projects{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
    .project{background:var(--card);padding:16px;border-radius:12px;border:1px solid rgba(255,255,255,0.02);display:flex;flex-direction:column;gap:10px}
    .project .thumb{height:130px;border-radius:10px;overflow:hidden;background:linear-gradient(90deg,#0b1220,#071431)}
    .project h3{margin:0;font-size:16px}
    .project p{margin:0;color:var(--muted);font-size:13px}
    .tags{display:flex;gap:8px;flex-wrap:wrap}
    .tag{font-size:12px;padding:6px 8px;border-radius:999px;background:rgba(255,255,255,0.03);color:var(--muted)}
    .project .actions{margin-top:auto;display:flex;gap:8px}

    /* Skills */
    .skills{grid-template-columns:repeat(auto-fit,minmax(140px,1fr))}
    .skill{background:var(--card);padding:10px;border-radius:10px;text-align:center}

    /* Contact */
    .contact-form{display:grid;gap:10px;grid-template-columns:1fr 1fr}
    .contact-form input,.contact-form textarea{grid-column:span 2;padding:10px;border-radius:8px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:var(--text)}
    .contact-form input[type="email"],.contact-form input[type="text"]{height:42px}
    .contact-form textarea{min-height:120px;resize:vertical}
    .contact-form button{grid-column:span 2;padding:10px;border-radius:10px;border:none;background:var(--accent);color:white}

    /* Footer */
    footer{text-align:center;color:var(--muted);padding:18px}

    /* Modal */
    .modal{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(2,6,23,0.6);visibility:hidden;opacity:0;transition:all .18s}
    .modal.show{visibility:visible;opacity:1}
    .modal-inner{background:var(--card);padding:18px;border-radius:12px;max-width:880px;width:92%}

    /* Responsive tweaks */
    @media (max-width:900px){
      .hero{grid-template-columns:1fr;}
      .hero-card{order:2}
      .avatar{width:120px;height:120px}
      nav{display:none}
      .hamburger{display:block}
      .contact-form{grid-template-columns:1fr}
      .contact-form input,.contact-form textarea, .contact-form button{grid-column:auto}
    }

    /* small devices */
    @media (max-width:480px){
      body{padding:18px 14px}
      h1{font-size:22px}
    }

    /* simple focus styles */
    a:focus,input:focus,button:focus{outline:3px solid rgba(124,58,237,0.18);outline-offset:2px}

  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="brand">
        <div class="logo">YS</div>
        <div>
          <div style="font-weight:700">Your Name</div>
          <div style="font-size:12px;color:var(--muted)">Frontend Developer • Open Source</div>
        </div>
      </div>

      <nav aria-label="Main navigation">
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#skills">Skills</a>
        <a href="#contact">Contact</a>
        <a class="cta" href="#contact">Hire me</a>
      </nav>

      <button class="hamburger" aria-label="Open menu">☰</button>
    </header>

    <main>
      <section class="hero">
        <div class="hero-card">
          <h1>Hi — I'm <span id="name">Your Name</span>.</h1>
          <p class="lead">I build accessible, responsive web experiences. I specialize in frontend development with a focus on performance and clarity.</p>
          <div class="socials" aria-hidden="false">
            <a href="#" title="GitHub">GitHub</a>
            <a href="#" title="Twitter">Twitter</a>
            <a href="#" title="LinkedIn">LinkedIn</a>
          </div>

          <div style="margin-top:20px; display:flex; gap:12px; align-items:center;">
            <a class="cta" href="#projects">See my work</a>
            <button id="themeToggle" style="padding:8px;border-radius:8px;background:transparent;border:1px solid rgba(255,255,255,0.04);color:var(--text)">Toggle Theme</button>
          </div>

          <div style="margin-top:18px;color:var(--muted);font-size:13px">Quick tech: HTML • CSS • JavaScript</div>
        </div>

        <aside style="display:flex;flex-direction:column;gap:12px;align-items:center">
          <div class="avatar">
            <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=800&auto=format&fit=crop&ixlib=rb-4.0.3&s=placeholder" alt="Your avatar">
          </div>
          <div style="text-align:center; color:var(--muted)">
            <div style="font-weight:700">Location</div>
            <div style="font-size:13px">City, Country</div>
          </div>
        </aside>
      </section>

      <section id="about">
        <div class="section-title"><h2>About</h2></div>
        <div class="hero-card">
          <p>I’m a frontend developer who cares about clear UX, performance and maintainable code. I enjoy turning design ideas into delightful experiences and contributing to open source.</p>
          <p style="color:var(--muted)">Tip: Fork this template and replace content (name, projects, images). The projects below are auto-generated from a small JS array — change them in the <code>&lt;script&gt;</code> at the bottom.</p>
        </div>
      </section>

      <section id="projects">
        <div class="section-title"><h2>Projects</h2></div>
        <div class="grid projects" id="projectsGrid"></div>
      </section>

      <section id="skills">
        <div class="section-title"><h2>Skills</h2></div>
        <div class="grid skills">
          <div class="skill">HTML &amp; Semantics</div>
          <div class="skill">CSS / Layouts</div>
          <div class="skill">JavaScript (Vanilla)</div>
          <div class="skill">Responsive Design</div>
          <div class="skill">Accessibility (a11y)</div>
          <div class="skill">Git &amp; Open Source</div>
        </div>
      </section>

      <section id="contact">
        <div class="section-title"><h2>Contact</h2></div>
        <div class="hero-card">
          <form id="contactForm" class="contact-form" novalidate>
            <input id="fullName" type="text" placeholder="Your full name" required />
            <input id="email" type="email" placeholder="Email address" required />
            <input id="subject" type="text" placeholder="Subject" />
            <textarea id="message" placeholder="Message" required></textarea>
            <button type="submit">Send message</button>
            <div id="formMsg" style="grid-column:span 2;color:var(--muted);font-size:13px"></div>
          </form>
        </div>
      </section>

    </main>

    <footer>
      <div>© <span id="year"></span> Your Name — Built with ❤️. Fork and customize.</div>
    </footer>

  </div>

  <!-- Modal for project details -->
  <div class="modal" id="modal" role="dialog" aria-hidden="true">
    <div class="modal-inner" role="document">
      <button id="modalClose" style="float:right;background:none;border:none;color:var(--muted);font-size:18px">✕</button>
      <div id="modalContent"></div>
    </div>
  </div>

  <script>
    // -----------------------------
    // Basic interactive JS
    // -----------------------------
    document.getElementById('year').textContent = new Date().getFullYear();

    // Projects data — replace or add your own projects here
    const projects = [
      {
        id: 'p1',
        title: 'Portfolio Template',
        desc: 'A minimal, responsive portfolio template you can fork and personalize.',
        img: 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=1200&auto=format&fit=crop&ixlib=rb-4.0.3&s=placeholder',
        tags: ['HTML','CSS','JS'],
        link: '#'
      },
      {
        id: 'p2',
        title: 'Open Data Visualizer',
        desc: 'Dashboard that visualizes open datasets with charts and filters.',
        img: 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1200&auto=format&fit=crop&ixlib=rb-4.0.3&s=placeholder',
        tags: ['React','D3'],
        link: '#'
      },
      {
        id: 'p3',
        title: 'Mini Habit Tracker',
        desc: 'A small, local-storage based habit tracker with streaks and progress.',
        img: 'https://images.unsplash.com/photo-1515879218367-8466d910aaa4?q=80&w=1200&auto=format&fit=crop&ixlib=rb-4.0.3&s=placeholder',
        tags: ['Vanilla JS','LocalStorage'],
        link: '#'
      }
    ];

    const projectsGrid = document.getElementById('projectsGrid');

    function renderProjects(){
      projectsGrid.innerHTML = '';
      projects.forEach(p => {
        const el = document.createElement('article');
        el.className = 'project';
        el.innerHTML = `
          <div class="thumb" aria-hidden="true"><img style="width:100%;height:100%;object-fit:cover" src="${p.img}" alt="${p.title}"></div>
          <h3>${p.title}</h3>
          <p>${p.desc}</p>
          <div class="tags">${p.tags.map(t => `<span class="tag">${t}</span>`).join('')}</div>
          <div class="actions">
            <a href="${p.link}" aria-label="Open project ${p.title}" style="text-decoration:none;padding:8px;border-radius:8px;border:1px solid rgba(255,255,255,0.04)">View</a>
            <button data-id="${p.id}" style="padding:8px;border-radius:8px;border:none;background:var(--accent);color:white">Details</button>
          </div>
        `;
        projectsGrid.appendChild(el);
      });

      // attach detail handlers
      document.querySelectorAll('.project button').forEach(btn => btn.addEventListener('click', e=> openModal(e.target.dataset.id)));
    }

    function openModal(id){
      const p = projects.find(x=>x.id===id);
      if(!p) return;
      const content = document.getElementById('modalContent');
      content.innerHTML = `
        <h3 style="margin-top:0">${p.title}</h3>
        <p style="color:var(--muted)">${p.desc}</p>
        <div style="margin:12px 0"><img src="${p.img}" alt="${p.title}" style="width:100%;border-radius:10px;max-height:320px;object-fit:cover"></div>
        <p class="tags">${p.tags.map(t => `<span class="tag">${t}</span>`).join('')}</p>
        <div style="margin-top:14px"><a href="${p.link}" class="cta">Open project</a></div>
      `;
      const modal = document.getElementById('modal');
      modal.classList.add('show');
      modal.setAttribute('aria-hidden','false');
    }

    document.getElementById('modalClose').addEventListener('click', ()=>{
      const modal = document.getElementById('modal');
      modal.classList.remove('show');
      modal.setAttribute('aria-hidden','true');
    });

    document.getElementById('modal').addEventListener('click', (e)=>{
      if(e.target.id === 'modal'){
        document.getElementById('modal').classList.remove('show');
      }
    });

    // Contact form handler (client-side only)
    document.getElementById('contactForm').addEventListener('submit', (e)=>{
      e.preventDefault();
      const name = document.getElementById('fullName').value.trim();
      const email = document.getElementById('email').value.trim();
      const message = document.getElementById('message').value.trim();
      const msgEl = document.getElementById('formMsg');
      if(!name || !email || !message){
        msgEl.textContent = 'Please fill required fields.';
        return;
      }
      // For a real site, post to server or use Formspree / Netlify Forms / email API
      msgEl.textContent = 'Thanks! Your message has been captured locally (demo). Replace this with a real backend.';
      e.target.reset();
    });

    // Theme toggle — simple light/dark swap by inverting colors
    const themeToggle = document.getElementById('themeToggle');
    themeToggle.addEventListener('click', ()=>{
      const root = document.documentElement;
      if(root.style.getPropertyValue('--bg') === '#0f1724'){
        // set light
        root.style.setProperty('--bg','#f7fafc');
        root.style.setProperty('--card','#ffffff');
        root.style.setProperty('--text','#0b1220');
        root.style.setProperty('--muted','#475569');
        root.style.setProperty('--glass','rgba(11,17,32,0.03)');
      } else {
        // back to dark
        root.style.setProperty('--bg','#0f1724');
        root.style.setProperty('--card','#111827');
        root.style.setProperty('--text','#e6eef8');
        root.style.setProperty('--muted','#9ca3af');
        root.style.setProperty('--glass','rgba(255,255,255,0.03)');
      }
    });

    // Hamburger menu for small screens (simple toggle)
    document.querySelector('.hamburger').addEventListener('click', ()=>{
      const nav = document.querySelector('nav');
      if(nav.style.display === 'flex') nav.style.display = 'none';
      else nav.style.display = 'flex';
      nav.style.flexDirection = 'column';
      nav.style.position = 'absolute';
      nav.style.right = '20px';
      nav.style.top = '70px';
      nav.style.background = 'var(--card)';
      nav.style.padding = '10px';
      nav.style.borderRadius = '10px';
      nav.style.boxShadow = '0 8px 40px rgba(2,6,23,0.6)';
    });

    // Smooth scrolling for in-page links
    document.querySelectorAll('a[href^="#"]').forEach(a=>{
      a.addEventListener('click', e=>{
        const href = a.getAttribute('href');
        if(href.length>1){
          e.preventDefault();
          const el = document.querySelector(href);
          if(el) el.scrollIntoView({behavior:'smooth',block:'start'});
        }
      })
    });

    // initial render
    renderProjects();

    // Accessibility: keyboard close on Esc
    document.addEventListener('keydown', (e)=>{
      if(e.key === 'Escape'){
        document.getElementById('modal').classList.remove('show');
      }
    });

  </script>
</body>
</html>
