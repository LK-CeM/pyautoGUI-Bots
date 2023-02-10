import pyautogui as pag
import time
import sys
import keyboard
import win32gui, win32ui, win32con, win32api

#run game in borderless

def main(argv):
    while(True):
        if (keyboard.is_pressed('p') and keyboard.is_pressed('alt')):
            playback("junkbox_top_left.txt") #playback filling junkbox that is in the top left corner of the screen
        elif (keyboard.is_pressed('r') and keyboard.is_pressed('alt')):
            record_mouse() # print mouseposition and safe 2 file when pressing 'a'
        elif (keyboard.is_pressed('f')):
            exit() 
        elif (keyboard.is_pressed('e') and keyboard.is_pressed('alt')):
            repair() #macro repair
        elif (keyboard.is_pressed('s') and keyboard.is_pressed('alt')):
            set_price()
        elif (keyboard.is_pressed('d') and keyboard.is_pressed('alt')):
            quick_sell()
        elif (keyboard.is_pressed('v') and keyboard.is_pressed('alt')):
            snipe()

def snipe(): #1777 180
    while(True):
        noffer = pag.locateOnScreen('./imgs/no_offer.png', confidence=0.8, grayscale=True)
        if (not noffer):
            pag.click(1777 , 180)
            pag.press("y")
            pag.moveTo(111, 111)
            pag.press("f5")
            continue
        time.sleep(1)
        pag.press("f5")

def set_price(): #sale window top left corner
    org_pos = pag.position()
    pag.click(button='right')
    filter = None
    while (filter == None):
        pag.screenshot('num1_.png')
        filter = pag.locateOnScreen('./imgs/filter_by_item.png', confidence=0.9)
    print(filter)
    pag.moveTo(filter)
    
    pag.click()
    if (pag.locateOnScreen('./imgs/autoselect_off.png', confidence=0.95, grayscale=True)):
        pag.click(485, 45) #select all
        time.sleep(1)
    pag.click(org_pos) #item
    time.sleep(0.6)
    pag.click(1052, 372)
    pag.click(996, 199)

def quick_sell(): #sale window top left corner
    pag.click(971, 897)
    pag.click(892, 747)
    time.sleep(0.5)
    pag.click(1228, 78)
    pag.moveTo(302, 405)
    time.sleep(1)
    pos = pag.locateOnScreen('./imgs/found_in_raid.png', confidence=0.8, grayscale=True)
    pag.moveTo(pos)
    if (pos):
        set_price()

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
    time.sleep(0.01)
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