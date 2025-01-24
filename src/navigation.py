# TODO: Need to configure the keyboard and entire UI system navigation.  There will be more than just the pages
#   of games in the UI.
from main import BUTTONS, PAGE_NUMBER


def focus_next(left, right):
    global BUTTONS
    global PAGE_NUMBER
    if PAGE_NUMBER == 7:
        if right.focus_get() == '.!frame.!menubutton':
            if left.focus_get() == '.!frame.!menubutton2':
                BUTTONS[PAGE_NUMBER].focus_set()
            else:
                left.focus_set()
        else:
            right.focus_set()
    else:
        PAGE_NUMBER += 1
        BUTTONS[PAGE_NUMBER].focus_set()


def focus_previous(left, right):
    global BUTTONS
    global PAGE_NUMBER
    if PAGE_NUMBER == 0:
        if left.focus_get() == '.!frame.!menubutton2':
            if right.focus_get() == '.!frame.!menubutton':
                PAGE_NUMBER = 7
                BUTTONS[PAGE_NUMBER].focus_set()
            else:
                PAGE_NUMBER = 0
                right.focus_set()
        else:
            right.focus_set()
    else:
        PAGE_NUMBER -= 1
        BUTTONS[PAGE_NUMBER].focus_set()


def select_direction_button(button, num):
    global PAGE_NUMBER
    PAGE_NUMBER = num
    button.focus_set()

