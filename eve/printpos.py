import pyautogui
import keyboard

def on_key_press(event):
    if event.name == 'a':
        x, y = pyautogui.position()
        print(f"Mouse position: {x} {y}")

keyboard.on_press(on_key_press)
keyboard.wait('esc')  # Keeps the script running until the 'esc' key is pressed
