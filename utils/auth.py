import hashlib
from datetime import datetime
import pandas as pd
import sqlite3
import os
import streamlit as st
from utils.logger import get_logger

logger = get_logger("auth")

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "candidates.db")

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def ensure_users_table_exists():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            Username TEXT PRIMARY KEY,
            Password_Hash TEXT,
            Created_At TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_users_df(conn):
    try:
        ensure_users_table_exists()
        df = pd.read_sql_query("SELECT * FROM Users", conn)
        if df.empty:
            return pd.DataFrame(columns=["Username", "Password_Hash", "Created_At"])
        return df
    except Exception as e:
        logger.warning(f"AUTH: Failed to read Users table, returning empty DF. {e}")
        return pd.DataFrame(columns=["Username", "Password_Hash", "Created_At"])

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username: str, password: str) -> bool:
    try:
        ensure_users_table_exists()
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if user already exists
        cursor.execute("SELECT 1 FROM Users WHERE Username = ?", (username,))
        if cursor.fetchone():
            conn.close()
            return False
            
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO Users (Username, Password_Hash, Created_At)
            VALUES (?, ?, ?)
        ''', (username, hash_password(password), created_at))
        
        conn.commit()
        conn.close()
        logger.info(f"AUTH: Successfully created user '{username}'")
        return True
    except Exception as e:
        logger.error(f"AUTH: Error creating user '{username}': {e}")
        return False

def check_credentials(username: str, password: str) -> bool:
    # First check if it's the admin from secrets
    try:
        if username == st.secrets["auth"]["admin_username"] and hash_password(password) == st.secrets["auth"]["admin_password_hash"]:
            logger.info(f"AUTH: Successful ADMIN login for '{username}'")
            return True
    except:
        pass
        
    # Check SQLite for regular users
    try:
        ensure_users_table_exists()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Password_Hash FROM Users WHERE Username = ?", (username,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            stored_hash = row[0]
            if hash_password(password) == stored_hash:
                logger.info(f"AUTH: Successful user login for '{username}'")
                return True
                
        logger.warning(f"AUTH: Failed login attempt for '{username}'")
        return False
    except Exception as e:
        logger.error(f"AUTH: Database check error: {e}")
        return False

def logout():
    for key in ["authenticated", "username"]:
        if key in st.session_state:
            del st.session_state[key]
    logger.info("AUTH: User logged out.")
    st.rerun()

def require_auth():
    """Render login UI if not authenticated. Returns True if authenticated."""
    if st.session_state.get("authenticated"):
        return True

    # Premium login page styling
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    .stApp { background: linear-gradient(135deg, #0A1628 0%, #0D2447 40%, #0066CC 100%); }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: rgba(255,255,255,0.7);
    }
    .stTabs [aria-selected="true"] {
        color: white !important;
        border-bottom: 2px solid white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("""
        <div style="
            background: rgba(255,255,255,0.07);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 24px 24px 0 0;
            padding: 48px 40px 20px 40px;
            margin-top: 80px;
            box-shadow: 0 32px 64px rgba(0,0,0,0.4);
            font-family: 'Plus Jakarta Sans', sans-serif;
        ">
            <div style="text-align:center;">
                <div style="font-size:48px; margin-bottom:8px;">⚡</div>
                <div style="font-size:11px; letter-spacing:4px; color:rgba(255,255,255,0.5); text-transform:uppercase; margin-bottom:6px;">TALENTAI · ENTERPRISE</div>
                <div style="font-size:26px; font-weight:800; color:white; line-height:1.2;">CV Screener Pro</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.container(border=True):
            tab1, tab2 = st.tabs(["🔐 Sign In", "📝 Sign Up"])
            
            with tab1:
                with st.form("login_form"):
                    username = st.text_input("Username", placeholder="Enter your username")
                    password = st.text_input("Password", type="password", placeholder="Enter your password")
                    submitted = st.form_submit_button("Sign In →", use_container_width=True)
                    if submitted:
                        if not username or not password:
                            st.warning("Please enter both username and password.")
                        elif check_credentials(username, password):
                            st.session_state["authenticated"] = True
                            st.session_state["username"] = username
                            st.rerun()
                        else:
                            st.error("Invalid credentials. Please try again.")
                            
            with tab2:
                with st.form("signup_form"):
                    new_username = st.text_input("Choose Username", placeholder="Enter a unique username")
                    new_password = st.text_input("Choose Password", type="password", placeholder="Enter a strong password")
                    confirm_password = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password")
                    signup_submitted = st.form_submit_button("Create Account →", use_container_width=True)
                    
                    if signup_submitted:
                        if not new_username or not new_password:
                            st.warning("All fields are required!")
                        elif new_password != confirm_password:
                            st.error("Passwords do not match!")
                        elif len(new_password) < 6:
                            st.warning("Password must be at least 6 characters long.")
                        else:
                            with st.spinner("Creating account..."):
                                success = create_user(new_username, new_password)
                                if success:
                                    st.success("Account created successfully! You can now Sign In.")
                                else:
                                    st.error("Username already exists or database error. Please try another.")

    return False
