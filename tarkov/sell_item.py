import pyautogui as pag
import time
import sys
import os
import sys

"""
(1272, 1059) move to fleamarket
(950, 1063) move to stash
"""

def setup():
    pag.FAILSAFE = False
    screenWidth, screenHeight = pag.size()
    pag.PAUSE = 0.00005
    time.sleep(0.1)
    print('Setup complete')

def print_mouse():
    file = "pos.txt"
    f = open(file, 'a')
    while(True):
        try:
            print(pag.position())
            f.write(str(pag.position())+',')
            time.sleep(5)
        except KeyboardInterrupt:
            print("done")
            f.close()
            sys.exit()
        
def make_offer(price): #makes offer for given price of the top left item in the stash
    posList = [(1278,78), # add offer
                (517, 37), # autoselect
                (41, 95), # select item top left
                (1060, 372), # select barter
                (981, 196), # money input field
                (940, 903), # press add
                (849, 744)] # place order
    
    for i in range(len(posList)):
        if (i == 1): # move window
            offer_screen_pos = pag.center(pag.locateOnScreen('./imgs/offerscreen.png',confidence=0.9))
            pag.moveTo(offer_screen_pos)
            pag.dragTo(0, 0, 0.1, button='left')
            time.sleep(0.1)
        if (i == 5):
            pag.write(price, interval=0.01)
        pag.moveTo(posList[i])
        pag.click()
        print(pag.position())
        time.sleep(0.1)
        
def move_to_fleamarket():
    pag.click(1272, 1059)
    time.sleep(0.1)

def move_to_stash():
    pag.click(950, 1063)
    time.sleep(0.1)

def main(argv):
    setup()
    pause = False
    if (argv[1]== '-pm'):#print mouse
        print_mouse()
    else:
        move_to_stash()
        move_to_fleamarket()
        make_offer(argv[1])
        move_to_stash()


if __name__ == "__main__":
    main(sys.argv)

