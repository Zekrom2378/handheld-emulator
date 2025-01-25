import os

class Game:
    def __init__(self, name, file, type):
        self.name = name
        self.file = file
        self.type = type

    def location(self, root):
        return root + '/' + self.type + '/' + self.file

    def colorized(self):
        if self.type == "nes":
            self.color = "gray"
            return self.color
        if self.type == "snes":
            self.color = "red"
            return self.color
        if self.type == "gb":
            self.color = "blue"
            return self.color
        if self.type == "gbc":
            self.color = "yellow"
            return self.color
        if self.type == "gba":
            self.color = "purple"
            return self.color
        if self.type == "nds":
            self.color = "white"
            return self.color

    def launch(self, root, emulator_path):
        os.system(f'{emulator_path} {self.location(root)}')
