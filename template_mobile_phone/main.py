from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.text import LabelBase
#import fonts
LabelBase.register(name='ChunkFive', fn_regular='ChunkFive-Regular.otf')

class MainController(ScreenManager):
    #Controller screens
    pass

class MainApp(MDApp):
    def build(self):
        kv = Builder.load_file('maincontroller.kv')
        return kv
        #run main app 
    pass




chatapp = MainApp()
chatapp.run()
#run app
