try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import pyautogui



pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#string_from_img = pytesseract.image_to_string(Image.open('./imgs/test.png'))
418,43
#im = pyautogui.screenshot(region=(1367,159, 80, 30)) #price of item
im = pyautogui.screenshot(region=(422,45, 12, 20)) #open offers
im.show()
string_from_img = pytesseract.image_to_string(im, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " ")) #this reads a single char
print(string_from_img)
cleaned_string = ""
for c in string_from_img:
    if c.isdigit():
        cleaned_string += c
print(cleaned_string)
