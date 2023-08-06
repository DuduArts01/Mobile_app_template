from kivy.uix.screenmanager import Screen


class Login(Screen):
    def logincontinue(self):
        self.username = self.ids.textUsername.text 
        username = ''
        
        if(username != self.username):
            login = self.username
            self.parent.current = ('Main_Menu')
            #change screen

        
    pass