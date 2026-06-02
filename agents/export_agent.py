"""
Export Agent
- Generates beautifully formatted Excel (.xlsx) via xlsxwriter with corporate colored headers
- Generates clean landscape-oriented PDF reports via fpdf2
"""
import io
import xlsxwriter
from fpdf import FPDF
from datetime import datetime
import pandas as pd
from utils.logger import get_logger

logger = get_logger("export_agent")

# Corporate Color Palette
CORP_NAVY    = "#0A1628"
CORP_BLUE    = "#0066CC"
CORP_CYAN    = "#00AAFF"
CORP_LIGHT   = "#EEF2FF"
CORP_WHITE   = "#FFFFFF"
CORP_GOLD    = "#F5A623"


def _hex_to_rgb(hex_color: str) -> tuple:
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def generate_excel_report(df: pd.DataFrame, title: str = "Laporan Kandidat") -> bytes:
    """
    Generate a beautifully formatted Excel file using xlsxwriter.
    Corporate color headers, auto-column widths, alternating rows.
    """
    logger.info(f"EXPORT_AGENT: Generating Excel report with {len(df)} records...")
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {"in_memory": True})
    worksheet = workbook.add_worksheet("Data Kandidat")
    worksheet.set_landscape()
    worksheet.fit_to_pages(1, 0)

    # Format definitions
    header_fmt = workbook.add_format({
        "bold": True, "font_name": "Calibri", "font_size": 11,
        "font_color": CORP_WHITE, "bg_color": CORP_NAVY,
        "border": 1, "border_color": CORP_BLUE,
        "align": "center", "valign": "vcenter",
        "text_wrap": True
    })
    subheader_fmt = workbook.add_format({
        "bold": True, "font_name": "Calibri", "font_size": 9,
        "font_color": CORP_WHITE, "bg_color": CORP_BLUE,
        "border": 1, "align": "center", "valign": "vcenter"
    })
    row_even_fmt = workbook.add_format({
        "font_name": "Calibri", "font_size": 9,
        "bg_color": CORP_WHITE, "border": 1, "border_color": "#D0D8E8",
        "valign": "vcenter"
    })
    row_odd_fmt = workbook.add_format({
        "font_name": "Calibri", "font_size": 9,
        "bg_color": CORP_LIGHT, "border": 1, "border_color": "#D0D8E8",
        "valign": "vcenter"
    })
    score_high_fmt = workbook.add_format({
        "font_name": "Calibri", "font_size": 9, "bold": True,
        "font_color": "#006400", "bg_color": "#E8F5E9",
        "border": 1, "align": "center", "valign": "vcenter"
    })
    score_mid_fmt = workbook.add_format({
        "font_name": "Calibri", "font_size": 9, "bold": True,
        "font_color": "#B8860B", "bg_color": "#FFFDE7",
        "border": 1, "align": "center", "valign": "vcenter"
    })
    score_low_fmt = workbook.add_format({
        "font_name": "Calibri", "font_size": 9, "bold": True,
        "font_color": "#8B0000", "bg_color": "#FFEBEE",
        "border": 1, "align": "center", "valign": "vcenter"
    })
    title_fmt = workbook.add_format({
        "bold": True, "font_name": "Calibri", "font_size": 16,
        "font_color": CORP_NAVY, "align": "left", "valign": "vcenter"
    })
    meta_fmt = workbook.add_format({
        "font_name": "Calibri", "font_size": 9,
        "font_color": "#666666", "align": "left"
    })

    cols = list(df.columns)
    n_cols = len(cols)

    # Title banner
    worksheet.merge_range(0, 0, 0, n_cols - 1, f"⚡ CV Screener Pro · {title}", title_fmt)
    worksheet.set_row(0, 30)
    worksheet.merge_range(1, 0, 1, n_cols - 1,
        f"Generated: {datetime.now().strftime('%d %B %Y, %H:%M')}  |  Total Kandidat: {len(df)}",
        meta_fmt)
    worksheet.set_row(1, 18)

    # Column headers
    for col_idx, col_name in enumerate(cols):
        worksheet.write(2, col_idx, col_name.replace("_", " ").upper(), header_fmt)
    worksheet.set_row(2, 28)

    # Data rows
    for row_idx, (_, row) in enumerate(df.iterrows()):
        excel_row = row_idx + 3
        fmt = row_even_fmt if row_idx % 2 == 0 else row_odd_fmt
        worksheet.set_row(excel_row, 18)
        for col_idx, col_name in enumerate(cols):
            val = row[col_name]
            if pd.isna(val):
                val = ""
            # Score color coding
            if col_name in ["Skor_AI", "score", "Score"] and isinstance(val, (int, float)) and val != "":
                if float(val) >= 75:
                    worksheet.write(excel_row, col_idx, val, score_high_fmt)
                elif float(val) >= 50:
                    worksheet.write(excel_row, col_idx, val, score_mid_fmt)
                else:
                    worksheet.write(excel_row, col_idx, val, score_low_fmt)
            else:
                worksheet.write(excel_row, col_idx, str(val) if val != "" else "", fmt)

    # Auto column widths
    for col_idx, col_name in enumerate(cols):
        max_width = max(len(str(col_name)), 10)
        for _, row in df.iterrows():
            val = str(row[col_name]) if not pd.isna(row[col_name]) else ""
            max_width = max(max_width, min(len(val), 50))
        worksheet.set_column(col_idx, col_idx, max_width + 2)

    workbook.close()
    output.seek(0)
    logger.info("EXPORT_AGENT: Excel report generated successfully.")
    return output.read()


def generate_pdf_report(df: pd.DataFrame, title: str = "Laporan Kandidat CV Screener") -> bytes:
    """
    Generate a clean landscape corporate PDF report using fpdf2.
    """
    logger.info(f"EXPORT_AGENT: Generating PDF report with {len(df)} records...")

    class CorporatePDF(FPDF):
        def header(self):
            r, g, b = _hex_to_rgb(CORP_NAVY)
            self.set_fill_color(r, g, b)
            self.rect(0, 0, 297, 22, "F")
            self.set_font("Helvetica", "B", 14)
            self.set_text_color(255, 255, 255)
            self.set_xy(10, 5)
            self.cell(0, 12, f"CV Screener Pro | {title}", align="L")
            self.set_font("Helvetica", "", 8)
            self.set_xy(10, 14)
            self.cell(0, 6, f"Generated: {datetime.now().strftime('%d %B %Y %H:%M')}  |  Total: {len(df)} kandidat", align="L")
            self.ln(8)

        def footer(self):
            self.set_y(-12)
            r, g, b = _hex_to_rgb(CORP_NAVY)
            self.set_fill_color(r, g, b)
            self.rect(0, self.get_y(), 297, 12, "F")
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(180, 200, 220)
            self.cell(0, 10, f"CV Screener Pro · Page {self.page_no()}", align="C")

    pdf = CorporatePDF(orientation="L", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Column configuration
    display_cols = [c for c in df.columns if c not in ["resume_text", "Analisis_AI"]]
    n_cols = len(display_cols)
    page_width = 267  # A4 landscape usable width
    col_width = page_width / n_cols

    # Table header
    r, g, b = _hex_to_rgb(CORP_BLUE)
    pdf.set_fill_color(r, g, b)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 7)
    pdf.set_xy(10, pdf.get_y() + 2)
    for col in display_cols:
        pdf.cell(col_width, 8, col.replace("_", " ").upper()[:18], border=1, align="C", fill=True)
    pdf.ln()

    # Data rows
    pdf.set_font("Helvetica", "", 7)
    for i, (_, row) in enumerate(df.iterrows()):
        if i % 2 == 0:
            pdf.set_fill_color(248, 250, 255)
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.set_text_color(10, 22, 40)
        for col in display_cols:
            val = str(row.get(col, ""))[:22]
            # Score coloring
            if col in ["Skor_AI", "score"] and val.replace(".", "").isdigit():
                score = float(val)
                if score >= 75:
                    pdf.set_text_color(0, 100, 0)
                elif score >= 50:
                    pdf.set_text_color(180, 120, 0)
                else:
                    pdf.set_text_color(180, 0, 0)
            else:
                pdf.set_text_color(10, 22, 40)
            pdf.cell(col_width, 7, val, border=1, align="C", fill=True)
        pdf.ln()

    output = io.BytesIO()
    pdf_bytes = pdf.output()
    logger.info("EXPORT_AGENT: PDF report generated successfully.")
    return bytes(pdf_bytes)
