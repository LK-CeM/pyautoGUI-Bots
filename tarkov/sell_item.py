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

def print_mouse():
    while(True):
        print(pag.position())
        time.sleep(1)

def main(argv):
    setup()
    pause = False
    if (argv[1]== '-pm'):#print mouse
        print_mouse()


if __name__ == "__main__":
    main(sys.argv)

