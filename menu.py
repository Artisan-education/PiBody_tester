from root_tools import display, ctrl_button, color565
from all_testers import test_list
from time import sleep_ms
menu_options = ["All tests"] + [tester.name for tester in test_list]

display.clear()
for i in range(4):
    for j in range(4):
        display.text_box(menu_options[i * 4 + j], 20 + j * 70, i * 60)

def select_cell(cnt):
    display.text_box(menu_options[cnt], 20 + (cnt % 4) * 70, (cnt // 4) * 60, text_color= color565(20, 20, 0), color= color565(80, 80, 0))
# (b, g, r)
def deselect_cell(cnt):
    display.text_box(menu_options[cnt], 20 + (cnt % 4) * 70, (cnt // 4) * 60)

# select_cell(0)

for i in range(16):
    select_cell(i)
    deselect_cell((i - 1) % 16)
    sleep_ms(500)
