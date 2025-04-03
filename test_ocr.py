from model_updated import ocr_core

# Test the OCR functionality
image_path = 'static/uploads/download.jpeg'  # Example image path
extracted_text = ocr_core(image_path)

if extracted_text:
    print("Extracted Text:")
    print(extracted_text)
else:
    print("Failed to extract text.")
