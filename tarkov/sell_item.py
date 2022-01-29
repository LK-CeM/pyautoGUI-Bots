import pyautogui as pag
import time
import sys
import os
import sys

"""
recording of actions
Point(1278, 78) === add offer
-- mising autoselect
Point(597, 213) === select item top left
Point(1629, 496) === select barter
Point(979, 196) === money input field

-- type price
Point(957, 898) === press add
Point(1446, 863) === place order
"""

def setup():
    pag.FAILSAFE = True
    screenWidth, screenHeight = pag.size()
    pag.PAUSE = 0.00005
    time.sleep(10)
    print('Setup complete')

def print_mouse():
    file = "pos.txt"
    f = open(file, 'a')
    while(True):
        try:
            print(pag.position())
            f.write(str(pag.position()) + '\n')
            time.sleep(10)
        except KeyboardInterrupt:
            print("done")
            f.close()
            sys.exit()
        
def make_offer(price):
    posList = [(1278,78),(597, 213),(1629, 496),(979, 196),(957, 898),(1446, 863)]
    for i in range(len(posList)):
        if (i == 4):
            pag.write(price, interval=0.1)
            time.sleep(0.1)
        pag.click(posList[i])
        print(pag.position())
        time.sleep(2)
        


def main(argv):
    setup()
    pause = False
    if (argv[1]== '-pm'):#print mouse
        print_mouse()
    else:
        make_offer(argv[1])


if __name__ == "__main__":
    main(sys.argv)

