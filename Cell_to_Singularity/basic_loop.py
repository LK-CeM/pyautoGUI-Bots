import keyboard
import pyautogui as pag
import time
import sys
import os


def setup():
    pag.FAILSAFE = True
    screenWidth, screenHeight = pag.size()
    pag.PAUSE = 0.00005
    time.sleep(2)
    print('Setup complete')

#the most basic of clickers - just click
def justClick():
    while (True):
        pag.click(pag.position())
        time.sleep(0.001)

def main(argv):
    setup()
    if (argv[1]== 'jc'):
        justClick()
    pause = True
    while (True):
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('p'):  # if key 'p' is pressed
                print('pause / unpause') 
                pag.click(pag.position()) #signals to user that pause changed
                pause = not pause
        except: pass
        time.sleep(2)
        if (not pause):
            pag.screenshot('test.png')
            for dinoPic in os.listdir("./dinoPictures/"):# click on all dinonames to level them up
                if dinoPic.endswith(".png"):
                    dinoPos = (pag.locateOnScreen("./dinoPictures/"+dinoPic, confidence=0.95))
                    if (dinoPos):
                        pag.click(dinoPos[0],dinoPos[1])
        


if __name__ == "__main__":
    main(sys.argv)

