import tkinter as tk
from main import THEMES, theme_reader


class MenuButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.config(
            relief=tk.RIDGE,             # Changes Button relief
            bd=3,                        # Removes Border at 0
            highlightthickness=0,        # Removes Highlight at 0
            padx=10,                     # Changes Horizontal Padding
            pady=5,                      # Changes Vertical Padding
            font=("Tekton Pro Ext", 18),       # Sets the Font
            foreground=THEMES[theme_reader()][5],          # Sets the Text Color
            background=THEMES[theme_reader()][6],        # Sets the background color
            activebackground=THEMES[theme_reader()][6],  # Sets the background color while it is clicked
            activeforeground=THEMES[theme_reader()][5]   # Sets the text color while it is clicked
        )
        # Bind Events
        # self.bind("<Leave>", self.on_leave)
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.off_focus)
        self.focus = False

    def on_focus(self, event):
        self.focus = True
        self.config(background=THEMES[theme_reader()][7])

    def off_focus(self, event):
        self.focus = False
        self.config(background=THEMES[theme_reader()][6])

    # def on_leave(self, event):
    #     if not self.focus:
    #         self.config(background=THEMES[THEME_NUMBER][6])  # Restore original color
    #     else:
    #         self.config(background=THEMES[THEME_NUMBER][7])


class SelectionButton(MenuButton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=tk.SUNKEN,
            bd=4,
            font=("Ubuntu", 14),
            foreground=THEMES[theme_reader()][2],
            background=THEMES[theme_reader()][3],
            activeforeground=THEMES[theme_reader()][2],
            activebackground=THEMES[theme_reader()][3]
        )

    def on_focus(self, event):
        self.focus = True
        self.config(background=THEMES[theme_reader()][4])

    def off_focus(self, event):
        self.focus = False
        self.config(background=THEMES[theme_reader()][3])

    # def on_leave(self, event):
    #     if not self.focus:
    #         self.config(background=THEMES[THEME_NUMBER][4])
    #     else:
    #         self.config(background=THEMES[THEME_NUMBER][3])
