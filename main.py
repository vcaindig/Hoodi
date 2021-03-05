from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from screen_nav import mainscreen
import re
from plyer import notification
from kivy_garden.zbarcam import ZBarCam
from circular_progress_bar import CircularProgressBar


def validacao(mensagem):
    padrao = r"^#\d{6};FAN:\d{1,3};BAT:\d{1,3};FIL:\d{1,2}\/\d{1,2}\/\d{2};$"

    return bool(re.match(padrao, mensagem))


class TelaPrincipal(Screen):

    def minus(self):
        if self.ids.cpbventilador.value > 0:
            self.ids.cpbventilador.value = self.ids.cpbventilador.value - 1
        else:
            self.ids.cpbventilador.value = 0
        if self.ids.cpbumidade.value > 1:
            self.ids.cpbumidade.value = self.ids.cpbumidade.value - 2
        else:
            self.ids.cpbumidade.value = 0
        if self.ids.cpbcapuz.value > 0:
            self.ids.cpbcapuz.value = self.ids.cpbcapuz.value - 1
        else:
            self.ids.cpbcapuz.value = 0
        if self.ids.cpbfiltro.value > 1:
            self.ids.cpbfiltro.value = self.ids.cpbfiltro.value - 2
        else:
            self.ids.cpbfiltro.value = 0
        if self.ids.cpbbateria.value > 3 and self.ids.cpbbateria.value >= 50:
            self.ids.cpbbateria.value = self.ids.cpbbateria.value - 3
        elif self.ids.cpbbateria.value < 50:
            self.ids.cpbbateria.value = self.ids.cpbbateria.value - 3
            notification.notify('Bateria', 'Sua bateria está com ' + str(self.ids.cpbbateria.value) + '%')
        else:
            self.ids.cpbbateria.value = 0


class TelaScanner(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class ConnexApp(MDApp):

    def abrirleitor(self):
        self.root.current = 'telascanner'

    def build(self):
        self.theme_cls.secondary_palette = "Yellow"
        self.theme_cls.theme_style = "Dark"
        screen = Builder.load_string(mainscreen)
        return screen

    def leitor(self):
        self.root.ids.codelabel.value = self.root.ids.qrlabel.value


ConnexApp().run()
