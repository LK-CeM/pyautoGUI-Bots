import pyautogui as pag
import time
import sys
import os


def setup():
    pag.FAILSAFE = True
    screenWidth, screenHeight = pag.size()
    time.sleep(2)
    print('Setup complete')

def main(argv):
    setup()
    while (True):
        pag.write("hello world")
        pag.screenshot('test.png')
        for dinoPic in os.listdir("./dinoPictures/"):
            if dinoPic.endswith(".png"):
                dinoPos = (pag.locateOnScreen("./dinoPictures/"+dinoPic, confidence=0.9))
                pag.click(dinoPos[0],dinoPos[1])
        time.sleep(2)


if __name__ == "__main__":
    main(sys.argv)
