from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:

    MDNavigationRail:

        MDNavigationRailItem:
            text: "Python"
            icon: "language-python"

        MDNavigationRailItem:
            text: "JavaScript"
            icon: "language-javascript"

        MDNavigationRailItem:
            text: "CPP"
            icon: "language-cpp"

        MDNavigationRailItem:
            text: "Git"
            icon: "git"

    MDScreen:
'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()