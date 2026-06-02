"""
CV Screener Pro — Enterprise Talent Intelligence Platform
100% Fully Audited Version - Zero Long Strings - Anti-Syntax Error
"""
import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

# Safe environment path configuration
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

st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

if not require_auth():
    st.stop()

logger.info("APP: Corporate Dashboard fully verified.")

# ==============================================================================
# PREMIUM ANIMATION ENGINE (CLEAN COMPONENT DESIGN)
# ==============================================================================
def render_corporate_animation(page_name):
    if page_name == "Overview":
        embed_url = "https://embed.lottiefiles.com/animation/95602"
    elif page_name == "Master Data":
        embed_url = "https://embed.lottiefiles.com/animation/68233"
    elif page_name == "Input":
        embed_url = "https://embed.lottiefiles.com/animation/93638"
    else:
        embed_url = "https://embed.lottiefiles.com/animation/41983"
        
    html_code = f"""
    <div style="display: flex; justify-content: center; align-items: center; background: transparent;">
        <iframe src="{embed_url}" style="border: none; width: 100%; height: 180px; background: transparent;" allowtransparency="true"></iframe>
    </div>
    """
    st.components.v1.html(html_code, height=185)

# ──────────────────────────────
# SIDEBAR NAVIGATION (NO AUTO-WRAP STYLE)
# ──────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="logo-icon">🏢</div>
        <div class="logo-name">CV Screener Pro</div>
        <div class="logo-sub">TalentAI · Enterprise</div>
    </div>
    """, unsafe_allow_html=True)

    username_string = str(st.session_state.get('username', 'admin')).title()
    badge_html = f"""
    <div class="user-profile-badge">
        <span style="font-size: 18px;">👤</span>
        <div class="user-profile-text">
            <span class="user-name-title">{username_string}</span>
            <span class="user-role-sub">Executive Administrator</span>
        </div>
    </div>
    """
    st.markdown(badge_html, unsafe_allow_html=True)

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
        
    date_string = datetime.now().strftime('%d %b %Y')
    st.markdown(f"<p class='version-text'>v4.1.0 · {date_string}</p>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# PAGE 1: EXECUTIVE OVERVIEW
# ════════════════
