"""
CV Screener Pro — Enterprise Talent Intelligence Platform
Full Complete Production Version - Fixed All Pages, Language, Rejection, and 3D HTML Animations
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
from agents.export_agent import generate_excel_report, generate_pdf_report
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
    with col_anim:
        render_corporate_animation("Overview")

    df = load_database()
    total_records = len(df)

    # Core Metric Cards Grid
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""<div class="metric-card"><span class="metric-icon">👥</span><div class="metric-value" style="color:#00E5FF;">{total_records}</div><div class="metric-label">Total Candidates</div></div>""", unsafe_allow_html=True)
    with c2:
        if "Skor_AI" in df.columns and df["Skor_AI"].notna().any():
            avg_score = df["Skor_AI"].dropna().astype(float).mean()
            st.markdown(f"""<div class="metric-card"><span class="metric-icon">🎯</span><div class="metric-value" style="color:#7000FF;">{avg_score:.1f}</div><div class="metric-label">Average Match Index</div></div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div class="metric-card"><span class="metric-icon">🎯</span><div class="metric-value" style="color:#7000FF;">—</div><div class="metric-label">Average Match Index</div></div>""", unsafe_allow_html=True)
    with c3:
        if "Status" in df.columns:
            passed = len(df[df["Status"].str.lower().str.contains("lolos|pass|approved|recommended", na=False)])
            st.markdown(f"""<div class="metric-card"><span class="metric-icon">✅</span><div class="metric-value" style="color:#00F5A0;">{passed}</div><div class="metric-label">Passed Selection</div></div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div class="metric-card"><span class="metric-icon">✅</span><div class="metric-value" style="color:#00F5A0;">—</div><div class="metric-label">Passed Selection</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="metric-card"><span class="metric-icon">⚡</span><div class="metric-value" style="color:#FF007A;">100%</div><div class="metric-label">AI Agent Health</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts Presentation
    col_chart1, col_chart2 = st.columns([3, 2])
    with col_chart1:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📊 Score Curve Allocation</div>', unsafe_allow_html=True)
        if "Skor_AI" in df.columns and df["Skor_AI"].notna().any():
            scores = df["Skor_AI"].dropna().astype(float)
            bins = pd.cut(scores, bins=[0,30,50,70,85,100], labels=["0-30","31-50","51-70","71-85","86-100"])
            chart_data = bins.value_counts().sort_index().reset_index()
            chart_data.columns = ["Score Range", "Count"]
            st.bar_chart(chart_data.set_index("Score Range"), color="#00E5FF")
        else:
            st.info("No screening logs available yet. Execute AI Candidate Screener to stream metrics.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_chart2:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🗂️ Department Distribution</div>', unsafe_allow_html=True)
        if "Departemen" in df.columns and not df["Departemen"].dropna().empty:
            dept_count = df["Departemen"].value_counts().head(5)
            st.bar_chart(dept_count, color="#7000FF")
        else:
            st.info("Department analytics empty.")
        st.markdown('</div>', unsafe_allow_html=True)

    # Reporting Actions
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📥 Global Export Matrix</div>', unsafe_allow_html=True)
    col_e1, col_e2, col_e3 = st.columns(3)
    with col_e1:
        if not df.empty:
            excel_bytes = generate_excel_report(df, "Executive Core Report")
            st.download_button("📊 Export System to Excel (.xlsx)", data=excel_bytes, file_name=f"Enterprise_Report_{datetime.now().strftime('%Y%m%d')}.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", use_container_width=True)
    with col_e2:
        if not df.empty:
            pdf_bytes = generate_pdf_report(df, "Executive Corporate Data")
            st.download_button("📄 Export Dashboard to PDF (.pdf)", data=pdf_bytes, file_name=f"Enterprise_Report_{datetime.now().strftime('%Y%m%d')}.pdf", mime="application/pdf", use_container_width=True)
    with col_e3:
        if st.button("🔄 Sync Cloud Data", use_container_width=True):
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# PAGE 2: MASTER DATA EXPLORER
# ══════════════════════════════════════════════════════════════════
elif "Master Data Explorer" in page:
    logger.info("NAV: Navigated to Master Data Explorer")

    col_title, col_anim = st.columns([2, 1])
    with col_title:
        st.markdown("""
        <div class="page-header" style="margin-top:10px;">
            <h1 style="font-size:38px; font-weight:800; color:white; margin-bottom:4px;">🗄️ Master Data Explorer</h1>
            <p style="color:#94A3B8; font-size:15px;">Enterprise ledger containing comprehensive structural talent indexes.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_anim:
        render_corporate_animation("Master Data")

    df = load_database()

    if df.empty:
        st.info("📭 Structural cloud database is currently unpopulated. Add records via Management Input.")
    else:
        with st.expander("🔎 Advanced Multi-Filter Grid", expanded=True):
            col_f1, col_f2, col_f3 = st.columns(3)
            with col_f1:
                search_query = st.text_input("🔍 Filter by ID / Name", "")
            with col_f2:
                pos_opts = ["All Positions"] + sorted(df["Posisi"].dropna().astype(str).unique().tolist()) if "Posisi" in df.columns else ["All Positions"]
                pos_filter = st.selectbox("Corporate Position", pos_opts)
            with col_f3:
                status_opts = ["All Statuses"] + sorted(df["Status"].dropna().astype(str).unique().tolist()) if "Status" in df.columns else ["All Statuses"]
                status_filter = st.selectbox("HR Stage Status", status_opts)

        filtered_df = df.copy()
        if search_query:
            mask = filtered_df.apply(lambda r: search_query.lower() in str(r).lower(), axis=1)
            filtered_df = filtered_df[mask]
        if pos_filter != "All Positions" and "Posisi" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Posisi"] == pos_filter]
        if status_filter != "All Statuses" and "Status" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["Status"] == status_filter]

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="section-title">📊 Records Rendered ({len(filtered_df)} items)</div>', unsafe_allow_html=True)
        display_fields = [c for c in filtered_df.columns if c not in ["resume_text", "Analisis_AI"]]
        
        renamed_df = filtered_df[display_fields].rename(columns={
            "NIP": "Candidate_ID", "Nama": "Full_Name", "Posisi": "Applied_Position",
            "Departemen": "Department", "Pendidikan": "Education", "Pengalaman_Tahun": "Experience_Yrs",
            "Universitas": "Institution", "Status": "Status_Stage", "Skor_AI": "AI_Match_Score", "Tanggal_Input": "Logged_Date"
        })
        st.dataframe(renamed_df.reset_index(drop=True), use_container_width=True, height=380)
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# PAGE 3: MANAGEMENT INPUT (WITH UNIQUE NIP DUPLICATE LOCK)
# ══════════════════════════════════════════════════════════════════
elif "Management Input" in page:
    logger.info("NAV: Navigated to Management Input")

    col_title, col_anim = st.columns([2, 1])
    with col_title:
        st.markdown("""
        <div class="page-header" style="margin-top:10px;">
            <h1 style="font-size:38px; font-weight:800; color:white; margin-bottom:4px;">➕ Workspace Data Entry</h1>
            <p style="color:#94A3B8; font-size:15px;">Append singular corporate records into the persistence core network ledger.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_anim:
        render_corporate_animation("Input")

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📋 Candidate Form Profile</div>', unsafe_allow_html=True)

    df_check = load_database()

    col_form1, col_form2 = st.columns(2)
    with col_form1:
        candidate_id = st.text_input("Candidate ID (Unique NIP) *", placeholder="e.g. 8812345678")
        full_name    = st.text_input("Full Name *", placeholder="e.g. Dewa Febrian")
        position     = st.text_input("Target Position *", placeholder="e.g. HR Business Partner")
        department   = st.text_input("Target Department *", placeholder="e.g. Human Capital")
    with col_form2:
        education    = st.selectbox("Highest Degree", ["S1", "S2", "S3", "D3", "D4", "High School"])
        institution  = st.text_input("University / Institution", placeholder="e.g. Universitas Diponegoro")
        experience   = st.number_input("Work Experience Tenure (Years)", min_value=0, max_value=40, value=0)
        stage_status = st.selectbox("Initial Selection Stage Status", ["Pending Review", "Shortlisted", "Interview Phase", "Not Recommended"])

    st.markdown("</div>", unsafe_allow_html=True)

    col_b1, col_b2, _ = st.columns([1, 1, 2])
    with col_b1:
        if st.button("💾 Write to Database", type="primary", use_container_width=True):
            if not candidate_id or not full_name or not position:
                st.error("⚠️ Constraint Violation: Candidate ID, Full Name, and Target Position are required.")
            else:
                is_duplicate = False
                if not df_check.empty and "NIP" in df_check.columns:
                    if str(candidate_id).strip() in df_check["NIP"].astype(str).str.strip().values:
                        is_duplicate = True
                
                if is_duplicate:
                    st.error(f"❌ Aborted: Candidate ID '{candidate_id}' already matches an existing ledger record. Duplicate entry blocked.")
                    logger.warning(f"INPUT: Append blocked. Duplicate NIP={candidate_id}")
                else:
                    record_payload = {
                        "NIP": candidate_id, "Nama": full_name, "Posisi": position,
                        "Departemen": department, "Pendidikan": education,
                        "Pengalaman_Tahun": experience, "Universitas": institution,
                        "Status": stage_status, "Skor_AI": None, "Analisis_AI": None,
                        "Tanggal_Input": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    if append_candidate_to_db(record_payload):
                        st.success(f"✅ Record successfully written for {full_name} ({candidate_id})!")
                        logger.info(f"INPUT: Successfully logged individual NIP={candidate_id}")
                        st.balloons()
                    else:
                        st.error("❌ Write pipeline failed. Evaluate runtime system logs for tracing info.")
    with col_b2:
        if st.button("🔄 Clear Form Canvas", use_container_width=True):
            st.rerun()


# ══════════════════════════════════════════════════════════════════
# PAGE 4: AI CANDIDATE SCREENER (WITH AUTO KEYWORD FALLBACK)
# ══════════════════════════════════════════════════════════════════
elif "AI Candidate Screener" in page:
    logger.info("NAV: Navigated to AI Candidate Screener")

    col_title, col_anim = st.columns([2, 1])
    with col_title:
        st.markdown("""
        <div class="page-header" style="margin-top:10px;">
            <h1 style="font-size:38px; font-weight:800; color:white; margin-bottom:4px;">🤖 AI Candidate Screener</h1>
            <p style="color:#94A3B8; font-size:15px;">Bulk parsing and semantic candidate ranking against strict job qualifications.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_anim:
        render_corporate_animation("Screener")

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📝 Job Requirement Mandate</div>', unsafe_allow_html=True)
    job_description = st.text_area("Paste Corporate Job Qualifications Profile", height=140, placeholder="Describe required skills, certifications, and stack (e.g. Python, SQL, HR Automation, SPSS)...", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📂 Bulk PDF Resumes Drag-and-Drop Dropzone</div>', unsafe_allow_html=True)
    uploaded_resumes = st.file_uploader("Upload Bulk Profiles", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⚡ Execute Agent Evaluation Sequence", type="primary"):
        if not job_description.strip() or not uploaded_resumes:
            st.warning("⚠️ Execution Interrupted: Provide job requirements context and drag at least 1 file.")
        else:
            openai_key_exists = False
            try:
                if "openai" in st.secrets and "api_key" in st.secrets["openai"]:
                    if st.secrets["openai"]["api_key"] and not st.secrets["openai"]["api_key"].startswith("sk-your"):
                        openai_key_exists = True
            except Exception:
                pass

            with st.spinner("⏳ Analyzing document structure arrays..."):
                if not openai_key_exists:
                    st.info("ℹ️ System Notification: OpenAI API key inactive/absent. Rerouting sequence to internal Deterministic Keyword Matching Engine.")
                    logger.info("SCREENER: OpenAI Key absent. Falling back automatically to Keyword Matching Engine.")
                
                screening_outputs = process_bulk_resumes(uploaded_resumes, job_description)
                st.session_state["active_screen_runs"] = screening_outputs
                st.success("🎉 Sequence finalized. Analytical matrix array established.")

    if "active_screen_runs" in st.session_state and st.session_state["active_screen_runs"]:
        runs = st.session_state["active_screen_runs"]
        st.markdown("<br><h3 style='color:white;'>🏆 Ranked Structural Talent Array</h3>", unsafe_allow_html=True)

        for rank, item in enumerate(runs):
            score_index = item["score"]
            medal_badge = {0: "🥇 Rank 1", 1: "🥈 Rank 2", 2: "🥉 Rank 3"}.get(rank, f"🏅 Rank {rank+1}")
            
            st.markdown(f"""
            <div class="metric-card" style="margin-bottom:15px; border-left:4px solid #00E5FF;">
                <div style="display:flex; justify-content:between; align-items:center;">
                    <div style="flex:1;">
                        <span style="background:rgba(0,229,255,0.1); color:#00E5FF; padding:4px 8px; border-radius:6px; font-size:11px; font-weight:700;">{medal_badge}</span>
                        <h4 style="margin:10px 0 2px; color:white; font-size:18px;">{item['candidate_name']}</h4>
                        <small style="color:#6B7A9A;">📁 Source File: {item['filename']}</small>
                    </div>
                    <div style="text-align:right;">
                        <div style="font-size:32px; font-weight:800; color:#00F5A0;">{score_index}</div>
                        <small style="color:#94A3B8; letter-spacing:1px; text-transform:uppercase; font-size:9px;">Match Score</small>
                    </div>
                </div>
                <div style="background:rgba(255,255,255,0.02); padding:12px; border-radius:8px; margin-top:12px; font-size:13px; color:#E2E8F0; line-height:1.5;">
                    💡 <strong>System Evaluation Analysis:</strong> {item['analysis']}
                </div>
            </div>
            """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# PAGE 5: SYSTEM OPERATIONS LOG
# ══════════════════════════════════════════════════════════════════
elif "System Operations Log" in page:
    logger.info("NAV: Navigated to System Logs")

    st.markdown("""
    <div class="page-header" style="margin-top:10px;">
        <h1 style="font-size:38px; font-weight:800; color:white; margin-bottom:4px;">📊 System Operations Log</h1>
        <p style="color:#94A3B8; font-size:15px;">Real-time diagnostics tracking core telemetry matrix arrays of background sub-agents.</p>
    </div>
    """, unsafe_allow_html=True)

    log_records = read_logs(150)
    
    col_l1, col_l2, _ = st.columns([1, 1, 4])
    with col_l1:
        if st.button("🔄 Force Reload Logs", use_container_width=True):
            st.rerun()
    with col_l2:
        if st.button("🗑️ Wipe Active Logs", use_container_width=True):
            clear_logs()
            st.rerun()

    html_log_array = []
    for line in log_records:
        style_class = "log-line-default"
        if "[ERROR]" in line: style_class = "log-line-error"
        elif "[WARNING]" in line: style_class = "log-line-warning"
        elif "[INFO]" in line: style_class = "log-line-info"
        
        sanitized_line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html_log_array.append(f'<div class="{style_class}">{sanitized_line}</div>')

    terminal_block = '<div class="log-terminal">' + "\n".join(html_log_array) + "</div>"
    st.markdown(terminal_block, unsafe_allow_html=True)
