import pyautogui as pag
import time
import sys


def setup():
    pag.FAILSAFE = True
    screenWidth, screenHeight = pag.size()
    time.sleep(5)
    print('Setup complete')

def main(argv):
    setup()
    while (True):
        pag.write("hello world")
        time.sleep(1)


if __name__ == "__main__":
    main(sys.argv)
