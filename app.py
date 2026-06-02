PREMIUM_CSS = """
<style>
/* ═══════════════════════════════════════════════════════════════════
   CV SCREENER PRO — CORPORATE PREMIUM v4.0
   Inspired by: Linear · Vercel · Notion · Raycast
   Palette: Deep Navy · Electric Blue · Cyan · Clean White
   Typography: Inter (primary) · JetBrains Mono (terminal)
═══════════════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ── Design Tokens ── */
:root {
  /* Backgrounds */
  --bg-canvas:      #080C14;
  --bg-base:        #0B1120;
  --bg-surface:     #0F1629;
  --bg-overlay:     #131E35;
  --bg-input:       #0D1526;

  /* Borders */
  --border-subtle:  rgba(255,255,255,0.06);
  --border-default: rgba(255,255,255,0.09);
  --border-strong:  rgba(255,255,255,0.14);
  --border-focus:   rgba(56,189,248,0.5);

  /* Brand Colors */
  --blue-500:   #38BDF8;
  --blue-400:   #60CAFF;
  --blue-300:   #93DDFF;
  --blue-600:   #1E9FD8;
  --cyan-400:   #22D3EE;
  --cyan-300:   #67E8F9;
  --navy-deep:  #060A14;
  --indigo-500: #6366F1;

  /* Semantic */
  --success:  #10B981;
  --warning:  #F59E0B;
  --danger:   #EF4444;
  --info:     #38BDF8;

  /* Text */
  --text-primary:   #F1F5FF;
  --text-secondary: #8896B3;
  --text-tertiary:  #4A5878;
  --text-disabled:  #2D3A52;

  /* Effects */
  --shadow-sm:   0 1px 3px rgba(0,0,0,0.4);
  --shadow-md:   0 4px 16px rgba(0,0,0,0.5);
  --shadow-lg:   0 12px 40px rgba(0,0,0,0.6);
  --shadow-blue: 0 0 0 1px rgba(56,189,248,0.15), 0 4px 20px rgba(56,189,248,0.08);
  --glow-blue:   0 0 24px rgba(56,189,248,0.18);
  --glow-cyan:   0 0 24px rgba(34,211,238,0.15);

  /* Spacing & Shape */
  --radius-xs: 6px;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 20px;

  /* Motion */
  --ease-out:    cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 400ms;
}

/* ══ RESET ══ */
*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  background: var(--bg-canvas) !important;
  color: var(--text-primary) !important;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
}

/* ══ STRIP ALL STREAMLIT CHROME ══ */
#MainMenu,
footer,
header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.viewerBadge_container__1QSob,
.stDeployButton { display: none !important; visibility: hidden !important; }

section.main > div:first-child { padding-top: 0 !important; }
.main .block-container {
  padding: 1.5rem 2rem 3rem !important;
  max-width: 100% !important;
}

/* ══ KEYFRAMES ══ */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0px); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}
@keyframes shimmer {
  0%   { transform: translateX(-100%); }
  100% { transform: translateX(200%); }
}
@keyframes pulse-dot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%       { opacity: 0.4; transform: scale(0.8); }
}
@keyframes gradient-flow {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
@keyframes border-breathe {
  0%, 100% { border-color: rgba(56,189,248,0.15); }
  50%       { border-color: rgba(56,189,248,0.35); }
}
@keyframes card-in {
  from { opacity: 0; transform: translateY(8px) scale(0.99); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}

/* ══ NOISE TEXTURE OVERLAY ══ */
.stApp::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
  opacity: 0.4;
}

/* ══ SIDEBAR — LINEAR-STYLE NAVIGATION RAIL ══ */
section[data-testid="stSidebar"] {
  background: var(--bg-base) !important;
  border-right: 1px solid var(--border-subtle) !important;
  min-width: 256px !important;
  max-width: 256px !important;
}
section[data-testid="stSidebar"] > div { padding: 0 !important; }
section[data-testid="stSidebar"] * { color: var(--text-primary) !important; }

/* Logo area */
.sb-logo {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 20px 16px 18px;
  border-bottom: 1px solid var(--border-subtle);
}
.sb-logo-mark {
  width: 32px; height: 32px;
  border-radius: 8px;
  background: linear-gradient(135deg, var(--blue-500), var(--cyan-400));
  display: flex; align-items: center; justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
  box-shadow: 0 0 16px rgba(56,189,248,0.3);
}
.sb-logo-text { line-height: 1.15; }
.sb-logo-name {
  font-size: 13px; font-weight: 700;
  color: var(--text-primary) !important;
  letter-spacing: -0.2px;
}
.sb-logo-sub {
  font-size: 10px; font-weight: 500;
  color: var(--text-tertiary) !important;
  letter-spacing: 0.3px;
}

/* User chip */
.sb-user {
  display: flex; align-items: center; gap: 10px;
  margin: 10px 10px 4px;
  padding: 8px 10px;
  border-radius: var(--radius-sm);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  cursor: default;
}
.sb-avatar {
  width: 28px; height: 28px;
  border-radius: 50%;
  background: linear-gradient(135deg, #1E40AF, #0891B2);
  display: flex; align-items: center; justify-content: center;
  font-size: 11px; font-weight: 700; color: white;
  flex-shrink: 0;
  border: 1.5px solid rgba(56,189,248,0.3);
}
.sb-user-name { font-size: 12px; font-weight: 600; color: var(--text-primary) !important; }
.sb-user-role { font-size: 10px; color: var(--text-tertiary) !important; }

/* Nav section label */
.sb-section-label {
  font-size: 10px; font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-disabled) !important;
  padding: 16px 16px 6px;
}

/* Nav items */
section[data-testid="stSidebar"] .stRadio > div {
  gap: 1px !important;
  padding: 0 8px !important;
}
section[data-testid="stSidebar"] .stRadio label {
  display: flex !important;
  align-items: center !important;
  padding: 7px 10px !important;
  border-radius: var(--radius-sm) !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  color: var(--text-secondary) !important;
  border: 1px solid transparent !important;
  transition: all var(--duration-fast) var(--ease-out) !important;
  cursor: pointer !important;
  position: relative !important;
  letter-spacing: -0.1px !important;
}
section[data-testid="stSidebar"] .stRadio label:hover {
  background: var(--bg-surface) !important;
  color: var(--text-primary) !important;
  border-color: var(--border-subtle) !important;
}
section[data-testid="stSidebar"] .stRadio label:has(input:checked) {
  background: rgba(56,189,248,0.08) !important;
  color: var(--blue-400) !important;
  border-color: rgba(56,189,248,0.18) !important;
  font-weight: 600 !important;
}
/* Active left indicator */
section[data-testid="stSidebar"] .stRadio label:has(input:checked)::before {
  content: '';
  position: absolute;
  left: -8px; top: 50%;
  transform: translateY(-50%);
  width: 2.5px; height: 14px;
  border-radius: 0 2px 2px 0;
  background: var(--blue-500);
  box-shadow: 0 0 8px var(--blue-500);
}
/* Hide radio circles */
section[data-testid="stSidebar"] .stRadio label span:first-child {
  display: none !important;
}

/* Sidebar divider */
.sb-divider {
  height: 1px;
  background: var(--border-subtle);
  margin: 8px 16px;
}

/* Sidebar version */
.sb-footer {
  padding: 12px 16px;
  font-size: 10px;
  color: var(--text-disabled) !important;
  letter-spacing: 0.3px;
}

/* Sign out button */
section[data-testid="stSidebar"] .stButton > button {
  background: transparent !important;
  color: var(--text-tertiary) !important;
  border: 1px solid var(--border-subtle) !important;
  border-radius: var(--radius-sm) !important;
  font-size: 12px !important;
  font-weight: 500 !important;
  padding: 6px 12px !important;
  height: 34px !important;
  transition: all var(--duration-fast) ease !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
  background: rgba(239,68,68,0.08) !important;
  border-color: rgba(239,68,68,0.2) !important;
  color: #FCA5A5 !important;
  transform: none !important;
  box-shadow: none !important;
}

/* ══ PAGE HEADER — VERCEL-STYLE ══ */
.page-header {
  padding: 0 0 24px 0;
  border-bottom: 1px solid var(--border-subtle);
  margin-bottom: 28px;
  animation: fadeUp var(--duration-slow) var(--ease-out) both;
  position: relative;
}
/* Hero variant — overview page with illustration */
.page-header-hero {
  background: var(--bg-surface);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-xl);
  padding: 28px 36px;
  margin-bottom: 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  overflow: hidden;
  position: relative;
}
/* Subtle grid behind hero */
.page-header-hero::before {
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(56,189,248,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(56,189,248,0.025) 1px, transparent 1px);
  background-size: 36px 36px;
  pointer-events: none;
  border-radius: var(--radius-xl);
}
/* Top glow line */
.page-header-hero::after {
  content: '';
  position: absolute;
  top: 0; left: 15%; right: 15%; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(56,189,248,0.35), transparent);
}
.page-header-content { position: relative; z-index: 1; }
.hero-illustration {
  width: 280px; height: 170px;
  flex-shrink: 0;
  position: relative; z-index: 1;
}
.hero-illustration svg { width: 100%; height: 100%; }

.page-header-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--blue-500);
  margin-bottom: 8px;
}
.live-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--success);
  animation: pulse-dot 2s ease infinite;
  box-shadow: 0 0 6px var(--success);
}
.page-header h1 {
  font-size: 22px !important;
  font-weight: 700 !important;
  color: var(--text-primary) !important;
  letter-spacing: -0.5px !important;
  line-height: 1.25 !important;
  margin: 0 0 4px !important;
}
.page-header p {
  font-size: 13px !important;
  color: var(--text-secondary) !important;
  margin: 0 !important;
  font-weight: 400 !important;
  line-height: 1.5 !important;
}

/* ══ METRIC CARDS — NOTION/LINEAR STYLE ══ */
.metric-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 20px;
  position: relative;
  overflow: hidden;
  transition: all var(--duration-base) var(--ease-out);
  animation: card-in var(--duration-slow) var(--ease-out) both;
  cursor: default;
}
/* Shimmer on load */
.metric-card::after {
  content: '';
  position: absolute;
  top: 0; left: 0; bottom: 0;
  width: 40%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.025), transparent);
  animation: shimmer 2s ease 0.5s both;
  pointer-events: none;
}
.metric-card:hover {
  border-color: var(--border-strong);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
  background: var(--bg-overlay);
}
/* Top accent line */
.metric-card-accent {
  position: absolute;
  top: 0; left: 20px; right: 20px;
  height: 1px;
}
.accent-blue   { background: linear-gradient(90deg, transparent, var(--blue-500), transparent); }
.accent-cyan   { background: linear-gradient(90deg, transparent, var(--cyan-400), transparent); }
.accent-green  { background: linear-gradient(90deg, transparent, var(--success), transparent); }
.accent-amber  { background: linear-gradient(90deg, transparent, var(--warning), transparent); }

.metric-icon {
  font-size: 18px;
  margin-bottom: 14px;
  display: block;
  opacity: 0.9;
}
.metric-value {
  font-size: 28px;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -1px;
  margin-bottom: 5px;
  font-variant-numeric: tabular-nums;
}
.mv-blue  { color: var(--blue-400); }
.mv-cyan  { color: var(--cyan-400); }
.mv-green { color: var(--success); }
.mv-amber { color: var(--warning); }
.mv-white { color: var(--text-primary); }

.metric-label {
  font-size: 11px;
  font-weight: 500;
  color: var(--text-tertiary);
  letter-spacing: 0.03em;
  text-transform: uppercase;
}
.metric-badge {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  margin-top: 10px;
  font-size: 10px;
  font-weight: 600;
  color: var(--success);
  background: rgba(16,185,129,0.08);
  border-radius: 4px;
  padding: 2px 7px;
}

/* ══ SECTION CARD ══ */
.section-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 24px;
  margin-bottom: 16px;
  animation: card-in var(--duration-slow) var(--ease-out) both;
  transition: border-color var(--duration-fast) ease;
}
.section-card:hover { border-color: var(--border-strong); }

.section-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-primary);
  letter-spacing: -0.1px;
  margin-bottom: 18px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  gap: 8px;
}

/* ══ SCORE BADGES ══ */
.score-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 52px; height: 52px;
  border-radius: 50%;
  font-size: 14px;
  font-weight: 800;
  flex-shrink: 0;
  font-variant-numeric: tabular-nums;
}
.score-high {
  background: rgba(16,185,129,0.1);
  color: #34D399;
  border: 1.5px solid rgba(16,185,129,0.25);
  box-shadow: 0 0 16px rgba(16,185,129,0.12);
}
.score-mid {
  background: rgba(245,158,11,0.1);
  color: #FBBF24;
  border: 1.5px solid rgba(245,158,11,0.25);
  box-shadow: 0 0 16px rgba(245,158,11,0.1);
}
.score-low {
  background: rgba(239,68,68,0.1);
  color: #F87171;
  border: 1.5px solid rgba(239,68,68,0.2);
  box-shadow: 0 0 12px rgba(239,68,68,0.08);
}

/* ══ RESUME RESULT CARDS ══ */
.resume-card {
  background: var(--bg-surface);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  padding: 20px 22px;
  margin: 10px 0;
  transition: all var(--duration-base) var(--ease-out);
  position: relative;
  overflow: hidden;
  animation: card-in var(--duration-slow) var(--ease-out) both;
}
.resume-card:hover {
  border-color: rgba(56,189,248,0.25);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md), var(--shadow-blue);
  background: var(--bg-overlay);
}
.resume-card.rank-1 { border-left: 2px solid #F59E0B; }
.resume-card.rank-2 { border-left: 2px solid #94A3B8; }
.resume-card.rank-3 { border-left: 2px solid #92400E; }

.rc-name {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
  letter-spacing: -0.2px;
}
.rc-file {
  font-size: 11px;
  color: var(--text-tertiary);
  margin-top: 2px;
  font-family: 'JetBrains Mono', monospace;
}
.rc-analysis {
  margin-top: 12px;
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.65;
  padding: 12px 14px;
  background: var(--bg-input);
  border-radius: var(--radius-sm);
  border-left: 2px solid rgba(56,189,248,0.2);
}
.rc-skills { margin-top: 10px; display: flex; flex-wrap: wrap; gap: 4px; align-items: center; }
.skill-pill {
  display: inline-block;
  background: var(--bg-overlay);
  border: 1px solid var(--border-default);
  border-radius: 4px;
  padding: 2px 8px;
  font-size: 10px;
  font-weight: 500;
  color: var(--text-secondary);
  font-family: 'JetBrains Mono', monospace;
}

.rank-medal { font-size: 20px; flex-shrink: 0; }
.rank-num {
  display: inline-flex; align-items: center; justify-content: center;
  width: 28px; height: 28px;
  border-radius: 50%;
  font-size: 11px; font-weight: 700;
  color: var(--text-tertiary);
  background: var(--bg-overlay);
  border: 1px solid var(--border-subtle);
  flex-shrink: 0;
}

/* ══ RECOMMENDATION CHIPS ══ */
.chip {
  display: inline-flex; align-items: center; gap: 4px;
  padding: 3px 9px;
  border-radius: var(--radius-xs);
  font-size: 11px; font-weight: 600;
  letter-spacing: 0.01em;
  white-space: nowrap;
}
.chip-green  { background: rgba(16,185,129,0.1);  border: 1px solid rgba(16,185,129,0.2); color: #34D399; }
.chip-blue   { background: rgba(56,189,248,0.1);  border: 1px solid rgba(56,189,248,0.2); color: var(--blue-400); }
.chip-yellow { background: rgba(245,158,11,0.1);  border: 1px solid rgba(245,158,11,0.2); color: #FBBF24; }
.chip-red    { background: rgba(239,68,68,0.1);   border: 1px solid rgba(239,68,68,0.15); color: #F87171; }

/* ══ BUTTONS ══ */
.stButton > button {
  font-family: 'Inter', sans-serif !important;
  font-weight: 500 !important;
  font-size: 13px !important;
  letter-spacing: -0.1px !important;
  border-radius: var(--radius-sm) !important;
  border: none !important;
  transition: all var(--duration-fast) var(--ease-out) !important;
  height: 36px !important;
}
.stButton > button[kind="primary"] {
  background: var(--blue-500) !important;
  color: #020812 !important;
  font-weight: 600 !important;
  box-shadow: 0 1px 2px rgba(0,0,0,0.3), 0 0 0 1px rgba(56,189,248,0.4) !important;
}
.stButton > button[kind="primary"]:hover {
  background: var(--blue-400) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 12px rgba(56,189,248,0.25), 0 0 0 1px rgba(56,189,248,0.5) !important;
}
.stButton > button[kind="secondary"] {
  background: var(--bg-surface) !important;
  color: var(--text-secondary) !important;
  border: 1px solid var(--border-default) !important;
}
.stButton > button[kind="secondary"]:hover {
  background: var(--bg-overlay) !important;
  border-color: var(--border-strong) !important;
  color: var(--text-primary) !important;
  transform: translateY(-1px) !important;
}

/* Download buttons */
.stDownloadButton > button {
  font-family: 'Inter', sans-serif !important;
  font-weight: 500 !important;
  font-size: 13px !important;
  border-radius: var(--radius-sm) !important;
  background: var(--bg-surface) !important;
  border: 1px solid var(--border-default) !important;
  color: var(--text-secondary) !important;
  height: 36px !important;
  transition: all var(--duration-fast) ease !important;
}
.stDownloadButton > button:hover {
  background: var(--bg-overlay) !important;
  border-color: rgba(56,189,248,0.3) !important;
  color: var(--blue-400) !important;
  transform: translateY(-1px) !important;
  box-shadow: var(--shadow-blue) !important;
}

/* ══ FORM INPUTS ══ */
.stTextInput input,
.stTextArea textarea {
  font-family: 'Inter', sans-serif !important;
  background: var(--bg-input) !important;
  border: 1px solid var(--border-default) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text-primary) !important;
  font-size: 13px !important;
  transition: border-color var(--duration-fast) ease,
              box-shadow var(--duration-fast) ease !important;
}
.stTextInput input:focus,
.stTextArea textarea:focus {
  border-color: var(--border-focus) !important;
  box-shadow: 0 0 0 3px rgba(56,189,248,0.07) !important;
  outline: none !important;
}
.stTextInput input::placeholder,
.stTextArea textarea::placeholder { color: var(--text-disabled) !important; }

.stSelectbox > div > div,
.stNumberInput input {
  background: var(--bg-input) !important;
  border: 1px solid var(--border-default) !important;
  border-radius: var(--radius-sm) !important;
  color: var(--text-primary) !important;
  font-family: 'Inter', sans-serif !important;
  font-size: 13px !important;
}
.stTextInput label, .stTextArea label,
.stSelectbox label, .stNumberInput label,
.stFileUploader label {
  font-size: 12px !important;
  font-weight: 500 !important;
  color: var(--text-secondary) !important;
  letter-spacing: 0.01em !important;
}

/* ══ TABS ══ */
.stTabs [data-baseweb="tab-list"] {
  gap: 0 !important;
  background: transparent !important;
  padding: 0 !important;
  border-bottom: 1px solid var(--border-subtle) !important;
  border-radius: 0 !important;
}
.stTabs [data-baseweb="tab"] {
  border-radius: 0 !important;
  font-family: 'Inter', sans-serif !important;
  font-weight: 500 !important;
  font-size: 13px !important;
  color: var(--text-tertiary) !important;
  padding: 10px 16px !important;
  border-bottom: 2px solid transparent !important;
  background: transparent !important;
  transition: all var(--duration-fast) ease !important;
}
.stTabs [data-baseweb="tab"]:hover { color: var(--text-secondary) !important; }
.stTabs [aria-selected="true"] {
  color: var(--blue-400) !important;
  border-bottom: 2px solid var(--blue-500) !important;
  font-weight: 600 !important;
  background: transparent !important;
  box-shadow: none !important;
}
.stTabs [data-baseweb="tab-panel"] { padding-top: 20px !important; }

/* ══ DATAFRAME ══ */
.stDataFrame {
  border-radius: var(--radius-md) !important;
  overflow: hidden !important;
  border: 1px solid var(--border-default) !important;
}

/* ══ ALERTS ══ */
[data-testid="stAlert"] {
  border-radius: var(--radius-sm) !important;
  font-size: 13px !important;
  font-family: 'Inter', sans-serif !important;
}
.stSuccess > div {
  background: rgba(16,185,129,0.06) !important;
  border: 1px solid rgba(16,185,129,0.15) !important;
  border-left: 2px solid var(--success) !important;
  border-radius: var(--radius-sm) !important;
  color: #6EE7B7 !important;
}
.stError > div {
  background: rgba(239,68,68,0.06) !important;
  border: 1px solid rgba(239,68,68,0.15) !important;
  border-left: 2px solid var(--danger) !important;
  border-radius: var(--radius-sm) !important;
}
.stWarning > div {
  background: rgba(245,158,11,0.06) !important;
  border: 1px solid rgba(245,158,11,0.15) !important;
  border-left: 2px solid var(--warning) !important;
  border-radius: var(--radius-sm) !important;
}
.stInfo > div {
  background: rgba(56,189,248,0.05) !important;
  border: 1px solid rgba(56,189,248,0.12) !important;
  border-left: 2px solid var(--blue-500) !important;
  border-radius: var(--radius-sm) !important;
}

/* ══ FILE UPLOADER ══ */
[data-testid="stFileUploader"] > div {
  background: var(--bg-input) !important;
  border: 1.5px dashed var(--border-default) !important;
  border-radius: var(--radius-md) !important;
  transition: all var(--duration-fast) ease !important;
}
[data-testid="stFileUploader"] > div:hover {
  border-color: rgba(56,189,248,0.3) !important;
  background: rgba(56,189,248,0.02) !important;
}

/* ══ PROGRESS BAR ══ */
.stProgress > div > div {
  background: var(--bg-overlay) !important;
  border-radius: 4px !important;
}
.stProgress > div > div > div {
  background: linear-gradient(90deg, var(--blue-500), var(--cyan-400)) !important;
  border-radius: 4px !important;
}

/* ══ EXPANDER ══ */
.stExpander {
  background: var(--bg-surface) !important;
  border: 1px solid var(--border-default) !important;
  border-radius: var(--radius-md) !important;
}
details summary {
  font-family: 'Inter', sans-serif !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  color: var(--text-secondary) !important;
  padding: 12px 16px !important;
}

/* ══ LOG TERMINAL ══ */
.log-terminal {
  background: #050810;
  border-radius: var(--radius-md);
  padding: 0;
  font-family: 'JetBrains Mono', 'Courier New', monospace;
  font-size: 11.5px;
  line-height: 1.75;
  max-height: 520px;
  overflow-y: auto;
  border: 1px solid var(--border-subtle);
  animation: border-breathe 4s ease-in-out infinite;
}
.log-terminal-header {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 10px 16px;
  border-bottom: 1px solid var(--border-subtle);
  background: rgba(255,255,255,0.02);
}
.terminal-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
}
.td-red    { background: #FF5F57; }
.td-yellow { background: #FEBC2E; }
.td-green  { background: #28C840; }
.terminal-title {
  font-size: 10px;
  color: var(--text-tertiary);
  margin-left: 4px;
  font-family: 'JetBrains Mono', monospace;
}
.log-body { padding: 14px 18px; }
.log-line-info    { color: #60CAFF; }
.log-line-warning { color: #FCD34D; }
.log-line-error   { color: #FC8181; }
.log-line-debug   { color: #374869; }
.log-line-default { color: #3D5070; }

/* ══ SCROLLBAR ══ */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb {
  background: var(--border-strong);
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover { background: rgba(56,189,248,0.3); }

/* ══ RADIO (page filters) ══ */
.stRadio [data-testid="stMarkdownContainer"] p {
  font-size: 13px !important;
  color: var(--text-secondary) !important;
  font-weight: 500 !important;
}

/* ══ DIVIDER ══ */
hr {
  border: none !important;
  border-top: 1px solid var(--border-subtle) !important;
  margin: 16px 0 !important;
}

/* ══ SPINNER ══ */
.stSpinner > div { border-top-color: var(--blue-500) !important; }

/* ══ TOOLTIP / SELECTBOX DROPDOWN ══ */
[data-baseweb="popover"] {
  background: var(--bg-overlay) !important;
  border: 1px solid var(--border-default) !important;
  border-radius: var(--radius-md) !important;
}
</style>
"""

CINEMATIC_CSS = """
<style>
/* ═══════════════════════════════════════════════════════════════════
   CINEMATIC HERO SCENES v5.0 — Per-page animated 3D-feel backgrounds
═══════════════════════════════════════════════════════════════════ */

.hero-scene {
  position: relative;
  width: 100%;
  height: 200px;
  border-radius: 20px;
  overflow: hidden;
  margin-bottom: 28px;
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}

/* ── Scene text overlay (shared) ── */
.scene-text {
  position: absolute;
  left: 36px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
  max-width: 60%;
}
.scene-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.15em;
  color: #38BDF8;
  text-transform: uppercase;
  margin-bottom: 8px;
  text-shadow: 0 0 12px rgba(56,189,248,0.5);
  animation: textGlow 2.5s ease infinite;
}
.scene-text-light .scene-eyebrow { color: white; text-shadow: 0 2px 8px rgba(0,0,0,0.4); }
@keyframes textGlow {
  0%,100% { text-shadow: 0 0 8px rgba(56,189,248,0.4); }
  50%      { text-shadow: 0 0 24px rgba(56,189,248,0.9); }
}
.live-pulse {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 10px #10B981;
  animation: pulse-dot 2s ease infinite;
}
.scene-title {
  font-size: 30px;
  font-weight: 800;
  color: white;
  letter-spacing: -0.7px;
  line-height: 1.1;
  text-shadow: 0 4px 16px rgba(0,0,0,0.6);
  animation: titleSlide 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}
.scene-sub {
  font-size: 13px;
  color: rgba(255,255,255,0.65);
  margin-top: 8px;
  text-shadow: 0 2px 8px rgba(0,0,0,0.5);
  animation: titleSlide 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.1s both;
}
@keyframes titleSlide {
  from { opacity: 0; transform: translateX(-20px); }
  to   { opacity: 1; transform: translateX(0); }
}

/* ════ SCENE 1 — OVERVIEW (rocket through space) ════ */
.scene-overview {
  background: radial-gradient(ellipse at top right, #1a1f3a 0%, #080C14 60%, #020510 100%);
}
.scene-overview .stars-layer-1,
.scene-overview .stars-layer-2 {
  position: absolute;
  inset: 0;
  pointer-events: none;
}
.star {
  position: absolute;
  background: white;
  border-radius: 50%;
  animation: twinkle 3s ease infinite;
}
.star.big-star {
  width: 3px; height: 3px;
  background: #93DDFF;
  box-shadow: 0 0 6px #93DDFF;
}
.star.big-star.amber { background: #FBBF24; box-shadow: 0 0 6px #FBBF24; }
.star.big-star.purple { background: #A855F7; box-shadow: 0 0 6px #A855F7; }
@keyframes twinkle {
  0%,100% { opacity: 0.3; transform: scale(1); }
  50%      { opacity: 1; transform: scale(1.5); }
}
.stars-layer-1 { animation: starDrift 80s linear infinite; }
.stars-layer-2 { animation: starDrift 50s linear infinite; }
@keyframes starDrift {
  from { transform: translateX(0); }
  to   { transform: translateX(-300px); }
}

.planet {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
}
.planet-purple {
  width: 44px; height: 44px;
  background: radial-gradient(circle at 30% 30%, #A855F7, #3B1F8C);
  top: 18%; right: 25%;
  box-shadow: inset -6px -4px 14px rgba(0,0,0,0.5), 0 0 28px rgba(168,85,247,0.35);
  animation: planetSpin 20s linear infinite;
}
.planet-amber {
  width: 22px; height: 22px;
  background: radial-gradient(circle at 35% 30%, #FCD34D, #92400E);
  bottom: 22%; left: 32%;
  box-shadow: inset -4px -2px 8px rgba(0,0,0,0.5), 0 0 16px rgba(252,211,77,0.4);
  animation: planetSpin 35s linear infinite reverse;
}
@keyframes planetSpin {
  from { transform: rotate(0); }
  to   { transform: rotate(360deg); }
}

.shooting-star {
  position: absolute;
  top: 25%; left: -10%;
  width: 100px; height: 1.5px;
  background: linear-gradient(90deg, transparent, white, white);
  animation: shoot 6s ease-in infinite;
  opacity: 0;
}
@keyframes shoot {
  0%   { left: -10%; top: 15%; opacity: 0; transform: rotate(20deg); }
  10%  { opacity: 1; }
  30%  { left: 110%; top: 60%; opacity: 0; transform: rotate(20deg); }
  100% { left: 110%; opacity: 0; }
}

.rocket-wrap {
  position: absolute;
  left: -80px;
  top: 50%;
  z-index: 5;
  animation: rocketFly 12s ease-in-out infinite;
}
@keyframes rocketFly {
  0%   { left: -80px; top: 65%; transform: rotate(-15deg) scale(0.7); }
  20%  { top: 35%; transform: rotate(15deg) scale(0.95); }
  40%  { left: 45%; top: 55%; transform: rotate(-8deg) scale(1.1); }
  60%  { top: 30%; transform: rotate(20deg) scale(1); }
  80%  { left: 80%; top: 45%; transform: rotate(5deg) scale(0.85); }
  100% { left: 110%; top: 35%; transform: rotate(10deg) scale(0.6); }
}
.rocket-flame {
  transform-origin: 30px 60px;
  animation: flameFlicker 0.1s ease infinite alternate;
}
@keyframes flameFlicker {
  from { transform: scaleY(0.8); opacity: 0.85; }
  to   { transform: scaleY(1.15); opacity: 1; }
}

/* ════ SCENE 2 — MASTER DATA (plane through clouds) ════ */
.scene-master {
  background: linear-gradient(to bottom, #0c1840 0%, #1a3a8a 40%, #2563EB 100%);
}
.cloud {
  position: absolute;
  background: rgba(255,255,255,0.18);
  border-radius: 50px;
}
.cloud::before, .cloud::after {
  content: '';
  position: absolute;
  background: rgba(255,255,255,0.2);
  border-radius: 50%;
}
.scene-master .c1 {
  width: 120px; height: 30px;
  top: 30%; left: -130px;
  animation: cloudMove 22s linear infinite;
}
.scene-master .c1::before { width: 50px; height: 50px; top: -25px; left: 20px; }
.scene-master .c1::after  { width: 38px; height: 38px; top: -18px; left: 65px; }
.scene-master .c2 {
  width: 80px; height: 22px;
  top: 60%; left: -100px;
  animation: cloudMove 28s linear infinite 5s;
  opacity: 0.7;
}
.scene-master .c2::before { width: 36px; height: 36px; top: -18px; left: 14px; }
.scene-master .c2::after  { width: 28px; height: 28px; top: -12px; left: 42px; }
.scene-master .c3 {
  width: 100px; height: 26px;
  top: 78%; left: -120px;
  animation: cloudMove 18s linear infinite 10s;
  opacity: 0.55;
}
.scene-master .c3::before { width: 42px; height: 42px; top: -22px; left: 18px; }
.scene-master .c3::after  { width: 32px; height: 32px; top: -15px; left: 55px; }
.scene-master .c4 {
  width: 90px; height: 24px;
  top: 15%; left: -110px;
  animation: cloudMove 32s linear infinite 14s;
  opacity: 0.45;
}
.scene-master .c4::before { width: 38px; height: 38px; top: -19px; left: 16px; }
.scene-master .c4::after  { width: 30px; height: 30px; top: -13px; left: 50px; }
@keyframes cloudMove {
  from { left: -130px; }
  to   { left: 110%; }
}

.plane-wrap {
  position: absolute;
  top: 35%; left: -80px;
  z-index: 5;
  animation: planeFly 14s ease-in-out infinite;
}
@keyframes planeFly {
  0%   { left: -80px; top: 40%; transform: rotate(2deg) scale(0.85); }
  25%  { top: 28%; transform: rotate(-3deg) scale(1); }
  50%  { left: 50%; top: 35%; transform: rotate(2deg) scale(1.1); }
  75%  { top: 25%; transform: rotate(-2deg) scale(0.95); }
  100% { left: 110%; top: 30%; transform: rotate(3deg) scale(0.8); }
}

.sun {
  position: absolute;
  width: 60px; height: 60px;
  border-radius: 50%;
  background: radial-gradient(circle, #FCD34D 0%, #F59E0B 60%, transparent 80%);
  top: 15%; right: 8%;
  animation: sunPulse 4s ease infinite;
}
@keyframes sunPulse {
  0%,100% { box-shadow: 0 0 30px rgba(252,211,77,0.4); }
  50%      { box-shadow: 0 0 60px rgba(252,211,77,0.8); }
}

/* ════ SCENE 3 — INPUT DATA (floating papers) ════ */
.scene-input {
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #1e3a8a 100%);
}
.paper {
  position: absolute;
  width: 48px; height: 60px;
  background: white;
  border-radius: 4px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.4);
}
.paper::before {
  content: '';
  position: absolute;
  top: 8px; left: 8px; right: 8px;
  height: 2px;
  background: #cbd5e1;
  border-radius: 1px;
  box-shadow: 0 6px 0 #cbd5e1,
              0 12px 0 #cbd5e1,
              0 18px 0 #e2e8f0,
              0 24px 0 #e2e8f0,
              0 30px 0 #e2e8f0;
}
.scene-input .p1 { top: 60%; left: 8%;  animation: paperFloat 10s ease-in-out 0s   infinite; }
.scene-input .p2 { top: 28%; left: 32%; animation: paperFloat 12s ease-in-out 1.5s infinite; }
.scene-input .p3 { top: 55%; left: 58%; animation: paperFloat 9s  ease-in-out 3s   infinite; }
.scene-input .p4 { top: 22%; left: 75%; animation: paperFloat 11s ease-in-out 5s   infinite; }
.scene-input .p5 { top: 68%; left: 85%; animation: paperFloat 13s ease-in-out 2s   infinite; }
.scene-input .p1 { transform: rotate(-15deg); }
.scene-input .p2 { transform: rotate(10deg);  }
.scene-input .p3 { transform: rotate(-8deg);  }
.scene-input .p4 { transform: rotate(20deg);  }
.scene-input .p5 { transform: rotate(-12deg); }
@keyframes paperFloat {
  0%,100% { transform: translateY(0)    rotate(var(--rot, 0)); }
  50%      { transform: translateY(-25px) rotate(var(--rot, 0)); }
}
.scene-input .p1 { --rot: -15deg; }
.scene-input .p2 { --rot: 10deg;  }
.scene-input .p3 { --rot: -8deg;  }
.scene-input .p4 { --rot: 20deg;  }
.scene-input .p5 { --rot: -12deg; }

.spark {
  position: absolute;
  width: 7px; height: 7px;
  background: #FCD34D;
  border-radius: 50%;
  box-shadow: 0 0 14px #FCD34D;
  animation: sparkle 2.4s ease infinite;
}
.scene-input .sp1 { top: 22%; left: 22%; animation-delay: 0s;   }
.scene-input .sp2 { top: 72%; left: 48%; animation-delay: 0.7s; }
.scene-input .sp3 { top: 35%; left: 65%; animation-delay: 1.3s; }
.scene-input .sp4 { top: 80%; left: 28%; animation-delay: 1.9s; }
@keyframes sparkle {
  0%,100% { opacity: 0; transform: scale(0); }
  50%      { opacity: 1; transform: scale(1.3); }
}

/* ════ SCENE 4 — AI SCREENER (neural network) ════ */
.scene-ai {
  background: radial-gradient(ellipse at center, #1e1b4b 0%, #0c0a3e 60%, #020510 100%);
}
.brain-core {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 80px; height: 80px;
}
.brain-ring {
  position: absolute;
  border-radius: 50%;
  inset: 0;
}
.brain-ring.r1 {
  border: 2px solid rgba(56,189,248,0.45);
  box-shadow: 0 0 20px rgba(56,189,248,0.3);
  animation: brainRotate 8s linear infinite;
}
.brain-ring.r2 {
  inset: -10px;
  border: 1.5px solid rgba(112,0,255,0.4);
  animation: brainRotate 12s linear infinite reverse;
}
.brain-ring.r3 {
  inset: -20px;
  border: 1px solid rgba(34,211,238,0.3);
  animation: brainRotate 16s linear infinite;
}
@keyframes brainRotate {
  from { transform: rotate(0); }
  to   { transform: rotate(360deg); }
}

.neural-net {
  position: absolute;
  inset: 0;
  width: 100%; height: 100%;
  opacity: 0.3;
  pointer-events: none;
  animation: netPulse 3s ease infinite;
}
@keyframes netPulse {
  0%,100% { opacity: 0.2; }
  50%      { opacity: 0.5; }
}

.ai-node {
  position: absolute;
  width: 14px; height: 14px;
  border-radius: 50%;
  background: #38BDF8;
  box-shadow: 0 0 18px #38BDF8;
  animation: nodePulse 2s ease infinite;
}
.scene-ai .n1 { top: 30%; left: 15%; animation-delay: 0s;   background: #38BDF8; box-shadow: 0 0 18px #38BDF8; }
.scene-ai .n2 { top: 60%; left: 15%; animation-delay: 0.3s; background: #22D3EE; box-shadow: 0 0 18px #22D3EE; }
.scene-ai .n3 { top: 20%; left: 45%; animation-delay: 0.6s; background: #A855F7; box-shadow: 0 0 18px #A855F7; }
.scene-ai .n4 { top: 50%; left: 45%; animation-delay: 0.9s; background: #22D3EE; box-shadow: 0 0 18px #22D3EE; }
.scene-ai .n5 { top: 80%; left: 45%; animation-delay: 1.2s; background: #38BDF8; box-shadow: 0 0 18px #38BDF8; }
.scene-ai .n6 { top: 35%; left: 78%; animation-delay: 1.5s; background: #10B981; box-shadow: 0 0 22px #10B981; }
.scene-ai .n7 { top: 65%; left: 78%; animation-delay: 1.8s; background: #10B981; box-shadow: 0 0 22px #10B981; }
@keyframes nodePulse {
  0%,100% { transform: scale(1);   opacity: 1; }
  50%      { transform: scale(1.6); opacity: 0.7; }
}

/* ════ SCENE 5 — SYSTEM LOGS (matrix code rain) ════ */
.scene-logs {
  background: linear-gradient(180deg, #020510 0%, #050810 100%);
}
.matrix-col {
  position: absolute;
  top: -120%;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  color: #10B981;
  text-shadow: 0 0 8px #10B981;
  animation: matrixFall linear infinite;
  line-height: 1.3;
  writing-mode: vertical-rl;
  letter-spacing: 2px;
  opacity: 0.55;
  pointer-events: none;
}
@keyframes matrixFall {
  from { top: -120%; }
  to   { top: 130%;  }
}

/* Responsive scaling for narrow screens */
@media (max-width: 900px) {
  .hero-scene { height: 170px; }
  .scene-title { font-size: 22px; }
  .scene-text { max-width: 70%; }
}
</style>
"""

PREMIUM_CSS = PREMIUM_CSS + CINEMATIC_CSS
