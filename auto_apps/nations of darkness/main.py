import pyautogui
import sys

#pyautogui.displayMousePosition()
TOP_LEFT = 64, 130
CENTER = 200, 400

def main(argv):
    logo_x, logo_y = pyautogui.locateCenterOnScreen('emulator.png')
    pyautogui.moveTo(logo_x,logo_y)
    pyautogui.dragTo(15,15)
    

if __name__ == "__main__":
    main(sys.argv)