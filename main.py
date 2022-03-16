from dataclasses import dataclass
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from hangedMan.hanged_man import HangedManGame


class Main(App):
    def build(self):
        return MyRoot()


@dataclass
class MyRoot(BoxLayout):
    hanged_man_game = None
    player_name = None
    widgets: dict = None
    default_button_style: dict = None
    default_input_style: dict = None

    def __init__(self):
        super(MyRoot, self).__init__()
        self.widgets = {}
        self.hidden_word.text = "First give your name"
        self.default_button_style = self.default_input_style = {
            "opacity": 1.0,
            "disabled": False,
            "height": 150.0,
            "size_hint_y": 1
        }
        
    def start_game(self):
        self.hanged_man_game = HangedManGame()
        self.hanged_man_game.player = self.player_name
        self.hidden_word.text = self.hanged_man_game.word_hidden
        self.show_widget(self.guess_submit)
        self.show_widget(self.guess_input)
        self.show_widget(self.log_label_id)
        self.hide_widget(self.new_game)
        self.guess_input.text = ""
        self.log_label_id.text = f"You have {self.hanged_man_game.round_to_play} chances"

    def get_user_name(self, user_name, button_submit):
        if str(user_name.text) == "":
            return
        self.hide_widget(user_name)
        self.hide_widget(button_submit)
        self.player_name = str(user_name.text).capitalize()
        self.start_game()

    def manage_guess(self, guess):
        guess = str(guess.text)
        log_text = ""
        if len(guess) == 1:
            result = self.hanged_man_game.manage_letter(guess)
            match result:
                case None:
                    log_text = "Put a correct letter."
                case True:
                    log_text = "Correct letter !"
                case False:
                    log_text = "Incorrect letter !"

        elif len(guess) > 1:
            result = self.hanged_man_game.guess_word(guess)
            if result:
                self.log_label_id.text = f"Congratulations ! You found the correct word !"
                self.hidden_word.text = self.hanged_man_game.word_to_guess
                self.hide_widget(self.guess_submit)
                self.hide_widget(self.guess_input)
                self.show_widget(self.new_game)
                return
            else:
                log_text = "You didn't find the word... try again, or put a letter."
        
        if self.hanged_man_game.round_to_play > 0:
            self.log_label_id.text = f"{log_text} You have {self.hanged_man_game.round_to_play} chances. \n You have proposed {self.hanged_man_game.letters_played}"
            self.guess_input.text = ""
            self.guess_input.focus = True
            self.hidden_word.text = self.hanged_man_game.word_hidden
        else:
            self.log_label_id.text = f"No more chances..."
            self.hidden_word.text = self.hanged_man_game.word_to_guess
            self.hide_widget(self.guess_submit)
            self.hide_widget(self.guess_input)
            self.show_widget(self.new_game)

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

    def show_widget(self, widget): 
        if isinstance(widget, TextInput):    
            widget.opacity = self.default_input_style['opacity']
            widget.disabled = self.default_input_style['disabled']
            widget.height = self.default_input_style['height']
            widget.size_hint_y = self.default_input_style['size_hint_y']
            return
        
        if isinstance(widget, Button) or isinstance(widget, Label):    
            widget.opacity = self.default_button_style['opacity']
            widget.disabled = self.default_button_style['disabled']
            widget.height = self.default_button_style['height']
            widget.size_hint_y = self.default_button_style['size_hint_y']
            return



testApp = Main()
testApp.run()
