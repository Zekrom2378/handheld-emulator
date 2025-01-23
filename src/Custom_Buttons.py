import tkinter as tk


class Menu_Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=tk.RIDGE,         # Changes Button relief
            bd=3,                     # Removes Border at 0
            highlightthickness=0,     # Removes Highlight at 0
            padx=10,                  # Changes Horizontal Padding
            pady=5,                   # Changes Vertical Padding
            font=("Terminal", 18),       # Sets the Font
            foreground="white",       # Sets the Text Color
            background="#3366cc",     # Sets the background color
        )
        # Bind Events
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        self.config(background="lightblue")  # Change color on hover

    def on_leave(self, event):
        self.config(background="#3366cc")      # Restore original color


class Selection_Button(Menu_Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=tk.SUNKEN,
            bd=4,
            font=("Ubuntu", 16),
            foreground="#99ccff",
            background="#336699",
        )

    def on_hover(self, event):
        self.config(background="#3366ee")

    def on_leave(self, event):
        self.config(background="#336699")
