import io
from fpdf import FPDF

def sanitize_for_fpdf(text):
    """Menghapus emoji dan karakter non-latin agar FPDF tidak crash encoding"""
    if not text:
        return ""
    # Konversi ke string aman, encode ke latin-1 dengan mengabaikan karakter aneh
    return str(text).encode('latin-1', 'ignore').decode('latin-1')

def generate_pdf_report(dataframe, title_text="Enterprise Report"):
    """Fungsi ekspor PDF kelas korporat yang kebal terhadap error unicode/emoji"""
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Header Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, sanitize_for_fpdf(title_text), ln=True, align="C")
    pdf.ln(5)
    
    if dataframe.empty:
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 10, "No records found.", ln=True, align="C")
        return pdf.output(dest="S")
        
    # Setup Table Header Columns
    pdf.set_font("Arial", "B", 10)
    pdf.set_fill_color(15, 23, 42) # Warna gelap premium
    pdf.set_text_color(255, 255, 255) # Teks putih
    
    # Hitung lebar kolom dinamis berdasarkan jumlah kolom dataframe
    columns = dataframe.columns.tolist()
    col_width = 270 / max(1, len(columns)) # Lebar total landscape A4 ~270mm
    
    # Cetak nama kolom (Header)
    for col in columns:
        clean_col = sanitize_for_fpdf(col)
        pdf.cell(col_width, 8, clean_col, border=1, align="C", fill=True)
    pdf.ln()
    
    # Cetak isi data baris per baris (Body)
    pdf.set_font("Arial", "", 9)
    pdf.set_text_color(0, 0, 0) # Kembalikan teks ke hitam
    
    for _, row in dataframe.iterrows():
        # Hitung tinggi baris otomatis agar tidak meluber (Gunakan MultiCell logic jika teks panjang)
        for col in columns:
            val = str(row[col]) if row[col] is not None else ""
            clean_val = sanitize_for_fpdf(val) # <--- DI SINI KUNCI PENYELAMATNYA
            
            # Deteksi jika teks terlalu panjang (seperti kolom Analisis), gunakan pembungkus otomatis
            if len(clean_val) > 40:
                # Menggunakan trik posisi koordinat agar multicell tidak merusak baris tabel sebelahnya
                curr_x = pdf.get_x()
                curr_y = pdf.get_y()
                pdf.multi_cell(col_width, 6, clean_val, border=1, align="L")
                pdf.set_xy(curr_x + col_width, curr_y)
            else:
                pdf.cell(col_width, 7, clean_val, border=1, align="C")
        pdf.ln()
        
    # Kembalikan file dalam bentuk byte stream agar bisa di-download via Streamlit
    return bytes(pdf.output(dest="S"))
