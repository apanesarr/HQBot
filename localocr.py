import screen
import pytesseract
from PIL import Image

def getText():
    im = Image.open(screen.IMAGE_DIR)
    ocr = pytesseract.image_to_string(im, lang = 'eng')
    question_options = ocr.split("?")
    question = question_options[0].replace('\n',' ') + " ?"
    options = list(filter(None,question_options[1].splitlines()))
    return {'question': question, 'options': options}
    