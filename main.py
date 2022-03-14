from dataclasses import dataclass
from time import sleep
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from hangedMan.hanged_man import HangedManGame


class Main(App):
    def build(self):
        return MyRoot()


@dataclass
class MyRoot(BoxLayout):
    hanged_man_game = HangedManGame()
    widgets: dict = None

    def __init__(self):
        super(MyRoot, self).__init__()
        self.widgets = {}
        self.hidden_word.text = "First give your name"

    def ask_user_name(self):
        print("ask user name")
        self.hidden_word.text = "Write your name below"
        print(f"{self.guess_inpt.text}")
        player_name = str(self.user_input()).capitalize()
        print(f"{self.guess_inpt.text}")
        self.hanged_man_game.player = player_name
        
    def start_game(self):
        self.hidden_word.text = self.hanged_man_game.word_hidden
        self.show_widget("guessInput")
        self.show_widget("guessSubmit")

    def get_user_name(self, user_name):
        self.hide_widget(user_name)
        self.hanged_man_game.player = user_name.text
        self.start_game()

    def hide_widget(self, widget):
        widget_attributes = {
            "opacity": widget.opacity,
            "disabled": widget.disabled,
            "height": widget.height,
            "size_hint_y": widget.size_hint_y
        }
        self.widgets[widget.name] = widget_attributes

        widget.opacity = 0
        widget.disabled = True
        widget.height = 0
        widget.size_hint_y = None

    def show_widget(self, widget_name): 
        print(f"widget in layout {self.ids.layout.names}")
        return


testApp = Main()
testApp.run()
