from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


Window.clearcolor=(1,1,1,1)

x=0
class hi(App):
    def build(self):
        
        lay=BoxLayout(orientation='vertical',spacing='10')
        self.lab=Label(text=f'{x}',font_size='70sp',bold=True,color=(1,0,0,1),pos_hint={'center_x':0.5,'center_y':0.3})
        b=Button(text='Click me',font_size='70sp',on_release=self.add)

        lay.add_widget(b)
        lay.add_widget(self.lab)

        return lay

    def add(self,b):
        global x
        x+=1
        self.lab.text = f'{x}'
     

hi().run()
