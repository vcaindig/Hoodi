mainscreen = """
#:import Label kivy.core.text.Label   
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol

#:set _bateria_label Label(text="Bateria\\n{}%", font_size= dp(30), halign= "center")
#:set _filtro_label Label(text="Filtro\\n{}%", font_size= dp(13), halign="center")
#:set _ventilador_label Label(text="Ventilador\\n{}%", font_size= dp(13), halign="center")
#:set _umidade_label Label(text="Umidade\\n{}%", font_size= dp(13), halign="center")
#:set _capuz_label Label(text="Capuz\\n{}%", font_size= dp(13), halign="center")

MyScreenManager:
    TelaPrincipal:
    TelaScanner:
    

<TelaPrincipal>:
    name: 'telaprincipal'
    MDBoxLayout:
        orientation: 'vertical' 
        MDBottomNavigation:
            MDBottomNavigationItem:
                name: 'main'
                text: 'Connex'
                icon: 'diving-helmet'
                MDIconButton:
                    icon: "minus"
                    pos_hint: {"center-x": .5, "center-y": .5}
                    on_release: root.minus()      
                CircularProgressBar:
                    id: cpbventilador
                    pos: dp(25), dp(50)
                    thickness: dp(4)
                    progress_colour: app.theme_cls.primary_color
                    widget_size: dp(90)
                    label: _ventilador_label
                    value: 100
                CircularProgressBar:
                    id: cpbfiltro
                    pos: Window.size[0] - dp(125), dp(50)
                    thickness: dp(4)
                    progress_colour: app.theme_cls.primary_color
                    widget_size: dp(90)
                    label: _filtro_label
                    value: 100
                CircularProgressBar:
                    id: cpbumidade
                    pos: dp(25), dp(170)
                    thickness: dp(4)
                    progress_colour: app.theme_cls.primary_color
                    widget_size: dp(90)
                    label: _umidade_label
                    value: 100
                CircularProgressBar:
                    id: cpbcapuz
                    pos: Window.size[0] - dp(125), dp(170)
                    thickness: dp(4)
                    progress_colour: app.theme_cls.primary_color
                    widget_size: dp(90)
                    label: _capuz_label
                    value: 100
                CircularProgressBar:
                    id: cpbbateria
                    pos: (Window.size[0] / 2) - dp(100), Window.size[1] - dp(300)
                    thickness: dp(7)
                    progress_colour: app.theme_cls.primary_color
                    widget_size: dp(200)
                    label: _bateria_label
                    value: 100
            MDBottomNavigationItem:
                name: 'manutencao'
                text: 'Manutenção'
                icon: 'settings'
                MDBoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Manutenção" 
                    MDFloatingActionButton:
                        id: btnleitor
                        icon: 'camera'
                        on_release: app.abrirleitor()
                    MDLabel:
                        id: codelabel
                        text: 'Esperando código'
                        
<TelaScanner>:
    name: 'telascanner'
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: "Filtro" 
        ZBarCam:
            id: zbarcam
            code_types: ZBarSymbol.QRCODE, ZBarSymbol.EAN13
            pos_hint: {'center_x': 0.5, 'center_y': 0.75}
            size_hint: [1, 1]
        MDLabel:
            id: qrlabel
            #size_hint: None, None
            size: self.texture_size[0], 50
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            halign: "center"
            text: ', '.join([str(symbol.data) for symbol in zbarcam.symbols])
      
        MDFloatingActionButton:
            id: btnvoltar
            icon: 'arrow-left'
            on_release: app.root.current = 'telaprincipal'


"""
