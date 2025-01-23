import os

class GBA:
    def __init__(self, name, file):
        self.name = name
        self.file = file

    def location(self, root):
        return root + '/gba/' + self.file

    def launch(self, root, gba_emulator_path):
        os.system(f'{gba_emulator_path} {self.location(root)}')
