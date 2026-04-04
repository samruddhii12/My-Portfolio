import streamlit as st
import base64
import os

st.set_page_config(
    page_title="Samruddhi Dhoot — Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Get base64 PDF for download
def get_pdf_download_link():
    pdf_path = r"C:\\Users\\Shree\\Desktop\\Python\\Python_projects\\sam_portfolio\\assets\\Samruddhi_Dhoot_CV-1.pdf"
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            pdf_data = base64.b64encode(f.read()).decode()
        return f'<a href="data:application/pdf;base64,{pdf_data}" download="Samruddhi_Dhoot_Resume.pdf" class="btn btn-primary">↓ Download Resume</a>'
    return ""

load_css()

# ── HERO ──────────────────────────────────────────────
st.markdown("""
<div class="hero-section">
  <div class="hero-tag">🟢 Open to opportunities</div>
  <h1 class="hero-name"><span class="name-solid">Samruddhi</span><br><span class="name-outline">Dhoot</span></h1>
  <p class="hero-role"><em>Senior Data Analyst & AI/DS Engineer</em></p>
  <p class="hero-desc">
    B.E. in Artificial Intelligence & Data Science (CGPA 8.8) ·
    Building ETL pipelines, interactive dashboards, and ML-powered systems
    at the intersection of data and design.
  </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    st.markdown('<a href="#contact" class="btn btn-primary">Get in touch ↗</a>', unsafe_allow_html=True)
with col2:
    st.markdown(get_pdf_download_link(), unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── ABOUT ─────────────────────────────────────────────
st.markdown('<p class="section-label">01 / About</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Who I am</h2>', unsafe_allow_html=True)

c1, c2 = st.columns([3, 2])
with c1:
    st.markdown("""
    <div class="about-text">
      <p>I graduated in 2024 with a B.E. in <strong>Artificial Intelligence & Data Science</strong> 
      with an excellent CGPA of <strong>8.8</strong>. My passion lies at the crossroads of 
      data engineering and intelligent systems.</p>
      <p>Currently at <strong>Cube Green Energy</strong> as a Senior Data Analyst Associate, 
      I design and maintain <strong>ETL/ELT pipelines</strong>, develop SQL-driven analytics 
      datasets, and build large-scale web applications using Dash with custom JS & CSS to 
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
        ("Python", "accent"), ("R", "accent"), ("DSA", ""), ("OOP", ""),
        ("HTML", ""), ("CSS", ""), ("JavaScript", "")
    ],
    "Data & Databases": [
        ("MySQL", "accent"), ("PL/SQL", "accent"), ("MongoDB", "accent"),
        ("ETL / ELT Pipelines", ""), ("Database Management", "")
    ],
    "Data Science & ML": [
        ("Machine Learning", "teal"), ("NLP", "teal"), ("Data Analytics", "teal"),
        ("Information Retrieval", "teal"), ("Stock Market Analysis", ""),
        ("Web Scraping", ""), ("API Development", "")
    ],
    "Visualization & Frameworks": [
        ("Power BI", "accent"), ("Plotly Dash", "accent"), ("Streamlit", "accent"),
        ("Pandas", ""), ("NumPy", "")
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
        "tags": ["ETL Pipelines", "SQL", "Plotly Dash", "Dashboards"]
    },
    {
        "period": "Dec 2024 — Nov 2025",
        "company": "Cube Green Energy",
        "role": "Data Analytics Intern",
        "location": "Hyderabad, Telangana, India",
        "desc": "Contributed to data analytics workflows, pipeline development, and building the foundation of dashboarding capabilities used in production.",
        "tags": ["Data Analytics", "Python", "Power BI"]
    },
    {
        "period": "Jan 2024 — Mar 2024",
        "company": "MaticAlgos",
        "role": "Python Intern",
        "location": "Pune, Maharashtra, India",
        "desc": "Developed web scrapers and APIs for collecting OHLCV data from trading websites. Gained strong understanding of stock market mechanics, technical analysis, and production API testing.",
        "tags": ["Python", "Web Scraping", "API Testing", "Stock Market"]
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
        <span class="exp-period">{exp['period']}</span> · <span class="exp-company">{exp['company']}</span>
      </div>
      <p class="exp-role">{exp['role']}</p>
      <p class="exp-loc">📍 {exp['location']}</p>
      <p class="exp-desc">{exp['desc']}</p>
      <div class="exp-tags">{tags_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── EDUCATION ─────────────────────────────────────────
st.markdown('<p class="section-label">04 / Education</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Academic background</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="exp-item">
  <div class="exp-meta-inline">
    <span class="exp-period">Sep 2020 — Jun 2024</span> · <span class="exp-company">AISSMS IOIT, Pune</span>
  </div>
  <p class="exp-role">B.E. — Artificial Intelligence & Data Science</p>
  <p class="exp-loc">📍 Pune, Maharashtra, India</p>
  <p class="exp-desc">Graduated with CGPA 8.8 specializing in AI and Data Science. 
  Coursework covered machine learning, data engineering, NLP, and information retrieval systems.</p>
  <div class="exp-tags">
    <span class="exp-tag">CGPA: 8.8</span>
    <span class="exp-tag">AI & Data Science</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='divider'/>", unsafe_allow_html=True)

# ── CONTACT ───────────────────────────────────────────
st.markdown('<a name="contact"></a><p class="section-label">05 / Contact</p>', unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Let\'s connect</h2>', unsafe_allow_html=True)

c1, c2 = st.columns([3, 2])
with c1:
    st.markdown("""
    <h3 class="contact-heading">Always open to collaborate.</h3>
    <p class="about-text" style="margin-bottom:24px;">Whether it's a data challenge, an interesting project, or just a chat about AI and analytics — reach out. I'm excited to connect with like-minded professionals.</p>
    <div class="contact-links">
      <a href="mailto:samruddhi1222@gmail.com" class="contact-link">
        <div class="contact-icon">✉</div> samruddhi1222@gmail.com
      </a>
      <a href="https://www.linkedin.com/in/samruddhiidhoot" target="_blank" class="contact-link">
        <div class="contact-icon">in</div> linkedin.com/in/samruddhiidhoot
      </a>
      <div class="contact-link" style="pointer-events:none;">
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
    st.markdown(get_pdf_download_link(), unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────
st.markdown("""
<footer>
  <p>Designed & built by <span>Samruddhi Dhoot</span> · samruddhi1222@gmail.com</p>
</footer>
""", unsafe_allow_html=True)
