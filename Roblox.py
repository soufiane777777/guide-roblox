from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="Bienvenue dans le Guide Roblox!", font_size=24))

        # Boutons vers différentes sections
        layout.add_widget(Button(text="Créer un compte", on_press=self.go_to_section1))
        layout.add_widget(Button(text="Créer son jeu", on_press=self.go_to_section2))
        layout.add_widget(Button(text="Gagner des Robux", on_press=self.go_to_section3))

        self.add_widget(layout)

    def go_to_section1(self, instance):
        self.manager.current = 'section1'

    def go_to_section2(self, instance):
        self.manager.current = 'section2'

    def go_to_section3(self, instance):
        self.manager.current = 'section3'


class SectionScreen(Screen):
    def __init__(self, title, content, **kwargs):
        super(SectionScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text=title, font_size=22))
        layout.add_widget(Label(text=content, font_size=16))
        layout.add_widget(Button(text="Retour", on_press=self.go_home))
        self.add_widget(layout)

    def go_home(self, instance):
        self.manager.current = 'home'


class RobloxGuideApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(SectionScreen(name='section1', title="Créer un compte", content="Étape 1 : Va sur roblox.com\nÉtape 2 : Clique sur 'Sign Up'..."))
        sm.add_widget(SectionScreen(name='section2', title="Créer son jeu", content="Télécharge Roblox Studio...\nCommence par un template simple..."))
        sm.add_widget(SectionScreen(name='section3', title="Gagner des Robux", content="1. Crée des vêtements\n2. Crée un jeu\n3. Utilise le système de passes"))

        return sm


if __name__ == '__main__':
    RobloxGuideApp().run()
