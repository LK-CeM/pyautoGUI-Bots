import pyautogui
import sys
import time

#pyautogui.displayMousePosition()
TOP_LEFT = 64, 130
CENTER = 200, 400

def main(argv):
    logo_x, logo_y = pyautogui.locateCenterOnScreen('emulator.png')
    pyautogui.moveTo(logo_x,logo_y)
    pyautogui.dragTo(15,15)
    time.sleep(0.1)
    upgrade_hq()
    while (pyautogui.locateCenterOnScreen('Free.png', confidence=0.9) != None):
        print("upgrading building ...")
        time.sleep(10)
    x,y = pyautogui.locateCenterOnScreen('Free.png', confidence=0.9)    
    pyautogui.click(x,y)
    

def upgrade_hq():
    x, y = pyautogui.locateCenterOnScreen('hq.png')
    if (x != None):
        pyautogui.click(x,y)
    time.sleep(1)
    while (pyautogui.locateCenterOnScreen('Go_to.png', confidence=0.9) != None):
        x,y = pyautogui.locateCenterOnScreen('Go_to.png', confidence=0.9)
        pyautogui.click(x,y)
        time.sleep(1)
    x,y = pyautogui.locateCenterOnScreen('Upgrade.png')
    print(x, y)
    if (x != None):
        pyautogui.click(x,y)
    pyautogui.press("A")
    time.sleep(1)
    

if __name__ == "__main__":
    main(sys.argv)