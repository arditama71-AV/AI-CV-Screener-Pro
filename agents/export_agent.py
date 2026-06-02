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
    ws.title = sheet_name[:31]
    ws.views.sheetView[0].showGridLines = True

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

    headers = dataframe.columns.tolist()
    ws.append(headers)
    for cell in ws[1]:
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = center_align
        cell.border = thin_border
    ws.row_dimensions[1].height = 28

    for _, row in dataframe.iterrows():
        row_values = [str(val) if val is not None else "" for val in row]
        ws.append(row_values)
        
    for row_idx in range(2, ws.max_row + 1):
        ws.row_dimensions[row_idx].height = 22
        for cell in ws[row_idx]:
            cell.font = data_font
            cell.border = thin_border
            if len(str(cell.value)) > 25:
                cell.alignment = left_align
            else:
                cell.alignment = center_align

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
    """Rigorous sanitation that drops emojis, quotes, and non-latin symbols entirely."""
    if text is None:
        return ""
    # Convert to pure string, encode to standard latin-1 while ignoring errors, then decode safely
    s = str(text).strip()
    return s.encode('latin-1', 'ignore').decode('latin-1')


def generate_pdf_report(dataframe: pd.DataFrame, title_text="Enterprise Report") -> bytes:
    """
    Generates an automated A4 report using robust modern fpdf2 Table block logic.
    Completely replaces legacy pdf.cell looping.
    """
    pdf = FPDF(orientation="L", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Render Structural Page Title Header
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 10, sanitize_for_fpdf(title_text), ln=True, align="L")
    pdf.ln(3)
    
    if dataframe.empty:
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 10, "No records available.", ln=True, align="C")
        return bytes(pdf.output())

    # Form clean list grids
    clean_headers = [sanitize_for_fpdf(col) for col in dataframe.columns]
    
    clean_rows = []
    for _, row in dataframe.iterrows():
        sanitized_row = [sanitize_for_fpdf(row[col]) for col in dataframe.columns]
        clean_rows.append(sanitized_row)

    # Initialize Modern Table block tool
    with pdf.table(
        borders_layout="HORIZONTAL_LINES", 
        cell_fill_color=245, 
        cell_fill_mode="ROWS",
        line_height=7,
        text_align="CENTER"
    ) as table:
        
        # Header Row
        header_row = table.row()
        pdf.set_font("Arial", "B", 10)
        pdf.set_text_color(255, 255, 255)
        for header_cell in clean_headers:
            header_row.cell(header_cell, background_color=(15, 23, 42))
            
        # Data Rows
        pdf.set_font("Arial", "", 9)
        pdf.set_text_color(15, 23, 42)
        for row_data in clean_rows:
            data_row = table.row()
            for cell_value in row_data:
                if len(cell_value) > 30:
                    data_row.cell(cell_value, text_align="LEFT")
                else:
                    data_row.cell(cell_value, text_align="CENTER")

    return bytes(pdf.output())
