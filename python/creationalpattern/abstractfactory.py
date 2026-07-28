class Button:

    def render(self):
        pass


class Checkbox:

    def render(self):
        pass
class WindowsButton(Button):

    def render(self):
        print("Windows Button")


class WindowsCheckbox(Checkbox):

    def render(self):
        print("Windows Checkbox")
class MacButton(Button):

    def render(self):
        print("Mac Button")


class MacCheckbox(Checkbox):

    def render(self):
        print("Mac Checkbox")

from abc import ABC, abstractmethod

class UIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass
class WindowsFactory(UIFactory):

    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(UIFactory):

    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()
    
factory = WindowsFactory()

button = factory.create_button()
checkbox = factory.create_checkbox()

button.render()
checkbox.render()