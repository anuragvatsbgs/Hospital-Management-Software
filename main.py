from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
import mysql.connector
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import ImageLeftWidget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import ThreeLineAvatarListItem
from kivy.utils import platform
import plyer
from kivymd.uix.list import TwoLineListItem
class Room_Rent_Khata(MDApp):
    global screen_manager
    screen_manager = ScreenManager()
    def build(self):
        login=Builder.load_file("log_in.kv")                    # Set Log in screen
        screen_manager.add_widget(login)                        # Add with screenmanager
        self.theme_cls.theme_style_switch_animation = True      # animation=true
        self.theme_cls.primary_palette ="BlueGray"              # Theme color ""
    def on_start(self):
        screen_manager.current="LOGIN"

if __name__ == "__main__":
    if platform == "win":
        Room_Rent_Khata().run()


#dataBase.close()