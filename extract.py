def extract_details(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text

    # Invoice No - multiple formats
    inv_match = re.search(
        r"(?:Invoice No|Inv serial No|Invoice Number)[:\s.]*([A-Z0-9/\-]+)",
        full_text, re.IGNORECASE
    )
    invoice_no = inv_match.group(1).strip() if inv_match else "Not found"

    # Date - DD/MM/YYYY or "June 05, 2026" format
    date_match = re.search(
        r"(?:Invoice Date|Date)[:\s]*(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{4}|\w+ \d{1,2},\s*\d{4})",
        full_text, re.IGNORECASE
    )
    invoice_date = date_match.group(1).strip() if date_match else "Not found"

    return invoice_no, invoice_date