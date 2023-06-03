import pyautogui
from PIL import ImageChops
import time
import pyscreenshot 
import psutil

def capture_screen(region):
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

def images_are_different(image1, image2, threshold=0.8):
    diff = ImageChops.difference(image1, image2)
    if diff.getbbox() is not None:
        # Calculate the difference ratio
        diff_ratio = diff.getbbox()[2] * diff.getbbox()[3] / (image1.size[0] * image1.size[1])
        if diff_ratio >= threshold:
            return True
    return False

# Define the region of the screen you want to capture
x1=75
y1=110
x2=335
y2=212
region = (x1, y1, x2, y2)

# Initialize the previous image as None
previous_image = None
first = True
while True:
    # Capture the current screen region
    current_image = pyscreenshot.grab(bbox=(126, 242, 293, 265))
    if first:
        current_image.show()
    first = False
    time.sleep(1)
    # Check if the images are significantly different
    if previous_image is not None and images_are_different(previous_image, current_image):
        current_image.show()
        previous_image.show()
        print("Text has changed significantly.")
        exit()
        

    # Update the previous image with the current image
    previous_image = current_image.copy()
    for proc in psutil.process_iter():
        if proc.name() == "display":
            proc.kill()

    # Wait for 1 second
    
