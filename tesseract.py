from PIL import Image
import pytesseract as ocr
from pytesseract.pytesseract import Output

ocr.pytesseract.tesseract_cmd = "C:/Users/Chuno/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

img = Image.open("images/cnh_full.jpg")

print(img)

# print(ocr.image_to_data(img, lang='por', output_type=Output.DICT))
print(ocr.image_to_string(img, lang='por'))
