import pandas as pd
import pdfplumber
import os

def extract_data_from_file(file):
    """Extracts structured data from an Excel or PDF file."""
    try:
        if file.name.endswith('.xlsx'):
            return pd.read_excel(file)
        elif file.name.endswith('.pdf'):
            return extract_table_from_pdf(file)
        else:
            return None
    except Exception as e:
        print(f"❌ Error extracting data: {e}")
        return None

def extract_table_from_pdf(file):
    """Extracts tables from a PDF file and returns as a Pandas DataFrame."""
    tables = []
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])  # First row as headers
                tables.append(df)
    return pd.concat(tables, ignore_index=True) if tables else None
