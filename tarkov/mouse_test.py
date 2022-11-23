import pyautogui as pag
import time
import sys


last_raid = 146000
last_skips = 16
last_raid = 126000
last_skips2 = 15
last_raid = 53000
last_raid = 104000  
last_raid = 51000

def skip_raid():
    time.sleep(2)
    skipC = 0
    while (True):
        pag.press('tab')
        time.sleep(2)
        pag.moveTo(1690, 956)
        pag.click()
        time.sleep(1.5)
        pag.moveTo(844, 810) #old was 857
        pag.click()
        time.sleep(0.5)
        pag.moveTo(951, 860)
        pag.click()
        time.sleep(0.5)
        pag.moveTo(951, 860)
        pag.click()
        time.sleep(12)
        pag.press('esc')
        time.sleep(1)
        pag.moveTo(946, 716)
        pag.click()
        time.sleep(1)
        pag.moveTo(869, 614)
        pag.click()
        time.sleep(14)
        skipC += 1
        print(" raids skiped: ", skipC)
    


def main(argv):
    skip_raid()
    #print_mouse()

def clean_string(str):
    cleaned_string = ""
    for c in str:
        if c.isdigit() or c == ',':
            cleaned_string += c
    return cleaned_string

def print_mouse():
    file = "pos.txt"
    f = open(file, 'a')
    time.sleep(5)
    while(True):
        try:
            print(pag.position())
            f.write(clean_string(str(pag.position()))+' , ')
            time.sleep(1)
        except KeyboardInterrupt:
            print("done")
            f.close()
            sys.exit()

if __name__ == "__main__":
    main(sys.argv)