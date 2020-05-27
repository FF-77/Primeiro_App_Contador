from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Contador(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        self.label = Label(text='1', font_size=37)
        button = Button(text='Acrescentar', font_size=37, on_release=self.Acrescentar)
        box.add_widget(self.label)
        box.add_widget(button)
        
        return box

    def Acrescentar(self,button):
        self.label.text = str(int(self.label.text)+1)



Contador().run()
