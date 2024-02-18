from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
import mysql.connector
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivy.utils import platform
from kivymd.uix.menu import MDDropdownMenu
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
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Password",
                "font_style" : 'Body1',
                "height": dp(45),
                "on_release": lambda x="Settings": self.reset_pasd(),
            },
            
            {
                "viewclass": "OneLineListItem",
                "text":"FAQ",
                "font_style" : 'Body1',
                "height": dp(45),
                "on_release": lambda x="Settings": self.faq(),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "About Us",
                "font_style" : 'Body1',
                "height": dp(45),
                "on_release": lambda x="Settings": self.about_us(),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Help & Support",
                "font_style" : 'Body1',
                "height": dp(45),
                "on_release": lambda x="Settings": self.help_support(),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Log Out",
                "font_style" : 'Body1',
                "height": dp(45),
                "on_release": lambda x="Log Out": self.log_out(),
            }]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=3,
        )

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
        self.menu.dismiss()
    def dot(self, button):
        self.menu.caller = button
        self.menu.open()
if __name__ == "__main__":
    if platform == "win":
        hospitalmanagementsystem().run()


#dataBase.close()