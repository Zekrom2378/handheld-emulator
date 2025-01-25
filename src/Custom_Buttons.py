import tkinter as tk


class MenuButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=tk.RIDGE,             # Changes Button relief
            bd=3,                        # Removes Border at 0
            highlightthickness=0,        # Removes Highlight at 0
            padx=10,                     # Changes Horizontal Padding
            pady=5,                      # Changes Vertical Padding
            font=("Terminal", 18),       # Sets the Font
            foreground="white",          # Sets the Text Color
            background="#3366cc",        # Sets the background color
            activebackground="#3366cc",  # Sets the background color while it is clicked
            activeforeground="white",    # Sets the text color while it is clicked
        )
        # Bind Events
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.off_focus)
        self.focus = False

    def on_hover(self, event):
        self.config(background="lightblue")  # Change color on hover

    def on_leave(self, event):
        if not self.focus:
            self.config(background="#3366cc")  # Restore original color
        else:
            self.config(background="#3366ee")

    def on_focus(self, event):
        self.focus = True
        self.config(background="#408df0")

    def off_focus(self, event):
        self.focus = False
        self.config(background="#3366cc")


class SelectionButton(MenuButton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=tk.SUNKEN,
            bd=4,
            font=("Ubuntu", 14),
            foreground="#99ccff",
            background="#336699",
        )
        self.bind("<FocusIn>", self.on_focus)
        self.bind("<FocusOut>", self.off_focus)
        self.focus = False

    def on_hover(self, event):
        self.config(background="#359aee")

    def on_focus(self, event):
        self.focus = True
        self.config(background="#3366ee")

    def off_focus(self, event):
        self.focus = False
        self.config(background="#336699")

    def on_leave(self, event):
        if not self.focus:
            self.config(background="#336699")
        else:
            self.config(background="#3366ee")
