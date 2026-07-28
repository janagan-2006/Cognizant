#not more important
# but it is link with obsever behavirol pattern
class File:

    def show(self):
        pass

class TextFile(File):

    def show(self):
        print("Text File")      

class Folder(File):

    def __init__(self):

        self.items = []

    def add(self, item):

        self.items.append(item)

    def show(self):

        print("Folder")

        for item in self.items:
            item.show()

folder = Folder()

folder.add(TextFile())

folder.add(TextFile())

folder.show()