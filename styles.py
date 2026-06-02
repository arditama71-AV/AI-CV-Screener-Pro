"""
Premium Glassmorphism & Cyber-Dark UI Design System
Fixed Sidebar Flexbox Layout - Anti-Text-Wrapping Edition
"""

PREMIUM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

/* Global Framework Element Overrides */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: #E2E8F0 !important;
}

.stApp {
    background: radial-gradient(circle at 50% 50%, #0B132B 0%, #050814 100%) !important;
}

/* Eliminate Default Streamlit Branding Signatures */
header, footer, [data-testid="stHeader"] {
    visibility: hidden !important;
    height: 0px !important;
}

/* Sidebar Custom Premium Frame */
[data-testid="stSidebar"] {
    background-color: rgba(6, 10, 26, 0.9) !important;
    backdrop-filter: blur(25px) !important;
    -webkit-backdrop-filter: blur(25px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.04) !important;
}

.sidebar-logo {
    text-align: center;
    padding: 10px 0;
}
.logo-icon {
    font-size: 38px;
    margin-bottom: 5px;
}
.logo-name {
    font-size: 24px;
    font-weight: 800;
    background: linear-gradient(135deg, #00E5FF 0%, #7000FF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
}
.logo-sub {
    font-size: 9px;
    color: rgba(255, 255, 255, 0.35);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 2px;
}

/* FIXING SIDEBAR WRAPPING LOGIC USING FLEXBOX */
.user-profile-badge {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    background: rgba(255, 255, 255, 0.03) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    padding: 12px 16px !important;
    border-radius: 12px !important;
    margin: 15px 0 25px 0 !important;
    width: 100% !important;
}

.user-profile-text {
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
}

.user-name-title {
    font-size: 14px !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
    line-height: 1.2 !important;
}

.user-role-sub {
    font-size: 10px !important;
    color: #00E5FF !important;
    font-weight: 500 !important;
    margin-top: 2px !important;
}

.nav-header-text {
    font-size: 10px !important;
    color: rgba(255, 255, 255, 0.4) !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    margin: 10px 4px !important;
}

.version-text {
    font-size: 10px !important;
    color: rgba(255, 255, 255, 0.25) !important;
    text-align: center !important;
    margin-top: 20px !important;
}

/* Premium High-Fidelity Glassmorphism Cards Layout */
.metric-card {
    background: rgba(255, 255, 255, 0.02) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 16px !important;
    padding: 22px !important;
    box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.4) !important;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.metric-card:hover {
    transform: translateY(-5px) !important;
    border-color: rgba(0, 229, 255, 0.35) !important;
    box-shadow: 0 16px 45px 0 rgba(0, 229, 255, 0.12) !important;
}

.metric-icon {
    font-size: 26px;
    margin-bottom: 8px;
    display: block;
}
.metric-value {
    font-size: 34px;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1.1;
}
.metric-label {
    font-size: 11px;
    color: #94A3B8;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
}

/* Section Containers Frame */
.section-card {
    background: rgba(10, 17, 40, 0.4) !important;
    border: 1px solid rgba(255, 255, 255, 0.04) !important;
    border-radius: 16px !important;
    padding: 22px !important;
    margin-bottom: 22px !important;
}

.section-title {
    font-size: 15px;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 14px;
    letter-spacing: 0.5px;
}
</style>
"""