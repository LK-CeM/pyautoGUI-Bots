import pyautogui
import keyboard
import pyscreenshot

class RegionSelector:
    def __init__(self):
        # Variables to store the coordinates
        self.x1, self.y1 = None, None
        self.x2, self.y2 = None, None
        self.is_first_click = True

    def run(self):
        print("Press 'A' to select the first point...")

        keyboard.on_press_key("a", self.on_key_press)

        while True:
            pass

    def on_key_press(self, event):
        if event.name == "a" and self.is_first_click:
            self.x1, self.y1 = pyautogui.position()
            self.is_first_click = False
            print("First point selected. Press 'A' to select the second point...")
        elif event.name == "a" and not self.is_first_click:
            self.x2, self.y2 = pyautogui.position()
            self.print_region()
            keyboard.unhook_all()
            return False

    def print_region(self):
        x1, x2 = min(self.x1, self.x2), max(self.x1, self.x2)
        y1, y2 = min(self.y1, self.y2), max(self.y1, self.y2)
        print(f"Region coordinates: \nx1={x1}\ny1={y1}\nx2={x2}\ny2={y2}\n")
        exit()

if __name__ == "__main__":
    region_selector = RegionSelector()
    region_selector.run()
