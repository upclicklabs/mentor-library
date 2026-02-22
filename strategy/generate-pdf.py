#!/usr/bin/env python3
"""Convert competitive analysis markdown to a styled PDF using fpdf2."""

from fpdf import FPDF, XPos, YPos
import re
import os

MD_PATH = os.path.join(os.path.dirname(__file__), "competitive-analysis.md")
PDF_PATH = os.path.join(os.path.dirname(__file__), "UpClick-Labs-Competitive-Analysis.pdf")


def sanitize(text):
    """Replace unicode chars that latin-1 can't encode."""
    replacements = {
        '\u2014': '--', '\u2013': '-', '\u2018': "'", '\u2019': "'",
        '\u201c': '"', '\u201d': '"', '\u2026': '...', '\u2022': '*',
        '\u2190': '<-', '\u2192': '->', '\u2713': '[x]', '\u2717': '[ ]',
        '\u25c0': '<', '\u25b6': '>', '\u2605': '*', '\u2764': '<3',
        '\u2248': '~', '\u2260': '!=', '\u2264': '<=', '\u2265': '>=',
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text.encode('latin-1', errors='replace').decode('latin-1')


def clean_md(text):
    """Remove markdown formatting for plain text."""
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'`(.*?)`', r'\1', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    return sanitize(text.strip())


class StyledPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 5, sanitize("UpClick Labs -- Competitive Analysis"), new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


def parse_table(lines):
    headers, rows = [], []
    for line in lines:
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if all(re.match(r'^[-:]+$', c) for c in cells):
            continue
        if not headers:
            headers = cells
        else:
            rows.append(cells)
    return headers, rows


def render_table(pdf, headers, rows):
    num_cols = len(headers)
    avail = 190
    col_w = [avail / num_cols] * num_cols

    if pdf.get_y() > 240:
        pdf.add_page()

    # Header row
    pdf.set_fill_color(30, 27, 75)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 7)
    for i, h in enumerate(headers):
        pdf.cell(col_w[i], 6, clean_md(h)[:30], border=1, fill=True)
    pdf.ln()

    # Data rows
    pdf.set_font("Helvetica", "", 7)
    for ri, row in enumerate(rows):
        if pdf.get_y() > 268:
            pdf.add_page()
            pdf.set_fill_color(30, 27, 75)
            pdf.set_text_color(255, 255, 255)
            pdf.set_font("Helvetica", "B", 7)
            for i, h in enumerate(headers):
                pdf.cell(col_w[i], 6, clean_md(h)[:30], border=1, fill=True)
            pdf.ln()
            pdf.set_font("Helvetica", "", 7)

        bg = (248, 249, 255) if ri % 2 == 0 else (255, 255, 255)
        pdf.set_fill_color(*bg)
        pdf.set_text_color(26, 26, 46)

        y_start = pdf.get_y()
        x_start = pdf.get_x()
        max_y = y_start

        # Draw cells
        for i, cell in enumerate(row):
            pdf.set_xy(x_start + sum(col_w[:i]), y_start)
            text = clean_md(cell)
            pdf.multi_cell(col_w[i], 4, text, border=1, fill=True)
            max_y = max(max_y, pdf.get_y())

        pdf.set_y(max_y)
    pdf.ln(3)


def main():
    with open(MD_PATH, "r") as f:
        lines = f.readlines()

    pdf = StyledPDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # ===== TITLE PAGE =====
    pdf.ln(30)
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(15, 15, 35)
    pdf.multi_cell(0, 14, "UpClick Labs\nCompetitive Analysis", align="C")
    pdf.ln(8)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(99, 102, 241)
    pdf.cell(0, 8, "v2 -- Corrected for Service-Based Competitors", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(0, 8, "February 2026", align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(15)
    pdf.set_draw_color(99, 102, 241)
    pdf.set_line_width(0.5)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(10)

    # TOC
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(30, 27, 75)
    pdf.cell(0, 10, "Contents", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(3)
    toc = [
        "1. Competitive Landscape Overview",
        "2. Messaging Matrix (Service Competitors)",
        "3. Positioning Map (2x2)",
        "4. Top 5 Content Gaps & Opportunities",
        "5. Competitive Battlecards (Top 5 Threats)",
        "6. LinkedIn Voice Analysis",
        "7. Revised Positioning Statement",
        "8. Niche Analysis -- First 3 Verticals",
        "9. Strategic Recommendations",
    ]
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(60, 60, 80)
    for item in toc:
        pdf.cell(0, 7, item, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.add_page()

    # ===== PARSE CONTENT =====
    i = 0
    in_table = False
    table_lines = []
    in_code = False
    code_lines = []

    while i < len(lines):
        raw = lines[i].rstrip("\n")

        # Code blocks
        if raw.strip().startswith("```"):
            if in_code:
                # Render code block
                pdf.set_fill_color(241, 245, 249)
                pdf.set_font("Courier", "", 6.5)
                pdf.set_text_color(50, 50, 50)
                for cl in code_lines:
                    if pdf.get_y() > 275:
                        pdf.add_page()
                    pdf.cell(0, 3.5, sanitize("  " + cl), fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.ln(3)
                code_lines = []
                in_code = False
            else:
                if in_table and table_lines:
                    headers, rows = parse_table(table_lines)
                    if headers:
                        render_table(pdf, headers, rows)
                    table_lines = []
                    in_table = False
                in_code = True
            i += 1
            continue

        if in_code:
            code_lines.append(raw)
            i += 1
            continue

        # Tables
        if raw.strip().startswith("|"):
            in_table = True
            table_lines.append(raw)
            i += 1
            continue
        elif in_table:
            headers, rows = parse_table(table_lines)
            if headers:
                render_table(pdf, headers, rows)
            table_lines = []
            in_table = False

        # Skip
        if raw.strip() == "---" or raw.startswith("> Last updated"):
            i += 1
            continue

        # H1 (skip, we have title page)
        if raw.startswith("# ") and not raw.startswith("## "):
            i += 1
            continue

        # H2
        if raw.startswith("## "):
            title = sanitize(raw[3:].strip())
            if pdf.get_y() > 40:
                pdf.add_page()
            pdf.set_font("Helvetica", "B", 15)
            pdf.set_text_color(30, 27, 75)
            pdf.ln(3)
            pdf.multi_cell(0, 8, title)
            pdf.set_draw_color(199, 210, 254)
            pdf.set_line_width(0.4)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(4)
            i += 1
            continue

        # H3
        if raw.startswith("### "):
            title = sanitize(raw[4:].strip())
            pdf.set_font("Helvetica", "B", 11)
            pdf.set_text_color(55, 48, 163)
            pdf.ln(3)
            pdf.multi_cell(0, 6, title)
            pdf.ln(2)
            i += 1
            continue

        # Blockquote
        if raw.startswith("> "):
            quote = clean_md(raw[2:])
            pdf.set_fill_color(238, 242, 255)
            y0 = pdf.get_y()
            pdf.set_font("Helvetica", "I", 9.5)
            pdf.set_text_color(49, 46, 129)
            pdf.set_x(16)
            pdf.multi_cell(178, 5.5, quote, fill=True)
            pdf.set_draw_color(99, 102, 241)
            pdf.set_line_width(1)
            pdf.line(14, y0, 14, pdf.get_y())
            pdf.ln(3)
            i += 1
            continue

        # Numbered list
        if re.match(r'^\d+\.\s', raw.strip()):
            text = clean_md(re.sub(r'^\d+\.\s*', '', raw.strip()))
            pdf.set_font("Helvetica", "", 9.5)
            pdf.set_text_color(26, 26, 46)
            pdf.set_x(14)
            pdf.cell(5, 5.5, "*")
            pdf.set_x(19)
            pdf.multi_cell(175, 5.5, text)
            pdf.ln(1)
            i += 1
            continue

        # Bullet list
        if raw.strip().startswith("- "):
            text = clean_md(raw.strip()[2:])
            pdf.set_font("Helvetica", "", 9.5)
            pdf.set_text_color(26, 26, 46)
            pdf.set_x(14)
            pdf.cell(5, 5.5, "*")
            pdf.set_x(19)
            pdf.multi_cell(175, 5.5, text)
            pdf.ln(1)
            i += 1
            continue

        # Bold standalone
        stripped = raw.strip()
        if stripped.startswith("**") and stripped.endswith("**"):
            text = clean_md(stripped)
            pdf.set_font("Helvetica", "B", 9.5)
            pdf.set_text_color(26, 26, 46)
            pdf.multi_cell(0, 5.5, text)
            pdf.ln(2)
            i += 1
            continue

        # Regular text
        text = clean_md(raw)
        if text:
            pdf.set_font("Helvetica", "", 9.5)
            pdf.set_text_color(26, 26, 46)
            pdf.multi_cell(0, 5.5, text)
            pdf.ln(2)

        i += 1

    # Flush remaining table
    if in_table and table_lines:
        headers, rows = parse_table(table_lines)
        if headers:
            render_table(pdf, headers, rows)

    pdf.output(PDF_PATH)
    size_kb = os.path.getsize(PDF_PATH) / 1024
    print(f"PDF generated: {PDF_PATH}")
    print(f"Size: {size_kb:.0f} KB")


if __name__ == "__main__":
    main()
