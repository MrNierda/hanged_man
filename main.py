from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random


class Main(App):
    def build(self):
        return MyRoot()


class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        # Get the item with the id 'random_label' as declared inside the .kv file
        # TypeCasting to str required to avoid an error
        self.random_label.text = str(random.randint(0, 2000))


testApp = Main()
testApp.run()
