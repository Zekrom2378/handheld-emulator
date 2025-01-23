import os

class Game:
    def __init__(self, name, file, type):
        self.name = name
        self.file = file
        self.type = type

    def location(self, root):
        return root + '/' + self.type + '/' + self.file

    def launch(self, root, emulator_path):
        os.system(f'{emulator_path} {self.location(root)}')
