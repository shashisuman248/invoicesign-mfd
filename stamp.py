import fitz
import pdfplumber
import re
import os

# Settings
SIGNATORY_NAME = "Aniket Chopra"
DESIGNATION = "Partner"
SIGNATURE_PATH = "signature.png"

def extract_details(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text

    inv_match = re.search(r"Invoice No[:\s]*(\w+)", full_text, re.IGNORECASE)
    invoice_no = inv_match.group(1) if inv_match else "Not found"

    date_match = re.search(r"Date[:\s]*(\d{1,2}/\d{1,2}/\d{4})", full_text, re.IGNORECASE)
    invoice_date = date_match.group(1) if date_match else "Not found"

    return invoice_no, invoice_date


def stamp_invoice(pdf_path, output_path):
    # Extract details
    invoice_no, invoice_date = extract_details(pdf_path)
    print(f"  Invoice No : {invoice_no}")
    print(f"  Date       : {invoice_date}")

    # Open and stamp
    doc = fitz.open(pdf_path)
    page = doc[-1]
    page_width = page.rect.width
    page_height = page.rect.height

    # Signature image
    sig_x = page_width - 220
    sig_y = page_height - 120
    sig_rect = fitz.Rect(sig_x, sig_y, sig_x + 150, sig_y + 45)
    page.insert_image(sig_rect, filename=SIGNATURE_PATH)

    # Name
    name_rect = fitz.Rect(sig_x - 10, sig_y + 47, sig_x + 200, sig_y + 62)
    page.insert_textbox(name_rect, SIGNATORY_NAME, fontsize=9,
                        fontname="helv", color=(0,0,0), align=1)

    # Designation
    desig_rect = fitz.Rect(sig_x - 10, sig_y + 63, sig_x + 200, sig_y + 76)
    page.insert_textbox(desig_rect, DESIGNATION, fontsize=8,
                        fontname="helv", color=(0,0,0), align=1)

    doc.save(output_path)
    doc.close()

    return invoice_no, invoice_date


def process_folder(input_folder="."):
    results = []
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf") and "_SIGNED" not in filename:
            pdf_path = os.path.join(input_folder, filename)
            output_path = os.path.join(input_folder, filename.replace(".pdf", "_SIGNED.pdf"))
            
            print(f"\n📄 Processing: {filename}")
            invoice_no, invoice_date = stamp_invoice(pdf_path, output_path)
            
            results.append({
                "filename": filename,
                "invoice_no": invoice_no,
                "invoice_date": invoice_date,
                "status": "Signed"
            })
            print(f"  ✅ Done!")

    return results


# Run
results = process_folder(".")
print(f"\n🎉 Total processed: {len(results)} invoices")