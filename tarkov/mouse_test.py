import pyautogui as pag
import time
import sys
import keyboard
import win32gui, win32ui, win32con, win32api



def main(argv):
    while(True):
        if (keyboard.is_pressed('p')):
            playback("junkbox_top_left.txt")
        if (keyboard.is_pressed('r')):
            record_mouse()
        if (keyboard.is_pressed('e')):
            exit()

def playback(file):
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



def record_mouse():
    file = "pos.txt"
    f = open(file, 'a')
    while(True):
        if (keyboard.is_pressed('a')):
            print(pag.position())
            f.write(str(pag.position()[0])+" "+ str(pag.position()[1])+" ")
            time.sleep(0.2)

if __name__ == "__main__":
    main(sys.argv)