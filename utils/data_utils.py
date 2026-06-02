import os
import sqlite3
import pandas as pd
import streamlit as st
from utils.logger import get_logger

logger = get_logger("data_utils")
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "candidates.db")

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def ensure_database_exists():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Candidates (
            NIP TEXT PRIMARY KEY,
            Nama TEXT,
            Posisi TEXT,
            Departemen TEXT,
            Pendidikan TEXT,
            Pengalaman_Tahun INTEGER,
            Universitas TEXT,
            Status TEXT,
            Skor_AI REAL,
            Analisis_AI TEXT,
            Tanggal_Input TEXT
        )
    ''')
    conn.commit()
    conn.close()

def load_database():
    try:
        ensure_database_exists()
        conn = get_db_connection()
        df = pd.read_sql_query("SELECT * FROM Candidates", conn)
        conn.close()
        if df.empty:
            return pd.DataFrame(columns=[
                "NIP", "Nama", "Posisi", "Departemen", "Pendidikan", 
                "Pengalaman_Tahun", "Universitas", "Status", "Skor_AI", 
                "Analisis_AI", "Tanggal_Input"
            ])
        return df
    except Exception as e:
        logger.error(f"DATABASE: Failed to load SQLite database - {e}")
        return pd.DataFrame()

def append_candidate_to_db(record):
    try:
        ensure_database_exists()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Candidates (
                NIP, Nama, Posisi, Departemen, Pendidikan, 
                Pengalaman_Tahun, Universitas, Status, Skor_AI, 
                Analisis_AI, Tanggal_Input
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(NIP) DO UPDATE SET
                Nama=excluded.Nama,
                Posisi=excluded.Posisi,
                Departemen=excluded.Departemen,
                Pendidikan=excluded.Pendidikan,
                Pengalaman_Tahun=excluded.Pengalaman_Tahun,
                Universitas=excluded.Universitas,
                Status=excluded.Status,
                Skor_AI=excluded.Skor_AI,
                Analisis_AI=excluded.Analisis_AI,
                Tanggal_Input=excluded.Tanggal_Input
        ''', (
            record.get('NIP'), record.get('Nama'), record.get('Posisi'),
            record.get('Departemen'), record.get('Pendidikan'),
            record.get('Pengalaman_Tahun'), record.get('Universitas'),
            record.get('Status'), record.get('Skor_AI'),
            record.get('Analisis_AI'), record.get('Tanggal_Input')
        ))
        conn.commit()
        conn.close()
        logger.info(f"DATABASE: Upserted candidate NIP={record.get('NIP', 'UNKNOWN')} to SQLite")
        return True
    except Exception as e:
        logger.error(f"DATABASE: Failed to append candidate to SQLite - {e}")
        return False

def radar_header_detect(file_path):
    try:
        if file_path.endswith('.csv'):
            df_raw = pd.read_csv(file_path, header=None, nrows=15)
        else:
            df_raw = pd.read_excel(file_path, header=None, nrows=15)
        
        header_row_idx = None
        for i, row in df_raw.iterrows():
            if any('NIP' in str(cell).upper() for cell in row.values):
                header_row_idx = i
                break
                
        if header_row_idx is not None:
            if file_path.endswith('.csv'):
                return pd.read_csv(file_path, header=header_row_idx)
            else:
                return pd.read_excel(file_path, header=header_row_idx)
        return None
    except Exception as e:
        logger.error(f"DATABASE: Radar header detection failed - {e}")
        return None
