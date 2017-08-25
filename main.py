from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.core.audio import SoundLoader
sound = SoundLoader.load('music.mp3')
sound.loop = True
sound.play()
#sound.unload()
class MainScreen(Screen):
	pass
class a1(Screen):
	pass
class a2(Screen):
	pass
class a3(Screen):
	pass
class a4(Screen):
	pass
class a5(Screen):
	pass
class a6(Screen):
	pass
class a7(Screen):
	pass
class a8(Screen):
	pass
class b1(Screen):
	pass
class b2(Screen):
	pass
class b3(Screen):
	pass
class b4(Screen):
	pass
class b5(Screen):
	pass
class b6(Screen):
	pass
class b7(Screen):
	pass
class b8(Screen):
	pass
class c1(Screen):
	pass
class c2(Screen):
	pass
class c3(Screen):
	pass
class c4(Screen):
	pass
class c5(Screen):
	pass
class c6(Screen):
	pass
class c7(Screen):
	pass
class c8(Screen):
	pass
class ScreenManagement(ScreenManager):
	pass

presentation = Builder.load_file("app.kv")
#Builder.load_string(""".""")
class celia(App):

	def build(self):
		return presentation


if __name__ == '__main__':
    celia().run()