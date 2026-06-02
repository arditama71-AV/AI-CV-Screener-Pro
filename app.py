"""
AI CV Screener Pro — Cinematic Edition v5.0
Each page has its own animated 3D-feel scene
"""
import streamlit as st
import pandas as pd
from datetime import datetime
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.auth import require_auth, logout
from utils.logger import get_logger, read_logs, clear_logs, LOG_FILE
from utils.data_utils import load_database, append_candidate_to_db, radar_header_detect
from agents.export_agent import generate_excel_report, generate_pdf_report
from assets.styles import PREMIUM_CSS

logger = get_logger("main_app")

st.set_page_config(
    page_title="CV Screener Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

if not require_auth():
    st.stop()

logger.info("APP: Dashboard session started.")

# ══════════════════════════════════════════════════════════════════
#  CINEMATIC SCENE TEMPLATES (plain strings — no f-string braces issue)
# ══════════════════════════════════════════════════════════════════

SCENE_OVERVIEW = """
<div class="hero-scene scene-overview">
  <div class="stars-layer-1">
    <span class="star" style="top:10%;left:5%;width:2px;height:2px"></span>
    <span class="star" style="top:25%;left:15%;width:1px;height:1px;animation-delay:.5s"></span>
    <span class="star" style="top:60%;left:8%;width:2px;height:2px;animation-delay:1.2s"></span>
    <span class="star" style="top:80%;left:20%;width:1px;height:1px;animation-delay:.8s"></span>
    <span class="star" style="top:15%;left:30%;width:2px;height:2px;animation-delay:1.8s"></span>
    <span class="star" style="top:45%;left:38%;width:1px;height:1px;animation-delay:.3s"></span>
    <span class="star" style="top:75%;left:45%;width:2px;height:2px;animation-delay:2.1s"></span>
    <span class="star" style="top:20%;left:55%;width:1px;height:1px;animation-delay:1.5s"></span>
    <span class="star" style="top:55%;left:65%;width:2px;height:2px;animation-delay:.6s"></span>
    <span class="star" style="top:85%;left:72%;width:1px;height:1px;animation-delay:1.9s"></span>
    <span class="star" style="top:30%;left:85%;width:2px;height:2px;animation-delay:.4s"></span>
    <span class="star" style="top:65%;left:92%;width:1px;height:1px;animation-delay:2.3s"></span>
    <span class="star" style="top:40%;left:48%;width:2px;height:2px;animation-delay:1.1s"></span>
    <span class="star" style="top:90%;left:60%;width:1px;height:1px;animation-delay:.2s"></span>
  </div>
  <div class="stars-layer-2">
    <span class="star big-star" style="top:20%;left:12%;animation-delay:.2s"></span>
    <span class="star big-star amber" style="top:50%;left:28%;animation-delay:1.4s"></span>
    <span class="star big-star" style="top:35%;left:58%;animation-delay:.9s"></span>
    <span class="star big-star purple" style="top:70%;left:82%;animation-delay:1.7s"></span>
  </div>
  <div class="planet planet-purple"></div>
  <div class="planet planet-amber"></div>
  <div class="shooting-star"></div>
  <div class="rocket-wrap">
    <svg width="60" height="80" viewBox="0 0 60 80" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="30" cy="35" rx="11" ry="22" fill="#E2E8F0"/>
      <path d="M30 13 Q20 25 19 35 L41 35 Q40 25 30 13" fill="#F1F5FF"/>
      <circle cx="30" cy="32" r="5" fill="#0EA5E9" stroke="#0369A1" stroke-width="1.5"/>
      <circle cx="30" cy="32" r="2.5" fill="#7DD3FC"/>
      <path d="M19 50 L11 60 L19 60 Z" fill="#EF4444"/>
      <path d="M41 50 L49 60 L41 60 Z" fill="#EF4444"/>
      <path d="M25 55 L35 55 L33 62 L27 62 Z" fill="#1E3A8A"/>
      <g class="rocket-flame">
        <path d="M25 60 Q30 75 35 60 Q33 68 30 70 Q27 68 25 60" fill="#F59E0B"/>
        <path d="M27 60 Q30 72 33 60 Q31 66 30 67 Q29 66 27 60" fill="#FCD34D"/>
        <path d="M28 60 Q30 68 32 60" fill="white"/>
      </g>
    </svg>
  </div>
  <div class="scene-text">
    <div class="scene-eyebrow"><span class="live-pulse"></span>LIVE DASHBOARD</div>
    <div class="scene-title">Selamat Datang!</div>
    <div class="scene-sub">Real-time talent intelligence · Powered by AI</div>
  </div>
</div>
"""

SCENE_MASTER = """
<div class="hero-scene scene-master">
  <div class="sun"></div>
  <div class="cloud c1"></div>
  <div class="cloud c2"></div>
  <div class="cloud c3"></div>
  <div class="cloud c4"></div>
  <div class="plane-wrap">
    <svg width="80" height="40" viewBox="0 0 80 40" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="42" cy="20" rx="32" ry="6" fill="white"/>
      <path d="M10 20 L0 14 L0 26 Z" fill="#E2E8F0"/>
      <path d="M30 14 L20 4 L18 4 L24 16 Z" fill="#94A3B8"/>
      <path d="M30 26 L20 36 L18 36 L24 24 Z" fill="#94A3B8"/>
      <path d="M55 16 L60 8 L62 8 L60 18 Z" fill="#64748B"/>
      <path d="M55 24 L60 32 L62 32 L60 22 Z" fill="#64748B"/>
      <ellipse cx="62" cy="20" rx="6" ry="4" fill="#0EA5E9"/>
      <rect x="20" y="18" width="3" height="4" fill="#0EA5E9"/>
      <rect x="27" y="18" width="3" height="4" fill="#0EA5E9"/>
      <rect x="34" y="18" width="3" height="4" fill="#0EA5E9"/>
      <rect x="41" y="18" width="3" height="4" fill="#0EA5E9"/>
      <rect x="48" y="18" width="3" height="4" fill="#0EA5E9"/>
    </svg>
  </div>
  <div class="scene-text scene-text-light">
    <div class="scene-eyebrow"><span class="live-pulse"></span>DATABASE EXPLORER</div>
    <div class="scene-title">Master Data</div>
    <div class="scene-sub">Soar through your candidate records</div>
  </div>
</div>
"""

SCENE_INPUT = """
<div class="hero-scene scene-input">
  <div class="paper p1"></div>
  <div class="paper p2"></div>
  <div class="paper p3"></div>
  <div class="paper p4"></div>
  <div class="paper p5"></div>
  <span class="spark sp1"></span>
  <span class="spark sp2"></span>
  <span class="spark sp3"></span>
  <span class="spark sp4"></span>
  <div class="scene-text">
    <div class="scene-eyebrow"><span class="live-pulse"></span>DATA ENTRY</div>
    <div class="scene-title">Input Data</div>
    <div class="scene-sub">Add new candidate records seamlessly</div>
  </div>
</div>
"""

SCENE_AI = """
<div class="hero-scene scene-ai">
  <div class="brain-core">
    <div class="brain-ring r1"></div>
    <div class="brain-ring r2"></div>
    <div class="brain-ring r3"></div>
  </div>
  <svg class="neural-net" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
    <line x1="15%" y1="30%" x2="45%" y2="20%" stroke="#38BDF8" stroke-width="1"/>
    <line x1="15%" y1="30%" x2="45%" y2="50%" stroke="#38BDF8" stroke-width="1"/>
    <line x1="15%" y1="60%" x2="45%" y2="50%" stroke="#22D3EE" stroke-width="1"/>
    <line x1="15%" y1="60%" x2="45%" y2="80%" stroke="#22D3EE" stroke-width="1"/>
    <line x1="45%" y1="20%" x2="78%" y2="35%" stroke="#7000FF" stroke-width="1"/>
    <line x1="45%" y1="50%" x2="78%" y2="35%" stroke="#22D3EE" stroke-width="1"/>
    <line x1="45%" y1="50%" x2="78%" y2="65%" stroke="#38BDF8" stroke-width="1"/>
    <line x1="45%" y1="80%" x2="78%" y2="65%" stroke="#38BDF8" stroke-width="1"/>
  </svg>
  <span class="ai-node n1"></span>
  <span class="ai-node n2"></span>
  <span class="ai-node n3"></span>
  <span class="ai-node n4"></span>
  <span class="ai-node n5"></span>
  <span class="ai-node n6"></span>
  <span class="ai-node n7"></span>
  <div class="scene-text">
    <div class="scene-eyebrow"><span class="live-pulse"></span>AI POWERED</div>
    <div class="scene-title">AI CV Screener</div>
    <div class="scene-sub">Claude analyzes every resume</div>
  </div>
</div>
"""

SCENE_LOGS = """
<div class="hero-scene scene-logs">
  <div class="matrix-col" style="left:8%;animation-duration:8s">01010110<br>11001010<br>00110101<br>10011010<br>01101100</div>
  <div class="matrix-col" style="left:22%;animation-duration:6s;animation-delay:1s">10110010<br>01010101<br>11100110<br>00101110<br>10110101</div>
  <div class="matrix-col" style="left:36%;animation-duration:10s;animation-delay:.5s">11000101<br>01101010<br>10010110<br>11110000<br>01010101</div>
  <div class="matrix-col" style="left:55%;animation-duration:7s;animation-delay:2s">01101001<br>10110011<br>01010111<br>10001010<br>11100110</div>
  <div class="matrix-col" style="left:70%;animation-duration:9s;animation-delay:.3s">10101010<br>01010101<br>11001100<br>00110011<br>10010110</div>
  <div class="matrix-col" style="left:85%;animation-duration:5s;animation-delay:1.5s">01010101<br>10101010<br>11110000<br>00001111<br>10110101</div>
  <div class="scene-text">
    <div class="scene-eyebrow"><span class="live-pulse"></span>MONITOR</div>
    <div class="scene-title">System Logs</div>
    <div class="scene-sub">Real-time agent health stream</div>
  </div>
</div>
"""

SCENES = {
    "overview": SCENE_OVERVIEW,
    "master":   SCENE_MASTER,
    "input":    SCENE_INPUT,
    "ai":       SCENE_AI,
    "logs":     SCENE_LOGS,
}


# ══════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════
def render_sidebar():
    with st.sidebar:
        uname   = st.session_state.get("username", "admin").title()
        initial = uname[0].upper()

        st.markdown(f"""
        <div class="sb-logo">
          <div class="sb-logo-mark">⚡</div>
          <div class="sb-logo-text">
            <div class="sb-logo-name">CV Screener Pro</div>
            <div class="sb-logo-sub">TalentAI Enterprise</div>
          </div>
        </div>
        <div class="sb-user">
          <div class="sb-avatar">{initial}</div>
          <div>
            <div class="sb-user-name">{uname}</div>
            <div class="sb-user-role">Administrator</div>
          </div>
        </div>
        <div class="sb-section-label">Menu</div>
        """, unsafe_allow_html=True)

        page = st.radio("nav", [
            "🏠  Overview",
            "🗄️  Master Data",
            "➕  Input Data",
            "🤖  AI Screener",
            "📊  System Logs",
        ], label_visibility="collapsed")

        st.markdown(f"""
        <div class="sb-divider"></div>
        <div class="sb-footer">v5.0.0 · {datetime.now().strftime('%d %b %Y')}</div>
        """, unsafe_allow_html=True)

        if st.button("Sign Out", use_container_width=True):
            logout()

    return page

page = render_sidebar()


# ══════════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════════
def render_scene(scene_key):
    """Render the cinematic hero scene for the current page."""
    st.markdown(SCENES.get(scene_key, ""), unsafe_allow_html=True)


def metric_card(icon, value, label, accent="blue", badge=None):
    accent_map = {
        "blue":  ("accent-blue",  "mv-blue"),
        "cyan":  ("accent-cyan",  "mv-cyan"),
        "green": ("accent-green", "mv-green"),
        "amber": ("accent-amber", "mv-amber"),
        "white": ("accent-blue",  "mv-white"),
    }
    ac, vc = accent_map.get(accent, ("accent-blue", "mv-blue"))
    badge_html = f'<div class="metric-badge">▲ {badge}</div>' if badge else ""
    return f"""
    <div class="metric-card">
      <div class="metric-card-accent {ac}"></div>
      <span class="metric-icon">{icon}</span>
      <div class="metric-value {vc}">{value}</div>
      <div class="metric-label">{label}</div>
      {badge_html}
    </div>"""


def score_cls(s):
    return "score-high" if s >= 75 else ("score-mid" if s >= 50 else "score-low")


def rec_chip(rec):
    m = {
        "Highly Recommended": ("chip-green",  "Highly Recommended"),
        "Recommended":        ("chip-blue",   "Recommended"),
        "Review Further":     ("chip-yellow", "Review Further"),
        "Not Recommended":    ("chip-red",    "Not Recommended"),
    }
    cls, lbl = m.get(rec, ("chip-yellow", rec))
    return f'<span class="chip {cls}">{lbl}</span>'


def skill_pills(skills):
    if not skills:
        return '<span style="color:var(--text-disabled);font-size:11px;">—</span>'
    return "".join(f'<span class="skill-pill">{s}</span>' for s in skills[:6])


# ══════════════════════════════════════════════════════════════════
#  PAGE 1 — OVERVIEW (rocket through stars)
# ══════════════════════════════════════════════════════════════════
if "Overview" in page:
    logger.info("NAV: Overview")
    render_scene("overview")

    df = load_database()
    total = len(df)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(metric_card("👥", total, "Total Candidates", "blue", "All Records"), unsafe_allow_html=True)
    with c2:
        if "Skor_AI" in df.columns and df["Skor_AI"].notna().any():
            avg = df["Skor_AI"].dropna().astype(float).mean()
            st.markdown(metric_card("🎯", f"{avg:.1f}", "Avg AI Score", "cyan"), unsafe_allow_html=True)
        else:
            st.markdown(metric_card("🎯", "—", "Avg AI Score", "cyan"), unsafe_allow_html=True)
    with c3:
        if "Status" in df.columns:
            lolos = len(df[df["Status"].str.lower().str.contains("lolos|pass|approved|diterima", na=False)])
            st.markdown(metric_card("✅", lolos, "Passed Screening", "green"), unsafe_allow_html=True)
        else:
            st.markdown(metric_card("✅", "—", "Passed Screening", "green"), unsafe_allow_html=True)
    with c4:
        n = df["Posisi"].nunique() if "Posisi" in df.columns else "—"
        st.markdown(metric_card("💼", n, "Open Positions", "amber"), unsafe_allow_html=True)

    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    col_a, col_b = st.columns([3, 2])
    with col_a:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📊 AI Score Distribution</div>', unsafe_allow_html=True)
        if "Skor_AI" in df.columns and df["Skor_AI"].notna().any():
            scores = df["Skor_AI"].dropna().astype(float)
            bins = pd.cut(scores, bins=[0,30,50,70,85,100],
                          labels=["0–30","31–50","51–70","71–85","86–100"])
            cd = bins.value_counts().sort_index().reset_index()
            cd.columns = ["Range","Count"]
            st.bar_chart(cd.set_index("Range"), color="#38BDF8")
        else:
            st.info("Run AI Screener to generate scores.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🗂️ Position Breakdown</div>', unsafe_allow_html=True)
        if "Posisi" in df.columns and not df["Posisi"].dropna().empty:
            st.bar_chart(df["Posisi"].value_counts().head(8), color="#22D3EE")
        else:
            st.info("No position data yet.")
        st.markdown('</div>', unsafe_allow_html=True)

    if "Skor_AI" in df.columns and df["Skor_AI"].notna().any():
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🏆 Top Candidates by AI Score</div>', unsafe_allow_html=True)
        top_cols = [c for c in ["NIP","Nama","Posisi","Departemen","Skor_AI","Status"] if c in df.columns]
        top_df = df.nlargest(5, "Skor_AI")[top_cols].reset_index(drop=True)
        top_df.index += 1
        st.dataframe(top_df, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📥 Export Report</div>', unsafe_allow_html=True)
    ec1, ec2, ec3 = st.columns(3)
    with ec1:
        if not df.empty:
            st.download_button("📊 Export Excel", data=generate_excel_report(df, "Executive Report"),
                file_name=f"CV_Report_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True)
    with ec2:
        if not df.empty:
            st.download_button("📄 Export PDF", data=generate_pdf_report(df, "Executive Report"),
                file_name=f"CV_Report_{datetime.now().strftime('%Y%m%d')}.pdf",
                mime="application/pdf", use_container_width=True)
    with ec3:
        if st.button("↺ Refresh", use_container_width=True):
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
#  PAGE 2 — MASTER DATA (plane through clouds)
# ══════════════════════════════════════════════════════════════════
elif "Master Data" in page:
    logger.info("NAV: Master Data")
    render_scene("master")

    df = load_database()
    if df.empty:
        st.info("Database is empty. Add candidates via Input Data.")
    else:
        with st.expander("Filter & Search", expanded=True):
            fc1, fc2, fc3, fc4 = st.columns(4)
            with fc1: search = st.text_input("Search name or NIP", "")
            with fc2:
                p_opts = ["All"] + (sorted(df["Posisi"].dropna().unique().tolist())
                                    if "Posisi" in df.columns else [])
                p_f = st.selectbox("Position", p_opts)
            with fc3:
                d_opts = ["All"] + (sorted(df["Departemen"].dropna().unique().tolist())
                                    if "Departemen" in df.columns else [])
                d_f = st.selectbox("Department", d_opts)
            with fc4:
                s_opts = ["All"] + (sorted(df["Status"].dropna().unique().tolist())
                                    if "Status" in df.columns else [])
                s_f = st.selectbox("Status", s_opts)

        fil = df.copy()
        if search:
            fil = fil[fil.apply(lambda r: search.lower() in str(r).lower(), axis=1)]
        if p_f != "All" and "Posisi" in fil.columns:
            fil = fil[fil["Posisi"] == p_f]
        if d_f != "All" and "Departemen" in fil.columns:
            fil = fil[fil["Departemen"] == d_f]
        if s_f != "All" and "Status" in fil.columns:
            fil = fil[fil["Status"] == s_f]

        sc1, sc2, sc3 = st.columns(3)
        with sc1: st.markdown(metric_card("📋", len(fil), "Filtered Results", "blue"), unsafe_allow_html=True)
        with sc2:
            if "Skor_AI" in fil.columns and fil["Skor_AI"].notna().any():
                avg = fil["Skor_AI"].dropna().astype(float).mean()
                st.markdown(metric_card("🎯", f"{avg:.1f}", "Avg Score", "cyan"), unsafe_allow_html=True)
            else:
                st.markdown(metric_card("🎯", "—", "Avg Score", "cyan"), unsafe_allow_html=True)
        with sc3:
            st.markdown(metric_card("💾", len(df), "Total in DB", "green"), unsafe_allow_html=True)

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="section-title">Candidates — {len(fil)} records</div>', unsafe_allow_html=True)
        disp = [c for c in fil.columns if c not in ["resume_text","Analisis_AI"]]
        st.dataframe(fil[disp].reset_index(drop=True), use_container_width=True, height=400)
        st.markdown('</div>', unsafe_allow_html=True)

        dc1, dc2 = st.columns(2)
        with dc1:
            st.download_button("📊 Export Excel",
                data=generate_excel_report(fil[disp], "Master Data"),
                file_name=f"CV_MasterData_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True)
        with dc2:
            st.download_button("📄 Export PDF",
                data=generate_pdf_report(fil[disp], "Master Data"),
                file_name=f"CV_MasterData_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                mime="application/pdf", use_container_width=True)


# ══════════════════════════════════════════════════════════════════
#  PAGE 3 — INPUT DATA (floating papers & sparkles)
# ══════════════════════════════════════════════════════════════════
elif "Input Data" in page:
    logger.info("NAV: Input Data")
    render_scene("input")

    tab1, tab2 = st.tabs(["Manual Entry", "Bulk Upload"])

    with tab1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">New Candidate Record</div>', unsafe_allow_html=True)
        ic1, ic2 = st.columns(2)
        with ic1:
            nip        = st.text_input("NIP *", placeholder="e.g. 8812345678")
            nama       = st.text_input("Full Name *", placeholder="e.g. Budi Santoso")
            posisi     = st.text_input("Position *", placeholder="e.g. Transmission Engineer")
            departemen = st.text_input("Department", placeholder="e.g. Transmission Java-Bali")
        with ic2:
            pendidikan  = st.selectbox("Education", ["S1","S2","S3","D3","D4","SMA/SMK"])
            universitas = st.text_input("University / Institution", placeholder="e.g. Universitas Indonesia")
            pengalaman  = st.number_input("Work Experience (Years)", min_value=0, max_value=50)
            status      = st.selectbox("Status", ["Pending Review","Lolos Seleksi Admin",
                                                   "Tidak Lolos","Interview","Diterima"])
        st.markdown('</div>', unsafe_allow_html=True)

        b1, b2, _ = st.columns([1, 1, 2])
        with b1:
            if st.button("Save Candidate", type="primary", use_container_width=True):
                if not nip or not nama or not posisi:
                    st.error("NIP, Name, and Position are required.")
                else:
                    existing = load_database()
                    if (not existing.empty and str(nip) in existing["NIP"].astype(str).values):
                        st.error(f"NIP {nip} already exists in the database.")
                    else:
                        rec = {
                            "NIP": nip, "Nama": nama, "Posisi": posisi, "Departemen": departemen,
                            "Pendidikan": pendidikan, "Pengalaman_Tahun": pengalaman,
                            "Universitas": universitas, "Status": status,
                            "Skor_AI": None, "Analisis_AI": None,
                            "Tanggal_Input": datetime.now().strftime("%Y-%m-%d %H:%M")
                        }
                        if append_candidate_to_db(rec):
                            st.success(f"**{nama}** (NIP: {nip}) saved successfully.")
                            logger.info(f"INPUT: NIP={nip}, Nama={nama}")
                        else:
                            st.error("Save failed. Check System Logs.")
        with b2:
            if st.button("Clear", use_container_width=True):
                st.rerun()

    with tab2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Bulk Upload · CSV or Excel</div>', unsafe_allow_html=True)
        st.info("Radar Header Detection automatically scans the first 15 rows to locate the NIP column.")
        uploaded_db = st.file_uploader("Choose file", type=["csv","xlsx","xls"])
        if uploaded_db:
            import tempfile
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_db.name)[1]) as tmp:
                tmp.write(uploaded_db.read()); tmp_path = tmp.name
            preview_df = radar_header_detect(tmp_path)
            if preview_df is not None and not preview_df.empty:
                st.success(f"{len(preview_df)} records detected.")
                st.dataframe(preview_df.head(8), use_container_width=True)
                if st.button("Import to Database", type="primary"):
                    for _, row in preview_df.iterrows():
                        r = row.to_dict()
                        r.setdefault("Tanggal_Input", datetime.now().strftime("%Y-%m-%d %H:%M"))
                        append_candidate_to_db(r)
                    st.success(f"{len(preview_df)} records imported.")
                    logger.info(f"IMPORT: {len(preview_df)} from '{uploaded_db.name}'")
            else:
                st.error("Could not find NIP column in the first 15 rows.")
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
#  PAGE 4 — AI SCREENER (neural network)
# ══════════════════════════════════════════════════════════════════
elif "AI Screener" in page:
    logger.info("NAV: AI Screener")
    render_scene("ai")

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Job Description</div>', unsafe_allow_html=True)
    jd_text = st.text_area("", height=160,
        placeholder="Paste the full job description here — requirements, responsibilities, qualifications...",
        label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Upload PDF Resumes</div>', unsafe_allow_html=True)
    uploaded_cvs = st.file_uploader("", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
    if uploaded_cvs:
        files_html = '<div style="font-size:12px;color:var(--blue-400);font-weight:500;margin-top:4px;">⚡ ' + str(len(uploaded_cvs)) + ' file(s) queued: '
        files_html += " · ".join(
            f'<code style="font-family:JetBrains Mono,monospace;font-size:10px;background:var(--bg-overlay);padding:2px 6px;border-radius:4px;color:var(--text-secondary)">{f.name}</code>'
            for f in uploaded_cvs)
        files_html += "</div>"
        st.markdown(files_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    rc, nc = st.columns([1, 3])
    with rc:
        run = st.button("⚡ Run Screening", type="primary", use_container_width=True,
                        disabled=(not uploaded_cvs or not jd_text.strip()))
    with nc:
        if not jd_text.strip():
            st.warning("Paste a Job Description to continue.")
        elif not uploaded_cvs:
            st.warning("Upload at least one PDF resume.")
        else:
            st.success(f"Ready · {len(uploaded_cvs)} resume(s) queued for analysis.")

    if run and uploaded_cvs and jd_text.strip():
        logger.info(f"SCREENER: {len(uploaded_cvs)} resumes.")
        bar = st.progress(0, text="Initializing agents...")
        results = []
        from agents.architect_agent import extract_text_from_pdf, evaluate_resume_with_ai
        for i, pdf in enumerate(uploaded_cvs):
            bar.progress((i+1)/len(uploaded_cvs), text=f"Analyzing {i+1}/{len(uploaded_cvs)} — {pdf.name}")
            text  = extract_text_from_pdf(pdf)
            cname = pdf.name.replace(".pdf","").replace("_"," ").replace("-"," ").title()
            res   = evaluate_resume_with_ai(text, jd_text, cname)
            results.append({
                "filename":       pdf.name,
                "candidate_name": cname,
                "score":          res.get("score", 0),
                "analysis":       res.get("analysis", ""),
                "skills_matched": res.get("skills_matched", []),
                "recommendation": res.get("recommendation", "Review Manually"),
            })
        results.sort(key=lambda x: x["score"], reverse=True)
        bar.progress(1.0, text="Analysis complete.")
        st.session_state["screening_results"] = results
        logger.info(f"SCREENER: Done. Top={results[0]['candidate_name']} ({results[0]['score']})")

    if st.session_state.get("screening_results"):
        results = st.session_state["screening_results"]
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="section-title" style="font-size:13px;padding:0 0 14px;margin-bottom:16px;
             border-bottom:1px solid var(--border-subtle);">
          Ranked Results
          <span style="margin-left:auto;font-size:11px;color:var(--text-tertiary);font-weight:400;">
            {len(results)} candidates evaluated
          </span>
        </div>""", unsafe_allow_html=True)

        for i, r in enumerate(results):
            rank_cls = {0:"rank-1",1:"rank-2",2:"rank-3"}.get(i,"")
            medal    = {0:"🥇",1:"🥈",2:"🥉"}.get(i, None)
            sc       = r["score"]
            badge = (f'<span class="rank-medal">{medal}</span>' if medal
                     else f'<span class="rank-num">#{i+1}</span>')

            st.markdown(f"""
            <div class="resume-card {rank_cls}">
              <div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap;">
                {badge}
                <div class="score-badge {score_cls(sc)}">{sc}</div>
                <div style="flex:1;min-width:140px;">
                  <div class="rc-name">{r['candidate_name']}</div>
                  <div class="rc-file">{r['filename']}</div>
                </div>
                <div>{rec_chip(r['recommendation'])}</div>
              </div>
              <div class="rc-analysis">{r['analysis']}</div>
              <div class="rc-skills">
                <span style="font-size:10px;color:var(--text-tertiary);margin-right:6px;font-weight:500;">SKILLS</span>
                {skill_pills(r.get('skills_matched',[]))}
              </div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

        rdf = pd.DataFrame([{
            "Rank": i+1, "Name": r["candidate_name"], "File": r["filename"],
            "AI_Score": r["score"], "Recommendation": r["recommendation"],
            "Skills": ", ".join(r.get("skills_matched",[])),
            "Analysis": r["analysis"]
        } for i,r in enumerate(results)])

        xc1, xc2, xc3 = st.columns(3)
        with xc1:
            st.download_button("📊 Export Excel",
                data=generate_excel_report(rdf,"AI Screening Results"),
                file_name=f"AI_Screening_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True)
        with xc2:
            st.download_button("📄 Export PDF",
                data=generate_pdf_report(rdf,"AI Screening Results"),
                file_name=f"AI_Screening_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                mime="application/pdf", use_container_width=True)
        with xc3:
            if st.button("💾 Save All to DB", type="primary", use_container_width=True):
                saved = 0
                for idx, r in enumerate(results):
                    rec = {
                        "NIP": f"AI-{datetime.now().strftime('%Y%m%d')}-{idx+1:04d}",
                        "Nama": r["candidate_name"], "Posisi":"—","Departemen":"—",
                        "Pendidikan":"—","Pengalaman_Tahun":0,"Universitas":"—",
                        "Status": r["recommendation"], "Skor_AI": r["score"],
                        "Analisis_AI": r["analysis"],
                        "Tanggal_Input": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    if append_candidate_to_db(rec): saved += 1
                st.success(f"{saved} results saved to database.")


# ══════════════════════════════════════════════════════════════════
#  PAGE 5 — SYSTEM LOGS (matrix rain)
# ══════════════════════════════════════════════════════════════════
elif "System Logs" in page:
    logger.info("NAV: System Logs")
    render_scene("logs")

    log_lines = read_logs(200)
    errors   = sum(1 for l in log_lines if "[ERROR]"   in l)
    warnings = sum(1 for l in log_lines if "[WARNING]" in l)
    infos    = sum(1 for l in log_lines if "[INFO]"    in l)

    lc1, lc2, lc3, lc4 = st.columns(4)
    with lc1: st.markdown(metric_card("📝", len(log_lines), "Total Entries",  "blue"),  unsafe_allow_html=True)
    with lc2: st.markdown(metric_card("ℹ️", infos,         "Info Events",    "cyan"),  unsafe_allow_html=True)
    with lc3: st.markdown(metric_card("⚠️", warnings,      "Warnings",       "amber"), unsafe_allow_html=True)
    with lc4: st.markdown(metric_card("❌", errors,        "Errors",         "white"), unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    ctrl1, ctrl2, ctrl3, _ = st.columns([1,1,1,3])
    with ctrl1:
        if st.button("↺ Refresh", use_container_width=True): st.rerun()
    with ctrl2:
        if st.button("🗑 Clear", use_container_width=True):
            clear_logs(); st.rerun()
    with ctrl3:
        n_lines = st.selectbox("Show:", [50,100,200,500], index=1, label_visibility="collapsed")

    lvl = st.radio("Level:", ["All","INFO","WARNING","ERROR","DEBUG"], horizontal=True, index=0)
    log_lines = read_logs(n_lines)
    if lvl != "All":
        log_lines = [l for l in log_lines if f"[{lvl}]" in l]

    rows = []
    for line in log_lines:
        cls = ("log-line-error"   if "[ERROR]"   in line else
               "log-line-warning" if "[WARNING]" in line else
               "log-line-info"    if "[INFO]"    in line else
               "log-line-debug"   if "[DEBUG]"   in line else "log-line-default")
        safe = line.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
        rows.append(f'<div class="{cls}">{safe}</div>')
    if not rows:
        rows = ['<div class="log-line-debug">— No entries match the selected filter —</div>']

    terminal_html = """
    <div class="log-terminal">
      <div class="log-terminal-header">
        <span class="terminal-dot td-red"></span>
        <span class="terminal-dot td-yellow"></span>
        <span class="terminal-dot td-green"></span>
        <span class="terminal-title">cv_screener_system.log</span>
      </div>
      <div class="log-body">
    """ + "\n".join(rows) + """
      </div>
    </div>"""
    st.markdown(terminal_html, unsafe_allow_html=True)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE,"rb") as f:
            st.download_button("📥 Download Log", data=f, file_name="cv_screener_system.log", mime="text/plain")
