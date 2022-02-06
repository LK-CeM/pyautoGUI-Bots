import pyautogui as pag
import time
import sys
import os
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    import Image

import pytesseract

"""
(1272, 1059) move to fleamarket
(950, 1063) move to stash

TO DO:
Autodetect price of item:
    - right click item
    - press 'filter by item'
    - screenshot price area
    - read price from screenshot
    - clean data
    - make offer at .99 of cheapest price
    - return to stash

autodect open offers:
    - go to fleamarket
    - screenshot open offers area
    - read single char
    - if 2 - sleep 5 secs
    - else can_sell_item = True

autosort inventory:
    - check if top left has sellable item
    - if so : return
    - else : 
        - find sellable item
        - put item in top left: #condition top left is empty 
            - check size of item (for ex. 1x2)
            - make space in top left ()
        
"""
def clean_string(str):
    cleaned_string = ""
    for c in str:
        if c.isdigit() or c == ',':
            cleaned_string += c
    return cleaned_string

def setup():
    pag.FAILSAFE = False
    screenWidth, screenHeight = pag.size()
    pag.PAUSE = 0.00005
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    time.sleep(4)
    print('Setup complete')

def can_make_offer():
    im = pag.screenshot(region=(420,45, 12, 20)) #open offers
    string_from_img = pytesseract.image_to_string(im, config=("-c tessedit"
                    "_char_whitelist=0123456789" #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
                    " --psm 10"
                    " -l osd"
                    " ")) #this reads a single char
    print("open offers are: ",string_from_img)
    cleaned_string = ""
    for c in string_from_img:
        if c.isdigit():
            cleaned_string += c             
    if (cleaned_string != "0" and cleaned_string != "3"):
        print("open offers are more then 1, offers found: ", cleaned_string)
        return False
    return True

def read_price_from_img():
    pag.moveTo(0,0) #get mouse out of screenshot
    im = pag.screenshot(region=(1363,159, 82, 30))
    im = ImageOps.grayscale(im)
    string_from_img = pytesseract.image_to_string(im)
    cleaned_string = ""
    for c in string_from_img:
        if c.isdigit():
            cleaned_string += c
    print("string from normal: ", cleaned_string)

    im2 = ImageOps.invert(im)
    string_from_img = pytesseract.image_to_string(im)
    cleaned_string2 = ""
    for c in string_from_img:
        if c.isdigit():
            cleaned_string2 += c
    print("string from invert: ", cleaned_string2)

    if (cleaned_string2 == cleaned_string):
        return cleaned_string
    else:
        return ""

def navigate_stash(row_count = 2):
    """
    requires filter for fleamarket to be set correctly to avoid problems with $ prices --- see ./imgs/filter_condition
    requires that items to be sold are in the top row_counts of the stash
    """
    print('nav stash...')
    item_size = (64,64)
    #row_count = 2 #max can be 11 rn now (without scrolling)
    columns = 10
    items_found = 0
    items_skipped = 0
    #startpoint = (1293,103,1)
    filter_by_item_offset = (1352-1293, 180-123)
    for j in range(row_count):
        for i in range(columns):
            print("i is: ", i, " j is: ", j)
            pag.moveTo(1293,103,0.1)
            time.sleep(0.1)
            pag.move(i*item_size[0],j*item_size[1],0.1)
            time.sleep(0.1)
            pag.click(button='right')
            time.sleep(0.1)
            search_img = pag.locateOnScreen('./imgs/filter_by_item.png',confidence=0.85)
            print("search image is: ",search_img)
            if (search_img):
                filter_pos = pag.center(search_img)
            else:
                print("can't find item-> skiping")
                items_skipped += 1
                continue
            pag.moveTo(filter_pos)
            time.sleep(0.2)
            pag.click()
            time.sleep(0.5)
            wait_counter = 0
            while(not can_make_offer()):
                print("can't make offer... waiting.....")
                wait_counter += 1
                time.sleep(1)
                if (wait_counter == 20):
                    return
            price = read_price_from_img()
            if (not price or int(price) < 5000 or int(price) > 50000):
                print("bad price -> skiping item")
                items_skipped += 1
                move_to_stash()
                continue
            #print("could make offer at marketprice -1: ",int(price)-1)
            make_offer(str(int(price)-11),i*item_size[0],j*item_size[1])
            items_found += 1

            move_to_stash()
    print("items found: ", items_found)
    print("items skipped: ", items_skipped)


def print_mouse():
    file = "pos.txt"
    f = open(file, 'a')
    time.sleep(5)
    while(True):
        try:
            print(pag.position())
            f.write(clean_string(str(pag.position()))+' , ')
            time.sleep(5)
        except KeyboardInterrupt:
            print("done")
            f.close()
            sys.exit()
        
def make_offer(price,x_off, y_off): #makes offer for given price of the top left item in the stash
    posList = [(1278,78), # add offer
                (517, 37), # autoselect
                (41+x_off, 95+y_off), # select item top left
                (1060, 372), # select barter
                (981, 196), # money input field
                (940, 903), # press add
                (849, 744)] # place order
    
    for i in range(len(posList)):
        if (i == 1): # move window
            time.sleep(0.1)
            offer_screen_pos = pag.center(pag.locateOnScreen('./imgs/offerscreen.png',confidence=0.85))
            if (offer_screen_pos[0] != 45):
                print("moving window to top left corner...")
                pag.moveTo(offer_screen_pos)
                pag.dragTo(0, 0, 1, button='left')
                time.sleep(0.1)
                
        if (i == 5):
            pag.write(price, interval=0.01)
        pag.moveTo(posList[i])
        pag.click()
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
    if (len(argv) > 1):
        if (argv[1]== '-ns'):#nav stash
            navigate_stash(int(argv[2]))
            return
        elif (argv[1]== '-pm'):#print mouse
            print_mouse()
    else:
        navigate_stash()


if __name__ == "__main__":
    main(sys.argv)

