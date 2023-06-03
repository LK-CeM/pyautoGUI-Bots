import time
import pyautogui as p
from PIL import Image
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

def capture_second_monitor_screenshot():
    # Get the coordinates of the second monitor
    monitor_info = ImageGrab.grab().getmonitorinfo()
    second_monitor_coords = monitor_info[1]

    # Capture the screenshot of the second monitor
    screenshot = ImageGrab.grab(bbox=second_monitor_coords)
    screenshot.show()  # Display the screenshot

    # Save the screenshot image to a file
    screenshot.save('screenshot.png')
    

monitor_one = False
pos1 = (158, 155)
pos2 = (265, 173)
if monitor_one == False:
    pos1 =(2089, 175)
    pos2 =(2171, 193)

while True:
    image = p.screenshot()
    pixel_value = image.getpixel((2095, 55))
    print (pixel_value)
    if (pixel_value[0] +pixel_value[1]+ pixel_value[2] > 380):
        time.sleep(1)
        p.moveTo(pos1)
        time.sleep(0.01)
        p.rightClick()
        time.sleep(0.01)
        p.moveTo(pos2)
        time.sleep(0.01)
        p.click()
        time.sleep(1)
        if (pixel_value[0] +pixel_value[1]+ pixel_value[2] > 380):
            time.sleep(0.2)
            p.moveTo((pos1[0]+10,pos1[1]))
            time.sleep(0.2)
            p.rightClick()
            time.sleep(0.2)
            p.moveTo(pos2)
            time.sleep(0.2)
            p.click()
            time.sleep(0.1)
    time.sleep(1)