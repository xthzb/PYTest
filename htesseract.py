import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def getText(__img:str)->str:
    img = Image.open(__img)
    text = pytesseract.image_to_string(img, lang='chi_sim')
    return text