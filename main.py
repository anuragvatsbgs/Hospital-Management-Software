from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
import mysql.connector

from kivy.utils import platform
class hospitalmanagementsystem(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    def build(self):
        login=Builder.load_file("log_in.kv")                    # Set Log in screen
        signin=Builder.load_file("sign_in.kv") 
        main=Builder.load_file("main.kv")                       # Set main screen
        screen_manager.add_widget(login)                        # Add log in screenwith screenmanager
        screen_manager.add_widget(signin) 
        screen_manager.add_widget(main)                         # Add Main screen with screenmanager
        self.theme_cls.theme_style_switch_animation = True      # animation=true
        self.theme_cls.primary_palette ="BlueGray"              # Theme color
        return screen_manager                                   # Return screen manager
    def on_start(self):
        screen_manager.current="LOGIN"
    def log_in(self):
        screen_manager.current="Main"
    def sign_in(self):
        screen_manager.current="SIGNIN"
    def back_to_log_in(self):
        screen_manager.current="LOGIN"
    def log_out(self):
        screen_manager.current="LOGIN"
if __name__ == "__main__":
    if platform == "win":
        hospitalmanagementsystem().run()


#dataBase.close()