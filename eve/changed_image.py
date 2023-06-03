import cv2
import numpy as np
import pyautogui
import time

class ImageWatcher:
    def __init__(self, region):
        self.region = region
        self.previous_image = None

    def run(self):
        while True:
            screenshot = self.capture_screenshot()
            if self.is_image_changed(screenshot):
                self.show_changed_image(screenshot)
            time.sleep(1)

    def capture_screenshot(self):
        x1, y1, x2, y2 = self.region
        screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        cv2.imshow("Changed Image", screenshot)
        return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    def is_image_changed(self, image):
        if self.previous_image is None:
            self.previous_image = image
            return False

        difference = cv2.absdiff(image, self.previous_image)
        gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 100:
                self.previous_image = image
                return True

        self.previous_image = image
        return False

    def show_changed_image(self, image):
        cv2.imshow("Changed Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Select the region of the screen to monitor.")
    x1=103
    y1=239
    x2=355
    y2=264
    image_watcher = ImageWatcher((x1,y1,x2,y2))
    image_watcher.run()
