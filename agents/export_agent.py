"""
Technical Export Agent — Clean FPDF2 Table Edition
- Handles clean data exports to Excel and PDF
- Uses modern fpdf2 Table Utility to completely prevent encoding crashes & overlapping text
"""
import io
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from fpdf import FPDF

# ──────────────────────────────────────────────────────────────────────────────
# EXCEL EXPORT ENGINE
# ──────────────────────────────────────────────────────────────────────────────
def generate_excel_report(dataframe: pd.DataFrame, sheet_name="Data Export") -> bytes:
    """Generates a professionally styled Excel sheet with corporate formatting."""
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name[:31]  # Excel limits sheet name to 31 chars
    ws.views.sheetView[0].showGridLines = True

    # Styles Setup
    font_family = "Segoe UI"
    header_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
    header_font = Font(name=font_family, size=11, bold=True, color="FFFFFF")
    data_font = Font(name=font_family, size=10, color="000000")
    
    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )
    
    center_align = Alignment(horizontal='center', vertical='center', wrap_text=True)
    left_align = Alignment(horizontal='left', vertical='center', wrap_text=True)

    # Write Headers
    headers = dataframe.columns.tolist()
    ws.append(headers)
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = center_align
        cell.border = thin_border
    ws.row_dimensions[1].height = 28

    # Write Data Rows
    for _, row in dataframe.iterrows():
        row_values = [str(val) if val is not None else "" for val in row]
        ws.append(row_values)
        
    # Formatting Data Rows
    for row_idx in range(2, ws.max_row + 1):
        ws.row_dimensions[row_idx].height = 22
        for cell in ws[row_idx]:
            cell.font = data_font
            cell.border = thin_border
            # Left align for long text fields, center for scores/IDs
            if len(str(cell.value)) > 25:
                cell.alignment = left_align
            else:
                cell.alignment = center_align

    # Auto-fit Column Widths
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 45)

    output = io.BytesIO()
    wb.save(output)
    return output.getvalue()


# ──────────────────────────────────────────────────────────────────────────────
# PDF EXPORT ENGINE (FIXED UNICODE & LAYOUT VIA FPDF2 TABLE UTILITY)
# ──────────────────────────────────────────────────────────────────────────────
def sanitize_for_fpdf(text):
    """Encodes text to standard western latin-1, completely throwing away unmappable symbols/emojis."""
    if text is None:
        return ""
    # Map common indonesian characters or strip breaking codes
    return str(text).encode('latin-1', 'ignore').decode('latin-1')


def generate_pdf_report(dataframe: pd.DataFrame, title_text="Enterprise Report") -> bytes:
    """
    Generates a world-class landscape A4 report using the robust fpdf2 Table Utility.
    Completely immune to UnicodeEncodingException and text-clipping.
    """
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Render Structural Page Title Header
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(15, 23, 42) # Premium deep indigo slate
    pdf.cell(0, 12, sanitize_for_fpdf(title_text), ln=True, align="L")
    pdf.ln(4)
    
    if dataframe.empty:
        pdf.set_font("Arial", "I", 11)
        pdf.set_text_color(148, 163, 184)
        pdf.cell(0, 10, "No operational records available in current grid selection.", ln=True, align="C")
        return bytes(pdf.output())

    # Build clean sanitized grid rows
    clean_headers = [sanitize_for_fpdf(col) for col in dataframe.columns.tolist()]
    
    clean_rows = []
    for _, row in dataframe.iterrows():
        sanitized_row = [sanitize_for_fpdf(row[col]) for col in dataframe.columns]
        clean_rows.append(sanitized_row)

    # Execute Modern FPDF2 Table Logic (No cell overlap, auto multi-line text-wrap)
    pdf.set_font("Arial", "", 9)
    pdf.set_text_color(0, 0, 0)
    
    # Initialize the Table Tool
    with pdf.table
