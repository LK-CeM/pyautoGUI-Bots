import winput
from winput.vk_codes import *
import time
import threading

left_button_pressed = False
right_button_pressed = False
recoil = 1
counter = 0
def move_mouse_while_both_pressed():
    global left_button_pressed, right_button_pressed, recoil, counter
    counter += 1
    print("i got called: ", counter)
    while True:
        if left_button_pressed and right_button_pressed:
            x, y = winput.get_mouse_pos()
            winput.set_mouse_pos(x, y - recoil)
            time.sleep(0.01)
        else:
            time.sleep(0.01)

def mouse_callback( event ):
    global left_button_pressed, right_button_pressed

    if event.action == winput.WM_LBUTTONDOWN:
        left_button_pressed = True
    elif event.action == winput.WM_LBUTTONUP:
        left_button_pressed = False
    elif event.action == winput.WM_RBUTTONDOWN:
        right_button_pressed = True
    elif event.action == winput.WM_RBUTTONUP:
        right_button_pressed = False

def keyboard_callback( event ):
    global recoil
    if event.vkCode == winput.VK_ESCAPE: # quit on pressing escape
        return winput.WP_STOP
        # alternatively you could also call:
        # winput.stop()
    if event.vkCode == winput.VK_NUMPAD0:
        print("lower recoil controll if any")
        if recoil >= 2:
            recoil -= 1
    if event.vkCode == winput.VK_NUMPAD1:
        print("higher recoil controll")
        recoil += 1


print("Press escape to quit")

# Start a separate thread to handle the mouse movement logic
mouse_movement_thread = threading.Thread(target=move_mouse_while_both_pressed)
mouse_movement_thread.daemon = True
mouse_movement_thread.start()

# hook input
winput.hook_mouse( mouse_callback )
winput.hook_keyboard( keyboard_callback )

# enter message loop
winput.wait_messages()
print("i got called ")

# remove input hook
winput.unhook_mouse()
winput.unhook_keyboard()
