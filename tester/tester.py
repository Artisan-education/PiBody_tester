import time
from root_tools import display, ctrl_button

class Tester():
    def __init__(self, name, pin):
        display.clear()
        self.name = name
        self.pin = pin
        
    def start(self):
       
        slot_names = {
            "0" : "I2C0",
            "2" : "I2C1",
            "6" : "D1 (GP6)",
            "7" : "D2 (GP7)",
            "8" : "D3 (GP8)",
            "9" : "D4 (GP9)",
            "26" : "UNIPORT",
            "28" : "Analog (GP28)"
        }

        slot_name = ""
        if type(self.pin) == list:
            slot_name = slot_names[str(self.pin[0])]
        else:
            slot_name = slot_names[str(self.pin)]

        display.display_text(f"Connect the {self.name} to {slot_name}. Press the button on GP6 to continue", 50, 50)

        time.sleep(0.5)
        while not ctrl_button.value():
            pass
        while ctrl_button.value():
            pass
        display.clear()
        display.display_text("Hold down the button GP6 to move to the next test", 50, 20)
        display.display_text(f"Testing: {self.name}", 60, display.height - 20)
        


    def finish(self):
        display.clear()
        display.display_text(f"{self.name} Test completed", 80, 80)
        time.sleep(1)  # Delay for stability
        display.display_text(f"Pull the button up!", 50, 100)
        while ctrl_button.value():
            pass
        display.clear()
        



