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
        about_us=Builder.load_file("about_us.kv") 
        faq=Builder.load_file("faq.kv") 
        main=Builder.load_file("main.kv")                       # Set main screen
        help_support=Builder.load_file("help_support.kv")
        pasd=Builder.load_file("password.kv")
        #help_support=Builder.load_file("help_support.kv")
        screen_manager.add_widget(login)                        # Add log in screenwith screenmanager
        screen_manager.add_widget(signin) 
        screen_manager.add_widget(about_us)
        screen_manager.add_widget(main)                         # Add Main screen with screenmanager
        screen_manager.add_widget(help_support)
        screen_manager.add_widget(faq)  
        screen_manager.add_widget(pasd)
        self.theme_cls.theme_style_switch_animation = True      # animation=true
        self.theme_cls.primary_palette ="BlueGray"              # Theme color
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Password",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Settings": self.reset_pasd(),
            },
            
            {
                "viewclass": "OneLineListItem",
                "text":"FAQ",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Settings": self.faq(),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "About Us",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Settings": self.about_us(),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Help & Support",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Settings": self.help_support(),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Log Out",
                "font_style" : 'H6',
                "font_name" : "Comic",
                "height": dp(60),
                "on_release": lambda x="Log Out": self.log_out(),
            }]
        self.menu = MDDropdownMenu(
            items=menu_items,
            width_mult=4,
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
    def about_us(self):
        screen_manager.current="AboutUs"
        self.menu.dismiss()
    def back_to_mainscreen(self):
        screen_manager.current="Main"
    def help_support(self):
        self.menu.dismiss()
        screen_manager.current="Help_Support"
    def faq(self):
        self.menu.dismiss()
        screen_manager.current="FAQ"
    def reset_pasd(self):
        self.menu.dismiss()
        screen_manager.current="Pasd"
if __name__ == "__main__":
    if platform == "win":
        hospitalmanagementsystem().run()


#dataBase.close()