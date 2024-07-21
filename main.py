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
    display.display_text("Press button Bluetooth(GP5)", 40, 106)
    while not ctrl_button.value():
        pass

menu_options = ["All tests"] + [tester.name for tester in test_list]

def select_cell(cnt):
    display.text_box(menu_options[cnt], 20 + (cnt % 4) * 70, (cnt // 4) * 60, text_color= color565(20, 20, 0), color= color565(80, 80, 0))
# (b, g, r)
def deselect_cell(cnt):
    display.text_box(menu_options[cnt], 20 + (cnt % 4) * 70, (cnt // 4) * 60)



def menu():
    global test_list
    display.clear()
    for i in range(4):
        for j in range(4):
            display.text_box(menu_options[i * 4 + j], 20 + j * 70, i * 60)
    
    selected_cell = 0
    select_cell(selected_cell)

    while True:
        if ctrl_button.value():
            hold_time_elapsed = ticks_ms()
            while ctrl_button.value():
                if ticks_ms() - hold_time_elapsed > hold_duration:
                    print("Selected test: ", menu_options[selected_cell])
                    if selected_cell != 0:
                        test_list = [test_list[selected_cell - 1]]
                        return
                    else:
                        test_ind = selected_cell - 1
                        return [test_list[test_ind]]
            selected_cell = (selected_cell + 1) % 16
            select_cell(selected_cell)
            deselect_cell((selected_cell - 1) % 16)
      
def main():
    global test_ind
    
    init()

    hold_time_elapsed = ticks_ms()

    menu()

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