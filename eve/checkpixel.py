import pyautogui as p
from PIL import Image

image = Image.open('test.png')


pixel_value = image.getpixel((2095, 55))

# Print the pixel value
print(pixel_value)