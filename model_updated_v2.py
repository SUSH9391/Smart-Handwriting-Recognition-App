import pytesseract
from PIL import Image
import os

# Verify Tesseract installation path
tesseract_cmd = r'Tesseract-OCR/tesseract.exe'
if not os.path.exists(tesseract_cmd):
    raise Exception(f"Tesseract executable not found at {tesseract_cmd}. Please check the installation.")

pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

def ocr_core(filename):
    try:
        # Open the image file
        img = Image.open(filename)
        print(f"Successfully opened image: {filename}")
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

    try:
        # Perform OCR on the image
        text = pytesseract.image_to_string(img)
        print("OCR process completed successfully.")
        return text
    except Exception as e:
        print(f"Error during OCR process: {e}")
        return None
