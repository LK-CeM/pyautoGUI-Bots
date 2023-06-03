import time
import pyautogui as p


monitor_one = False
pos1 = (158, 155)
pos2 = (265, 173)
if monitor_one == False:
    pos1 =(2084, 175)
    pos2 =(2171, 193)
while True:
    current = p.position()
    time.sleep(0.2)
    p.moveTo(pos1)
    time.sleep(0.2)
    p.rightClick()
    time.sleep(0.2)
    p.moveTo(pos2)
    time.sleep(0.2)
    p.click()
    time.sleep(0.1)
    p.moveTo(current)
    time.sleep(10)