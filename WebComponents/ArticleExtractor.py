import pytesseract
from PIL import Image
from io import BytesIO
import easyocr

# Function to perform OCR with Tesseract
def ocr_with_tesseract(image):
	# Perform OCR on the image using pytesseract
	extracted_text = pytesseract.image_to_string(image)
	return extracted_text

# Function to perform OCR with EasyOCR
def ocr_with_easyocr(image):
	# Convert the image to bytes for easyocr
	image_bytes = image.tobytes()
	
	# Perform OCR on the image using easyocr
	reader = easyocr.Reader(['en'])  # You can add other languages as needed
	result = reader.readtext(image_bytes)
	
	# Extract text from OCR result
	extracted_text = [text[1] for text in result]
	
	return extracted_text
