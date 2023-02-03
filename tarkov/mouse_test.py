import pyautogui as pag
import time
import sys
import keyboard
import win32gui, win32ui, win32con, win32api



def main(argv):
    while(True):
        if (keyboard.is_pressed('p')and keyboard.is_pressed('alt')):
            playback("junkbox_top_left.txt")
        if (keyboard.is_pressed('r') and keyboard.is_pressed('alt')):
            record_mouse()
        elif (keyboard.is_pressed('f')):
            exit()
        elif (keyboard.is_pressed('e')):
            repair()

def change_pos(x, y):
    pos = list(pag.position())
    pos[0] += x
    pos[1] += y
    pos = tuple(pos)
    return pos

def repair(): #1432 101, 1481 230, 981 906 
    print("starting repair...")
    org_pos = pag.position()
    pag.click(button='right')
    pag.moveTo(pag.locateOnScreen('./imgs/repair.png', confidence=0.8))
    pag.click()
    pag.moveTo((981,  906))
    pag.click()
    time.sleep(0.15)
    pag.press("esc")
    pag.moveTo(org_pos)

def playback(file):
    print("starting playback...")
    f = open(file, "r")
    lines = f.readlines()
    test = [[int(j) for j in x.split()] for x in lines]
    test = test[0]
    home = [test[0],test[1]]
    pag.moveTo(test[0],test[1])
    for i in range(2,len(test),2):
        pag.moveTo(test[i], test[i+1])
        pag.mouseDown()
        pag.moveTo(home[0], home[1])
        pag.mouseUp()




def record_mouse(): #press a to record pos
    print("start recording...")
    file = "pos.txt"
    f = open(file, 'a')
    while(True):
        if (keyboard.is_pressed('a')):
            print(pag.position())
            f.write(str(pag.position()[0])+" "+ str(pag.position()[1])+" ")
            time.sleep(0.2)

if __name__ == "__main__":
    main(sys.argv)