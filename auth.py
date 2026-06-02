"""
Secure Authentication Module — SHA-256
Supports: Streamlit secrets.toml (local/Streamlit Cloud) + HuggingFace env vars
"""
import hashlib
import os
import streamlit as st
from utils.logger import get_logger

logger = get_logger("auth")


def _get_secret(section: str, key: str, env_fallback: str = None) -> str:
    """
    Read secret with priority:
    1. Streamlit secrets (secrets.toml / Streamlit Cloud)
    2. Environment variable (HuggingFace Spaces)
    """
    try:
        return st.secrets[section][key]
    except Exception:
        if env_fallback:
            val = os.environ.get(env_fallback, "")
            if val:
                return val
        return ""


def hash_password(p: str) -> str:
    return hashlib.sha256(p.encode()).hexdigest()


def check_credentials(username: str, password: str) -> bool:
    try:
        stored_user = _get_secret("auth", "admin_username", "AUTH_USERNAME")
        stored_hash = _get_secret("auth", "admin_password_hash", "AUTH_PASSWORD_HASH")

        if not stored_user or not stored_hash:
            logger.error("AUTH: Credentials not configured in secrets or env vars.")
            return False

        valid = (username == stored_user and hash_password(password) == stored_hash)
        logger.info(f"AUTH: {'OK' if valid else 'FAILED'} — user='{username}'")
        return valid
    except Exception as e:
        logger.error(f"AUTH: Error — {e}")
        return False


def logout():
    for k in ["authenticated", "username"]:
        st.session_state.pop(k, None)
    logger.info("AUTH: Logged out.")
    st.rerun()


def require_auth() -> bool:
    if st.session_state.get("authenticated"):
        return True

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    *, *::before, *::after { box-sizing: border-box; }
    html, body, .stApp {
      font-family: 'Inter', sans-serif !important;
      background: #080C14 !important;
      -webkit-font-smoothing: antialiased !important;
    }
    #MainMenu, footer, header,
    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    .stDeployButton { display:none !important; }
    .main .block-container { padding: 0 !important; max-width: 100% !important; }
    .stTextInput label {
      font-size: 12px !important; font-weight: 500 !important;
      color: #8896B3 !important;
    }
    .stTextInput input {
      background: #0B1120 !important;
      border: 1px solid rgba(255,255,255,0.09) !important;
      border-radius: 8px !important;
      color: #F1F5FF !important;
      font-size: 13px !important;
      font-family: 'Inter', sans-serif !important;
    }
    .stTextInput input:focus {
      border-color: rgba(56,189,248,0.45) !important;
      box-shadow: 0 0 0 3px rgba(56,189,248,0.07) !important;
    }
    .stTextInput input::placeholder { color: #2D3A52 !important; }
    .stFormSubmitButton > button {
      background: #38BDF8 !important;
      color: #020812 !important;
      font-family: 'Inter', sans-serif !important;
      font-weight: 600 !important;
      font-size: 13px !important;
      border: none !important;
      border-radius: 8px !important;
      height: 40px !important;
      width: 100% !important;
      transition: all 150ms ease !important;
      box-shadow: 0 0 0 1px rgba(56,189,248,0.35) !important;
    }
    .stFormSubmitButton > button:hover {
      background: #60CAFF !important;
      transform: translateY(-1px) !important;
    }
    .stAlert > div {
      background: rgba(239,68,68,0.07) !important;
      border: 1px solid rgba(239,68,68,0.15) !important;
      border-left: 2px solid #EF4444 !important;
      border-radius: 8px !important;
      font-size: 12px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.1, 1])
    with col2:
        st.markdown("""
        <div style="height:60px"></div>
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:28px">
          <div style="width:36px;height:36px;border-radius:10px;
            background:linear-gradient(135deg,#38BDF8,#22D3EE);
            display:flex;align-items:center;justify-content:center;font-size:18px;
            box-shadow:0 0 20px rgba(56,189,248,0.3)">⚡</div>
          <div>
            <div style="font-size:14px;font-weight:700;color:#F1F5FF">CV Screener Pro</div>
            <div style="font-size:10px;color:#4A5878">TalentAI Enterprise</div>
          </div>
        </div>
        <div style="font-size:21px;font-weight:700;color:#F1F5FF;letter-spacing:-.4px;margin-bottom:4px">
          Sign in to your workspace
        </div>
        <div style="font-size:12px;color:#4A5878;margin-bottom:24px">
          Enter your credentials to access the dashboard.
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form"):
            username = st.text_input("Username", placeholder="your username")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            submitted = st.form_submit_button("Continue →", use_container_width=True)
            if submitted:
                if check_credentials(username, password):
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username
                    st.rerun()
                else:
                    st.error("Incorrect username or password.")

        st.markdown("""
        <div style="margin-top:20px;font-size:11px;color:#2D3A52;text-align:center">
          Secured with SHA-256 · TalentAI Enterprise v5.0
        </div>
        """, unsafe_allow_html=True)

    return False
