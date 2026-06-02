PREMIUM_CSS = """
<style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Page Header */
    .page-header {
        background: linear-gradient(135deg, #0A1628 0%, #1A2C4D 100%);
        padding: 30px;
        border-radius: 12px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    .page-header h1 {
        margin: 0;
        font-size: 28px;
        font-weight: 700;
        color: white;
    }
    .page-header p {
        margin: 8px 0 0;
        opacity: 0.8;
        font-size: 14px;
    }

    /* Metric Cards */
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        border: 1px solid #E5E9F2;
        display: flex;
        flex-direction: column;
        position: relative;
    }
    .metric-icon {
        font-size: 24px;
        margin-bottom: 12px;
    }
    .metric-value {
        font-size: 32px;
        font-weight: 700;
        line-height: 1.2;
    }
    .metric-label {
        font-size: 13px;
        color: #6B7A9A;
        font-weight: 500;
        margin-top: 4px;
    }
    .metric-delta {
        position: absolute;
        top: 20px;
        right: 20px;
        background: rgba(0,170,68,0.1);
        color: #00AA44;
        padding: 4px 8px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }

    /* Sections */
    .section-card {
        background: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.04);
        border: 1px solid #E5E9F2;
        margin-bottom: 24px;
    }
    .section-title {
        font-size: 16px;
        font-weight: 700;
        color: #0A1628;
        margin-bottom: 16px;
        border-bottom: 1px solid #E5E9F2;
        padding-bottom: 12px;
    }

    /* Resume Cards (AI Screener) */
    .resume-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E5E9F2;
        margin-bottom: 16px;
        transition: all 0.2s;
    }
    .resume-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.06);
    }
    .rank-1 { border-left: 4px solid #FFB300; }
    .rank-2 { border-left: 4px solid #B0BEC5; }
    .rank-3 { border-left: 4px solid #8D6E63; }

    /* Score Badges */
    .score-badge {
        width: 44px;
        height: 44px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 16px;
        color: white;
    }
    .score-high { background: #00AA44; }
    .score-mid { background: #FFB300; }
    .score-low { background: #FF4444; }

    /* Chips */
    .chip {
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    .chip-green { background: rgba(0,170,68,0.1); color: #00AA44; }
    .chip-blue { background: rgba(0,102,204,0.1); color: #0066CC; }
    .chip-yellow { background: rgba(255,179,0,0.1); color: #FFB300; }
    .chip-red { background: rgba(255,68,68,0.1); color: #FF4444; }

    /* Log Terminal */
    .log-terminal {
        background: #0A1628;
        color: #A0B0C0;
        font-family: 'Consolas', monospace;
        font-size: 12px;
        padding: 16px;
        border-radius: 8px;
        height: 400px;
        overflow-y: auto;
    }
    .log-line-info { color: #00AAFF; }
    .log-line-warning { color: #FFB300; }
    .log-line-error { color: #FF4444; font-weight: bold; }
    .log-line-debug { color: #6B7A9A; }
    .log-line-default { color: #A0B0C0; }

    /* Sidebar Customization */
    [data-testid="stSidebar"] {
        background-color: #0A1628;
        color: white;
    }
    .sidebar-logo {
        text-align: center;
        padding: 20px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }
    .logo-icon { font-size: 32px; }
    .logo-name { font-size: 18px; font-weight: 700; color: white; margin-top: 8px; }
    .logo-sub { font-size: 11px; color: #00AAFF; text-transform: uppercase; letter-spacing: 1px; }
    
    .user-badge {
        background: rgba(255,255,255,0.05);
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 24px;
        font-size: 13px;
        border: 1px solid rgba(255,255,255,0.1);
    }

</style>
"""
