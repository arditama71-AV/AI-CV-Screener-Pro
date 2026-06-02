"""
CV Screener Pro — Enterprise Talent Intelligence Platform
Full Complete Production Version - Fixed All Pages, Language, Rejection, and 3D HTML Animations
Combined with Bulletproof PDF V2 Engine Bypass & Fixed Colon Bracket 115
"""
import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# Ensure project root is in path safely
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from utils.auth import require_auth, logout
from utils.logger import get_logger, read_logs, clear_logs
from utils.data_utils import load_database, append_candidate_to_db
from agents.architect_agent import process_bulk_resumes
from agents.export_agent import generate_excel_report, generate_pdf_report_v2
from assets.styles import PREMIUM_CSS

logger = get_logger("main_app")

st.set_page_config(
    page_title="CV Screener Pro",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Fixed Premium CSS
st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

# Authentication Gate
if not require_auth():
    st.stop()

logger.info("APP: Corporate Dashboard fully loaded.")

# ==============================================================================
# PREMIUM KORPORAT MULTI-PAGE ANIMATION ENGINE (HTML EMBED METHOD)
# ==============================================================================
def render_corporate_animation(page_name):
    """Menampilkan animasi gedung perkantoran & korporat mewah berbasis HTML murni"""
    if page_name == "Overview":
        embed_url = "https://embed.lottiefiles.com/animation/95602" # HQ Building Sky
    elif page_name == "Master Data":
        embed_url = "https://embed.lottiefiles.com/animation/68233" # Analytics Tower
    elif page_name == "Input":
        embed_url = "https://embed.lottiefiles.com/animation/93638" # Office Workspace Desk
    else:
        embed_url = "https://embed.lottiefiles.com/animation/41983" # Tech Scanner Hub
        
    html_code = f"""
    <div style="display: flex; justify-content: center; align-items: center; background: transparent;">
        <iframe src="{embed_url}" style="border: none; width: 100%; height: 180px; background: transparent;" allowtransparency="true"></iframe>
    </div>
    """
    st.components.v1.html(html_code, height=185)

# ──────────────────────────────
# FIXED SIDEBAR NAVIGATION
# ──────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="logo-icon">🏢</div>
        <div class="logo-name">CV Screener Pro</div>
        <div class="logo-sub">TalentAI · Enterprise</div>
    </div>
    """, unsafe_allow_html=True)

    # User identity profile
    st.markdown(f"""
    <div class="user-profile-badge">
        <span style="font-size: 18px;">👤</span>
        <div class="user-profile-text">
            <span class="user-name-title">{st.session_state.get('username','admin').title()}</span>
            <span class="user-role-sub">Executive Administrator</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<p class='nav-header-text'>Navigation Panel</p>", unsafe_allow_html=True)

    page = st.radio("", [
        "🏠  Executive Overview",
        "🗄️  Master Data Explorer",
        "➕  Management Input",
        "🤖  AI Candidate Screener",
        "📊  System Operations Log"
    ], label_visibility="collapsed")

    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    if st.button("🔒 Sign Out Account", use_container_width=True):
        logout()
        
    st.markdown(f"<p class='version-text'>v4.1.0 · {datetime.now().strftime('%d %b %Y')}</p>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# PAGE 1: EXECUTIVE OVERVIEW (BERANDA)
# ══════════════════════════════════════════════════════════════════
if "Executive Overview" in page:
    logger.info("NAV: Navigated to Executive Overview")

    col_title, col_anim = st.columns([2, 1])
    with col_title:
        st.markdown("""
        <div class="page-header" style="margin-top:10px;">
            <h1 style="font-size:38px; font-weight:800; color:white; margin-bottom:4px;">🏢 Headquarter Overview</h1>
            <p style="color:#94A3B8; font-size:15px;">Real-time asset management control room and core talent analytical network.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_anim: # <-- FIXED COLON HERE (BARIS 115)
        render_corporate_animation("Overview")

    df = load_database()
    total_records = len(df)

    # Core Metric Cards Grid
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="metric-card"><span class="metric-icon">👥</span><div class="metric-value" style="color:#00E5FF;">{total_records}</div><div class="metric-label">Total Candidates</div></div>', unsafe_allow_html=True)
    with c2:
        if "Skor_AI" in df.columns and df["Skor_AI"].notna().any():
            avg_score = df["Skor_AI"].dropna().astype(float).mean()
            st.markdown(f'<div class="metric-card"><span class="metric-icon">🎯</span><div class="metric-value" style="color:#7000FF;">{avg_score:.1f}</div><div class="metric-label">Average Match Index</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="metric-card"><span class="metric-icon">🎯</span><div class="metric-value" style="color:#7000FF;">—</div><div class="metric-label">Average Match Index</div></div>', unsafe_allow_html=True)
    with c3:
        if "Status" in df.columns:
            passed = len(df[df["Status"].str.lower().
