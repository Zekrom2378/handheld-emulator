import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import Custom_Buttons as cb


ROMS = {"NES":  {"Title": [], "File": []},
        "SNES": {"Title": [], "File": []},
        "GB":   {"Title": [], "File": []},
        "GBC":  {"Title": [], "File": []},
        "GBA":  {"Title": [], "File": []},
        "NDS":  {"Title": [], "File": []}}

ROOT_PATH = r"C:\Users\tanne\OneDrive\Desktop\School2024\Python Stuff\EmulatorController"
# ROOT_PATH = r"/home/zekrom2378/"

GAME_COUNT = 0
BOOK = [[]]
PAGE = 0

def title_grabber(title):
    if len(title.split('.')) > 2:
        temp = title.split('.')
        temp = temp[:-1]
        title = ''.join(temp)
    else:
        title = title.split('.')[0]

    if '(' in title:
        temp = title.split('(')
        title = temp[0]

    if '[' in title:
        temp = title.split('[')
        title = temp[0]

    if ' - ' in title:
        temp = title.split(' - ')
        if temp[0].isnumeric():
            title = temp[1:]
            title = ''.join(title)
        elif temp[0].isalpha():
            title = ' '.join(temp)

    title = title.strip()
    return title


for key in ROMS:
    files = os.listdir(ROOT_PATH + '\\' + key.lower())
    # files = os.listdir(ROOT_PATH + '/' + key.lower())
    for file in files:
        ROMS[key]["File"].append(file)
        GAME_COUNT += 1
        ROMS[key]["Title"].append(title_grabber(file))

        if len(BOOK[len(BOOK) - 1]) >= 8:
            BOOK.append([])
        BOOK[len(BOOK) - 1].append(title_grabber(file))


# TODO : Create a function that does need parameters to launch a game specified by the text on the selection button that
#   is pressed ROM[EMULATOR][TITLE] and ROM[EMULATOR][FILE] should have all info needed
def play_game():

    pass


def selection_button(frm, title, row_num):
    selection = cb.Selection_Button(frm, text=title, command=root.destroy, anchor="w")
    selection.grid(row=row_num, column=1, columnspan=2, sticky="ew")


def next_page():
    global PAGE
    PAGE += 1
    if PAGE >= len(BOOK):
        PAGE = 0
    display_page(PAGE)


def last_page():
    global PAGE
    PAGE -= 1
    if abs(PAGE) >= len(BOOK):
        PAGE = 0
    display_page(PAGE)


def display_page(page_num):
    frm = tk.Frame(root, bg="#515b79")
    frm.grid(row=0, column=0, sticky="nsew")

    frm.columnconfigure(1, weight=1)
    frm.columnconfigure(2, weight=1)
    frm.rowconfigure(9, weight=1)
    frm.rowconfigure(10, weight=0)

    header = tk.Label(frm, text="       Select A Game", font=("System", 16), foreground="black", anchor="w", border=5)
    header.grid(row=0, column=0, columnspan=3, sticky="new")

    for num in range(10):
        tk.Label(frm, text='_', foreground="#515b79", bg="#515b79", border=0, anchor="e").grid(row=num, column=0, sticky="nws")
        tk.Label(frm, text='_', foreground="#515b79", bg="#515b79", border=0, anchor="e").grid(row=num, column=3, sticky="nes")

    # footer = tk.Label(frm, text="", pady=2)
    # footer.grid(row=10, column=0, columnspan=4, sticky="ews")

    c = 1
    for game in BOOK[page_num]:
        selection_button(frm, game, c)
        c += 1

    forward_button = cb.Menu_Button(frm, text=">", command=next_page)
    forward_button.grid(row=9, column=2, sticky="sw", pady=3)

    back_button = cb.Menu_Button(frm, text="<", command=last_page)
    back_button.grid(row=9, column=1, sticky="se", pady=3)



# def selection_button(text, game, row):
#     selection = cb.Selection_Button(frm, text=text, command=game, anchor="w")
#     selection.grid(row=row, column=0, columnspan=2, sticky="ew")
#     return selection

root = Tk()
root.geometry("800x480")
# root.attributes('-fullscreen', True)   # Disable while testing, Enable while on actual 800x480 screen.
root.configure(bg="#515b79")


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# selection1 = selection_button("First Item", root.destroy, 1)
# selection2 = selection_button("Second Item", root.destroy, 2)
# selection3 = selection_button("Third Item", root.destroy, 3)
# selection4 = selection_button("Fourth Item", root.destroy, 4)
# selection5 = selection_button("Fifth Item", root.destroy, 5)
# selection6 = selection_button("Sixth Item", root.destroy, 6)
# selection7 = selection_button("Seventh Item", root.destroy, 7)
# selection8 = selection_button("Eighth Item", root.destroy, 8)

PAGE_COUNT = GAME_COUNT // 8
if GAME_COUNT % 8 > 0:
    PAGE_COUNT += 1
# i = 0
# j = 0
# for key in ROMS:
#     if i % 8 == 0 and i != 0:
#         j += 1
#
#
#
# for i in range(PAGE_COUNT):
#     for j in range(GAME_COUNT):
#         selection_button(ROMS, j+(1-(8*i)))

display_page(PAGE)




if __name__ == '__main__':
    root.mainloop()



