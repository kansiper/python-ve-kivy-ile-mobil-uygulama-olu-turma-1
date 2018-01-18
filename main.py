from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
Builder.load_file('main.kv')

class index(Screen):
    pass
 
sm = ScreenManager()
sm.add_widget(index(name='index'))

class TestApp(App):

    def build(self):
        return sm #On envoie le screen manager pour affichage

if __name__ == '__main__':
    TestApp().run()
