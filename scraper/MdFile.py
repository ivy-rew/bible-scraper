class MdFile():

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            return file.readlines()

    def write(self, lines):
        with open(self.path, 'w', encoding='utf-8') as file:
            file.writelines(lines)