import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Samruddhi Dhoot — Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_pdf_download_link(label="↓ Download Resume"):
    # Look for the PDF in common locations
    candidates = [
        "assets/Samruddhi_Dhoot_CV-1.pdf",
        "Samruddhi_Dhoot_CV-1.pdf",
    ]
    for pdf_path in candidates:
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                pdf_data = base64.b64encode(f.read()).decode()
            return f'<a href="data:application/pdf;base64,{pdf_data}" download="Samruddhi_Dhoot_Resume.pdf" class="btn btn-primary">{label}</a>'
    return ""

load_css()

# ── HERO ──────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
  <div class="hero-availability">🟢 Open to opportunities</div>
  <h1 class="hero-name">Samruddhi Dhoot</h1>
  <p class="hero-role">Senior Data Analyst &amp; AI/DS Engineer</p>
  <p class="hero-desc">
    B.E. in Artificial Intelligence &amp; Data Science · CGPA 8.8<br>
    Building ETL pipelines, interactive dashboards, and ML-powered systems.
  </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    st.markdown('<a href="#contact" class="btn btn-primary">Get in touch ↗</a>', unsafe_allow_html=True)
with col2:
    dl = get_pdf_download_link()
    if dl:
        st.markdown(dl, unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── ABOUT ─────────────────────────────────────────────
st.markdown('<p class="section-label">01 / About</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Who I am</h2>', unsafe_allow_html=True)

c1, c2 = st.columns([3, 2])
with c1:
    st.markdown("""
    <div class="about-text">
      <p>I graduated in 2024 with a B.E. in <strong>Artificial Intelligence &amp; Data Science</strong>
      with an excellent CGPA of <strong>8.8</strong>. My passion lies at the crossroads of
      data engineering and intelligent systems.</p>
      <p>Currently at <strong>Cube Green Energy</strong> as a Senior Data Analyst Associate,
      I design and maintain <strong>ETL/ELT pipelines</strong>, develop SQL-driven analytics
      datasets, and build large-scale web applications using Dash with custom JS &amp; CSS to
      deliver production-ready dashboards.</p>
      <p>My journey also includes an internship as a <strong>Python Developer at MaticAlgos</strong>,
      where I built solid experience in stock market analysis, web scraping, and API testing.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stats-grid">
      <div class="stat-card"><div class="stat-number">8.8</div><div class="stat-label">CGPA</div></div>
      <div class="stat-card"><div class="stat-number">1.5+</div><div class="stat-label">Yrs Exp</div></div>
      <div class="stat-card"><div class="stat-number">5+</div><div class="stat-label">Tech Stacks</div></div>
      <div class="stat-card"><div class="stat-number">2024</div><div class="stat-label">Graduate</div></div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── SKILLS ────────────────────────────────────────────
st.markdown('<p class="section-label">02 / Skills</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Tech Stack</h2>', unsafe_allow_html=True)

skills_data = {
    "Languages & Core": [
        ("Python", "accent"), ("R", "accent"), ("SQL", "accent"),
        ("DSA", ""), ("OOP", ""), ("HTML", ""), ("CSS", ""), ("JavaScript", "")
    ],
    "Databases": [
        ("PostgreSQL", "accent"), ("MySQL", "accent"), ("MongoDB", "accent"),
        ("PL/SQL", ""), ("ETL / ELT Pipelines", ""), ("Database Design", "")
    ],
    "Data Science & ML": [
        ("Machine Learning", "teal"), ("NLP", "teal"), ("Data Analytics", "teal"),
        ("Information Retrieval", "teal"), ("Stock Market Analysis", ""),
        ("Web Scraping", ""), ("API Development", "")
    ],
    "Frameworks & Visualization": [
        ("Flask", "accent"), ("FastAPI", "accent"), ("Django", ""),
        ("Plotly Dash", "accent"), ("Streamlit", "accent"),
        ("Power BI", ""), ("Pandas", ""), ("NumPy", "")
    ],
    "Tools & Platforms": [
        ("Git", ""), ("Postman", ""), ("Jupyter Notebook", ""),
        ("VS Code", ""), ("AWS", "")
    ],
}

for category, tags in skills_data.items():
    tag_html = "".join([f'<span class="skill-tag {cls}">{name}</span>' for name, cls in tags])
    st.markdown(f"""
    <div class="skill-category">
      <p class="skill-cat-title">{category}</p>
      <div class="skill-tags">{tag_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── EXPERIENCE ────────────────────────────────────────
st.markdown('<p class="section-label">03 / Experience</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Where I\'ve worked</h2>', unsafe_allow_html=True)

experiences = [
    {
        "period": "Dec 2025 — Present",
        "company": "Cube Green Energy",
        "role": "Senior Data Analyst Associate",
        "location": "Hyderabad, India",
        "desc": "Designing and maintaining ETL/ELT pipelines, developing SQL-driven analytics datasets, and building large-scale web applications using Dash with custom JS & CSS for interactive, production-ready dashboards.",
        "tags": ["ETL Pipelines", "SQL", "Plotly Dash", "PostgreSQL", "Python"]
    },
    {
        "period": "Dec 2024 — Nov 2025",
        "company": "Cube Green Energy",
        "role": "Data Analytics Intern",
        "location": "Hyderabad, Telangana, India",
        "desc": "Developed data applications using Plotly Dash, Flask, and PostgreSQL, integrating RESTful APIs. Optimized SQL queries and database schemas, reducing query latency by 30%. Implemented backend ETL scripts for ingestion and transformation of large renewable energy datasets. Created a multilingual text-processing module using NLP for German and French reports.",
        "tags": ["Data Analytics", "Python", "Power BI", "Flask", "NLP"]
    },
    {
        "period": "Jan 2024 — Mar 2024",
        "company": "MaticAlgos",
        "role": "Python Developer Intern",
        "location": "Pune, Maharashtra, India",
        "desc": "Built and deployed FastAPI-based microservices for backtesting trading algorithms on historical OHLCV data. Integrated Python scripts for data cleaning, feature engineering, and analytics pipelines. Modularized endpoints to support scalability for future deployment.",
        "tags": ["FastAPI", "Python", "Web Scraping", "API Testing", "Stock Market"]
    },
    {
        "period": "Aug 2022 — Mar 2023",
        "company": "GDSC AISSMS IOIT",
        "role": "Management Team Member",
        "location": "Pune, Maharashtra, India",
        "desc": "Contributed to the Google Developer Student Club, organizing events, workshops, and community initiatives around technology and innovation.",
        "tags": ["Leadership", "Community", "Event Management"]
    }
]

for exp in experiences:
    tags_html = "".join([f'<span class="exp-tag">{t}</span>' for t in exp["tags"]])
    st.markdown(f"""
    <div class="exp-item">
      <div class="exp-meta-inline">
        <span class="exp-period">{exp['period']}</span> &nbsp;·&nbsp; <span class="exp-company">{exp['company']}</span>
      </div>
      <p class="exp-role">{exp['role']}</p>
      <p class="exp-loc">📍 {exp['location']}</p>
      <p class="exp-desc">{exp['desc']}</p>
      <div class="exp-tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── PROJECTS ──────────────────────────────────────────
st.markdown('<p class="section-label">04 / Projects</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Things I\'ve built</h2>', unsafe_allow_html=True)

projects = [
    {
        "title": "Multi-Hierarchy Task Tracker",
        "stack": "Python · Dash · MongoDB · CSS · JavaScript",
        "year": "2024",
        "desc": "Built a task management system supporting multi-level hierarchies, improving task organization efficiency by 30% for simulated user workflows. Enhanced front-end usability with custom CSS and JS Dash components, reducing task navigation time by 25%. Optimized MongoDB schema to handle nested tasks, ensuring fast retrieval and updates even for complex hierarchies.",
        "tags": ["Python", "Plotly Dash", "MongoDB", "JavaScript"]
    },
    {
        "title": "WhatsApp Chat Analysis",
        "stack": "Python · Streamlit · Pandas · NLP",
        "year": "2024",
        "desc": "Built a web app to analyze WhatsApp chats, providing insights into user engagement and conversation trends, improving decision-making for social interactions by 20%. Applied NLP and data preprocessing to extract sentiment, keyword frequency, and activity patterns. Interactive dashboards using Streamlit enabled users to explore chat analytics easily and intuitively.",
        "tags": ["Python", "Streamlit", "NLP", "Pandas"]
    },
]

proj_cols = st.columns(2)
for i, proj in enumerate(projects):
    tags_html = "".join([f'<span class="exp-tag">{t}</span>' for t in proj["tags"]])
    with proj_cols[i % 2]:
        st.markdown(f"""
        <div class="proj-card">
          <div class="proj-header">
            <span class="proj-year">{proj['year']}</span>
          </div>
          <h3 class="proj-title">{proj['title']}</h3>
          <p class="proj-stack">{proj['stack']}</p>
          <p class="exp-desc">{proj['desc']}</p>
          <div class="exp-tags" style="margin-top:16px;">{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── EDUCATION ─────────────────────────────────────────
st.markdown('<p class="section-label">05 / Education</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Academic background</h2>', unsafe_allow_html=True)

education = [
    {
        "period": "Sep 2020 — Jun 2024",
        "institute": "AISSMS IOIT, Pune",
        "degree": "B.E. — Artificial Intelligence & Data Science",
        "location": "Pune, Maharashtra, India",
        "desc": "Graduated with CGPA 8.8, specializing in AI and Data Science. Coursework covered machine learning, data engineering, NLP, and information retrieval systems.",
        "tags": ["CGPA: 8.8", "AI & Data Science"]
    },
    {
        "period": "2018 — 2020",
        "institute": "YCIS, Satara",
        "degree": "HSC — Science",
        "location": "Satara, Maharashtra, India",
        "desc": "Completed Higher Secondary Certificate in Science stream with 70%.",
        "tags": ["70%", "Science"]
    },
    {
        "period": "2017 — 2018",
        "institute": "NESS, Satara",
        "degree": "SSC",
        "location": "Satara, Maharashtra, India",
        "desc": "Completed Secondary School Certificate with an excellent score of 94.4%.",
        "tags": ["94.4%"]
    },
]

for edu in education:
    tags_html = "".join([f'<span class="exp-tag">{t}</span>' for t in edu["tags"]])
    st.markdown(f"""
    <div class="exp-item">
      <div class="exp-meta-inline">
        <span class="exp-period">{edu['period']}</span> &nbsp;·&nbsp; <span class="exp-company">{edu['institute']}</span>
      </div>
      <p class="exp-role">{edu['degree']}</p>
      <p class="exp-loc">📍 {edu['location']}</p>
      <p class="exp-desc">{edu['desc']}</p>
      <div class="exp-tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── CERTIFICATIONS ────────────────────────────────────
st.markdown('<p class="section-label">06 / Certifications</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Credentials</h2>', unsafe_allow_html=True)

certs = [
    {
        "title": "Full Stack Web Development with Python",
        "issuer": "Technogeeks",
        "year": "2024",
        "desc": "Trained in Flask, Django, SQL, and deployment workflows (Heroku).",
        "tags": ["Flask", "Django", "SQL", "Heroku"]
    },
    {
        "title": "AWS Cloud Practitioner Essentials",
        "issuer": "Amazon Web Services",
        "year": "2024",
        "desc": "Fundamentals of AWS architecture, services, and deployment models.",
        "tags": ["AWS", "Cloud", "Architecture"]
    },
    {
        "title": "HackerRank — Python & SQL",
        "issuer": "HackerRank",
        "year": "2024",
        "desc": "5-star Gold Badge in Problem Solving. Certified in Python and SQL.",
        "tags": ["Python", "SQL", "Problem Solving"]
    },
]

cert_cols = st.columns(3)
for i, cert in enumerate(certs):
    tags_html = "".join([f'<span class="exp-tag">{t}</span>' for t in cert["tags"]])
    with cert_cols[i % 3]:
        st.markdown(f"""
        <div class="cert-card">
          <div class="cert-meta">
            <span class="cert-issuer">{cert['issuer']}</span>
            <span class="cert-year">{cert['year']}</span>
          </div>
          <h3 class="cert-title">{cert['title']}</h3>
          <p class="exp-desc">{cert['desc']}</p>
          <div class="exp-tags" style="margin-top:14px;">{tags_html}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────────────
st.markdown('<a name="contact"></a><p class="section-label">07 / Contact</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Let\'s connect</h2>', unsafe_allow_html=True)

c1, c2 = st.columns([3, 2])
with c1:
    st.markdown("""
    <h3 class="contact-heading">Always open to collaborate.</h3>
    <p class="about-text" style="margin-bottom:24px;">Whether it's a data challenge, an interesting project,
    or just a chat about AI and analytics — reach out. I'm excited to connect with like-minded professionals.</p>
    <div class="contact-links">
      <a href="mailto:samruddhi1222@gmail.com" class="contact-link">
        <div class="contact-icon">✉</div> samruddhi1222@gmail.com
      </a>
      <a href="https://www.linkedin.com/in/samruddhiidhoot" target="_blank" class="contact-link">
        <div class="contact-icon">in</div> linkedin.com/in/samruddhiidhoot
      </a>
      <a href="https://github.com/samruddhidhoot" target="_blank" class="contact-link">
        <div class="contact-icon">⌥</div> github.com/samruddhidhoot
      </a>
      <div class="contact-link non-link">
        <div class="contact-icon">📍</div> Hyderabad, Telangana, India
      </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="resume-card">
      <div class="resume-icon">📄</div>
      <h3>My Resume</h3>
      <p>Download my full resume with detailed experience, skills, and education history.</p>
    </div>
    """, unsafe_allow_html=True)
    dl = get_pdf_download_link()
    if dl:
        st.markdown(dl, unsafe_allow_html=True)
    else:
        st.markdown("""
        <p style="color:var(--muted);font-size:12px;margin-top:12px;">
        Place <code>Samruddhi_Dhoot_CV-1.pdf</code> in the <code>assets/</code> folder to enable download.
        </p>
        """, unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────
st.markdown("""
<footer>
  <p>Designed &amp; built by <span>Samruddhi Dhoot</span> · samruddhi1222@gmail.com</p>
</footer>
""", unsafe_allow_html=True)