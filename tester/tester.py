import time
from root_tools import display, ctrl_button

class Tester():
    def __init__(self, name, pin):
        display.clear()
        self.name = name
        self.pin = pin
        
    def start(self):
       
        display.display_text(f"Connect the {self.name} to PIN GP{self.pin}. Press the button on GP6 to continue", 50, 50)

        time.sleep(0.5)
        while not ctrl_button.value():
            pass
        while ctrl_button.value():
            pass
        display.clear()
        display.display_text("Hold down the button GP6 to move to the next test", 50, 50)
        display.display_text(f"Testing: {self.name}", 60, display.height - 20)
        


    def finish(self):
        display.clear()
        display.display_text(f"{self.name} Test completed", 80, 80)
        time.sleep(1)  # Delay for stability
        display.display_text(f"Pull the button up!", 50, 100)
        while ctrl_button.value():
            pass
        display.clear()
        



