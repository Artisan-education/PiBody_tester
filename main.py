from machine import Pin, SPI
from utime import sleep_ms, ticks_ms

from root_tools import display, ctrl_button, color565
from all_testers import test_list

test_ind = 0
hold_duration = 750


def start_test(ind):
    if test_ind != 0:
        test_list[test_ind - 1].finish()
    display.clear()
    current_test = test_list[ind]
    return current_test.start()


def draw_loading_bar(value):
    display.fill_rectangle(40, 60, int(value * 240), 10, color565(128, 255, 0))

def init_loading_bar():
    display.fill_rectangle(40, 60, 240, 10, color565(64, 64, 64))

def init():
    display.clear()
    display.display_text("Connect button to D1(GP6)", 40, 106)
    display.display_text("And press it", 40, 126)
    while not ctrl_button.value():
        pass

def main():
    global test_ind
    
    init()
        
    hold_time_elapsed = ticks_ms()
    test_count = len(test_list)

    while not start_test(test_ind):
        test_ind = (test_ind + 1) % len(test_list)

    init_loading_bar()
    while True:
        if ctrl_button.value():
            if ticks_ms() - hold_time_elapsed > hold_duration:
                test_ind += 1
                if test_ind == test_count :
                    display.clear()
                    display.display_text("All tests passed!", 0, 116)
                    return
                                      
                while not start_test(test_ind):
                    test_ind = (test_ind + 1) % len(test_list)
                
                hold_time_elapsed = ticks_ms()
                print("Ticked")
            else:
                draw_loading_bar((ticks_ms() - hold_time_elapsed) / hold_duration)
        else:
            hold_time_elapsed = ticks_ms()
            init_loading_bar()
            test_list[test_ind].test()



main()