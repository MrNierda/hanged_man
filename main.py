from dataclasses import dataclass
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
from hangedMan import hanged_man
from hangedMan.hanged_man import HangedManGame


class Main(App):
    def build(self):
        return MyRoot()


@dataclass
class MyRoot(BoxLayout):
    hanged_man_game = HangedManGame()

    def __init__(self):
        super(MyRoot, self).__init__()

    def ask_user_name(self):
        print("ask user name")
        self.hidden_word.text = "Write your name below"
        print(f"{self.guess_inpt.text}")
        player_name = str(self.user_input()).capitalize()
        print(f"{self.guess_inpt.text}")
        self.hanged_man_game.player = player_name
        self.hidden_word_text = f"Hello {player_name}, let's start"
        

    def start_game(self):
        # Get the item with the id 'random_label' as declared inside the .kv file
        # TypeCasting to str required to avoid an error
        self.hidden_word.text = self.hanged_man_game.word_hidden

    def user_input(self, v_input):
        print(f"submit input: {v_input.text}")
        return v_input.text


testApp = Main()
testApp.run()
