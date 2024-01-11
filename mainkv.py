from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.pickers import MDDatePicker
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


import pyrebase

#chaves
firebaseConfig = {
#coloca seu arquivo json aqui
}

firebase = pyrebase.initialize_app(firebaseConfig)
mAuth = firebase.auth()
db = firebase.database()
        
class FirstScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class HomeScreen(Screen):
    def voltar(self, *args):
        MDApp.get_running_app().root.current = 'login'

    def on_save(self, instance, value, date_range):
        date_string = value.strftime('%m-%d-%Y')
        self.ids.data.text = date_string

    def mostrarCalendario(self):
        date_dialog = MDDatePicker(primary_color="pink", selector_color="pink")
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()


    def agendar(self, data, horario):
        db.child("/schedule/").push({
            "Data": data,
            "Hora": horario
        })
        dialog = MDDialog(
        text=f"Agendamento confirmado {data}, {horario}",
        radius=[20, 7, 20, 7],
        buttons=[
            MDFlatButton(
                text="OK",
                on_release=lambda x: dialog.dismiss()
            )
        ]
    )
        dialog.open()
    

sm = ScreenManager()
sm.add_widget(FirstScreen(name='first'))
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(HomeScreen(name='home'))

class SalaoDeBeleza(MDApp):
    def build(self):
        
        Window.size = (330, 600)
        self.title = "Salão de Beleza"
        return Builder.load_file("mainkv.kv")
    
    def signup(self, em, ps, msg):
        
        try:
            mAuth.create_user_with_email_and_password(email=em.text, password=ps.text)
            print("Usuário criado, fazer login")
            msg.text = "Usuário Cadastrado!" + "\n" + "Faça login"
            msg.color = 'green'

            
        except:
            print("O email já está em uso")
            #msg.text = 'O email já está em uso'

    def login(self, em, ps, msg):
        try:
            print(em.text)
            print(ps.text)
            mAuth.sign_in_with_email_and_password(email=em.text, password=ps.text)
            print('Login')
            self.root.current = 'home'
         
                
        except:
            msg.text = "Dados inválidos"
            msg.color = 'red'
            toast("Dados inválidos")

SalaoDeBeleza().run()
