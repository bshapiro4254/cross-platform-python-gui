import sys
sys.path.append("_applibs")
sys.path.append(".")
### Python Lib imports ###
import random
import os
import re
import platform
import json
import time
import threading
import urllib
import hashlib

### Kivy Imports ###
import kivy
from kivy.config import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.image import Image, AsyncImage
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.dropdown import DropDown
from kivy.factory import Factory
from kivy.effects.scroll import ScrollEffect
from kivy.properties import ListProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest

Builder.load_string("""
<ScrolllabelLabel>:
	Label:
		text: root.text
		font_size: 34
		text_size: self.width, None
		size_hint_y: None
		height: self.texture_size[1]
		markup: True
""")

class ScrolllabelLabel(ScrollView):
	text =  StringProperty('')

class CustomScreen(Screen):
	hue = NumericProperty(0)

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
								 RecycleBoxLayout):
	''' Adds selection and focus behaviour to the view. '''

class resultBox(Popup):
	message = StringProperty()

class RecycleViewRow(BoxLayout):
	text = StringProperty()   

api_key = '1337-39393-7331'
api_url = 'https://3.16.215.215:33933'
# api_url = 'https://192.168.1.133:33733'

class LabelB(Label):
  bcolor = ListProperty([1,1,1,1])
Factory.register('KivyB', module='LabelB')

class GridB(GridLayout):
  bcolor = ListProperty([1,1,1,1])
Factory.register('KivyB', module='GridB') 

class MDD(DropDown):
	pass

class MaR_MUDRoot(BoxLayout):
	pass

class MaR_MUDApp(App):
	repeat_cmd = ''
	ROOM_INFO = Label()
	CMD_INFO = Label()
	CMD_IN = ObjectProperty(None)
	CMD_result = Popup()
	HUD_Scroll1 = ScrollView(size_hint=(None, None))
	HUD_Scroll2 = ScrollView(size_hint=(None, None))
	HUD_GUI = ScrollView(size_hint=(None, None))
	s = Slider()
	s2 = Slider()
	def __init__(self, **kwargs): 
		super().__init__(**kwargs) 
	
	def build(self):
		self.Cucumber = self.eat_a_pickle()
		self.Fav_Spells =  {"0":{"Type":"blank","Spell":"blank","Data":"blank"},"1":{"Type":"blank","Spell":"blank","Data":"blank"},"2":{"Type":"blank","Spell":"blank","Data":"blank"},"3":{"Type":"blank","Spell":"blank","Data":"blank"},"4":{"Type":"blank","Spell":"blank","Data":"blank"},"5":{"Type":"blank","Spell":"blank","Data":"blank"},"6":{"Type":"blank","Spell":"blank","Data":"blank"},"7":{"Type":"blank","Spell":"blank","Data":"blank"},		"8":{"Type":"blank","Spell":"blank","Data":"blank"},"9":{"Type":"blank","Spell":"blank","Data":"blank"},"10":{"Type":"blank","Spell":"blank","Data":"blank"},"11":{"Type":"blank","Spell":"blank","Data":"blank"},"12":{"Type":"blank","Spell":"blank","Data":"blank"},"13":{"Type":"blank","Spell":"blank","Data":"blank"},"14":{"Type":"blank","Spell":"blank","Data":"blank"},"15":{"Type":"blank","Spell":"blank","Data":"blank"},"16":{"Type":"blank","Spell":"blank","Data":"blank"}}
		self.Build_MDD_Menu()
		self.Pre_Load_Sounds()
		self.Build_SFAV_Menu()
		self.RMU = self.Silent = self.MUTE_SOUND = self.MUTE_MUSIC = False
		self.CMD_IN = TextInput(text='', multiline=False)
		self.CMD_IN = self.CMD_IN.__self__
		self.CMD_IN.bind(on_touch_down=self.hint_clear)
		self.CMD_IN.bind(text=self.on_move)
		self.CMD_IN.bind(on_text_validate=self.Execute_CMD)
		self.Char_POS = self.rrsm_Location = self.Warp_Location = ['0','0','0','0']
		self.move = ''
		self.AliveDetails = self.MoveDetails = self.RoomDetails = self.Class_Select = ''
		self.result_layout = {}
		self.result_layout1 = {}
		self.result_layout2 = {}
		self.result_layout3 = {}
		self.result_layout4 = {}
		self.result_layout5 = {}
		self.CMD_result = {}
		self.MiR = {}
		self.Char_Stats = {}
		self.CRoom = {}
		self.MyTexts = {}
		self.F_Num = '0'
		self.GItem = self.MSG_Alerts = self.sMSG = self.STarget = self.FN = self.LN = self.EA = self.password = self.username = ''
		self.ROSIE_PW = 'Empty'
		self.ROSIE_MENU = False
		self.Build_Stats_Display()
		self.root=ScreenManager()
		self.root = self.root.__self__	
		self.Login_Page()
		self.Login_Failed()
		self.Main_Screen()
		self.Reg_Page()
		self.Phone_Main()
		self.ROSIE_Main()
		self.Play_Sound('Startup')
		return self.root

	def Main_Screen(self):
		Window.softinput_mode = 'resize'
		self.Main_Screen_sm = Screen(name='Main_Page')
		self.Main_Screen_sm = self.Main_Screen_sm.__self__	
		self.icon = './data/MaR_MUD_Icon.png'
		self.Main_Screen_MaR_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		self.Main_Screen_MaR_MUDLogo.allow_stretch = True
		self.Main_Screen_MaR_MUDLogo.keep_ratio = True
		self.Main_Screen_MaR_MUDLogo = self.Main_Screen_MaR_MUDLogo.__self__
		
		self.HUD_Scroll1 = GridLayout(rows=1, size_hint_y=None, size=(Window.width -2, Window.height *.45 ))
		self.HUD_Scroll2 = GridLayout(rows=6, size_hint_y=None, size=(Window.width  -3, Window.height * .45))
		self.HUD_Stats = GridLayout(rows=1, size_hint_y=None, size=(Window.width  -3, Window.height * .16))
		self.HUD_GUI =  GridLayout(cols=3, size_hint_y=None, size=(Window.width  -3, Window.height * .07))
		self.HUD_GUI2 = GridLayout(cols=4, size_hint_y=None, size=(Window.width  -3, Window.height * .07))
		self.HUD_GUI3 = GridLayout(cols=3, size_hint_y=None, size=(Window.width  -3, Window.height * .07))
		# self.HUD_GUI4 = GridLayout(cols=3, size_hint_y=None, size=(Window.width  -3, Window.height * .06))
		self.Hud_CMD =  GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .07))

		layout = GridLayout(rows=3,size=(Window.width , Window.height *.98))
		self.Main_Screen_sm.add_widget(layout)
		self.root.add_widget(self.Main_Screen_sm)	
		
		room_info = self.RoomDetails
		cmd_result = ''
		
		self.ROOM_INFO = ScrolllabelLabel(text=room_info)
		self.CMD_INFO = Label(text=cmd_result,halign='left',font_size='12sp',text_size=self.CMD_INFO.size, markup = True)
													# self.CMD_IN = TextInput(text='', multiline=False)
													# self.CMD_IN.bind(on_text_validate=self.Execute_CMD)
		self.HUD_Scroll1.add_widget(self.ROOM_INFO)
		btn1 = Button(text="Go!",size_hint = (.2,1))

		btnRest = Button(text=self.pm("Rest",'fg_yellow'),markup=True,size_hint = (.2,1))
		btnRest.bind(on_press=self.Execute_Rest)
		btnPhone = Button(text=self.pm("Phone",'fg_yellow'),markup=True,size_hint = (.2,1))
		btnPhone.bind(on_press=self.changeScreenPhone)

		self.btnN = Button(text="Go N!",size_hint = (.2,1),markup=True)
		self.btnN.bind(on_press=self.Execute_N)
		self.btnS = Button(text="Go S!",size_hint = (.2,1),markup=True)
		self.btnS.bind(on_press=self.Execute_S)
		self.btnE = Button(text="Go E!",size_hint = (.2,1),markup=True)
		self.btnE.bind(on_press=self.Execute_E)
		self.btnW = Button(text="Go W!",size_hint = (.2,1),markup=True)
		self.btnW.bind(on_press=self.Execute_W)
		self.btnU = Button(text="Go U!",size_hint = (.2,1),markup=True)
		self.btnU.bind(on_press=self.Execute_U)
		self.btnD = Button(text="Go D!",size_hint = (.2,1),markup=True)
		self.btnD.bind(on_press=self.Execute_D)

		self.btnA = Button(text="Attack!",size_hint = (.2,1),markup=True)
		# btnA.bind(on_press=self.Execute_A)
		self.btnA.bind(on_press=lambda *args:self.changeScreenAttack())
		
		self.btnGA = Button(text="Get\nAll!",size_hint = (.2,1),markup=True)
		self.btnGA.bind(on_press=self.Execute_GA)

		btnLR = Button(text=self.pm("Look\nRoom!",'fg_yellow'),markup=True,size_hint = (.2,1))
		btnLR.bind(on_press=lambda *args: self.changeScreenItems())		

		btnI = Button(text=self.pm("Inv",'fg_yellow'),markup=True,size_hint = (.2,1))
		btnI.bind(on_press=self.Execute_Inv)
		btnSay = Button(text=self.pm("Say",'fg_yellow'),markup=True,size_hint = (.2,1))
		btnSay.bind(on_press=self.result_PopUP_Player_Speaks)		

		self.HUD_GUI.add_widget(self.btnU)
		self.HUD_GUI.add_widget(self.btnN)
		self.HUD_GUI.add_widget(self.btnGA)

		self.HUD_GUI2.add_widget(self.btnW)
		self.HUD_GUI2.add_widget(self.btnA)
		self.HUD_GUI2.add_widget(self.btnE)

		self.HUD_GUI3.add_widget(self.btnD)
		self.HUD_GUI3.add_widget(self.btnS)
		self.HUD_GUI3.add_widget(btnLR)
		
		# self.HUD_GUI4.add_widget(btnRest)
		# self.HUD_GUI4.add_widget(btnSay)
		# self.HUD_GUI4.add_widget(btnPhone)

		btn1.bind(on_press=self.Execute_CMD)

		self.HUD_Stats.add_widget(self.Stats_displaym[1])

		self.Hud_CMD.add_widget(btn1)
		self.Hud_CMD.add_widget(self.CMD_IN)


		self.HUD_Scroll2.add_widget(self.Hud_CMD)
		self.HUD_Scroll2.add_widget(self.HUD_Stats)
		self.HUD_Scroll2.add_widget(self.HUD_GUI)
		self.HUD_Scroll2.add_widget(self.HUD_GUI2)
		self.HUD_Scroll2.add_widget(self.HUD_GUI3)
		# self.HUD_Scroll2.add_widget(self.HUD_GUI4)
		layout.add_widget(self.MDD_Layout[0])
		layout.add_widget(self.HUD_Scroll1)		
		layout.add_widget(self.HUD_Scroll2)

	def Phone_Main(self,*args):
		Window.softinput_mode = 'pan'
		self.Phone_Main_sm = Screen(name='Phone_Main')
		self.Phone_Main_sm = self.Phone_Main_sm.__self__

		self.icon = './data/MaR_MUD_Icon.png'
		self.Phone_Main_MaR_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		self.Phone_Main_MaR_MUDLogo.allow_stretch = True
		self.Phone_Main_MaR_MUDLogo.keep_ratio = True
		self.Phone_Main_MaR_MUDLogo = self.Phone_Main_MaR_MUDLogo.__self__
		self.Phone_Main_PG1 = GridLayout(rows=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Phone_Main_PG1 = self.Phone_Main_PG1.__self__
		self.Phone_Main_PG2 = GridLayout(rows=7, size_hint_y=None, size=(Window.width  * .95, (Window.height * .6)))
		self.Phone_Main_PG2 = self.Phone_Main_PG2.__self__
		self.Phone_Main_G1 = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .125)))
		self.Phone_Main_G1 = self.Phone_Main_G1.__self__
		self.Phone_Main_G2 = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .125)))
		self.Phone_Main_G2 = self.Phone_Main_G2.__self__
		if self.ROSIE_MENU == True or self.ROSIE_MENU == 'True':
			self.Phone_Main_G3 = GridLayout(cols=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		else:
			self.Phone_Main_G3 = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Phone_Main_G3 = self.Phone_Main_G3.__self__
		self.Phone_Main_G4 = GridLayout(cols=5, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Phone_Main_G4 = self.Phone_Main_G4.__self__
		self.Phone_Main_G5 = GridLayout(cols=5, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Phone_Main_G5 = self.Phone_Main_G5.__self__
		self.Phone_Main_G6 = GridLayout(cols=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Phone_Main_G6 = self.Phone_Main_G6.__self__
		self.Phone_Main_spacer = BoxLayout(padding=.2,spacing=.2, orientation='horizontal',size_hint=(1, 30),pos_hint={'center_x': .5, 'center_y': .5})

		layout = GridLayout(rows=3, size_hint_y=None, size=(Window.width, Window.height))
		layout = layout.__self__
		layout2 = GridLayout(rows=2, size_hint_y=None, size=(Window.width, Window.height * .15))
		layout2 = layout2.__self__
		self.Phone_Main_sm.add_widget(layout)
		self.root.add_widget(self.Phone_Main_sm)
		
		self.Phone_Main_Text_Area = ScrolllabelLabel(text='Welcome to the MaR_MUD Communications\n Enjoy your phone.')
		self.Phone_Main_Text_Area = self.Phone_Main_Text_Area.__self__
		self.Phone_Main_New_MSGs = Label(text='{}'.format(''),halign='left',font_size='12sp',size=(Window.width * .8,Window.height * .2), markup = True)
		self.Phone_Main_New_MSGs = self.Phone_Main_New_MSGs.__self__

		# self.Phone_Main_btnWM = Button(text=self.pm("Warp\nMonsters",'fg_red'),markup=True,size_hint = (1,1))
		# self.Phone_Main_btnWM.bind(on_press=(lambda *args: self.Execute_API_SM('warp monsters')))
		# self.Phone_Main_btnCrafts = Button(text=self.pm("Crafts\nMenu",'fg_green'),markup=True,size_hint = (1,1))
		# self.Phone_Main_btnCrafts.bind(on_press=(lambda *args: self.API_List_Crafts(self.username,self.password,api_key)))
		# self.Phone_Main_btnWH = Button(text=self.pm("Warp\nHome",'fg_cyan'),markup=True,size_hint = (1,1))
		# self.Phone_Main_btnWH.bind(on_press=(lambda *args: self.Execute_API_SM('warp home')))

		self.Phone_Main_btnRead = Button(text=self.pm("Read\nNew",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Phone_Main_btnRead.bind(on_press=(lambda *args: self.API_Phone(self.username,self.password,'rtext','new','',api_key)))
		self.Phone_Main_btnReadAll = Button(text=self.pm("Read\nAll",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Phone_Main_btnReadAll.bind(on_press=(lambda *args: self.API_Phone(self.username,self.password,'rtext','all','',api_key)))

		self.Phone_Main_btnNMsg = Button(text=self.pm("New\nMessage",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Phone_Main_btnNMsg.bind(on_press=(lambda *args: self.result_PopUP_Send_PMSGs('New Message','Enter your Message.')))
		self.Phone_Main_btnNInvite = Button(text=self.pm("New\nHouse Invite",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Phone_Main_btnNInvite.bind(on_press=(lambda *args: self.PopUp_Send_Invite('New Invite','Who Do You Want to Invite?')))
		self.Phone_Main_btnNMsg = self.Phone_Main_btnNMsg.__self__
		self.Phone_Main_btnCall = Button(text=self.pm("New\nCall",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Phone_Main_btnCall.bind(on_press=(lambda *args: self.result_PopUP_Send_Call('New Call','Enter the number you wish to reach.')))
		self.Phone_Main_btnCall = self.Phone_Main_btnCall.__self__
		# self.Phone_Main_btnStore = Button(text=self.pm("Shop\nFrank\nCorp",'fg_green'),markup=True,size_hint = (1,1))
		# self.Phone_Main_btnStore.bind(on_press=(lambda *args: self.API_Store(self.username,self.password,'api_list',api_key)))
		# self.Phone_Main_btnStore = self.Phone_Main_btnStore.__self__
		# self.Phone_Main_btnSound = Button(text="Play\nSounds?",size_hint = (1,1),markup=True)
		# self.Phone_Main_btnSound.bind(on_press=(lambda *args: self.OnMute('SoundFX')))
		# self.Phone_Main_btnSound = self.Phone_Main_btnSound.__self__
		# self.Phone_Main_btnMusic = Button(text="Play\nMusic?",size_hint = (1,1),markup=True)
		# self.Phone_Main_btnMusic.bind(on_press=(lambda *args: self.OnMute('Music')))
		# self.Phone_Main_btnMusic = self.Phone_Main_btnMusic.__self__		
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.changeScreenBack)
		back = back.__self__

		# btnDGPS = Button(text="DGPS",size_hint = (.2,1))
		# btnDGPS.bind(on_press=lambda *args: self.result_PopUP_DGPS('Frank Corp Warp Menu.','Warp Almost Anywhere With Frank Corp.'))
		# self.Phone_Main_G6.add_widget(btnDGPS)

		btnLogout = Button(text="Quit",size_hint = (.2,1))
		btnLogout.bind(on_press=self.Logout_Script)
		self.Phone_Main_G4.add_widget(btnLogout)

		# btnSB = Button(text=self.pm("Spell\nBook!",'fg_green'),markup=True,size_hint = (.2,1))
		# btnA.bind(on_press=self.Execute_A)
		# btnSB.bind(on_press=lambda *args:self.API_LSpell(self.username,self.password,api_key))	
		# self.Phone_Main_G6.add_widget(btnSB)

		self.Phone_Main_G1.add_widget(self.Phone_Main_Text_Area)
		self.Phone_Main_G2.add_widget(self.Phone_Main_New_MSGs)
		
		self.Phone_Main_G3.add_widget(self.Phone_Main_btnRead)
		self.Phone_Main_G3.add_widget(self.Phone_Main_btnReadAll)
		

		# self.Phone_Main_G4.add_widget(self.Phone_Main_btnSound)
		# self.Phone_Main_G4.add_widget(self.Phone_Main_btnMusic)
		self.Phone_Main_G4.add_widget(back)
		self.Phone_Main_G4.add_widget(self.Phone_Main_btnCall)
		self.Phone_Main_G4.add_widget(self.Phone_Main_btnNMsg)
		self.Phone_Main_G4.add_widget(self.Phone_Main_btnNInvite)
		
		# self.Phone_Main_G5.add_widget(self.Phone_Main_btnStore)
		# self.Phone_Main_G5.add_widget(self.Phone_Main_btnCrafts)
		
		# self.Phone_Main_G5.add_widget(self.Phone_Main_btnWM)
		# self.Phone_Main_G5.add_widget(self.Phone_Main_btnWH)

		layout.add_widget(layout2)
		# layout2.add_widget(self.Phone_Main_G1)
		layout.add_widget(self.MDD_Layout[1])
		self.Phone_Main_PG2.add_widget(self.Phone_Main_G1)
		self.Phone_Main_PG2.add_widget(self.Phone_Main_G2)
		self.Phone_Main_PG2.add_widget(self.Phone_Main_G3)
		self.Phone_Main_PG2.add_widget(self.Phone_Main_G4)
		# self.Phone_Main_PG2.add_widget(self.Phone_Main_G6)
		# self.Phone_Main_PG2.add_widget(self.Phone_Main_G5)
		layout.add_widget(self.Phone_Main_PG2)

	def Login_Page(self):
		Window.softinput_mode = 'pan'
		self.Login_Page_sm = Screen(name='Login_Page')
		self.Login_Page_sm = self.Login_Page_sm.__self__

		self.icon = './data/MaR_MUD_Icon.png'
		self.Login_Page_MaR_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		self.Login_Page_MaR_MUDLogo.allow_stretch = True
		self.Login_Page_MaR_MUDLogo.keep_ratio = True
		self.Login_Page_MaR_MUDLogo = self.Login_Page_MaR_MUDLogo.__self__
		self.Login_Page_Main_PG1 = GridLayout(rows=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .56)))
		self.Login_Page_Main_PG1 = self.Login_Page_Main_PG1.__self__
		self.Login_Page_Main_PG2 = GridLayout(rows=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .24)))
		self.Login_Page_Main_PG2 = self.Login_Page_Main_PG2.__self__
		self.Login_Page_Main_G1 = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Login_Page_Main_G1 = self.Login_Page_Main_G1.__self__
		self.Login_Page_Main_G2 = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Login_Page_Main_G2 = self.Login_Page_Main_G2.__self__
		self.Login_Page_Main_G3 = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Login_Page_Main_G3 = self.Login_Page_Main_G3.__self__
		self.Login_Page_Main_spacer = BoxLayout(padding=.2,spacing=.2, orientation='horizontal',size_hint=(1, 30),pos_hint={'center_x': .5, 'center_y': .5})
		layout = GridLayout(rows=3, size_hint_y=None, size=(Window.width, Window.height))
		layout = layout.__self__
		layout2 = BoxLayout(padding=7,spacing=10, orientation='horizontal',size_hint=(1, Window.height *.6),pos_hint={'center_x': .5, 'center_y': .5})
		layout2 = layout2.__self__
		self.Login_Page_sm.add_widget(layout)
		self.root.add_widget(self.Login_Page_sm)
		
		self.Login_Page_Text_Area = ScrolllabelLabel(text='Welcome to the MaR_MUD Delivery Platform.')
		self.Login_Page_Text_Area = self.Login_Page_Text_Area.__self__
		self.Login_Page_UN_Input = TextInput(hint_text='Enter Username : ',text='', multiline=False)
		self.Login_Page_UN_Input.bind(on_touch_down=self.hint_clear)
		self.Login_Page_UN_Input = self.Login_Page_UN_Input.__self__
		self.Login_Page_UN_Input.bind(text=self.on_username)
		self.Login_Page_UN_Input.bind(on_touch_down=self.hint_clear)
		# self.Login_Page_UN_Input.bind(on_text_validate=self.Next_Field)
		self.Login_Page_PW_Input = TextInput(hint_text='Enter Password : ',text='',password=True, multiline=False)
		self.Login_Page_PW_Input = self.Login_Page_PW_Input.__self__
		self.Login_Page_PW_Input.bind(text=self.on_password)
		self.Login_Page_PW_Input.bind(on_touch_down=self.hint_clear)
		self.Login_Page_PW_Input.bind(on_text_validate=self.login_script)

		self.Login_Page_btnLogIn = Button(text="Log In",size_hint = (.2,1))
		self.Login_Page_btnLogIn.bind(on_press=self.login_script)
		self.Login_Page_btnLogIn = self.Login_Page_btnLogIn.__self__
		self.Login_Page_btnRegister = Button(text="New? Register!",size_hint = (.2,1))
		self.Login_Page_btnRegister.bind(on_press=self.changeScreenRegister)
		self.Login_Page_btnRegister = self.Login_Page_btnRegister.__self__
		
		self.Login_Page_Main_G1.add_widget(self.Login_Page_UN_Input)

		self.Login_Page_Main_G2.add_widget(self.Login_Page_PW_Input)

		self.Login_Page_Main_G3.add_widget(self.Login_Page_btnLogIn)
		self.Login_Page_Main_G3.add_widget(self.Login_Page_btnRegister)
		
		layout2.add_widget(self.Login_Page_MaR_MUDLogo)
		layout.add_widget(layout2)
		
		self.Login_Page_Main_PG2.add_widget(self.Login_Page_Main_G1)
		self.Login_Page_Main_PG2.add_widget(self.Login_Page_Main_G2)
		self.Login_Page_Main_PG2.add_widget(self.Login_Page_Main_G3)
		layout.add_widget(self.Login_Page_Main_PG2)
		

	def Login_Failed(self):
		Window.softinput_mode = 'pan'
		self.Login_Failed_sm = Screen(name='Login_Failed')
		self.Login_Failed_sm = self.Login_Failed_sm.__self__
		self.icon = './data/MaR_MUD_Icon.png'
		self.Login_Failed_MaR_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		self.Login_Failed_MaR_MUDLogo = self.Login_Failed_MaR_MUDLogo.__self__
		self.Login_Failed_MaR_MUDLogo.allow_stretch = True
		self.Login_Failed_MaR_MUDLogo.keep_ratio = True
		self.Login_Failed_Main_PG1 = GridLayout(rows=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .56)))
		self.Login_Failed_Main_PG1 = self.Login_Failed_Main_PG1.__self__
		self.Login_Failed_Main_PG2 = GridLayout(rows=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .24)))
		self.Login_Failed_Main_PG2 = self.Login_Failed_Main_PG2.__self__
		self.Login_Failed_Main_G1 = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Login_Failed_Main_G1 = self.Login_Failed_Main_G1.__self__
		self.Login_Failed_Main_G2 = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Login_Failed_Main_G2 = self.Login_Failed_Main_G2.__self__
		self.Login_Failed_Main_G3 = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Login_Failed_Main_G3 = self.Login_Failed_Main_G3.__self__
		layout = GridLayout(rows=3, size_hint_y=None, size=(Window.width, Window.height))
		layout = layout.__self__
		layout2 = BoxLayout(padding=7,spacing=10, orientation='horizontal',size_hint=(1, Window.height *.6),pos_hint={'center_x': .5, 'center_y': .5})
		layout2 = layout2.__self__
		self.Login_Failed_sm.add_widget(layout)
		self.root.add_widget(self.Login_Failed_sm)
		
		
		
		self.Login_Failed_Text_Area = ScrolllabelLabel(text='Welcome to the MaR_MUD Driver Platform.\n Your Login Attempt Failed. \n Check your Login Details and Try Again. \n un {0} pw {1}'.format(self.username,self.password))
		self.Login_Failed_Text_Area = self.Login_Failed_Text_Area.__self__
		self.Login_Failed_UN_Input = TextInput(hint_text='Enter Username : ',text='', multiline=False)
		self.Login_Failed_UN_Input = self.Login_Failed_UN_Input.__self__
		self.Login_Failed_UN_Input.bind(on_touch_down=self.hint_clear)
		self.Login_Failed_UN_Input.bind(text=self.on_username)
		# self.Login_Failed_UN_Input.bind(on_text_validate=self.Next_Field)
		self.Login_Failed_PW_Input = TextInput(hint_text='Enter Password : ',text='', password=True, multiline=False)
		self.Login_Failed_PW_Input = self.Login_Failed_PW_Input.__self__
		self.Login_Failed_PW_Input.bind(on_touch_down=self.hint_clear)
		self.Login_Failed_PW_Input.bind(text=self.on_password)
		self.Login_Failed_PW_Input.bind(on_text_validate=self.login_script)
		self.Login_Failed_Main_PG1.add_widget(self.Login_Failed_Text_Area)
		

		self.Login_Failed_btnLogIn = Button(text="Log In",size_hint = (.2,1))
		self.Login_Failed_btnLogIn.bind(on_press=self.login_script)
		self.Login_Failed_btnLogIn = self.Login_Failed_btnLogIn.__self__
		self.Login_Failed_btnRegister = Button(text="New? Register!",size_hint = (.2,1))
		self.Login_Failed_btnRegister.bind(on_press=self.changeScreenRegister)
		self.Login_Failed_btnRegister = self.Login_Failed_btnRegister.__self__
		self.Login_Failed_Main_G1.add_widget(self.Login_Failed_UN_Input)

		self.Login_Failed_Main_G2.add_widget(self.Login_Failed_PW_Input)

		self.Login_Failed_Main_G3.add_widget(self.Login_Failed_btnLogIn)
		self.Login_Failed_Main_G3.add_widget(self.Login_Failed_btnRegister)
		layout2.add_widget(self.Login_Failed_MaR_MUDLogo)
		layout.add_widget(layout2)
		layout.add_widget(self.Login_Failed_Main_PG1)
		self.Login_Failed_Main_PG2.add_widget(self.Login_Failed_Main_G1)
		self.Login_Failed_Main_PG2.add_widget(self.Login_Failed_Main_G2)
		self.Login_Failed_Main_PG2.add_widget(self.Login_Failed_Main_G3)
		layout.add_widget(self.Login_Failed_Main_PG2)

	def Reg_Page(self):
		Window.softinput_mode = 'pan'
		self.Reg_Page_sm = Screen(name='Reg_Page')
		self.Reg_Page_sm = self.Reg_Page_sm.__self__

		self.icon = './data/MaR_MUD_Icon.png'
		self.Reg_Page_MaR_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		self.Reg_Page_MaR_MUDLogo.allow_stretch = True
		self.Reg_Page_MaR_MUDLogo.keep_ratio = True
		self.Reg_Page_MaR_MUDLogo = self.Reg_Page_MaR_MUDLogo.__self__
		self.Reg_Page_Main_PG1 = GridLayout(rows=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Reg_Page_Main_PG1 = self.Reg_Page_Main_PG1.__self__
		self.Reg_Page_Main_PG2 = GridLayout(rows=5, size_hint_y=None, size=(Window.width  * .8, (Window.height * .75)))
		self.Reg_Page_Main_PG2 = self.Reg_Page_Main_PG2.__self__
		self.Reg_Page_Main_G1 = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Reg_Page_Main_G1 = self.Reg_Page_Main_G1.__self__
		self.Reg_Page_Main_G2 = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Reg_Page_Main_G2 = self.Reg_Page_Main_G2.__self__
		self.Reg_Page_Main_G3 = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Reg_Page_Main_G3 = self.Reg_Page_Main_G3.__self__
		self.Reg_Page_Main_G4 = GridLayout(cols=4, size_hint_y=None, size=(Window.width  * .8, (Window.height * .4)))
		self.Reg_Page_Main_G4 = self.Reg_Page_Main_G4.__self__
		self.Reg_Page_Main_G5 = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .08)))
		self.Reg_Page_Main_G5 = self.Reg_Page_Main_G5.__self__
		self.Reg_Page_Main_spacer = BoxLayout(padding=.2,spacing=.2, orientation='horizontal',size_hint=(1, 30),pos_hint={'center_x': .5, 'center_y': .5})
		layout = GridLayout(rows=3, size_hint_y=None, size=(Window.width, Window.height))
		layout = layout.__self__
		layout2 = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		layout2 = layout2.__self__
		self.Reg_Page_sm.add_widget(layout)
		self.root.add_widget(self.Reg_Page_sm)
		
		self.Reg_Page_Text_Area = ScrolllabelLabel(text=self.Paint_SVAR('''MaR_MUD Platform Registration.\nWelcome to MaR_MUD, A Land of adventure. We hope you enjoy the game.\nYou can use the buttons or Type your commands. Type "Help" for a list of some typable commands.\nEnter Login Details to get started.''','fg_magenta','fg_black'))
		self.Reg_Page_Text_Area = self.Reg_Page_Text_Area.__self__
		
		self.Reg_Page_UN_Input = TextInput(hint_text='Username : ',text='', multiline=False)
		self.Reg_Page_UN_Input.bind(on_touch_down=self.hint_clear)
		self.Reg_Page_UN_Input = self.Reg_Page_UN_Input.__self__
		self.Reg_Page_UN_Input.bind(text=self.on_username)
		self.Reg_Page_UN_Input.bind(on_touch_down=self.hint_clear)
		
		self.Reg_Page_PW_Input = TextInput(hint_text='Password : ',text='',password=True, multiline=False)
		self.Reg_Page_PW_Input = self.Reg_Page_PW_Input.__self__
		self.Reg_Page_PW_Input.bind(text=self.on_password)
		self.Reg_Page_PW_Input.bind(on_touch_down=self.hint_clear)
		self.Reg_Page_PW_Input.bind(on_text_validate=self.login_script)

		self.Reg_Page_FN_Input = TextInput(hint_text='First Name : ',text='', multiline=False)
		self.Reg_Page_FN_Input.bind(on_touch_down=self.hint_clear)
		self.Reg_Page_FN_Input = self.Reg_Page_FN_Input.__self__
		self.Reg_Page_FN_Input.bind(text=self.on_FN)
		self.Reg_Page_FN_Input.bind(on_touch_down=self.hint_clear)

		self.Reg_Page_LN_Input = TextInput(hint_text='Last Name : ',text='', multiline=False)
		self.Reg_Page_LN_Input.bind(on_touch_down=self.hint_clear)
		self.Reg_Page_LN_Input = self.Reg_Page_LN_Input.__self__
		self.Reg_Page_LN_Input.bind(text=self.on_LN)
		self.Reg_Page_LN_Input.bind(on_touch_down=self.hint_clear)
	
		# self.Reg_Page_UN_Input.bind(on_text_validate=self.Next_Field)
		self.Reg_Page_EA_Input = TextInput(hint_text='Email : ',text='', multiline=False)
		self.Reg_Page_EA_Input = self.Reg_Page_EA_Input.__self__
		self.Reg_Page_EA_Input.bind(text=self.on_EA)
		self.Reg_Page_EA_Input.bind(on_touch_down=self.hint_clear)
		self.Reg_Page_EA_Input.bind(on_text_validate=self.reg_script)

		self.Reg_Page_dd_btn_Mage = Button(text="Class:\n Mage\nBNS\nAt/Df\nSpells\n++Max\n MP\n+At\n+Attack\n Spells",size_hint = (.2,1))
		self.Reg_Page_dd_btn_Mage.bind(on_press=lambda *args:self.OnClassSelect('Mage'))
		self.Reg_Page_dd_btn_Mage = self.Reg_Page_dd_btn_Mage.__self__		

		self.Reg_Page_dd_btn_Medic = Button(text="Class:\n Medic\nBNS\nHl/Df\n+Max\n MP\n++Df\n+Heal\n Spells",size_hint = (.2,1))
		self.Reg_Page_dd_btn_Medic.bind(on_press=lambda *args:self.OnClassSelect('Medic'))
		self.Reg_Page_dd_btn_Medic = self.Reg_Page_dd_btn_Medic.__self__		

		self.Reg_Page_dd_btn_Marauder = Button(text="Class:\n Marauder\nBNS\n M_At\n+++Max\n HP\n++Attack",size_hint = (.2,1))
		self.Reg_Page_dd_btn_Marauder.bind(on_press=lambda *args:self.OnClassSelect('Marauder'))
		self.Reg_Page_dd_btn_Marauder = self.Reg_Page_dd_btn_Marauder.__self__		

		self.Reg_Page_dd_btn_Marksmen = Button(text="Class:\n Marksmen\nBNS\n R_At\n+Max\n HP\n+Max\n Ammo\n++Defense",size_hint = (.2,1))
		self.Reg_Page_dd_btn_Marksmen.bind(on_press=lambda *args:self.OnClassSelect('Marksmen'))
		self.Reg_Page_dd_btn_Marksmen = self.Reg_Page_dd_btn_Marksmen.__self__

		self.Reg_Page_btnSubmit = Button(text="Register",size_hint = (1,.08))
		self.Reg_Page_btnSubmit.bind(on_press=self.reg_script)
		self.Reg_Page_btnSubmit = self.Reg_Page_btnSubmit.__self__

		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back = back.__self__
		back.bind(on_press=self.changeScreenLogin)

		self.Reg_Page_Main_G1.add_widget(self.Reg_Page_UN_Input)
		self.Reg_Page_Main_G1.add_widget(self.Reg_Page_PW_Input)
		
		self.Reg_Page_Main_G2.add_widget(self.Reg_Page_FN_Input)
		self.Reg_Page_Main_G2.add_widget(self.Reg_Page_LN_Input)

		self.Reg_Page_Main_G3.add_widget(self.Reg_Page_EA_Input)
		
		self.Reg_Page_Main_G4.add_widget(self.Reg_Page_dd_btn_Mage)
		self.Reg_Page_Main_G4.add_widget(self.Reg_Page_dd_btn_Medic)
		self.Reg_Page_Main_G4.add_widget(self.Reg_Page_dd_btn_Marauder)
		self.Reg_Page_Main_G4.add_widget(self.Reg_Page_dd_btn_Marksmen)

		self.Reg_Page_Main_G5.add_widget(back)
		self.Reg_Page_Main_G5.add_widget(self.Reg_Page_btnSubmit)


		layout2.add_widget(self.Reg_Page_Text_Area)
		
		
		self.Reg_Page_Main_PG1.add_widget(self.Reg_Page_MaR_MUDLogo)

		self.Reg_Page_Main_PG2.add_widget(self.Reg_Page_Main_G4)
		self.Reg_Page_Main_PG2.add_widget(self.Reg_Page_Main_G1)
		self.Reg_Page_Main_PG2.add_widget(self.Reg_Page_Main_G2)
		self.Reg_Page_Main_PG2.add_widget(self.Reg_Page_Main_G3)
		self.Reg_Page_Main_PG2.add_widget(self.Reg_Page_Main_G5)

		layout.add_widget(self.Reg_Page_Main_PG1)	
		layout.add_widget(layout2)
		layout.add_widget(self.Reg_Page_Main_PG2)

	def OnClassSelect(self,Class_Select):
		self.Class_Select = Class_Select

	def result_PopUP(self,func,result,backone=False,norepeat=False):
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True		
		self.result_layout4[1] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .425, Window.height * .2))
		self.result_layout4[1] = self.result_layout4[1].__self__
		self.result_layout4[1].add_widget(result_Mar_MUDLogo)
		self.result_layout[1] =  GridLayout(rows=5, size_hint_y=None, size=(Window.width, Window.height))
		self.result_layout[1] = self.result_layout[1].__self__
		self.result_layout[1].bind(height = self.result_layout[1].setter('top'))
		self.RPopUp_result_Stats = GridLayout(rows=1, size_hint_y=None, size=(Window.width, Window.height * .19))
		self.RPopUp_result_Stats = self.RPopUp_result_Stats.__self__
		self.result_layout3[1] = GridLayout(rows=1, size_hint_y=None, size=(Window.width, Window.height * .425))
		self.result_layout3[1] = self.result_layout3[1].__self__
		if norepeat == True:
			self.result_layout2[1] = GridLayout(cols=1, size_hint_y=None, size=(Window.width, Window.height * .08))
		else:
			self.result_layout2[1] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[1] = self.result_layout2[1].__self__
		if (scroll_height < (Window.height / 2)):
			scroll_height = scroll_height + 120
		scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[1].height - 30), size = (Window.width, scroll_height))
		Res_Scroll1 = ScrolllabelLabel(text=str(result))
		Res_Scroll1.text_size = Res_Scroll1.size
		Res_Scroll1 = Res_Scroll1.__self__
		scrlFBtns.add_widget(Res_Scroll1)
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back = back.__self__
		if norepeat == True:
			self.result_layout2[1].add_widget(back)
		else:
			if self.AliveDetails == False:
				restart = Button(text='Restart',size_hint = (1,2))
				lquit = Button(text='Quit',size_hint = (1,2))
				restart.bind(on_press=self.restart)
				lquit.bind(on_press=self.Logout_Script)
				self.result_layout2[1].add_widget(restart)
				self.result_layout2[1].add_widget(lquit)
			else:			
				repeat = Button(text='Repeat last!',size_hint = (1,1.5))
				repeat.bind(on_press=self.Repeat_CMD)			
				self.result_layout2[1].add_widget(repeat)
				self.result_layout2[1].add_widget(back)

		self.result_layout3[1].add_widget(scrlFBtns)
		self.RPopUp_result_Stats.add_widget(self.Stats_displaym[5])
		self.result_layout[1].add_widget(self.MDD_Layout[4])
		self.result_layout[1].add_widget(self.result_layout4[1])
		self.result_layout[1].add_widget(self.result_layout3[1])
		self.result_layout[1].add_widget(self.RPopUp_result_Stats)
		self.result_layout[1].add_widget(self.result_layout2[1])
		self.CMD_result[1] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[1],auto_dismiss=False)
		self.CMD_result[1] = self.CMD_result[1].__self__
		if backone == False:
			back.bind(on_press=self.Dismiss_All)
		else:
			back.bind(on_press=lambda *args,index=1:self.Dismiss_One(index))

		self.CMD_result[1].open()

	def PopUP_List_Crafts(self,func,result):
		self.Dismiss_One(1)
		self.Dismiss_All()
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[2] = GridLayout(rows=4, size_hint_y=None, size=(Window.width * .9, Window.height))
		self.result_layout[2].bind(height = self.result_layout[2].setter('top'))
		self.result_layout[2] = self.result_layout[2].__self__
		self.result_layout[2].bind(height = self.result_layout[2].setter('top'))
		self.result_layout4[2] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .9, Window.height * .2))
		self.result_layout4[2] = self.result_layout4[2].__self__
		self.result_layout4[2].bind(height = self.result_layout[2].setter('top'))
		self.result_layout4[2].add_widget(result_Mar_MUDLogo)
		self.result_layout3[2] = GridLayout(cols=1, size_hint_y=None, size=(Window.width - 10, Window.height * .55))
		self.result_layout3[2] = self.result_layout3[2].__self__
		self.result_layout2[2] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .1))
		self.result_layout2[2] = self.result_layout2[2].__self__
		self.CMD_result[2] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[2],auto_dismiss=False)
		self.CMD_result[2] = self.CMD_result[2].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__

		self.Crafts_List_Page_Result = {}
		self.Crafts_List_Page_btn_give = {}
		self.Crafts_List_Page_MSG_Details = {}
		self.Crafts_List_Page_btn_use = {}
		self.Crafts_List_Page_btn_drop = {}
		self.Crafts_List_Page_btn_send = {}
		self.Craft_Details = {}
		self.Crafts_List_Page_btn_CL = {}
		i = 0
		if result != False or result != None or result != '' or result.upper() != 'NULL' or result != {} or result != '{}' :
			for Item, Item_Data in result.items():
				if Item == '' or 'item' not in Item_Data.keys():
					continue
				if Item_Data['item_class'].upper() in ['RW','W']:
					scolor = 'fg_lred'
					bcolor = 'fg_lred'
				elif Item_Data['item_class'].upper() in ['AMMO']:
					scolor = 'fg_dred'
					bcolor = 'fg_dred'
				elif Item_Data['item_class'].upper() == 'P':
					scolor = 'fg_orange'
					bcolor = 'fg_dorange'
				elif Item_Data['item_class'].upper() in ['PG']:
					scolor = 'fg_gold'
					bcolor = 'fg_gold'
				elif Item_Data['item_class'].upper() in ['WK', 'K']:
					scolor = 'fg_lbrown'
					bcolor = 'fg_lbrown'
				elif Item_Data['item_class'].upper() in ['WM', 'PF']:
					scolor = 'fg_lgold'
					bcolor = 'fg_lgold'
				elif Item_Data['item_class'].upper() in ['TD']:
					scolor = 'fg_lyellow'
					bcolor = 'fg_dyellow'
				elif Item_Data['item_class'].upper() in ['CR','SB' ]:
					scolor = 'fg_white'
					bcolor = 'fg_white'
				elif Item_Data['item_class'].upper() in ['CI']:
					scolor = 'fg_lgreen'
					bcolor = 'fg_dgreen'
				elif Item_Data['item_class'].upper() in ['A','PANTS','BOOTS','GLOVES','BRACERS']:
					scolor = 'fg_dcyan'
					bcolor = 'fg_dblue'
				elif Item_Data['item_class'].upper() in ['MW','RING_RIGHT','RING_LEFT','NECKLACE','GLASSES']:
					scolor = 'fg_lred'
					bcolor = 'fg_lred'					
				else:
					scolor = 'fg_lgreen'	
					bcolor = 'fg_dgreen'

				self.Craft_Details[i] = self.pm('Craft : {0}\nCrafted Item : {1}\nClass: {2}\nValue:\n {3}\nDescription: {4}'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_name'],4,20),self.split_lines(Item_Data['item_class'],4,20),self.split_lines(Item_Data['item_value'],4,20),self.split_lines(Item_Data['item_description'],4,20)),scolor)
				self.Crafts_List_Page_Result[i] = GridLayout(cols=5, size_hint_y=None, size=(Window.width * .9, Window.height * .25))
				self.Crafts_List_Page_MSG_Details[i] = Label(text=self.pm('Craft : {0}\nCrafted Item : {1}\nClass: {2}\nValue:\n {3}'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_name'],4,20),self.split_lines(Item_Data['item_class'],4,20),self.split_lines(Item_Data['item_value'],4,20)),scolor),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
				self.Crafts_List_Page_MSG_Details[i] = self.Crafts_List_Page_MSG_Details[i].__self__
				self.Crafts_List_Page_Result[i].add_widget(self.Crafts_List_Page_MSG_Details[i])
				self.Crafts_List_Page_btn_send[i] = Button(text=self.pm("Craft\n Item",bcolor),markup=True, size_hint = (.2,1.5))
				self.Crafts_List_Page_btn_send[i].bind(on_press=lambda *Args,litem=Item: self.Execute_API_SM('craft {}'.format(litem)))
				self.Crafts_List_Page_btn_send[i] = self.Crafts_List_Page_btn_send[i].__self__
				self.Crafts_List_Page_Result[i].add_widget(self.Crafts_List_Page_btn_send[i])
				self.Crafts_List_Page_btn_CL[i] = Button(text=self.pm("Craft\nDetails",'fg_yellow'),markup=True, size_hint = (.2,1.5))
				self.Crafts_List_Page_btn_CL[i].bind(on_press=lambda *Args,details='Details for {}'.format,craft=self.Craft_Details[i],backone=True: self.result_PopUP(details,craft,backone=backone))								
				self.Crafts_List_Page_Result[i].add_widget(self.Crafts_List_Page_btn_CL[i])
				if (scroll_height < (Window.height / 2)):
					scroll_height = scroll_height + 120
				i += 1

		Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
		Main_result.bind(minimum_height = Main_result.setter('height'))
		Main_result = Main_result.__self__
		for x in range(0,i):
			Main_result.add_widget(self.Crafts_List_Page_Result[x])

		scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[2].height - 30), size = (Window.width, scroll_height)) 
		#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
		scrlFBtns.add_widget(Main_result)
		self.result_layout3[2].add_widget(scrlFBtns)
		# lblmain = Label(text = 'List of your Orders', halign = 'center', y = (Window.height - 10), width = Window.width,size=(2,.15), color = (1,1,1,1))
		self.result_layout[2].add_widget(self.MDD_Layout[2])
		self.result_layout[2].add_widget(self.result_layout4[2])
		# self.result_layout[2].add_widget(lblmain)
		self.result_layout[2].add_widget(self.result_layout3[2])
		self.result_layout2[2].add_widget(back)
		self.result_layout[2].add_widget(self.result_layout2[2])

		self.CMD_result[2].open()

	def PopUP_List_Inv(self,func,result):
		self.Dismiss_One(1)
		##print(result)
		self.Play_Sound('Inventory')
		self.Dismiss_All()
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[3] =  GridLayout(rows=7, size_hint_y=None, size=(Window.width * .7, Window.height))
		self.result_layout[3] = self.result_layout[3].__self__
		self.result_layout[3].bind(height = self.result_layout[3].setter('top'))
		self.result_layout4[3] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout4[3] = self.result_layout4[3].__self__
		self.result_layout4[3].bind(height = self.result_layout[3].setter('top'))
		self.result_layout4[3].add_widget(result_Mar_MUDLogo)
		self.result_layout3[3] = GridLayout(cols=2, size_hint_y=None, size=(Window.width - 10, Window.height * .55))
		self.result_layout3[3] = self.result_layout3[3].__self__
		self.result_layout2[3] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[3] = self.result_layout2[3].__self__
		self.CMD_result[3] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[3],auto_dismiss=False)
		self.CMD_result[3] = self.CMD_result[3].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__

		self.Inv_List_Page_Result = {}
		self.Inv_List_Page_btn_give = {}
		self.Inv_List_Page_MSG_Details = {}
		self.Inv_List_Page_btn_use = {}
		self.Inv_List_Page_btn_drop = {}
		self.Inv_List_Page_btn_send = {}
		self.Inv_List_Page_btn_CL = {}
		self.Item_D = self.Item_B = {}
		

		i = 0
		if result != False:
			for Item, Item_Data in result.items():
				if Item == '':
					continue
				if 'Req_LVL' not in Item_Data.keys():
					Item_Data['Req_LVL'] = '1'
				if 'count' not in Item_Data.keys():
					Item_Data['count'] = '1'
				if Item_Data['item_class'].upper() in ['RW','W']:
					scolor = 'fg_lred'
					bcolor = 'fg_lred'
				elif Item_Data['item_class'].upper() in ['AMMO']:
					scolor = 'fg_dred'
					bcolor = 'fg_dred'
				elif Item_Data['item_class'].upper() == 'P':
					scolor = 'fg_orange'
					bcolor = 'fg_dorange'
				elif Item_Data['item_class'].upper() in ['PG']:
					scolor = 'fg_gold'
					bcolor = 'fg_gold'
				elif Item_Data['item_class'].upper() in ['WK', 'K']:
					scolor = 'fg_lbrown'
					bcolor = 'fg_lbrown'
				elif Item_Data['item_class'].upper() in ['WM', 'PF']:
					scolor = 'fg_lgold'
					bcolor = 'fg_lgold'
				elif Item_Data['item_class'].upper() in ['TD']:
					scolor = 'fg_lyellow'
					bcolor = 'fg_dyellow'
				elif Item_Data['item_class'].upper() in ['CR','SB' ]:
					scolor = 'fg_white'
					bcolor = 'fg_white'
				elif Item_Data['item_class'].upper() in ['CI']:
					scolor = 'fg_lgreen'
					bcolor = 'fg_dgreen'
				elif Item_Data['item_class'].upper() in ['A','PANTS','BOOTS','GLOVES','BRACERS']:
					scolor = 'fg_dcyan'
					bcolor = 'fg_dblue'
				elif Item_Data['item_class'].upper() in ['MW','RING_RIGHT','RING_LEFT','NECKLACE','GLASSES']:
					scolor = 'fg_lred'
					bcolor = 'fg_lred'					
				else:
					scolor = 'fg_lgreen'	
					bcolor = 'fg_dgreen'

				self.Inv_List_Page_Result[i] = GridLayout(cols=6,size_hint_y=None, size=(Window.width * .9, Window.height * .25))
				self.Item_D[i] = self.pm('Item : {0}\nClass: {1}\nValue: {3}\n Level Req: {4}\n Count:{5}\nDescription: {2}'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_class'],4,20),self.split_lines(Item_Data['item_value'],4,20),self.split_lines(Item_Data['item_description'],4,20),self.split_lines(Item_Data['Req_LVL'],4,20),self.split_lines(Item_Data['count'],4,20),self.split_lines(Item_Data['Req_LVL'],4,20),self.split_lines(Item_Data['count'],4,20)),scolor)
				self.Item_B[i] = self.pm('Item : {0}\nClass: {1}\nValue: {2}\n Level Req: {3}\n Count:{4}'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_class'],4,20),self.split_lines(Item_Data['item_value'],4,20),self.split_lines(Item_Data['Req_LVL'],4,20),self.split_lines(Item_Data['count'],4,20)),scolor)
				self.Inv_List_Page_MSG_Details[i] = Label(text=self.Item_B[i],halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
				self.Inv_List_Page_MSG_Details[i] = self.Inv_List_Page_MSG_Details[i].__self__
				self.Inv_List_Page_btn_give[i] = Button(text=self.pm("Give\n Item",'fg_cyan'),markup=True, size_hint = (.2,1.5))
				self.Inv_List_Page_btn_give[i].bind(on_press=lambda *Args,litem=Item: self.PopUp_Give_Item('Give Items.',litem))
				self.Inv_List_Page_btn_send[i] = Button(text=self.pm("Send\n Item",'fg_cyan'),markup=True, size_hint = (.2,1.5))
				self.Inv_List_Page_btn_send[i].bind(on_press=lambda *Args,litem=Item: self.PopUp_Send_Item('Send Items.',litem))
				self.Inv_List_Page_btn_send[i] = self.Inv_List_Page_btn_send[i].__self__
				self.Inv_List_Page_btn_use[i] = Button(text=self.pm("Use",bcolor),markup=True, size_hint = (.2,1.5))
				self.Inv_List_Page_btn_use[i].bind(on_press=lambda *Args,litem='use {}'.format(Item): self.Execute_API_SM(litem))
				self.Inv_List_Page_btn_use[i] = self.Inv_List_Page_btn_use[i].__self__
				self.Inv_List_Page_btn_drop[i] = Button(text=self.pm("Drop",'fg_red'),markup=True, size_hint = (.2,1.5))
				self.Inv_List_Page_btn_drop[i].bind(on_press=lambda *Args,litem='drop {}'.format(Item): self.Execute_API_SM(litem))
				self.Inv_List_Page_btn_drop[i] = self.Inv_List_Page_btn_drop[i].__self__
				self.Inv_List_Page_btn_CL[i] = Button(text=self.pm("Look\nCloser!",'fg_yellow'),markup=True, size_hint = (.2,1.5))
				self.Inv_List_Page_btn_CL[i].bind(on_press=lambda *Args,PItem='Details for item : {}'.format(Item),PItem_Details=self.Item_D[i],backone=True: self.result_PopUP(PItem,PItem_Details,backone))
									
				self.Inv_List_Page_Result[i].add_widget(self.Inv_List_Page_MSG_Details[i])
				self.Inv_List_Page_Result[i].add_widget(self.Inv_List_Page_btn_use[i])
				self.Inv_List_Page_Result[i].add_widget(self.Inv_List_Page_btn_give[i])
				self.Inv_List_Page_Result[i].add_widget(self.Inv_List_Page_btn_send[i])
				self.Inv_List_Page_Result[i].add_widget(self.Inv_List_Page_btn_CL[i])
				self.Inv_List_Page_Result[i].add_widget(self.Inv_List_Page_btn_drop[i])
				if (scroll_height < (Window.height / 2)):
					scroll_height = scroll_height + 120
				i += 1

		Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
		Main_result.bind(minimum_height = Main_result.setter('height'))
		Main_result = Main_result.__self__
		for x in range(0,i):
			Main_result.add_widget(self.Inv_List_Page_Result[x])

		scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[3].height - 30), size = (Window.width, scroll_height)) 
		#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
		scrlFBtns.add_widget(Main_result)
		self.result_layout3[3].add_widget(scrlFBtns)
		# lblmain = Label(text = 'List of your Orders', halign = 'center', y = (Window.height - 10), width = Window.width,size=(2,.15), color = (1,1,1,1))
		self.result_layout[3].add_widget(self.MDD_Layout[2])
		self.result_layout[3].add_widget(self.result_layout4[3])
		# self.result_layout[3].add_widget(lblmain)
		self.result_layout[3].add_widget(self.result_layout3[3])
		self.result_layout2[3].add_widget(back)
		self.result_layout[3].add_widget(self.result_layout2[3])

		self.CMD_result[3].open()

	def PopUP_List_RRLM(self,func,result):
		self.Dismiss_One(1)
		self.Dismiss_All()
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[4] = GridLayout(rows=5, size_hint_y=None, size=(Window.width * .7, Window.height))
		self.result_layout[4] = self.result_layout[4].__self__
		self.result_layout[4].bind(height = self.result_layout[4].setter('top'))
		self.result_layout4[4] = GridLayout(cols=3, size_hint_y=None, size=(Window.width * .7, Window.height * .1))
		self.result_layout4[4] = self.result_layout4[4].__self__
		self.result_layout4[4].bind(height = self.result_layout[4].setter('top'))
		self.result_layout4[4].add_widget(result_Mar_MUDLogo)
		self.result_layoutloc = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layoutloc = self.result_layoutloc.__self__
		self.result_layout3[4] = GridLayout(cols=4, size_hint_y=None, size=(Window.width - 10, Window.height * .35))
		self.result_layout3[4] = self.result_layout3[4].__self__
		self.result_layout2[4] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[4] = self.result_layout2[4].__self__
		self.CMD_result[4] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[4],auto_dismiss=False)
		self.CMD_result[4] = self.CMD_result[4].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		
		Reg_Page_Target_Input_D = TextInput(hint_text='D:{}'.format(self.Char_POS[0]),text='', multiline=False)
		Reg_Page_Target_Input_D = Reg_Page_Target_Input_D.__self__
		Reg_Page_Target_Input_D.bind(text=self.on_rrsmD)
		Reg_Page_Target_Input_D.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_Z = TextInput(hint_text='Z:{}'.format(self.Char_POS[1]),text='', multiline=False)
		Reg_Page_Target_Input_Z = Reg_Page_Target_Input_Z.__self__
		Reg_Page_Target_Input_Z.bind(text=self.on_rrsmZ)
		Reg_Page_Target_Input_Z.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_X = TextInput(hint_text='X:{}'.format(self.Char_POS[2]),text='', multiline=False)
		Reg_Page_Target_Input_X = Reg_Page_Target_Input_X.__self__
		Reg_Page_Target_Input_X.bind(text=self.on_rrsmX)
		Reg_Page_Target_Input_X.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_Y = TextInput(hint_text='Y:{}'.format(self.Char_POS[3]),text='', multiline=False)
		Reg_Page_Target_Input_Y = Reg_Page_Target_Input_Y.__self__
		Reg_Page_Target_Input_Y.bind(text=self.on_rrsmY)
		Reg_Page_Target_Input_Y.bind(on_touch_down=self.hint_clear)

		self.result_layoutloc.add_widget(Reg_Page_Target_Input_D)
		self.result_layoutloc.add_widget(Reg_Page_Target_Input_Z)
		self.result_layoutloc.add_widget(Reg_Page_Target_Input_X)
		self.result_layoutloc.add_widget(Reg_Page_Target_Input_Y)



		self.RRSM_List_Page_Result = {}
		self.RRSM_List_Page_MSG_Details = {}
		self.RRSM_List_Page_btn_spawn = {}
		self.RRSM_List_Page_btn_CL = {}
		self.Monster_D = {}

		i = 0
		if result != False and result != '' and result != '{}' and result != {}:
			for _type, Monsters in json.loads(result).items():
				#print(_type)
				for Monster, Monster_Data in Monsters.items():
					if Monster == '':
						continue
					self.RRSM_List_Page_Result[i] = GridLayout(cols=3, size_hint_y=None, size=(Window.width * .9, Window.height * .25))
					self.Monster_D[i] = 'IMonster: {0}\nStats: {1}\nDescription:\n  {2}'.format(self.split_lines(Monster,4,20),self.split_lines(Monster_Data['stats'],4,20),self.split_lines(Monster_Data['description'],4,20))
					self.RRSM_List_Page_MSG_Details[i] = Label(text='IMonster: {0}\nStats: {1}\n'.format(self.split_lines(Monster,4,20),self.split_lines(Monster_Data['stats'],4,20)),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
					self.RRSM_List_Page_MSG_Details[i] = self.RRSM_List_Page_MSG_Details[i].__self__
					self.RRSM_List_Page_btn_spawn[i] = Button(text=self.pm("R.O.S.I.E\nSpawn\nMonster",'fg_magenta'),markup=True, size_hint = (.2,1.5))
					self.RRSM_List_Page_btn_spawn[i].bind(on_press=lambda *Args,lmonster=Monster: self.API_ROSIE_SM(self.username,self.password,lmonster,api_key))
					self.RRSM_List_Page_btn_CL[i] = Button(text=self.pm("Look\nCloser!",'fg_yellow'),markup=True, size_hint = (.2,1.5))
					self.RRSM_List_Page_btn_CL[i].bind(on_press=lambda *Args,PItem='Details for Monster : {}'.format(Monster),PItem_Details=self.Monster_D[i],backone=True: self.result_PopUP(PItem,PItem_Details,backone=backone))

					self.RRSM_List_Page_Result[i].add_widget(self.RRSM_List_Page_MSG_Details[i])
					self.RRSM_List_Page_Result[i].add_widget(self.RRSM_List_Page_btn_spawn[i])
					self.RRSM_List_Page_Result[i].add_widget(self.RRSM_List_Page_btn_CL[i])
					
					if (scroll_height < (Window.height / 2)):
						scroll_height = scroll_height + 120
					i += 1

			Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
			Main_result.bind(minimum_height = Main_result.setter('height'))
			Main_result = Main_result.__self__
			for x in range(0,i):
				Main_result.add_widget(self.RRSM_List_Page_Result[x])

			scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[4].height - 30), size = (Window.width, scroll_height)) 
			#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
			scrlFBtns.add_widget(Main_result)
			self.result_layout3[4].add_widget(scrlFBtns)
		self.result_layout[4].add_widget(self.MDD_Layout[2])
		self.result_layout[4].add_widget(self.result_layout4[4])
		self.result_layout[4].add_widget(self.result_layout3[4])
		self.result_layout[4].add_widget(self.result_layoutloc)
		self.result_layout2[4].add_widget(back)
		self.result_layout[4].add_widget(self.result_layout2[4])

		self.CMD_result[4].open()


	def PopUP_List_RRGI(self,func,result):
		self.Dismiss_All()
		self.Dismiss_One(1)
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[5] =  GridLayout(rows=4)
		self.result_layout[5].bind(height = self.result_layout[5].setter('top'))
		self.result_layout[5] = self.result_layout[5].__self__
		self.result_layout[5].bind(height = self.result_layout[5].setter('top'))
		self.result_layout4[5] = GridLayout(cols=3, size_hint_y=None, size=(Window.width * .7, Window.height * .1))
		self.result_layout4[5] = self.result_layout4[5].__self__
		self.result_layout4[5].bind(height = self.result_layout[5].setter('top'))
		self.result_layout4[5].add_widget(result_Mar_MUDLogo)
		self.result_layout3[5] = BoxLayout(padding=3, orientation='vertical',size_hint=(Window.width - 10, Window.height * .7),size=(Window.width - 10, Window.height * .45))
		self.result_layout3[5] = self.result_layout3[5].__self__
		self.result_layout2[5] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[5] = self.result_layout2[5].__self__
		self.CMD_result[5] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[5],auto_dismiss=False)
		self.CMD_result[5] = self.CMD_result[5].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__

		self.RRGI_List_Page_Result = {}
		self.RRGI_List_Page_btn_give = {}
		self.RRGI_List_Page_MSG_Details = {}
		self.RRGI_List_Page_btn_use = {}
		self.RRGI_List_Page_btn_drop = {}
		self.RRGI_List_Page_btn_send = {}
		self.RRGI_List_Page_btn_CL = {}
		self.RRGI_Item_D = {}
		

		i = 0
		if result != False and result != '' and result != '{}' and result != {}:
			for _type, Items in json.loads(result).items():
				for Item, Item_Data in Items.items():
					if Item == '' or Item == None:
						continue
					if Item_Data['item_class'].upper() in ['RW','W']:
						scolor = 'fg_lred'
						bcolor = 'fg_lred'
					elif Item_Data['item_class'].upper() in ['AMMO']:
						scolor = 'fg_dred'
						bcolor = 'fg_dred'
					elif Item_Data['item_class'].upper() == 'P':
						scolor = 'fg_orange'
						bcolor = 'fg_dorange'
					elif Item_Data['item_class'].upper() in ['PG']:
						scolor = 'fg_gold'
						bcolor = 'fg_gold'
					elif Item_Data['item_class'].upper() in ['WK', 'K']:
						scolor = 'fg_lbrown'
						bcolor = 'fg_lbrown'
					elif Item_Data['item_class'].upper() in ['WM', 'PF']:
						scolor = 'fg_lgold'
						bcolor = 'fg_lgold'
					elif Item_Data['item_class'].upper() in ['TD']:
						scolor = 'fg_lyellow'
						bcolor = 'fg_dyellow'
					elif Item_Data['item_class'].upper() in ['CR','SB' ]:
						scolor = 'fg_white'
						bcolor = 'fg_white'
					elif Item_Data['item_class'].upper() in ['CI']:
						scolor = 'fg_lgreen'
						bcolor = 'fg_dgreen'
					elif Item_Data['item_class'].upper() in ['A','PANTS','BOOTS','GLOVES','BRACERS']:
						scolor = 'fg_dcyan'
						bcolor = 'fg_dblue'
					elif Item_Data['item_class'].upper() in ['MW','RING_RIGHT','RING_LEFT','NECKLACE','GLASSES']:
						scolor = 'fg_lred'
						bcolor = 'fg_lred'					
					else:
						scolor = 'fg_lgreen'
						bcolor = 'fg_dgreen'

					self.RRGI_List_Page_Result[i] = GridLayout(cols=5, size_hint_y=None, size=(Window.width * .9, Window.height * .25))
					self.RRGI_Item_D[i] = self.pm('Item : {0}\nClass: {1}\nDescription:\n  {2}\nValue: {3}'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_class'],4,20),self.split_lines(Item_Data['item_value'],4,20),self.split_lines(Item_Data['item_description'],4,20)),scolor)
					self.RRGI_List_Page_MSG_Details[i] = Label(text=self.pm('Item : {0}\nClass: {1}\nValue: {2}'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_class'],4,20),self.split_lines(Item_Data['item_value'],4,20)),scolor),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))
					self.RRGI_List_Page_MSG_Details[i] = self.RRGI_List_Page_MSG_Details[i].__self__
					self.RRGI_List_Page_btn_give[i] = Button(text=self.pm("Give\n Item",'fg_magenta'),markup=True, size_hint = (.2,1.5))
					self.RRGI_List_Page_btn_give[i].bind(on_press=lambda *Args,litem=Item: self.API_ROSIE_GI(self.username,self.password,litem,api_key))
					self.RRGI_List_Page_btn_send[i] = Button(text=self.pm("Send\n Item",'fg_magenta'),markup=True, size_hint = (.2,1.5))
					self.RRGI_List_Page_btn_send[i].bind(on_press=lambda *Args,litem=Item: self.PopUp_RRSI('Frank Corps R.O.S.I.E. Item Generate and send menu',litem))
					self.RRGI_List_Page_btn_CL[i] = Button(text=self.pm("Item Details",'fg_yellow'),markup=True, size_hint = (.2,1.5))
					self.RRGI_List_Page_btn_CL[i].bind(on_press=lambda *Args,PItem='Details for item : {}'.format(Item),PItem_Details=self.RRGI_Item_D[i],backone=True: self.result_PopUP(PItem,PItem_Details,backone=backone))


					self.RRGI_List_Page_Result[i].add_widget(self.RRGI_List_Page_MSG_Details[i])			
					self.RRGI_List_Page_Result[i].add_widget(self.RRGI_List_Page_btn_give[i])
					self.RRGI_List_Page_Result[i].add_widget(self.RRGI_List_Page_btn_send[i])
					self.RRGI_List_Page_Result[i].add_widget(self.RRGI_List_Page_btn_CL[i])
					if (scroll_height < (Window.height / 2)):
						scroll_height = scroll_height + 120
					i += 1
			if len(self.RRGI_List_Page_Result) == i:
				Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
				Main_result.bind(minimum_height = Main_result.setter('height'))
				Main_result = Main_result.__self__
				for x in range(0,i):
					Main_result.add_widget(self.RRGI_List_Page_Result[x])

				scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[5].height - 30), size = (Window.width, scroll_height)) 
				#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
				scrlFBtns.add_widget(Main_result)
				self.result_layout3[5].add_widget(scrlFBtns)
		# lblmain = Label(text = 'List of your Orders', halign = 'center', y = (Window.height - 10), width = Window.width,size=(2,.15), color = (1,1,1,1))
		self.result_layout[5].add_widget(self.MDD_Layout[2])
		self.result_layout[5].add_widget(self.result_layout4[5])
		# self.result_layout[5].add_widget(lblmain)
		self.result_layout[5].add_widget(self.result_layout3[5])
		self.result_layout2[5].add_widget(back)
		self.result_layout[5].add_widget(self.result_layout2[5])

		self.CMD_result[5].open()

	def PopUp_Give_Item(self,func,result):
		self.Dismiss_All()
		self.GItem = result
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[6] =  GridLayout(rows=4)
		self.result_layout[6].bind(height = self.result_layout[6].setter('top'))
		self.result_layout[6] = self.result_layout[6].__self__
		self.result_layout[6].bind(height = self.result_layout[6].setter('top'))
		self.result_layout4[6] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .3))
		self.result_layout4[6] = self.result_layout4[6].__self__
		self.result_layout4[6].bind(height = self.result_layout[6].setter('top'))
		self.result_layout4[6].add_widget(result_Mar_MUDLogo)
		self.result_layout3[6] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout3[6] = self.result_layout3[6].__self__
		self.result_layout2[6] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[6] = self.result_layout2[6].__self__
		self.CMD_result[6] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[6],auto_dismiss=False)
		self.CMD_result[6] = self.CMD_result[6].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		send = Button(text=self.pm('Send','fg_green'),markup=True,size_hint = (1,3))
		send.bind(on_press=lambda *Args,Target=self.STarget,Item=result: self.Execute_API_SM('auto give'))
		send = send.__self__
		Reg_Page_Target_Input = TextInput(hint_text='Recipients Username :',text='', multiline=False)
		Reg_Page_Target_Input.bind(text=self.on_target)
		Reg_Page_Target_Input.bind(on_touch_down=self.hint_clear)

		self.result_layout[6].add_widget(self.MDD_Layout[2])
		self.result_layout[6].add_widget(self.result_layout3[6])
		self.result_layout[6].add_widget(self.result_layout4[6])
		self.result_layout2[6].add_widget(back)
		self.result_layout2[6].add_widget(send)
		self.result_layout3[6].add_widget(Reg_Page_Target_Input)
		self.result_layout[6].add_widget(self.result_layout2[6])

		self.CMD_result[6].open()
		
	def PopUp_Send_Item(self,func,result):
		self.Dismiss_All()
		self.GItem = result.rstrip().lstrip().lower()
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[7] =  GridLayout(rows=4)
		self.result_layout[7].bind(height = self.result_layout[7].setter('top'))
		self.result_layout[7] = self.result_layout[7].__self__
		self.result_layout[7].bind(height = self.result_layout[7].setter('top'))
		self.result_layout4[7] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .35))
		self.result_layout4[7] = self.result_layout4[7].__self__
		self.result_layout4[7].bind(height = self.result_layout[7].setter('top'))
		self.result_layout4[7].add_widget(result_Mar_MUDLogo)
		self.result_layout3[7] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout3[7] = self.result_layout3[7].__self__
		self.result_layout2[7] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[7] = self.result_layout2[7].__self__
		self.CMD_result[7] = Popup(title='Send an item to Player below.', content=self.result_layout[7],auto_dismiss=False)
		self.CMD_result[7] = self.CMD_result[7].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		send = Button(text=self.pm('Send','fg_green'),markup=True,size_hint = (1,3))
		send.bind(on_press=lambda *Args,Target=self.STarget,Item=result: self.Execute_API_SM('auto send item'))
		send = send.__self__
		Reg_Page_Target_Input = TextInput(hint_text='Recipients Username :',text='', multiline=False)
		Reg_Page_Target_Input.bind(text=self.on_target)
		Reg_Page_Target_Input.bind(on_touch_down=self.hint_clear)
		
		self.result_layout[7].add_widget(self.MDD_Layout[2])
		self.result_layout[7].add_widget(self.result_layout3[7])
		self.result_layout[7].add_widget(self.result_layout4[7])
		self.result_layout2[7].add_widget(back)
		self.result_layout2[7].add_widget(send)
		self.result_layout3[7].add_widget(Reg_Page_Target_Input)
		self.result_layout[7].add_widget(self.result_layout2[7])

		self.CMD_result[7].open()

	def PopUp_RRSI(self,func,result):
		self.Dismiss_All()
		self.SItem = result
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[8] =  GridLayout(rows=4)
		self.result_layout[8].bind(height = self.result_layout[8].setter('top'))
		self.result_layout[8] = self.result_layout[8].__self__
		self.result_layout[8].bind(height = self.result_layout[8].setter('top'))
		self.result_layout4[8] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .35))
		self.result_layout4[8] = self.result_layout4[8].__self__
		self.result_layout4[8].bind(height = self.result_layout[8].setter('top'))
		self.result_layout4[8].add_widget(result_Mar_MUDLogo)
		self.result_layout3[8] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout3[8] = self.result_layout3[8].__self__
		self.result_layout2[8] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[8] = self.result_layout2[8].__self__
		self.CMD_result[8] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[8],auto_dismiss=False)
		self.CMD_result[8] = self.CMD_result[8].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		send = Button(text=self.pm('Send','fg_green'),markup=True,size_hint = (1,3))
		send.bind(on_press=lambda *Args,Target=self.STarget,Item=result: self.API_ROSIE_SI(self.username,self.password,Target,Item,api_key))
		send = send.__self__
		Reg_Page_Target_Input = TextInput(hint_text='Recipients Username :',text='', multiline=False)
		Reg_Page_Target_Input.bind(text=self.on_target)
		Reg_Page_Target_Input.bind(on_touch_down=self.hint_clear)

		self.result_layout3[8].add_widget(Reg_Page_Target_Input)
		self.result_layout[8].add_widget(self.MDD_Layout[2])
		self.result_layout[8].add_widget(self.result_layout3[8])
		self.result_layout[8].add_widget(self.result_layout4[8])
		self.result_layout2[8].add_widget(back)
		self.result_layout2[8].add_widget(send)
		self.result_layout[8].add_widget(self.result_layout2[8])

		self.CMD_result[8].open()

	def PopUp_Send_Invite(self,func,result):		
		self.Dismiss_All()
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[9] =  GridLayout(rows=4)
		self.result_layout[9].bind(height = self.result_layout[9].setter('top'))
		self.result_layout[9] = self.result_layout[9].__self__
		self.result_layout[9].bind(height = self.result_layout[9].setter('top'))
		self.result_layout4[9] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .35))
		self.result_layout4[9] = self.result_layout4[9].__self__
		self.result_layout4[9].bind(height = self.result_layout[9].setter('top'))
		self.result_layout4[9].add_widget(result_Mar_MUDLogo)
		self.result_layout3[9] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout3[9] = self.result_layout3[9].__self__
		self.result_layout2[9] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .1))
		self.result_layout2[9] = self.result_layout2[9].__self__

		self.CMD_result[9] = Popup(title='Send an invite to Player below.'.format(func), content=self.result_layout[9],auto_dismiss=False)
		self.CMD_result[9] = self.CMD_result[9].__self__

		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__

		send = Button(text=self.pm('Send','fg_green'),markup=True,size_hint = (1,3))
		send.bind(on_press=lambda *Args: self.Execute_API_SM('auto send invite'))
		send = send.__self__

		Reg_Page_Target_Input = TextInput(hint_text='Recipients Username :',text='', multiline=False)
		Reg_Page_Target_Input.bind(text=self.on_target)
		Reg_Page_Target_Input.bind(on_touch_down=self.hint_clear)

		self.result_layout[9].add_widget(self.MDD_Layout[2])
		self.result_layout3[9].add_widget(Reg_Page_Target_Input)
		self.result_layout[9].add_widget(self.result_layout4[9])
		self.result_layout2[9].add_widget(back)
		self.result_layout2[9].add_widget(send)
		self.result_layout[9].add_widget(self.result_layout2[9])
		self.result_layout[9].add_widget(self.result_layout3[9])

		self.CMD_result[9].open()

	def result_PopUP_Read_PMSGs(self,func,result):
		##print(result)
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[10] =  GridLayout(rows=5)
		self.result_layout[10] = self.result_layout[10].__self__
		self.result_layout[10].bind(height = self.result_layout[10].setter('top'))
		self.result_layout4[10] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .7, Window.height * .1))
		self.result_layout4[10] = self.result_layout4[10].__self__
		self.result_layout4[10].bind(height = self.result_layout[10].setter('top'))
		self.result_layout4[10].add_widget(result_Mar_MUDLogo)
		self.result_layout3[10] = GridLayout(cols=1, size_hint_y=None, size=(Window.width - 10, Window.height * .45))
		self.result_layout3[10] = self.result_layout3[10].__self__
		self.result_layout2[10] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[10] = self.result_layout2[10].__self__
		self.CMD_result[10] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[10],auto_dismiss=False)
		self.CMD_result[10] = self.CMD_result[10].__self__
		delall = Button(text=self.pm('Delete\nAll MSGs','fg_red'),markup=True,size_hint = (1,3))
		delall.bind(on_press=lambda *Args,Indx='all':  self.result_PopUP_Confirm('all messages','',Indx))
		delall = delall.__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=lambda *args,index=10:self.Dismiss_One(index))
		back = back.__self__

		self.PMSGs_Page_Result = {}
		self.PMSGs_Page_btn_delete = {}
		self.PMSGs_Page_MSG_Details = {}
		self.PMSGs_Page_btn_reply = {}
		self.PMSGs_Page_btn_accept = {}
		self.PMSGs_Page_btn_decline = {}
		self.PMSGs_Page_btn_CL = {}
		self.PMSGs_Details = {}

		i = 0
		if result != False:
			for Index, MSG_Data in result.items():
				if Index == '':
					continue
				if len(MSG_Data.keys()) > 0:
					if 'Is_Item' not in MSG_Data or 'Is_Invite' not in MSG_Data:
						continue
					self.PMSGs_Page_Result[i] = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .9, Window.height * .25))
					self.PMSGs_Details[i] = 'Msg# : {0}\nFrom: {1}\nMessage:\n  {2}\nSent: {3}\nRead?: {4}'.format(self.split_lines(Index,4,20),self.split_lines(MSG_Data['Sender'],4,20),self.split_lines(MSG_Data['Message'],4,20),self.split_lines(MSG_Data['Sent'],4,20),self.split_lines(MSG_Data['Read'],4,20))
					self.PMSGs_Page_MSG_Details[i] = Label(text='Msg# : {0}\nFrom: {1}\nSent: {2}\nRead?: {3}'.format(self.split_lines(Index,4,20),self.split_lines(MSG_Data['Sender'],4,20),self.split_lines(MSG_Data['Sent'],4,20),self.split_lines(MSG_Data['Read'],4,20)),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
					self.PMSGs_Page_MSG_Details[i] = self.PMSGs_Page_MSG_Details[i].__self__
					self.PMSGs_Page_Result[i].add_widget(self.PMSGs_Page_MSG_Details[i])
					if MSG_Data['Is_Item'] == True:
						
						self.PMSGs_Page_btn_accept[i] = Button(text=self.pm("Accept \n Item",'fg_green'),markup=True, size_hint = (.2,.8))
						self.PMSGs_Page_btn_accept[i].bind(on_press=lambda *Args,index=str(Index):self.Execute_API_SM('accept item {}'.format(index)))
						self.PMSGs_Page_Result[i].add_widget(self.PMSGs_Page_btn_accept[i])
						
						self.PMSGs_Page_btn_decline[i] = Button(text=self.pm("Decline \n Item",'fg_red'),markup=True, size_hint = (.2,.8))
						self.PMSGs_Page_btn_decline[i].bind(on_press=lambda *Args,index=str(Index):self.API_Phone(self.username,self.password,'dtext',index,'',api_key))
						self.PMSGs_Page_Result[i].add_widget(self.PMSGs_Page_btn_decline[i])

					elif MSG_Data['Is_Invite'] == True:
						
						self.PMSGs_Page_btn_accept[i] = Button(text=self.pm("Accept \n Invite",'fg_green'),markup=True, size_hint = (.2,.8))
						self.PMSGs_Page_btn_accept[i].bind(on_press=lambda *Args,index=str(Index):self.Execute_API_SM('accept invite {}'.format(index)))
						self.PMSGs_Page_Result[i].add_widget(self.PMSGs_Page_btn_accept[i])
						
						self.PMSGs_Page_btn_decline[i] = Button(text=self.pm("Decline\n Item",'fg_red'),markup=True, size_hint = (.2,.8))
						self.PMSGs_Page_btn_decline[i].bind(on_press=lambda *Args,index=str(Index):self.API_Phone(self.username,self.password,'dtext',index,'',api_key))
						self.PMSGs_Page_Result[i].add_widget(self.PMSGs_Page_btn_decline[i])

					else:
						self.PMSGs_Page_btn_CL[i] = Button(text=self.pm("Read",'fg_green'),markup=True, size_hint = (.2,1.5))
						self.PMSGs_Page_btn_CL[i].bind(on_press=lambda *Args,ditem=Index,litem=self.PMSGs_Details[i],backone=True: self.Mark_Read(ditem,litem,backone=backone))
						
						self.PMSGs_Page_btn_reply[i] = Button(text="Reply", size_hint = (.2,.8))
						self.PMSGs_Page_btn_reply[i].bind(on_press=lambda *Args,OPlayer=str(MSG_Data['Sender']):self.result_PopUP_Send_PMSGs('reply',OPlayer))
						self.PMSGs_Page_btn_reply[i] = self.PMSGs_Page_btn_reply[i].__self__
						self.PMSGs_Page_Result[i].add_widget(self.PMSGs_Page_btn_CL[i])						
						self.PMSGs_Page_Result[i].add_widget(self.PMSGs_Page_btn_reply[i])
					
					self.PMSGs_Page_btn_delete[i] = Button(text=self.pm("Delete\nMessage",'fg_red'),markup=True, size_hint = (.2,.8))
					self.PMSGs_Page_btn_delete[i].bind(on_press=lambda *Args,Indx=int(Index): self.result_PopUP_Confirm('all messages','',Indx))
					self.PMSGs_Page_btn_delete[i] = self.PMSGs_Page_btn_delete[i].__self__
					self.PMSGs_Page_Result[i].add_widget(self.PMSGs_Page_btn_delete[i])
				if (scroll_height < (Window.height / 2)):
					scroll_height = scroll_height + 120
				i += 1

		Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
		Main_result.bind(minimum_height = Main_result.setter('height'))
		Main_result = Main_result.__self__
		for x in range(0,i):
			Main_result.add_widget(self.PMSGs_Page_Result[x])

		scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[10].height - 30), size = (Window.width, scroll_height)) 
		#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
		scrlFBtns.add_widget(Main_result)
		self.result_layout[10].add_widget(self.MDD_Layout[2])
		self.result_layout2[10].add_widget(back)
		self.result_layout2[10].add_widget(delall)
			
		self.result_layout3[10].add_widget(scrlFBtns)
		# lblmain = Label(text = 'List of your Orders', halign = 'center', y = (Window.height - 10), width = Window.width,size=(2,.15), color = (1,1,1,1))
		self.result_layout[10].add_widget(self.result_layout4[10])
		# self.result_layout[10].add_widget(lblmain)
		self.result_layout[10].add_widget(self.result_layout3[10])

		self.result_layout[10].add_widget(self.result_layout2[10])

		self.CMD_result[10].open()

	def Mark_Read(self,Index,Litem,backone):
		self.API_Phone(self.username,self.password,'vtext','mread-{}'.format(Index),'',api_key)
		self.Dismiss_One(1)		
		self.result_PopUP('Message {} Details:'.format(Index),Litem,backone=True)

	def result_PopUP_Send_PMSGs(self,func,result):
		self.Dismiss_All()
		if func == 'reply':
			self.STarget = result
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[11] = GridLayout(rows=5, size_hint_y=None, size=(Window.width * .95, Window.height))
		self.result_layout[11] = self.result_layout[11].__self__
		self.result_layout[11].bind(height = self.result_layout[11].setter('top'))
		self.result_layout5[11] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .95, Window.height * .35))
		self.result_layout5[11] = self.result_layout5[11].__self__
		self.result_layout4[11] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .95, Window.height * .35))
		self.result_layout4[11] = self.result_layout4[11].__self__
		self.result_layout4[11].add_widget(result_Mar_MUDLogo)
		self.result_layout3[11] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .95, Window.height * .1))
		self.result_layout3[11] = self.result_layout3[11].__self__
		self.result_layout2[11] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[11] = self.result_layout2[11].__self__
		self.CMD_result[11] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[11],auto_dismiss=False)
		self.CMD_result[11] = self.CMD_result[11].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		send = Button(text=self.pm('Send','fg_green'),markup=True,size_hint = (1,3))
		send.bind(on_press=lambda *Args: self.API_Phone(self.username,self.password,'stext',self.STarget,self.sMSG,api_key))
		send = send.__self__
		if func == 'reply':
			Reg_Page_Target_Input = TextInput(hint_text='',text=result, multiline=False)
		else:
			Reg_Page_Target_Input = TextInput(hint_text='Recipients Username :',text='', multiline=False)
		Reg_Page_Msg_InputReg_Page_Target_Input = Reg_Page_Target_Input.__self__
		
		Reg_Page_Target_Input.bind(text=self.on_target)
		Reg_Page_Target_Input.bind(on_touch_down=self.hint_clear)

		Reg_Page_Msg_Input = TextInput(hint_text='Message Text :',text='', multiline=True)
		Reg_Page_Msg_Input = Reg_Page_Msg_Input.__self__
		
		Reg_Page_Msg_Input.bind(text=self.on_MSG)
		Reg_Page_Msg_Input.bind(on_touch_down=self.hint_clear)
		Reg_Page_Msg_Input.bind(on_text_validate=(lambda *Args: self.API_Phone(self.username,self.password,'stext',self.STarget,self.sMSG,api_key)))

		self.result_layout2[11].add_widget(back)
		self.result_layout2[11].add_widget(send)

		self.result_layout3[11].add_widget(Reg_Page_Target_Input)
		self.result_layout5[11].add_widget(Reg_Page_Msg_Input)

		self.result_layout[11].add_widget(self.MDD_Layout[2])
		self.result_layout[11].add_widget(self.result_layout4[11])
		self.result_layout[11].add_widget(self.result_layout2[11])
		self.result_layout[11].add_widget(self.result_layout3[11])
		self.result_layout[11].add_widget(self.result_layout5[11])

		self.CMD_result[11].open()

	def result_PopUP_Send_Call(self,func,result):
		self.Dismiss_All()
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[12] =  GridLayout(rows=4)
		self.result_layout[12].bind(height = self.result_layout[12].setter('top'))
		self.result_layout[12] = self.result_layout[12].__self__
		self.result_layout[12].bind(height = self.result_layout[12].setter('top'))
		self.result_layout4[12] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .45))
		self.result_layout4[12] = self.result_layout4[12].__self__
		self.result_layout4[12].bind(height = self.result_layout[12].setter('top'))
		self.result_layout4[12].add_widget(result_Mar_MUDLogo)
		self.result_layout3[12] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout3[12] = self.result_layout3[12].__self__
		self.result_layout2[12] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .1))
		self.result_layout2[12] = self.result_layout2[12].__self__
		self.CMD_result[12] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[12],auto_dismiss=False)
		self.CMD_result[12] = self.CMD_result[12].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		send = Button(text=self.pm('Send','fg_green'),markup=True,size_hint = (1,3))
		send.bind(on_press=lambda *Args: self.API_Phone(self.username,self.password,'scall',self.STarget,'',api_key))
		send = send.__self__

		Reg_Page_Target_Input = TextInput(hint_text='Phone Number :',text='', multiline=False)
		Reg_Page_Target_Input = Reg_Page_Target_Input.__self__
		Reg_Page_Target_Input.bind(text=self.on_target)
		Reg_Page_Target_Input.bind(on_touch_down=self.hint_clear)
		Reg_Page_Target_Input.bind(on_text_validate=(lambda *Args: self.API_Phone(self.username,self.password,'scall',self.STarget,'',api_key)))

		self.result_layout3[12].add_widget(Reg_Page_Target_Input)
		self.result_layout2[12].add_widget(back)
		self.result_layout2[12].add_widget(send)
		self.result_layout[12].add_widget(self.MDD_Layout[2])
		self.result_layout[12].add_widget(self.result_layout4[12])
		self.result_layout[12].add_widget(self.result_layout2[12])
		self.result_layout[12].add_widget(self.result_layout3[12])

		self.CMD_result[12].open()

	def result_PopUP_DGPS(self,func,result):
		self.Dismiss_All()
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[13] =  GridLayout(rows=4)
		self.result_layout[13].bind(height = self.result_layout[13].setter('top'))
		self.result_layout[13] = self.result_layout[13].__self__
		self.result_layout[13].bind(height = self.result_layout[13].setter('top'))
		self.result_layout4[13] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .4))
		self.result_layout4[13] = self.result_layout4[13].__self__
		self.result_layout4[13].bind(height = self.result_layout[13].setter('top'))
		self.result_layout4[13].add_widget(result_Mar_MUDLogo)
		self.result_layout3[13] = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .7, Window.height * .15))
		self.result_layout3[13] = self.result_layout3[13].__self__
		self.result_layout2[13] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[13] = self.result_layout2[13].__self__
		self.CMD_result[13] = Popup(title='DGPS Menu', content=self.result_layout[13],auto_dismiss=False)
		self.CMD_result[13] = self.CMD_result[13].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		warp = Button(text=self.pm('Warp','fg_green'),markup=True,size_hint = (1,3))
		warp.bind(on_press=lambda *Args: self.API_DGPS(self.username,self.password,'warp',self.Warp_Location,api_key))
		warp = warp.__self__

		Reg_Page_Target_Input_D = TextInput(hint_text='D:{}'.format(self.Char_POS[0]),text='', multiline=False)
		Reg_Page_Target_Input_D = Reg_Page_Target_Input_D.__self__
		Reg_Page_Target_Input_D.bind(text=self.on_D)
		Reg_Page_Target_Input_D.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_Z = TextInput(hint_text='Z:{}'.format(self.Char_POS[1]),text='', multiline=False)
		Reg_Page_Target_Input_Z = Reg_Page_Target_Input_Z.__self__
		Reg_Page_Target_Input_Z.bind(text=self.on_Z)
		Reg_Page_Target_Input_Z.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_X = TextInput(hint_text='X:{}'.format(self.Char_POS[2]),text='', multiline=False)
		Reg_Page_Target_Input_X = Reg_Page_Target_Input_X.__self__
		Reg_Page_Target_Input_X.bind(text=self.on_X)
		Reg_Page_Target_Input_X.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_Y = TextInput(hint_text='Y:{}'.format(self.Char_POS[3]),text='', multiline=False)
		Reg_Page_Target_Input_Y = Reg_Page_Target_Input_Y.__self__
		Reg_Page_Target_Input_Y.bind(text=self.on_Y)
		Reg_Page_Target_Input_Y.bind(on_touch_down=self.hint_clear)
		Reg_Page_Target_Input_Y.bind(on_text_validate=self.onWarpLocation)
		self.result_layout[13].add_widget(self.MDD_Layout[2])
		self.result_layout3[13].add_widget(Reg_Page_Target_Input_D)
		self.result_layout3[13].add_widget(Reg_Page_Target_Input_Z)
		self.result_layout3[13].add_widget(Reg_Page_Target_Input_X)
		self.result_layout3[13].add_widget(Reg_Page_Target_Input_Y)
		self.result_layout[13].add_widget(self.result_layout4[13])
		self.result_layout[13].add_widget(self.result_layout3[13])
		self.result_layout2[13].add_widget(back)
		self.result_layout2[13].add_widget(warp)
		self.result_layout[13].add_widget(self.result_layout2[13])

		self.CMD_result[13].open()

	def result_PopUP_aDGPS(self,func,result):
		# self.Dismiss_All()
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[14] =  GridLayout(rows=4, size_hint_y=None, size=(Window.width * .7, Window.height))
		self.result_layout[14].bind(height = self.result_layout[14].setter('top'))
		self.result_layout[14] = self.result_layout[14].__self__
		self.result_layout[14].bind(height = self.result_layout[14].setter('top'))
		self.result_layout4[14] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .35))
		self.result_layout4[14] = self.result_layout4[14].__self__
		self.result_layout4[14].bind(height = self.result_layout[14].setter('top'))
		self.result_layout4[14].add_widget(result_Mar_MUDLogo)
		self.result_layout3[14] = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout3[14] = self.result_layout3[14].__self__
		self.result_layout2[14] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[14] = self.result_layout2[14].__self__
		self.CMD_result[14] = Popup(title='ROSIE Admin DGPS Menu'.format(func), content=self.result_layout[14],auto_dismiss=False)
		self.CMD_result[14] = self.CMD_result[14].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		warp = Button(text='Send',size_hint = (1,3))
		warp.bind(on_press=lambda *Args: self.API_aDGPS(self.username,self.password,'awarp',self.Warp_Location,api_key))
		warp = warp.__self__

		Reg_Page_Target_Input_D = TextInput(hint_text='D:{}'.format(self.Char_POS[0]),text='', multiline=False)
		Reg_Page_Target_Input_D = Reg_Page_Target_Input_D.__self__
		Reg_Page_Target_Input_D.bind(text=self.on_D)
		Reg_Page_Target_Input_D.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_Z = TextInput(hint_text='Z:{}'.format(self.Char_POS[1]),text='', multiline=False)
		Reg_Page_Target_Input_Z = Reg_Page_Target_Input_Z.__self__
		Reg_Page_Target_Input_Z.bind(text=self.on_Z)
		Reg_Page_Target_Input_Z.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_X = TextInput(hint_text='X:{}'.format(self.Char_POS[2]),text='', multiline=False)
		Reg_Page_Target_Input_X = Reg_Page_Target_Input_X.__self__
		Reg_Page_Target_Input_X.bind(text=self.on_X)
		Reg_Page_Target_Input_X.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_Y = TextInput(hint_text='Y:{}'.format(self.Char_POS[3]),text='', multiline=False)
		Reg_Page_Target_Input_Y = Reg_Page_Target_Input_Y.__self__
		Reg_Page_Target_Input_Y.bind(text=self.on_Y)
		Reg_Page_Target_Input_Y.bind(on_touch_down=self.hint_clear)
		Reg_Page_Target_Input_Y.bind(on_text_validate=self.onaWarpLocation)
		
		self.result_layout3[14].add_widget(Reg_Page_Target_Input_D)
		self.result_layout3[14].add_widget(Reg_Page_Target_Input_Z)
		self.result_layout3[14].add_widget(Reg_Page_Target_Input_X)
		self.result_layout3[14].add_widget(Reg_Page_Target_Input_Y)

		self.result_layout2[14].add_widget(back)
		self.result_layout2[14].add_widget(warp)

		self.result_layout[14].add_widget(self.MDD_Layout[2])
		self.result_layout[14].add_widget(self.result_layout4[14])
		self.result_layout[14].add_widget(self.result_layout3[14])
		self.result_layout[14].add_widget(self.result_layout2[14])

		self.CMD_result[14].open()


	def PopUP_List_RRLC(self,func,result):
		self.Dismiss_All()
		self.Dismiss_One(1)
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[15] = GridLayout(rows=4, size_hint_y=None, size=(Window.width * .7, Window.height))
		self.result_layout[15] = self.result_layout[15].__self__
		self.result_layout[15].bind(height = self.result_layout[15].setter('top'))
		self.result_layout4[15] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout4[15] = self.result_layout4[15].__self__
		self.result_layout4[15].bind(height = self.result_layout[15].setter('top'))
		self.result_layout4[15].add_widget(result_Mar_MUDLogo)
		self.result_layoutloc = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layoutloc = self.result_layoutloc.__self__
		self.result_layout3[15] = BoxLayout(padding=3, orientation='vertical',size_hint=(Window.width - 10, Window.height * .7),size=(Window.width - 10, Window.height * .55))
		self.result_layout3[15] = self.result_layout3[15].__self__
		self.result_layout2[15] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[15] = self.result_layout2[15].__self__
		self.CMD_result[15] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[15],auto_dismiss=False)
		self.CMD_result[15] = self.CMD_result[15].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		
		Reg_Page_Target_Input_D = TextInput(hint_text='D:{}'.format(self.Char_POS[0]),text='', multiline=False)
		Reg_Page_Target_Input_D = Reg_Page_Target_Input_D.__self__
		Reg_Page_Target_Input_D.bind(text=self.on_rrsmD)
		Reg_Page_Target_Input_D.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_Z = TextInput(hint_text='Z:{}'.format(self.Char_POS[1]),text='', multiline=False)
		Reg_Page_Target_Input_Z = Reg_Page_Target_Input_Z.__self__
		Reg_Page_Target_Input_Z.bind(text=self.on_rrsmZ)
		Reg_Page_Target_Input_Z.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_X = TextInput(hint_text='X:{}'.format(self.Char_POS[2]),text='', multiline=False)
		Reg_Page_Target_Input_X = Reg_Page_Target_Input_X.__self__
		Reg_Page_Target_Input_X.bind(text=self.on_rrsmX)
		Reg_Page_Target_Input_X.bind(on_touch_down=self.hint_clear)

		Reg_Page_Target_Input_Y = TextInput(hint_text='Y:{}'.format(self.Char_POS[3]),text='', multiline=False)
		Reg_Page_Target_Input_Y = Reg_Page_Target_Input_Y.__self__
		Reg_Page_Target_Input_Y.bind(text=self.on_rrsmY)
		Reg_Page_Target_Input_Y.bind(on_touch_down=self.hint_clear)

		self.result_layoutloc.add_widget(Reg_Page_Target_Input_D)
		self.result_layoutloc.add_widget(Reg_Page_Target_Input_Z)
		self.result_layoutloc.add_widget(Reg_Page_Target_Input_X)
		self.result_layoutloc.add_widget(Reg_Page_Target_Input_Y)


		self.RRSC_List_Page_Result = {}
		self.RRSC_List_Page_MSG_Details = {}
		self.RRSC_List_Page_btn_spawn = {}
		self.RRSC_List_Page_btn_CL = {}
		self.RRSC_D = {}
		

		i = 0
		if result != False and result != '' and result != '{}' and result != {} and result != None:
			if len(result) > 5:
				for _type, Monsters in json.loads(result).items():
					for Monster, Monster_Data in Monsters.items():
						if Monster == '':
							continue
						self.RRSC_List_Page_Result[i] = GridLayout(cols=3, size_hint_y=None, size=(Window.width * .9, Window.height * .25))
						self.RRSC_D[i] = 'IMonster: {0}\nStats: {1}\nDescription:\n  {2}'.format(self.split_lines(Monster,4,20),self.split_lines(Monster_Data['stats'],4,20),self.split_lines(Monster_Data['description'],4,20))
						self.RRSC_List_Page_MSG_Details[i] = Label(text='IMonster: {0}\nStats: {1}\nDescription:\n  {2}'.format(self.split_lines(Monster,4,20),self.split_lines(Monster_Data['stats'],4,20)),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
						self.RRSC_List_Page_MSG_Details[i] = self.RRSC_List_Page_MSG_Details[i].__self__						
						self.RRSC_List_Page_btn_spawn[i] = Button(text=self.pm("R.O.S.I.E\nSpawn\nMonster",'fg_magenta'),markup=True, size_hint = (.2,1.5))
						self.RRSC_List_Page_btn_spawn[i].bind(on_press=lambda *Args,lmonster=Monster: self.API_ROSIE_SM(self.username,self.password,lmonster,api_key))
						self.RRSC_List_Page_btn_CL[i] = Button(text=self.pm(",monster\nDetails",'fg_yellow'),markup=True, size_hint = (.2,1.5))
						self.RRSC_List_Page_btn_CL[i].bind(on_press=lambda *Args,PItem='Details for Monster : {}'.format(Monster),PItem_Details=self.RRSC_D[i],backone=True: self.result_PopUP(PItem,PItem_Details,backone))

						self.RRSC_List_Page_Result[i].add_widget(self.RRSC_List_Page_MSG_Details[i])
						self.RRSC_List_Page_Result[i].add_widget(self.RRSC_List_Page_btn_spawn[i])
						self.RRSC_List_Page_Result[i].add_widget(self.RRSC_List_Page_btn_CL[i])
						
						if (scroll_height < (Window.height / 2)):
							scroll_height = scroll_height + 120
						i += 1

			Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
			Main_result.bind(minimum_height = Main_result.setter('height'))
			Main_result = Main_result.__self__
			for x in range(0,i):
				Main_result.add_widget(self.RRSC_List_Page_Result[x])

			scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[15].height - 30), size = (Window.width, scroll_height)) 
			#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
			scrlFBtns.add_widget(Main_result)
			self.result_layout3[15].add_widget(scrlFBtns)
		self.result_layout[15].add_widget(self.MDD_Layout[2])
		self.result_layout[15].add_widget(self.result_layout4[15])
		self.result_layout[15].add_widget(self.result_layout3[15])
		self.result_layout[15].add_widget(self.result_layoutloc)
		self.result_layout2[15].add_widget(back)
		self.result_layout[15].add_widget(self.result_layout2[15])

		self.CMD_result[15].open()

	def result_PopUP_ROSIE_Speaks(self,func,result):
		self.Dismiss_All()
		if func == 'reply':
			self.STarget = result
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[18] = GridLayout(rows=4, size_hint_y=None, size=(Window.width * .95, Window.height))
		self.result_layout[18] = self.result_layout[18].__self__
		self.result_layout[18].bind(height = self.result_layout[18].setter('top'))
		self.result_layout5[18] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .95, Window.height * .3))
		self.result_layout5[18] = self.result_layout5[18].__self__
		self.result_layout4[18] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .95, Window.height * .3))
		self.result_layout4[18] = self.result_layout4[18].__self__
		self.result_layout4[18].add_widget(result_Mar_MUDLogo)
		self.result_layout3[18] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .95, Window.height * .1))
		self.result_layout3[18] = self.result_layout3[18].__self__
		self.result_layout2[18] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .1))
		self.result_layout2[18] = self.result_layout2[18].__self__
		self.CMD_result[18] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[18],auto_dismiss=False)
		self.CMD_result[18] = self.CMD_result[18].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		send = Button(text=self.pm('Send\nAll','fg_magenta'),markup=True,size_hint = (1,3))
		send.bind(on_press=lambda *Args: self.API_ROSIE_Speaks(self.username,self.password,self.ROSIE_PW,self.sMSG,api_key))
		send = send.__self__

		Reg_Page_Msg_Input = TextInput(hint_text='Message Text :',text='', multiline=True)
		Reg_Page_Msg_Input = Reg_Page_Msg_Input.__self__
		
		Reg_Page_Msg_Input.bind(text=self.on_MSG)
		Reg_Page_Msg_Input.bind(on_touch_down=self.hint_clear)
		Reg_Page_Msg_Input.bind(on_text_validate=(lambda *Args: self.API_ROSIE_Speaks(self.username,self.password,self.ROSIE_PW,self.sMSG,api_key)))

		self.result_layout2[18].add_widget(back)
		self.result_layout2[18].add_widget(send)

		self.result_layout5[18].add_widget(Reg_Page_Msg_Input)
		
		self.result_layout[18].add_widget(self.MDD_Layout[2])
		self.result_layout[18].add_widget(self.result_layout4[18])
		self.result_layout[18].add_widget(self.result_layout5[18])
		self.result_layout[18].add_widget(self.result_layout2[18])

		self.CMD_result[18].open()


	def result_PopUP_Player_Speaks(self,*Args):
		self.Dismiss_All()
		# if func == 'reply':
		# 	self.STarget = result
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[19] = GridLayout(rows=6, size_hint_y=None, size=(Window.width * .95, Window.height))
		self.result_layout[19] = self.result_layout[19].__self__
		self.result_layout[19].bind(height = self.result_layout[19].setter('top'))
		self.result_layout5[19] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .95, Window.height * .15))
		self.result_layout5[19] = self.result_layout5[19].__self__
		self.result_layout4[19] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .95, Window.height * .4))
		self.result_layout4[19] = self.result_layout4[19].__self__
		self.result_layout4[19].add_widget(result_Mar_MUDLogo)
		self.result_layout3[19] = GridLayout(cols=3, size_hint_y=None, size=(Window.width * .95, Window.height * .1))
		self.result_layout3[19] = self.result_layout3[19].__self__
		self.result_layout2[19] = GridLayout(cols=3, size_hint_y=None, size=(Window.width, Window.height * .1))
		self.result_layout2[19] = self.result_layout2[19].__self__
		self.result_layout1[19] = GridLayout(cols=1, size_hint_y=None, size=(Window.width, Window.height * .1))
		self.result_layout1[19] = self.result_layout1[19].__self__

		self.CMD_result[19] = Popup(title='{0}'.format('Speak to Room.'), content=self.result_layout[19],auto_dismiss=False)
		self.CMD_result[19] = self.CMD_result[19].__self__
		
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__

		Speak = Button(text=self.pm('Speak','fg_cyan'),markup=True,size_hint = (1,3))
		Speak.bind(on_press=(lambda *Args,Type='speak': self.OnSay(Type)))
		Speak = Speak.__self__

		Say = Button(text=self.pm('Say','fg_cyan'),markup=True,size_hint = (1,3))
		Say.bind(on_press=(lambda *Args,Type='say': self.OnSay(Type)))
		Say = Say.__self__

		Whisper = Button(text=self.pm('Whisper','fg_cyan'),markup=True,size_hint = (1,3))
		Whisper.bind(on_press=(lambda *Args,Type='whisper': self.OnSay(Type)))
		Whisper = Whisper.__self__

		Shout = Button(text=self.pm('Shout','fg_magenta'),markup=True,size_hint = (1,3))
		Shout.bind(on_press=(lambda *Args,Type='shout': self.OnSay(Type)))
		Shout = Shout.__self__

		Yell = Button(text=self.pm('Yell','fg_magenta'),markup=True,size_hint = (1,3))
		Yell.bind(on_press=(lambda *Args,Type='yell': self.OnSay(Type)))
		Yell = Yell.__self__

		Scream = Button(text=self.pm('Scream','fg_magenta'),markup=True,size_hint = (1,3))
		Scream.bind(on_press=(lambda *Args,Type='scream': self.OnSay(Type)))
		Scream = Scream.__self__

		Reg_Page_Msg_Input = TextInput(hint_text='Message Text :',text='', multiline=True)
		Reg_Page_Msg_Input = Reg_Page_Msg_Input.__self__
		
		Reg_Page_Msg_Input.bind(text=self.on_MSG)
		Reg_Page_Msg_Input.bind(on_touch_down=self.hint_clear)
		Reg_Page_Msg_Input.bind(on_text_validate=(lambda *Args,Type='say': self.OnSay(Type)))

		self.result_layout2[19].add_widget(Speak)
		self.result_layout2[19].add_widget(Whisper)
		self.result_layout2[19].add_widget(Say)
				
		self.result_layout3[19].add_widget(Scream)
		self.result_layout3[19].add_widget(Shout)
		self.result_layout3[19].add_widget(Yell)

		self.result_layout1[19].add_widget(back)

		self.result_layout5[19].add_widget(Reg_Page_Msg_Input)
		
		self.result_layout[19].add_widget(self.MDD_Layout[2])
		self.result_layout[19].add_widget(self.result_layout4[19])
		self.result_layout[19].add_widget(self.result_layout5[19])
		self.result_layout[19].add_widget(self.result_layout3[19])
		self.result_layout[19].add_widget(self.result_layout2[19])
		self.result_layout[19].add_widget(self.result_layout1[19])

		self.CMD_result[19].open()

	def PopUp_List_Store(self,func,result):
		self.Dismiss_All()
		self.Dismiss_One(1)
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[20] = GridLayout(rows=5, size_hint_y=None, size=(Window.width * .7, Window.height))
		self.result_layout[20] = self.result_layout[20].__self__
		self.result_layout[20].bind(height = self.result_layout[20].setter('top'))
		self.result_layout4[20] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .7, Window.height * .1))
		self.result_layout4[20] = self.result_layout4[20].__self__
		self.result_layout4[20].bind(height = self.result_layout[20].setter('top'))
		self.result_layout4[20].add_widget(result_Mar_MUDLogo)
		self.result_layoutloc = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .7, Window.height * .15))
		self.result_layoutloc = self.result_layoutloc.__self__
		self.result_layout3[20] = GridLayout(cols=2, size_hint_y=None,size=(Window.width - 10, Window.height * .5))
		self.result_layout3[20] = self.result_layout3[20].__self__
		self.result_layout2[20] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[20] = self.result_layout2[20].__self__
		self.result_layout1[20] = GridLayout(cols=1, size_hint_y=None, size=(Window.width, Window.height * .15))
		self.result_layout1[20] = self.result_layout1[20].__self__		
		self.CMD_result[20] = Popup(title='Welcome to Frank Corp\nInterDemensional Online\Store.'.format(func), content=self.result_layout[20],auto_dismiss=False)
		self.CMD_result[20] = self.CMD_result[20].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		
		self.Shop_List_Page_Result = {}
		self.Shop_List_Page_MSG_Details = {}
		self.Shop_List_Page_btn_spawn = {}
		self.Shop_Items_Details = {}
		self.Shop_List_Page_btn_CL = {}
		self.Money_Left = Label(text=self.pm('Credits Available : {}'.format(re.findall(r'\](.*)\[',self.Char_Stats['CRDT'])[0]),'fg_yellow'), markup = True,size=(Window.width * .5, Window.height * .2))				

		i = 0
		if result != False and result != '' and result != '{}' and result != {}:
			if len(result) > 0:
				for _type, Items in json.loads(result).items():
					for Item, Item_Data in Items.items():
						if 'have_it' not in Item_Data.keys():
							Item_Data['have_it'] = '0'
						if Item == '':
							continue
						if 'Req_LVL' not in Item_Data.keys():
							Item_Data['Req_LVL'] = '1'
						if 'count' not in Item_Data.keys():
							Item_Data['count'] = '1'
						if Item_Data['item_class'].upper() in ['RW','W']:
							scolor = 'fg_lred'
							bcolor = 'fg_lred'
						elif Item_Data['item_class'].upper() in ['AMMO']:
							scolor = 'fg_dred'
							bcolor = 'fg_dred'
						elif Item_Data['item_class'].upper() == 'P':
							scolor = 'fg_orange'
							bcolor = 'fg_dorange'
						elif Item_Data['item_class'].upper() in ['PG']:
							scolor = 'fg_gold'
							bcolor = 'fg_gold'
						elif Item_Data['item_class'].upper() in ['WK', 'K']:
							scolor = 'fg_lbrown'
							bcolor = 'fg_lbrown'
						elif Item_Data['item_class'].upper() in ['WM', 'PF']:
							scolor = 'fg_lgold'
							bcolor = 'fg_lgold'
						elif Item_Data['item_class'].upper() in ['TD']:
							scolor = 'fg_lyellow'
							bcolor = 'fg_dyellow'
						elif Item_Data['item_class'].upper() in ['CR','SB' ]:
							scolor = 'fg_white'
							bcolor = 'fg_white'
						elif Item_Data['item_class'].upper() in ['CI']:
							scolor = 'fg_lgreen'
							bcolor = 'fg_dgreen'
						elif Item_Data['item_class'].upper() in ['A','PANTS','BOOTS','GLOVES','BRACERS']:
							scolor = 'fg_dcyan'
							bcolor = 'fg_dblue'
						elif Item_Data['item_class'].upper() in ['MW','RING_RIGHT','RING_LEFT','NECKLACE','GLASSES']:
							scolor = 'fg_lred'
							bcolor = 'fg_lred'					
						else:
							scolor = 'fg_lgreen'
							bcolor = 'fg_dgreen'
						self.Shop_List_Page_Result[i] = GridLayout(cols=5, size_hint_y=None, size=(Window.width * .9, Window.height * .25))
						self.Shop_Items_Details[i] = self.pm('Item : {0}\nClass: {1}\nDescription:\n  {2}\nStrength: {3}\n Price:{4}\n You Have {5}'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_class'],4,20),self.split_lines(Item_Data['item_description'],4,20),self.split_lines(Item_Data['item_value'],4,20),self.split_lines(Item_Data['s_value'],4,20),self.split_lines(Item_Data['have_it'],4,20)),scolor)
						self.Shop_List_Page_MSG_Details[i] = Label(text=self.pm('Item : {0}\nClass: {1}\nStrength: {3}\n Price:{4}\n You Have {5}'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_class'],4,20),'',self.split_lines(Item_Data['item_value'],4,20),self.split_lines(Item_Data['s_value'],4,20),self.split_lines(Item_Data['have_it'],4,20)),scolor),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
						self.Shop_List_Page_MSG_Details[i] = self.Shop_List_Page_MSG_Details[i].__self__
						self.Shop_List_Page_btn_spawn[i] = Button(text=self.pm("Purchase\nItem",bcolor),markup=True, size_hint = (.2,1.5))
						self.Shop_List_Page_btn_spawn[i].bind(on_press=lambda *Args,litem='buy {}'.format(Item): self.API_Store(self.username,self.password,litem,api_key))
						self.Shop_List_Page_btn_CL[i] = Button(text=self.pm("Item\nDetails",'fg_yellow'),markup=True, size_hint = (.2,1.5))
						self.Shop_List_Page_btn_CL[i].bind(on_press=lambda *Args,ditem='Details for {}'.format(Item),litem=self.Shop_Items_Details[i],backone=True: self.result_PopUP(ditem,litem,backone=backone))

						self.Shop_List_Page_Result[i].add_widget(self.Shop_List_Page_MSG_Details[i])
						self.Shop_List_Page_Result[i].add_widget(self.Shop_List_Page_btn_spawn[i])
						self.Shop_List_Page_Result[i].add_widget(self.Shop_List_Page_btn_CL[i])
						
						if (scroll_height < (Window.height / 2)):
							scroll_height = scroll_height + 120
						i += 1

				Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
				Main_result.bind(minimum_height = Main_result.setter('height'))
				Main_result = Main_result.__self__
				for x in range(0,i):
					Main_result.add_widget(self.Shop_List_Page_Result[x])

				scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[20].height - 30), size = (Window.width, scroll_height)) 
				#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
				scrlFBtns.add_widget(Main_result)
				self.result_layout3[20].add_widget(scrlFBtns)
		
		self.result_layout[20].add_widget(self.MDD_Layout[2])				
		self.result_layout1[20].add_widget(self.Money_Left)
		self.result_layout[20].add_widget(self.result_layout4[20])
		self.result_layout[20].add_widget(self.result_layout3[20])
		self.result_layout[20].add_widget(self.result_layout1[20])
		self.result_layout2[20].add_widget(back)
		self.result_layout[20].add_widget(self.result_layout2[20])

		self.CMD_result[20].open()


	def PopUp_List_Spells(self,func,result):
		self.Play_Sound('Cast_Magic')
		self.Dismiss_All()
		self.Dismiss_One(1)
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[21] = GridLayout(rows=5, size_hint_y=None, size=(Window.width * .85, Window.height))
		self.result_layout[21] = self.result_layout[21].__self__
		self.result_layout[21].bind(height = self.result_layout[21].setter('top'))
		self.RPopUp1_result_Stats = GridLayout(rows=1, size_hint_y=None, size=(Window.width, Window.height * .19))
		self.RPopUp1_result_Stats = self.RPopUp1_result_Stats.__self__
		self.result_layout4[21] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .7, Window.height * .18))
		self.result_layout4[21] = self.result_layout4[21].__self__
		self.result_layout4[21].bind(height = self.result_layout4[21].setter('top'))
		self.result_layout4[21].add_widget(result_Mar_MUDLogo)
		self.result_layoutloc = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .7, Window.height * .18))
		self.result_layoutloc = self.result_layoutloc.__self__
		self.result_layout3[21] = BoxLayout(padding=3, orientation='vertical',size_hint=(Window.width - 10, Window.height * .7),size=(Window.width - 10, Window.height * .5))
		self.result_layout3[21] = self.result_layout3[21].__self__
		self.result_layout2[21] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[21] = self.result_layout2[21].__self__
		self.CMD_result[21] = Popup(title='{}'.format(func), content=self.result_layout[21],auto_dismiss=False)
		self.CMD_result[21] = self.CMD_result[21].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		
		self.Spell_List_Page_Final = {}
		self.Spell_List_Page_Result = {}
		self.Spell_List_Page_Result_2 = {}
		self.Spell_List_Page_MSG_Details = {}
		self.Spell_List_Page_btn_Cast = {}
		self.Spell_List_Page_btn_SetF1 = {}
		self.Spell_List_FavNum1_8 = {}
		self.Spell_List_FavNum9_16 = {}
		
		self.Spell_Details = {}
		self.Spell_List_Page_btn_CL = {}
		 
		i = 0
		if result != False and result != '' and result != '{}' and result != {}:
			if len(result) > 0:
				for Spell, Spell_Data in json.loads(result).items():
					if Spell == '':
						continue
					if 'enchant' in Spell_Data['m_type'].lower():
						scolor = 'lg_magenta'
						bcolor = 'fg_magenta'
					elif 'heal' in Spell_Data['m_type'].lower():
						scolor = 'fg_cyan'
						bcolor = 'fg_lcyan'
					elif 'charm' in Spell_Data['m_type'].lower():
						scolor = 'fg_orange'
						bcolor = 'fg_lorange'
					elif 'shield' in Spell_Data['m_type'].lower():
						scolor = 'fg_dcyan'
						bcolor = 'fg_dblue'
					elif 'spawn_i' in Spell_Data['m_type'].lower():
						scolor = 'fg_gold'
						bcolor = 'fg_lgold'
					elif 'spawn_wm' in Spell_Data['m_type'].lower():
						scolor = 'fg_dpink'
						bcolor = 'fg_pink'
					elif 'spawn_a' in Spell_Data['m_type'].lower():
						scolor = 'fg_yellow'
						bcolor = 'fg_dyellow'
					elif 'spawn_c' in Spell_Data['m_type'].lower():
						scolor = 'fg_lbrown'
						bcolor = 'fg_dbrown'
					elif 'targeted_attack' in Spell_Data['m_type'].lower():
						scolor = 'fg_red'
						bcolor = 'fg_dred'
					elif 'area_attack' in Spell_Data['m_type'].lower():
						scolor = 'fg_purple'
						bcolor = 'fg_dpurple'
					elif 'spawn_m' in Spell_Data['m_type'].lower():
						scolor = 'fg_red'
						bcolor = 'fg_lred'
					self.Spell_List_Page_Result[i] = GridLayout(cols=2, size_hint_y=None, size=(Window.width *.9, Window.height * .12))
					self.Spell_List_Page_Result_2[i] = GridLayout(cols=3, size_hint_y=None, size=(Window.width *.9, Window.height * .28))
					self.Spell_List_Page_Final[i] = GridLayout(rows=2, size_hint_y=None, size=(Window.width *.9, Window.height * .4))
					self.Spell_Details[i] = self.pm('Spell : {0}\nType: {1}\nDescription:\n  {2}\nStrength: {3}\n Magic Cost: {4}'.format(self.split_lines(Spell,4,20),self.split_lines(Spell_Data['m_type'],4,20),self.split_lines(Spell_Data['description'],4,20),self.split_lines(Spell_Data['m_strength'],4,20),self.split_lines(Spell_Data['m_cost'],4,20)),scolor)
					self.Spell_List_Page_MSG_Details[i] = Label(text=self.pm('Spell : {0}\nType: {1}\nStrength: {3}\n Magic Cost: {4}'.format(self.split_lines(Spell,4,20),self.split_lines(Spell_Data['m_type'],4,20),'',self.split_lines(Spell_Data['m_strength'],4,20),self.split_lines(Spell_Data['m_cost'],4,20)),scolor),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
					self.Spell_List_Page_MSG_Details[i] = self.Spell_List_Page_MSG_Details[i].__self__

					if 'target' in Spell_Data['m_type'].lower():
						if 'attack' in Spell_Data['m_type'].lower():
							self.Spell_List_Page_btn_Cast[i] = Button(text=self.pm("Cast\n{}".format('*' * 6 + '\n' + re.sub(' ','\n',Spell)),scolor),markup=True,font_size='11sp', size_hint = (.2,1.5))
							self.Spell_List_Page_btn_Cast[i].bind(on_press=lambda *Args,spell=Spell: self.PopUp_List_Monsters_SP('Cast',spell))
						else:
							self.Spell_List_Page_btn_Cast[i] = Button(text=self.pm("Cast\n{}".format(re.sub(' ','\n',Spell)),scolor),markup=True,font_size='11sp', size_hint = (.2,1.5))
							self.Spell_List_Page_btn_Cast[i].bind(on_press=lambda *Args,spell=Spell: self.PopUp_Spell_Target_Player('Friend',spell))
					elif 'enchant' in Spell_Data['m_type'].lower() and 'monster' in Spell_Data['m_type'].lower():
						self.Spell_List_Page_btn_Cast[i] = Button(text=self.pm("Cast\n{}".format('*' * 6 + '\n' + re.sub(' ','\n',Spell)),'fg_magenta'),markup=True,font_size='11sp', size_hint = (.2,1.5))
						if 'monster' in Spell_Data['m_type'].lower():
							self.Spell_List_Page_btn_Cast[i].bind(on_press=lambda *Args,spell=Spell: self.PopUp_List_Monsters_SP('Cast',spell))
						else:
							self.Spell_List_Page_btn_Cast[i].bind(on_press=lambda *Args,spell=Spell: self.PopUp_Spell_Target_Player('Friend',spell))
					else:
						self.Spell_List_Page_btn_Cast[i] = Button(text=self.pm("Cast\n\n{}".format('*' * 6 + '\n' + re.sub(' ','\n',Spell)),scolor),markup=True,font_size='11sp', size_hint = (.2,1.5))
						self.Spell_List_Page_btn_Cast[i].bind(on_press=lambda *Args,Move='cast Spell:{}%Target:all%'.format(Spell): self.API_Send_Move(self.username,self.password,Move,api_key))

					self.Spell_List_FavNum1_8[i] = Button(text='Select\nSlot1-8', size_hint=(.1, 1.5))
					self.Spell_List_FavNum1_8[i].bind(on_release=self.SFAV_Menu1_8.open)
					self.Spell_List_FavNum9_16[i] = Button(text='Select\nSlot9-16', size_hint=(.1, 1.5))								
					self.Spell_List_FavNum9_16[i].bind(on_release=self.SFAV_Menu9_16.open)
					self.Spell_List_Page_btn_SetF1[i] = Button(text=self.pm("Set!",'fg_yellow'),markup=True, size_hint = (.1,1.5))
					self.Spell_List_Page_btn_SetF1[i].bind(on_press=lambda *Args,sname=Spell,spell=Spell_Data: self.OnSetFavSpell('0',sname,spell))
					
					self.Spell_List_Page_btn_CL[i] = Button(text=self.pm("Spell\nDetails",'fg_yellow'),markup=True, size_hint = (.2,1.5))
					self.Spell_List_Page_btn_CL[i].bind(on_press=lambda *Args,details='Details for {}'.format,Spelld=self.Spell_Details[i],backone=True: self.result_PopUP(details,Spelld,backone=backone))
					self.Spell_List_Page_Result[i].add_widget(self.Spell_List_Page_MSG_Details[i])
					self.Spell_List_Page_Result_2[i].add_widget(self.Spell_List_FavNum1_8[i])
					self.Spell_List_Page_Result_2[i].add_widget(self.Spell_List_FavNum9_16[i])
					self.Spell_List_Page_Result_2[i].add_widget(self.Spell_List_Page_btn_SetF1[i])
					self.Spell_List_Page_Result[i].add_widget(self.Spell_List_Page_btn_CL[i])
					self.Spell_List_Page_Final[i].add_widget(self.Spell_List_Page_Result[i])
					self.Spell_List_Page_Final[i].add_widget(self.Spell_List_Page_Result_2[i])

					if (scroll_height < (Window.height / 2)):
						scroll_height = scroll_height + 120
					i += 1

				Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
				Main_result.bind(minimum_height = Main_result.setter('height'))
				Main_result = Main_result.__self__
				for x in range(0,i):
					Main_result.add_widget(self.Spell_List_Page_Final[x])

				scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[21].height - 30), size = (Window.width, scroll_height)) 
				#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
				scrlFBtns.add_widget(Main_result)
				self.result_layout3[21].add_widget(scrlFBtns)
		
		self.result_layout[21].add_widget(self.MDD_Layout[2]) 
		self.result_layout[21].add_widget(self.result_layout4[21])
		self.result_layout[21].add_widget(self.result_layout3[21])
		self.RPopUp1_result_Stats.add_widget(self.Stats_displaym[3])
		self.result_layout[21].add_widget(self.RPopUp1_result_Stats)
		self.result_layout2[21].add_widget(back)
		self.result_layout[21].add_widget(self.result_layout2[21])

		self.CMD_result[21].open()

	def PopUp_Spell_Target_Player(self,func,spell):
		self.Dismiss_All()
		self.Dismiss_One(1)
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[22] = GridLayout(rows=6, size_hint_y=None, size=(Window.width * .7, Window.height))
		self.result_layout[22] = self.result_layout[22].__self__
		self.result_layout[22].bind(height = self.result_layout[22].setter('top'))
		self.RPopUp2_result_Stats = GridLayout(rows=1, size_hint_y=None, size=(Window.width, Window.height * .19))
		self.RPopUp2_result_Stats = self.RPopUp2_result_Stats.__self__		
		self.result_layout4[22] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout4[22] = self.result_layout4[22].__self__
		self.result_layout4[22].bind(height = self.result_layout[22].setter('top'))
		self.result_layout4[22].add_widget(result_Mar_MUDLogo)
		self.result_layoutloc = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layoutloc = self.result_layoutloc.__self__
		self.result_layout3[22] = GridLayout(cols=1, size_hint_y=None, size=(Window.width - 10, Window.height * .55))
		self.result_layout3[22] = self.result_layout3[22].__self__
		self.result_layout2[22] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[22] = self.result_layout2[22].__self__
		self.CMD_result[22] = Popup(title='Select Target for Spell : {}'.format(spell), content=self.result_layout[22],auto_dismiss=False)
		self.CMD_result[22] = self.CMD_result[22].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		self.Spell_List_Page_Result = {}
		self.Spell_List_Page_MSG_Details = {}
		self.Spell_List_Page_btn_Cast = {}
		self.Spell_List_Page_btn_SetF1 = {}
		self.Spell_List_Page_btn_SetF2 = {}
		

		i = 0
		if self.CRoom != False and self.CRoom != '' and self.CRoom != '{}' and self.CRoom != {}:
			if type(self.CRoom['players']) == list:
				me = self.username.lower().rstrip().lstrip()
				if me not in self.CRoom['players']:
					self.CRoom['players'].append(me)
			if len(self.CRoom['players']) > 0:
				for Player in self.CRoom['players']:
					if Player == '':
						continue
					self.Spell_List_Page_Result[i] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .9, Window.height * .25))
					self.Spell_List_Page_MSG_Details[i] = Label(text='Player : {0}'.format(self.split_lines(Player.title(),4,80)),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
					self.Spell_List_Page_MSG_Details[i] = self.Spell_List_Page_MSG_Details[i].__self__
					self.Spell_List_Page_btn_Cast[i] = Button(text=self.pm("Cast\n",'fg_magenta'),markup=True, size_hint = (.2,1.5))
					self.Spell_List_Page_btn_Cast[i].bind(on_press=lambda *Args,Move='cast Spell:{}%Target:{}%'.format(spell,Player): self.API_Send_Move(self.username,self.password,Move,api_key))
					self.Spell_List_Page_Result[i].add_widget(self.Spell_List_Page_MSG_Details[i])
					self.Spell_List_Page_Result[i].add_widget(self.Spell_List_Page_btn_Cast[i])
					
					if (scroll_height < (Window.height / 2)):
						scroll_height = scroll_height + 120
					i += 1

				Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
				Main_result.bind(minimum_height = Main_result.setter('height'))
				Main_result = Main_result.__self__
				for x in range(0,i):
					Main_result.add_widget(self.Spell_List_Page_Result[x])

				scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[22].height - 30), size = (Window.width, scroll_height)) 
				#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
				scrlFBtns.add_widget(Main_result)
				self.result_layout3[22].add_widget(scrlFBtns)
		self.result_layout[22].add_widget(self.MDD_Layout[2])
		self.result_layout[22].add_widget(self.result_layout4[22])
		self.result_layout[22].add_widget(self.result_layout3[22])
		self.RPopUp2_result_Stats.add_widget(self.Stats_displaym[3])
		self.result_layout[22].add_widget(self.RPopUp2_result_Stats)
		self.result_layout2[22].add_widget(back)
		self.result_layout[22].add_widget(self.result_layout2[22])
		self.CMD_result[22].open()

	def PopUp_List_Monsters_SP(self,func,Spell='Attack_Screen'):
		# self.API_Refresh_GData(self.username,self.password,api_key)
		self.Play_Sound('MonsterG')
		self.Dismiss_All()
		MP = int(re.findall('\](\d*)\[',self.Char_Stats['MP'])[0])
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[23] = GridLayout(rows=6, size_hint_y=None, size=(Window.width * .7, Window.height))
		self.result_layout[23] = self.result_layout[23].__self__
		self.result_layout[23].bind(height = self.result_layout[23].setter('top'))
		self.RPopUp3_result_Stats = GridLayout(rows=1, size_hint_y=None, size=(Window.width, Window.height * .19))
		self.RPopUp3_result_Stats = self.RPopUp3_result_Stats.__self__		
		self.result_layout4[23] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout4[23] = self.result_layout4[23].__self__
		self.result_layout4[23].bind(height = self.result_layout[23].setter('top'))
		self.result_layout4[23].add_widget(result_Mar_MUDLogo)
		self.result_layoutloc = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layoutloc = self.result_layoutloc.__self__
		self.result_layout3[23] = BoxLayout(padding=3, orientation='vertical',size_hint=(Window.width - 10, Window.height * .7),size=(Window.width - 10, Window.height * .7))
		self.result_layout3[23] = self.result_layout3[23].__self__
		self.result_layout2[23] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[23] = self.result_layout2[23].__self__
		self.CMD_result[23] = Popup(title='{}'.format(func), content=self.result_layout[23],auto_dismiss=False)
		self.CMD_result[23] = self.CMD_result[23].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		
		self.Monsters_List_Page_Result_Final = {}
		self.Monsters_List_Page_Result = {}
		self.Monsters_List_Page_Result_2 = {}
		self.Monsters_List_Page_MSG_Details = {}
		self.Monsters_List_Page_btn_Attack = {}
		self.Monsters_List_Page_btn_CSpell_1 = {}
		self.Monsters_List_Page_btn_CSpell_2 = {}
		self.Monsters_List_Page_btn_CSpell_sp = {}
		self.Monsters_List_Page_btn_CL = {}
		self.M_Text = {}
		self.M_Text_Details = {}

		i = 0
		if self.CRoom != False and self.CRoom != '' and self.CRoom != '{}' and self.CRoom != {}:
			if len(self.CRoom) > 0:
				if 'monsters' in self.CRoom.keys():
					for Monster, Monster_Data in self.CRoom['monsters'].items():
						if Monster == '':
							continue
						Spell = str(Spell)
						if 'attack_screen' in str(Spell).lower():
							self.Monsters_List_Page_Result[i] = GridLayout(cols=2, size_hint_y=None, size=(Window.width *.9, Window.height * .12))
							self.Monsters_List_Page_Result_2[i] = GridLayout(cols=3, size_hint_y=None, size=(Window.width *.9, Window.height * .28))
						else:
							self.Monsters_List_Page_Result[i] = GridLayout(cols=2, size_hint_y=None, size=(Window.width *.9, Window.height * .2))
							self.Monsters_List_Page_Result_2[i] = GridLayout(cols=1, size_hint_y=None, size=(Window.width *.9, Window.height * .2))
						self.Monsters_List_Page_Result_Final[i]  = GridLayout(rows=2, size_hint_y=None, size=(Window.width *.9, Window.height * .4))
						self.M_Text_Details[i] = 'Monster : {0}\nDescription:\n  {1}\nAttack Strength: {2}\n Defense Strength: {3}\nHealh: {4}'.format(self.split_lines(Monster,4,20),self.split_lines(Monster_Data['description'],4,20),self.split_lines(Monster_Data['stats'][1],4,20),self.split_lines(Monster_Data['stats'][2],4,20),self.split_lines(Monster_Data['stats'][0],4,20))							
						self.M_Text[i] = 'Monster : {0}\nAttack Strength: {2}\n Defense Strength: {3}\nHealh: {4}'.format(self.split_lines(Monster,4,20),'',self.split_lines(Monster_Data['stats'][1],4,20),self.split_lines(Monster_Data['stats'][2],4,20),self.split_lines(Monster_Data['stats'][0],4,20))
						if int(Monster_Data['stats'][2]) > 5 * (int(re.findall(r'\](\d*)\[',self.Char_Stats['AT'])[0])):
							self.M_Text[i] = self.pm(self.M_Text[i],'fg_magenta')
							self.M_Text_Details[i] = self.pm(self.M_Text_Details[i],'fg_magenta')
						elif int(Monster_Data['stats'][2]) > 3 * (int(re.findall(r'\](\d*)\[',self.Char_Stats['AT'])[0])):
							self.M_Text[i] = self.pm(self.M_Text[i],'fg_red')
							self.M_Text_Details[i] = self.pm(self.M_Text_Details[i],'fg_red')
						elif int(Monster_Data['stats'][2]) > 2 * (int(re.findall(r'\](\d*)\[',self.Char_Stats['AT'])[0])):
							self.M_Text[i] = self.pm(self.M_Text[i],'fg_lred')					
							self.M_Text_Details[i] = self.pm(self.M_Text_Details[i],'fg_lred')		
						elif int(Monster_Data['stats'][2]) > int(re.findall(r'\](\d*)\[',self.Char_Stats['AT'])[0]):
							self.M_Text[i] = self.pm(self.M_Text[i],'fg_lgreen')
							self.M_Text_Details[i] = self.pm(self.M_Text_Details[i],'fg_lgreen')
						elif int(Monster_Data['stats'][2]) < (int(re.findall(r'\](\d*)\[',self.Char_Stats['AT'])[0])):
							self.M_Text[i] = self.pm(self.M_Text[i],'fg_dcyan')
							self.M_Text_Details[i] = self.pm(self.M_Text_Details[i],'fg_dcyan')
							
						self.Monsters_List_Page_MSG_Details[i] = Label(text=self.M_Text[i] ,halign='left',font_size='12sp', size=(Window.width * .7, Window.height * .2),markup=True)				
						self.Monsters_List_Page_MSG_Details[i] = self.Monsters_List_Page_MSG_Details[i].__self__
						self.Monsters_List_Page_Result[i].add_widget(self.Monsters_List_Page_MSG_Details[i])

						if 'attack_screen' in str(Spell).lower():
							if len(self.CRoom['monsters']) > 0:
								self.Monsters_List_Page_btn_Attack[i] = Button(text=self.pm("Attack!",'fg_red'),font_size='11sp', size=(Window.width * .25, Window.height * .2), markup=True)
							else:
								self.Monsters_List_Page_btn_Attack[i] = Button(text=self.pm("Attack!",'fg_black'),font_size='11sp', size=(Window.width * .25, Window.height * .2), markup=True)
							self.Monsters_List_Page_btn_Attack[i].bind(on_press=lambda *Args,Move='attack {}'.format(Monster): self.API_Send_Move(self.username,self.password,Move,api_key))
							self.Monsters_List_Page_Result_2[i].add_widget(self.Monsters_List_Page_btn_Attack[i])
							

							if len(self.Fav_Spells['0']) == 0:
								fs1_text = 'Attack\nFav1\nNot\nSet!'
							else:
								if MP > 30:
									fs1_text = self.pm("Cast\n :\n--------\n" + re.sub(' ','\n',self.Fav_Spells['0']['Spell']),'fg_lgreen')
								else:
									fs1_text = self.pm("Cast\n :\n--LowMP--\n" + re.sub(' ','\n',self.Fav_Spells['0']['Spell']),'fg_dred')

							self.Monsters_List_Page_btn_CSpell_1[i] = Button(text="{}".format(fs1_text),font_size='11sp', size=(Window.width * .25, Window.height * .2), markup=True)
							if self.Fav_Spells['0']['Type'] == 'Attack':
								self.Monsters_List_Page_btn_CSpell_1[i].bind(on_press=lambda *Args,Move='cast Spell:{}%Target:{}%'.format(self.Fav_Spells['0']['Spell'],Monster): self.API_Send_Move(self.username,self.password,Move,api_key))
							else:
								self.Monsters_List_Page_btn_CSpell_1[i].bind(on_press=lambda *Args,Move='cast Spell:{}%Target:{}%'.format(self.Fav_Spells['0']['Spell'],'all'): self.API_Send_Move(self.username,self.password,Move,api_key))
							self.Monsters_List_Page_Result_2[i].add_widget(self.Monsters_List_Page_btn_CSpell_1[i])

							if len(self.Fav_Spells['1']) == 0:
								fs2_text = 'Attack\nFav0\nNot\nSet!'
							else:
								if MP > 50:
									fs2_text = self.pm("Cast\n :\n--------\n" + re.sub(' ','\n',self.Fav_Spells['1']['Spell']),'fg_lgreen')
								else:
									fs2_text = self.pm("Cast\n :\n--LowMP--\n" + re.sub(' ','\n',self.Fav_Spells['1']['Spell']),'fg_dred')
							self.Monsters_List_Page_btn_CSpell_2[i] = Button(text="{}".format(fs2_text), size=(Window.width * .12, Window.height * .25),font_size='11sp',markup=True)
							
							if self.Fav_Spells['1']['Type'] == 'Attack':
								self.Monsters_List_Page_btn_CSpell_2[i].bind(on_press=lambda *Args,Move='cast Spell:{}%Target:{}%'.format(self.Fav_Spells['1']['Spell'],Monster): self.API_Send_Move(self.username,self.password,Move,api_key))
							else:
								self.Monsters_List_Page_btn_CSpell_2[i].bind(on_press=lambda *Args,Move='cast Spell:{}%Target:{}%'.format(self.Fav_Spells['1']['Spell'],'all'): self.API_Send_Move(self.username,self.password,Move,api_key))
							self.Monsters_List_Page_Result_2[i].add_widget(self.Monsters_List_Page_btn_CSpell_2[i])
			
						else:
							self.Monsters_List_Page_btn_CSpell_2[i] = Button(text="Cast\n :\n--------\n" + re.sub(' ','\n',Spell),font_size='11sp', size=(Window.width * .15, Window.height * .2),markup=True)
							
							if 'target' in self.Fav_Spells[Spell]['Data']['m_type'].lower():
								self.Monsters_List_Page_btn_CSpell_2[i].bind(on_press=lambda *Args,Move='cast Spell:{}%Target:{}%'.format(self.Fav_Spells[Spell]['Spell'],Monster): self.API_Send_Move(self.username,self.password,Move,api_key))
							else:
								self.Monsters_List_Page_btn_CSpell_2[i].bind(on_press=lambda *Args,Move='cast Spell:{}%Target:{}%'.format(self.Fav_Spells[Spell]['Spell'],'all'): self.API_Send_Move(self.username,self.password,Move,api_key))
							self.Monsters_List_Page_Result_2[i].add_widget(self.Monsters_List_Page_btn_CSpell_2[i])
						

						self.Monsters_List_Page_btn_CL[i] = Button(text=self.pm("Look\nCloser!",'fg_yellow'),markup=True, size=(Window.width * .30, Window.height * .2),)
						self.Monsters_List_Page_btn_CL[i].bind(on_press=lambda *Args,PMonster='Details for Monster : {}'.format(Monster),MDetails=self.M_Text_Details[i],backone=True: self.result_PopUP(PMonster,MDetails,backone=backone))
						self.Monsters_List_Page_Result[i].add_widget(self.Monsters_List_Page_btn_CL[i])							
						self.Monsters_List_Page_Result_Final[i].add_widget(self.Monsters_List_Page_Result[i])
						self.Monsters_List_Page_Result_Final[i].add_widget(self.Monsters_List_Page_Result_2[i])
						if (scroll_height < (Window.height / 2)):
							scroll_height = scroll_height + 120
						i += 1

					Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
					Main_result.bind(minimum_height = Main_result.setter('height'))
					Main_result = Main_result.__self__
					for x in range(0,i):
						Main_result.add_widget(self.Monsters_List_Page_Result_Final[x])
						
					scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[23].height - 30), size = (Window.width, scroll_height)) 
					#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
					scrlFBtns.add_widget(Main_result)
					self.result_layout3[23].add_widget(scrlFBtns)

		self.Base_Actions = GridLayout(cols=3, size_hint_y=None, size=(Window.width, Window.height * .2))

		if len(self.Fav_Spells['2']) == 0:
			fs3_text = 'Defense\nFav1\nNot\nSet!'
		else:
			if MP > 50:
				fs3_text = self.pm("Cast\n :\n--------\n" + re.sub(' ','\n',self.Fav_Spells['2']['Spell']),'fg_green')
			else:
				fs3_text = self.pm("Cast\n :\n--LowMP--\n" + re.sub(' ','\n',self.Fav_Spells['2']['Spell']),'fg_red')
		self.Base_Actions_btn_favdspell1 = Button(text=fs3_text, size_hint = (.2,1.5),font_size='11sp',markup=True)

		if self.Fav_Spells['2']['Type'].lower() == 'd_area':
			self.Base_Actions_btn_favdspell1.bind(on_press=lambda *Args,Move='cast Spell:{}%Target:{}%'.format(self.Fav_Spells['2']['Spell'],'all'): self.API_Send_Move(self.username,self.password,Move,api_key))
		else:
			self.Base_Actions_btn_favdspell1.bind(on_press=lambda *Args,spell=Spell: self.PopUp_Spell_Target_Player('Friend',self.Fav_Spells[2]['Spell']))					
		if len(self.CRoom['monsters']) > 0:
			self.Base_Actions_btn_RAttack = Button(text=self.pm("Attack\nNext!",'fg_green'), markup=True, size_hint = (.2,1.5))
		else:
			self.Base_Actions_btn_RAttack = Button(text=self.pm("Attack\nNext!",'fg_black'), markup=True, size_hint = (.2,1.5))
		self.Base_Actions_btn_RAttack.bind(on_press=self.Execute_A)

		if len(self.Fav_Spells['3']) == 0:
			fs4_text = 'Defense\nFav2\nNot\nSet!'
		else:
			if MP > 50:
				fs4_text = self.pm("Cast\n :\n--------\n" + re.sub(' ','\n',self.Fav_Spells['3']['Spell']),'fg_green')
			else:
				fs4_text = self.pm("Cast\n :\n--LowMP--\n" + re.sub(' ','\n',self.Fav_Spells['3']['Spell']),'fg_red')
		self.Base_Actions_btn_favdspell2 = Button(text=fs4_text, size_hint = (.2,1.5),font_size='11sp',markup=True)
		if self.Fav_Spells['3']['Type'].lower() == 'd_area':
			self.Base_Actions_btn_favdspell2.bind(on_press=lambda *Args,Move='cast Spell:{}%Target:{}%'.format(self.Fav_Spells[3]['Spell'],'all'): self.API_Send_Move(self.username,self.password,Move,api_key))
		else:
			self.Base_Actions_btn_favdspell2.bind(on_press=lambda *Args,spell=self.Fav_Spells['3']['Spell']: self.PopUp_Spell_Target_Player('Friend',spell))					

		self.Base_Actions.add_widget(self.Base_Actions_btn_favdspell1)
		self.Base_Actions.add_widget(self.Base_Actions_btn_RAttack)
		self.Base_Actions.add_widget(self.Base_Actions_btn_favdspell2)
		self.result_layout2[23].add_widget(back)
		self.RPopUp3_result_Stats.add_widget(self.Stats_displaym[3])

		self.result_layout[23].add_widget(self.MDD_Layout[2])
		self.result_layout[23].add_widget(self.result_layout4[23])
		self.result_layout[23].add_widget(self.result_layout3[23])
		self.result_layout[23].add_widget(self.RPopUp3_result_Stats)
		self.result_layout[23].add_widget(self.Base_Actions)
		self.result_layout[23].add_widget(self.result_layout2[23])

		self.CMD_result[23].open()

	def PopUp_List_Room_Items(self,func,Spell='Attack_Screen'):
		self.Dismiss_All()
		self.Dismiss_One(1)
		self.API_Refresh_GData(self.username,self.password,api_key)
		self.Play_Sound('Inventory')
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[24] = GridLayout(rows=6, size_hint_y=None, size=(Window.width * .7, Window.height))
		self.result_layout[24] = self.result_layout[24].__self__
		self.result_layout[24].bind(height = self.result_layout[24].setter('top'))
		self.RPopUp4_result_Stats = GridLayout(rows=1, size_hint_y=None, size=(Window.width, Window.height * .19))
		self.RPopUp4_result_Stats = self.RPopUp4_result_Stats.__self__		
		self.result_layout4[24] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout4[24] = self.result_layout4[24].__self__
		self.result_layout4[24].bind(height = self.result_layout4[24].setter('top'))
		self.result_layout4[24].add_widget(result_Mar_MUDLogo)
		self.result_layoutloc = GridLayout(cols=4, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layoutloc = self.result_layoutloc.__self__
		self.result_layout3[24] = BoxLayout(padding=3, orientation='vertical',size_hint=(Window.width - 10, Window.height * .7),size=(Window.width - 10, Window.height * .7))
		self.result_layout3[24] = self.result_layout3[24].__self__
		self.result_layout2[24] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[24] = self.result_layout2[24].__self__
		self.CMD_result[24] = Popup(title='{}'.format(func), content=self.result_layout[24],auto_dismiss=False)
		self.CMD_result[24] = self.CMD_result[24].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__
		
		self.Items_List_Page_Result = {}
		self.Items_List_Page_MSG_Details = {}
		self.Items_List_Page_btn_Take = {}
		self.Items_List_Page_btn_CL = {}		
		self.Item_Details = {}

		self.Object_List_Page_Result = {}
		self.Object_List_Page_MSG_Details = {}
		self.Object_List_Page_btn_CL = {}
		self.Object_Details = {}

		self.Player_List_Page_Result = {}
		self.Player_List_Page_MSG_Details = {}
		self.Player_List_Page_btn_CL = {}

		self.Comps_List_Page_Result = {}
		self.Comps_List_Page_MSG_Details = {}
		self.Comps_List_Page_btn_CL = {}		
		self.Object_D = self.Item_B = self.Item_D = {}		
		z = h = i = j = k = 0
		if self.CRoom != False and self.CRoom != '' and self.CRoom != '{}' and self.CRoom != {}:
			if len(self.CRoom) > 0:
				if 'items' in self.CRoom.keys():
					for Item, Item_Data in self.CRoom['items'].items():
						if Item == '':
							continue
						if Item_Data['item_class'].upper() in ['RW','W']:
							scolor = 'fg_lred'
							bcolor = 'fg_lred'
						elif Item_Data['item_class'].upper() in ['AMMO']:
							scolor = 'fg_dred'
							bcolor = 'fg_dred'
						elif Item_Data['item_class'].upper() == 'P':
							scolor = 'fg_orange'
							bcolor = 'fg_dorange'
						elif Item_Data['item_class'].upper() in ['PG']:
							scolor = 'fg_gold'
							bcolor = 'fg_gold'
						elif Item_Data['item_class'].upper() in ['WK', 'K']:
							scolor = 'fg_lbrown'
							bcolor = 'fg_lbrown'
						elif Item_Data['item_class'].upper() in ['WM', 'PF']:
							scolor = 'fg_lgold'
							bcolor = 'fg_lgold'
						elif Item_Data['item_class'].upper() in ['TD']:
							scolor = 'fg_lyellow'
							bcolor = 'fg_dyellow'
						elif Item_Data['item_class'].upper() in ['CR','SB' ]:
							scolor = 'fg_white'
							bcolor = 'fg_white'
						elif Item_Data['item_class'].upper() in ['CI']:
							scolor = 'fg_lgreen'
							bcolor = 'fg_dgreen'
						elif Item_Data['item_class'].upper() in ['A','PANTS','BOOTS','GLOVES','BRACERS']:
							scolor = 'fg_dcyan'
							bcolor = 'fg_dblue'
						elif Item_Data['item_class'].upper() in ['MW','RING_RIGHT','RING_LEFT','NECKLACE','GLASSES']:
							scolor = 'fg_lred'
							bcolor = 'fg_dred'
						else:
							scolor = 'fg_lgreen'
							bcolor = 'fg_dgreen'
						self.Items_List_Page_Result[i] = GridLayout(cols=3, size_hint_y=None, size=(Window.width * .8, Window.height * .25))
						self.Item_B[i] = self.pm('Item : {0}\nClass: {1}\nValue: {2}\n\n\n'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_class'],4,20),self.split_lines(Item_Data['item_value'],4,20)),scolor)
						self.Item_D[i] = self.pm('Item : {0}\nClass: {1}\nValue: {2}\nDescription: {3}'.format(self.split_lines(Item,4,20),self.split_lines(Item_Data['item_class'],4,20),self.split_lines(Item_Data['item_value'],4,20),self.split_lines(Item_Data['item_description'],4,20)),scolor)
						self.Items_List_Page_MSG_Details[i] = Label(text=self.Item_B[i],halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
						self.Items_List_Page_MSG_Details[i] = self.Items_List_Page_MSG_Details[i].__self__
						self.Items_List_Page_Result[i].add_widget(self.Items_List_Page_MSG_Details[i])
						
						self.Items_List_Page_btn_Take[i] = Button(text=self.pm("Take!",bcolor),markup=True, size_hint = (.2,Window.height * .2))
						self.Items_List_Page_btn_Take[i].bind(on_press=lambda *Args,Move='take {}'.format(Item): self.API_Send_Move(self.username,self.password,Move,api_key))
						self.Items_List_Page_Result[i].add_widget(self.Items_List_Page_btn_Take[i])

						self.Items_List_Page_btn_CL[i] = Button(text=self.pm("Look\nCloser!",'fg_yellow'),markup=True, size_hint = (.2,Window.height * .2))
						self.Items_List_Page_btn_CL[i].bind(on_press=lambda *Args,PItem='Details for item : {}'.format(Item),PItem_Details=self.Item_D[i],backone=True: self.result_PopUP(PItem,PItem_Details,backone=backone))
						self.Items_List_Page_Result[i].add_widget(self.Items_List_Page_btn_CL[i])						
						z += 1					
						i += 1

					for Object, Object_Data in self.CRoom['objects'].items():
						if Object == '':
							continue
						self.Object_List_Page_Result[h] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .8, Window.height * .2))
						self.Object_D[i] = "Name: {} \n Description: {}".format(self.split_lines(Object,4,20),self.split_lines(Object_Data,4,80))
						self.Object_List_Page_MSG_Details[h] = Label(text=self.pm('Object : {0}\n\n\n\n'.format(self.split_lines(Object,4,80)),'fg_white'),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
						self.Object_List_Page_MSG_Details[h] = self.Object_List_Page_MSG_Details[h].__self__
						self.Object_List_Page_MSG_Details[h].text_size=self.Object_List_Page_MSG_Details[h].size
						self.Object_List_Page_btn_CL[h] = Button(text=self.pm("Look\nCloser!",'fg_yellow'),markup=True, size_hint = (.2,Window.height * .2))
						self.Object_List_Page_btn_CL[h].bind(on_press=lambda *Args,PItem='Details for Object : {}'.format(Object),PItem_Details=self.Object_D[i],backone=True: self.result_PopUP(PItem,PItem_Details,backone=backone))
						self.Object_List_Page_Result[h].add_widget(self.Object_List_Page_MSG_Details[h])
						self.Object_List_Page_Result[h].add_widget(self.Object_List_Page_btn_CL[h])						

						z += 1					
						h += 1

					for Player, Player_Data in self.Player_Details.items():
						if Player == '':
							continue
						self.Player_List_Page_Result[j] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .9, Window.height * .2))
						self.Player_List_Page_MSG_Details[j] = Label(text=self.pm('Player : {}\nHP: {}\nAT: {} | DF {}'.format(self.split_lines(Player,4,20),self.split_lines(Player_Data['HP'],4,20),self.split_lines(Player_Data['At'],4,20),self.split_lines(Player_Data['Df'],4,20)),'fg_cyan'),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
						self.Player_List_Page_MSG_Details[j] = self.Player_List_Page_MSG_Details[j].__self__
						self.Player_List_Page_MSG_Details[j].text_size=self.Player_List_Page_MSG_Details[j].size
						self.Player_List_Page_Result[j].add_widget(self.Player_List_Page_MSG_Details[j])
						if Player.lower() == self.username.lower():
							Player = 'myself'
						self.Player_List_Page_btn_CL[j] = Button(text=self.pm("Look\nCloser!",'fg_yellow'),markup=True, size_hint = (.2,Window.height * .2))
						self.Player_List_Page_btn_CL[j].bind(on_press=lambda *Args,Move='look {}'.format(Player): self.API_Send_Move(self.username,self.password,Move,api_key))
						self.Player_List_Page_Result[j].add_widget(self.Player_List_Page_btn_CL[j])
						z += 1
						j += 1

					for Companion, Companion_Data in self.CRoom['Comps'].items():
						if Companion == '':
							continue
						self.Comps_List_Page_Result[k] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .9, Window.height * .2))
						self.Comps_List_Page_MSG_Details[k] = Label(text=self.pm('Companion : {}\nHP: {}\nAT: {} | DF: {}\n\n\n'.format(self.split_lines(Companion,4,20),self.split_lines(Companion_Data['stats'][0],4,20),self.split_lines(Companion_Data['stats'][1],4,20),self.split_lines(Companion_Data['stats'][2],4,20)),'fg_magenta'),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
						self.Comps_List_Page_MSG_Details[k] = self.Comps_List_Page_MSG_Details[k].__self__
						self.Comps_List_Page_MSG_Details[k].text_size=self.Comps_List_Page_MSG_Details[k].size
						self.Comps_List_Page_Result[k].add_widget(self.Comps_List_Page_MSG_Details[k])

						self.Comps_List_Page_btn_CL[k] = Button(text=self.pm("Look\nCloser!",'fg_yellow'),markup=True, size_hint = (.2,Window.height * .2))
						self.Comps_List_Page_btn_CL[k].bind(on_press=lambda *Args,Move='look {}'.format(Companion): self.API_Send_Move(self.username,self.password,Move,api_key))
						self.Comps_List_Page_Result[k].add_widget(self.Comps_List_Page_btn_CL[k])
						z += 1
						k += 1

					for Companion, Companion_Data in self.CRoom['Cmons'].items():
						if Companion == '':
							continue
						self.Comps_List_Page_Result[k] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .9, Window.height * .2))
						self.Comps_List_Page_MSG_Details[k] = Label(text=self.pm('Companion : {}\nHP: {}\nAT: {} | DF: {} | Turns: {}\n\n\n'.format(self.split_lines(Companion,4,20),self.split_lines(Companion_Data['stats'][0],4,20),self.split_lines(Companion_Data['stats'][1],4,20),self.split_lines(Companion_Data['stats'][2],4,20),self.split_lines(Companion_Data['turns'])),'fg_magenta'),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .2))				
						self.Comps_List_Page_MSG_Details[k] = self.Comps_List_Page_MSG_Details[k].__self__
						self.Comps_List_Page_MSG_Details[k].text_size=self.Comps_List_Page_MSG_Details[k].size
						self.Comps_List_Page_Result[k].add_widget(self.Comps_List_Page_MSG_Details[k])

						self.Comps_List_Page_btn_CL[k] = Button(text=self.pm("Look\nCloser!",'fg_yellow'),markup=True, size_hint = (.2,Window.height * .2))
						self.Comps_List_Page_btn_CL[k].bind(on_press=lambda *Args,Move='look {}'.format(Companion): self.API_Send_Move(self.username,self.password,Move,api_key))
						self.Comps_List_Page_Result[k].add_widget(self.Comps_List_Page_btn_CL[k])
						z += 1
						k += 1

					if (scroll_height < (Window.height / 2)):
							scroll_height = scroll_height + 120

					Main_result = GridLayout(rows=z, size_hint_y=None, size=(Window.width, Window.height * .9))
					Main_result.bind(minimum_height = Main_result.setter('height'))
					Main_result = Main_result.__self__
					
					for x in range(0,j):
						Main_result.add_widget(self.Player_List_Page_Result[x])				

					for x in range(0,h):
						Main_result.add_widget(self.Object_List_Page_Result[x])				

					for x in range(0,i):
						Main_result.add_widget(self.Items_List_Page_Result[x])

					for x in range(0,k):
						Main_result.add_widget(self.Comps_List_Page_Result[x])						

					scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[24].height - 30), size = (Window.width, scroll_height)) 
					#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
					scrlFBtns.add_widget(Main_result)
					self.result_layout3[24].add_widget(scrlFBtns)

		self.Base_Actions_btn_TakeAll = Button(text="Take\nAll\nItems!", size_hint = (.2,1.5))
		self.Base_Actions_btn_TakeAll.bind(on_press=self.Execute_GA)
		self.result_layout2[24].add_widget(back)
		self.result_layout2[24].add_widget(self.Base_Actions_btn_TakeAll)

		self.RPopUp4_result_Stats.add_widget(self.Stats_displaym[3])

		self.result_layout[24].add_widget(self.MDD_Layout[2])
		self.result_layout[24].add_widget(self.result_layout4[24])
		self.result_layout[24].add_widget(self.result_layout3[24])		
		self.result_layout[24].add_widget(self.RPopUp4_result_Stats)
		self.result_layout[24].add_widget(self.result_layout2[24])

		self.CMD_result[24].open()


	def result_PopUP_Confirm(self,func,result,msg='all'):
		self.Dismiss_All()
		##print(result)
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[25] =  GridLayout(rows=4)
		self.result_layout[25].bind(height = self.result_layout[25].setter('top'))
		self.result_layout[25] = self.result_layout[25].__self__
		self.result_layout[25].bind(height = self.result_layout[25].setter('top'))
		self.result_layout4[25] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .7, Window.height * .2))
		self.result_layout4[25] = self.result_layout4[25].__self__
		self.result_layout4[25].bind(height = self.result_layout[25].setter('top'))
		self.result_layout4[25].add_widget(result_Mar_MUDLogo)
		self.result_layout3[25] = BoxLayout(padding=3, orientation='vertical',size_hint=(Window.width - 10, Window.height * .7),size=(Window.width - 10, Window.height * .7))
		self.result_layout3[25] = self.result_layout3[25].__self__
		self.result_layout2[25] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.result_layout2[25] = self.result_layout2[25].__self__
		self.CMD_result[25] = Popup(title='Delete {0} Confirmation Page'.format(func), content=self.result_layout[25],auto_dismiss=False)
		self.CMD_result[25] = self.CMD_result[25].__self__
		if msg == 'all':
			self.ConfirmText = Label(text='Are you sure you want to delete all messages?',halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .5))				
		else:
			self.ConfirmText = Label(text='Are you sure you want to delete message {}?'.format(msg),halign='left',font_size='12sp', markup = True,size=(Window.width * .5, Window.height * .5))				

		delall = Button(text='Confirm\nDelete!',size_hint = (1,3))
		delall.bind(on_press=lambda *Args,Indx=msg: self.API_Phone(self.username,self.password,'dtext',Indx,'',api_key))
		delall = delall.__self__
		back = Button(text=self.pm("Cancle!",'fg_lred'),markup=True,size_hint = (1,1))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__

		self.result_layout2[25].add_widget(back)
		self.result_layout2[25].add_widget(delall)
		self.result_layout[25].add_widget(self.MDD_Layout[2])
		self.result_layout[25].add_widget(self.result_layout4[25])
		self.result_layout[25].add_widget(self.result_layout3[25])

		self.result_layout[25].add_widget(self.result_layout2[25])

		self.CMD_result[25].open()

	def restart(self,btn):
		self.Dismiss_All()
		self.CMD_Prompt('')
		self.ROOM_INFO.text = self.RoomDetails
		self.Dismiss_All()

	def quit(self,btn):
		self.PLogout(self.username,self.password,api_key)		
		self.Dismiss_All()
		sys.exit(0)

	def Repeat_CMD(self,btn):
		self.Dismiss_All()
		self.move = self.CMD_IN.text = self.repeat_cmd
		self.Dismiss_All()
		self.Execute_CMD(btn)
		# self.on_move(self.move,self.move)

	def Execute_Rest(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Rest')
		self.move = self.CMD_IN.text = 'rest'
		self.Execute_CMD(btn)

	def Execute_N(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Walking')
		self.move = self.CMD_IN.text = 'N'
		self.Execute_CMD(btn)
		# self.on_move(self.move,self.move)


	def Execute_S(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Walking')
		self.move = self.CMD_IN.text = 'S'
		self.Execute_CMD(btn)
		# self.on_move(self.move,self.move)


	def Execute_E(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Walking')
		self.move = self.CMD_IN.text = 'E'
		self.Execute_CMD(btn)
		# self.on_move(self.move,self.move)

	def Execute_W(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Walking')
		self.move = self.CMD_IN.text = 'W'
		self.Execute_CMD(btn)
		# self.on_move(self.move,self.move)


	def Execute_U(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Climbing')
		self.move = self.CMD_IN.text = 'U'
		self.Execute_CMD(btn)
		# self.on_move(self.move,self.move)

	def Execute_D(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Climbing')
		self.move = self.CMD_IN.text = 'D'
		self.Execute_CMD(btn)
		# self.on_move(self.move,self.move)

	def Execute_GA(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Pickup')
		self.move = self.CMD_IN.text = 'get all'
		self.Execute_CMD(btn)
		# self.on_move(self.move,self.move)

	def Execute_Inv(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Inventory')
		self.move = self.CMD_IN.text = 'inventory'
		self.API_List_Inv(self.username,self.password,api_key)
		# self.on_move(self.move,self.move)

	def Execute_A(self,btn):
		self.Dismiss_All()
		self.Play_Sound('Sword')
		self.move = self.CMD_IN.text = 'rhit'
		self.Execute_CMD(btn)

	def Execute_CMD(self,btn):
		self.Dismiss_All()
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True		
		self.result_layout4[26] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .5, Window.height * .2))
		self.result_layout4[26] = self.result_layout4[26].__self__
		self.result_layout4[26].add_widget(result_Mar_MUDLogo)
		self.result_layout[26] =  GridLayout(rows=4, size_hint_y=None, size=(Window.width, Window.height))
		self.result_layout3[26] = GridLayout(cols=3, size_hint_y=None, size=(Window.width, Window.height * .5))
		self.result_layout3[26].bind(height = self.result_layout3[26].setter('top'))
		self.result_layout2[26] = GridLayout(cols=2, size_hint_y=None, size=(Window.width, Window.height * .08))
		self.EXE_CMD_result_Stats =  GridLayout(cols=1, size_hint_y=None, size=(Window.width, Window.height * .16))
		self.repeat_cmd = self.move
		dead,result = self.CMD_Prompt(str(self.move))
		result = '\n' + self.Paint_SVAR('Your Move result: ','fg_cyan','bg_black') + '\n' + str(self.split_lines(str(result),4,100))
		Res_Scroll1 = ScrolllabelLabel(text=result)
		Res_Scroll1.text_size = Res_Scroll1.size
		self.result_layout3[26].add_widget(Res_Scroll1)
		if dead == False:
			self.CMD_result[26] = Popup(title='Your move result.', content=self.result_layout,auto_dismiss=False, markup=True,size_hint=(1,None))
			# Res_Scroll1 = ScrollView(size_hint=(700, 300), size=(700, 300),text_size=(700, 300), do_scroll_x = True, pos_hint={'center_x': .5, 'center_y': .5})
			# rtitle = Label(text=result,font_size='12sp',valign='top',text_size=(700, None), markup = True)
			# Res_Scroll1.add_widget(rtitle)
			restart = Button(text='Restart',size_hint = (1,2))
			quit = Button(text='Quit',size_hint = (1,2))
			restart.bind(on_press=self.Dismiss_All)
			quit.bind(on_press=self.Logout_Script)
			self.result_layout2[26].add_widget(restart)
			self.result_layout2[26].add_widget(quit)
		else:
			self.CMD_result[26] = Popup(title='', content=self.result_layout[26],auto_dismiss=False)
			content = Button(text='Done!',size_hint = (1,1.5))
			content.bind(on_press=self.Dismiss_All)
			repeat = Button(text='Repeat last!',size_hint = (1,1.5))
			repeat.bind(on_press=self.Repeat_CMD)
			self.result_layout2[26].add_widget(repeat)
			self.result_layout2[26].add_widget(content)
		self.EXE_CMD_result_Stats.add_widget(self.Stats_displaym[3]) 
		self.result_layout[26].add_widget(self.result_layout4[26])
		self.result_layout[26].add_widget(self.result_layout3[26])
		self.result_layout[26].add_widget(self.EXE_CMD_result_Stats)
		self.result_layout[26].add_widget(self.result_layout2[26])
		
		self.CMD_result[26].open()
		self.CMD_IN.text = ''
		

	def CMD_Prompt(self,Move):
		self.returned_values == False
		dead = True
		trap = False
		self.repeat_cmd = Move
		self.Execute_API_SM_Muted(Move)
		self.CMD_IN.text = ''
		# while(self.returned_values == False):
		# 	time.sleep(.3)
		output_return = self.MoveDetails
		return dead,output_return


	def Dismiss_One(self,index,bulk=False):
		if bulk == False:
			try:
				self.Dismiss_All_Stats_Screen()
			except:
				pass
		try:
			self.result_layout[index].remove_widget(self.MDD_Layout[2]) 
		except:
			pass						
		try:
			self.result_layout[index].remove_widget(self.MDD_Layout[4])
		except:
			pass		
		try:
			self.CMD_result[index].dismiss()
		except:
			pass

	def Dismiss_All(self,*args):
		try:
			self.Dismiss_All_Stats_Screen()
		except:
			pass
		for x in range(0,30):
			self.Dismiss_One(x,True)


	def Dismiss_All_Stats_Screen(self,*Args):
		try: 
			self.EXE_CMD_result_Stats.remove_widget(self.Stats_displaym[3]) 
		except:
			pass
		try: 
			self.RPopUp_result_Stats.remove_widget(self.Stats_displaym[5]) 
		except:
			pass
		try: 
			self.RPopUp1_result_Stats.remove_widget(self.Stats_displaym[3]) 
		except:
			pass
		try: 
			self.RPopUp2_result_Stats.remove_widget(self.Stats_displaym[3]) 
		except:
			pass
		try: 
			self.RPopUp3_result_Stats.remove_widget(self.Stats_displaym[3]) 
		except:
			pass						
		try: 
			self.RPopUp4_result_Stats.remove_widget(self.Stats_displaym[3]) 
		except:
			pass								

	def Execute_API_SM(self,move):
		self.Dismiss_All()
		if 'auto' in move:
			move = re.sub('auto ','',move)
			self.repeat_cmd = move
			if 'invite' in move:
				move = move + ' {}'.format(self.STarget)
			elif move in ['send item','give']:
				move = move + ' {} {}'.format(self.STarget,self.GItem)
		self.API_Send_Move(self.username,self.password,move,api_key)
		# self.result_PopUP('Move result :',self.MoveDetails)
		self.changeScreenBack()

	def Execute_API_SM_Muted(self,move):
		self.Dismiss_All()		
		if 'auto' in move:
			move = re.sub('auto ','',move)
			self.repeat_cmd = move
			if 'invite' in move:
				move = move + ' {}'.format(self.STarget)
			elif move in ['send item','give item']:
				move = move + ' {} {}'.format(self.STarget,self.GItem)
		self.API_Send_Move_Muted(self.username,self.password,move,api_key)
		self.changeScreenBack()

################################################################
##						 Play Audio						 	  ##
################################################################
	def Mute_Sound(self,onoff):
		if onoff == False:
			self.MUTE_SOUND = False
		else:
			self.MUTE_SOUND = True	

	def Pre_Load_Sounds(self):
		self.MUTE_SOUND = False
		#print('Loading Sounds L')
		#print('-  Loading Sword')
		self.SwordClash = SoundLoader.load('./data/Swords1.ogg')
		#print('-  Loading Sword2')
		self.SwordClash2 = SoundLoader.load('./data/Swords2.ogg')
		#print('-  Loading Sword3')
		self.SwordClash3 = SoundLoader.load('./data/Swords3.ogg')
		#print('-  Loading M1')
		self.MonsterGrowl = SoundLoader.load('./data/MonsterG.ogg')
		#print('-  Loading M2')
		self.MonsterGrowl2 = SoundLoader.load('./data/MonsterG2.ogg')
		#print('-  Loading Magic')
		self.CastMagic = SoundLoader.load('./data/CastMagic.ogg')
		#print('-  Loading Magic2')
		self.CastMagic2 = SoundLoader.load('./data/Magic2.ogg')
		#print('-  Loading Magic3')
		self.CastMagic3 = SoundLoader.load('./data/Magic3.ogg')
		#print('-  Loading Magic4')
		self.CastMagic4 = SoundLoader.load('./data/Magic4.ogg')	
		#print('-  Loading Inv')
		self.InventoryShuffle = SoundLoader.load('./data/Inventory.ogg')
		#print('-  Loading Inv2')
		self.InventoryShuffle2 = SoundLoader.load('./data/Inventory2.ogg')
		#print('-  Loading portal1')
		self.Portal1 = SoundLoader.load('./data/Portal1.ogg')
		#print('-  Loading portal2')
		self.Portal2 = SoundLoader.load('./data/Portal2.ogg')		
		#print('-  Loading climb1')
		self.Climbing1 = SoundLoader.load('./data/Climbing1.ogg')
		#print('-  Loading climb1')
		self.Climbing2 = SoundLoader.load('./data/Climbing2.ogg')
		#print('-  Loading climb1')
		self.Climbing3 = SoundLoader.load('./data/Climbing3.ogg')
		#print('-  Loading pick1')
		self.Pickup1 = SoundLoader.load('./data/Pickup1.ogg')
		#print('-  Loading pick2')
		self.Pickup2 = SoundLoader.load('./data/Pickup2.ogg')
		#print('-  Loading pick3')
		#print('-  Walking')
		self.Walking = SoundLoader.load('./data/Walking.ogg')
		#print('-  Walking2')
		self.Walking2 = SoundLoader.load('./data/Walking2.ogg')		
		#print('-  Walking3')
		self.Walking3 = SoundLoader.load('./data/Walking3.ogg')				
		#print('-  Theme 1')
		self.Theme1 = SoundLoader.load('./data/Theme1.ogg')
		#print('-  Theme 2')
		self.Theme2 = SoundLoader.load('./data/Theme2.ogg')			
		#print('-  Theme 3')
		self.Theme3 = SoundLoader.load('./data/Theme3.ogg')			

	def Play_Sound(self,Sound):
		if self.MUTE_SOUND == False:
			myrand = random.randint(0,10)
			if Sound == 'Sword':
				if myrand % 3 == 0:
					self.SwordClash2.play()
				elif myrand % 2 == 0:
					self.SwordClash3.play()				
				else:
					self.SwordClash.play()
			elif Sound == 'Inventory':
				if myrand % 2 == 0:
					self.InventoryShuffle.play()
				else:
					self.InventoryShuffle2.play()
			elif Sound == 'Magic_Menu':
				self.CastMagic.play()

			elif Sound == 'Cast_Magic':		
				if myrand % 3 == 0:
					self.CastMagic2.play()
				elif myrand % 2 == 0:
					self.CastMagic3.play()
				else:
					self.CastMagic4.play()		

			elif Sound == 'Walking':
				if myrand % 3 == 0:
					self.Walking.play()
				elif myrand % 2 == 0:
					self.Walking2.play()
				else:
					self.Walking3.play()

			elif Sound == 'Pickup':
				if myrand % 2 == 0:
					self.Pickup1.play()
				else:
					self.Pickup2.play()		

			elif Sound == 'Climbing':
				if myrand % 3 == 0:
					self.Climbing1.play()
				elif myrand % 2 == 0:
					self.Climbing2.play()					
				else:
					self.Climbing3.play()

			elif Sound == 'Portal':
				if myrand % 2 == 0:
					self.Portal1.play()
				else:
					self.Portal2.play()

			elif Sound == 'Registration':
				if self.MUTE_MUSIC == False:
					self.Theme1.stop()
					self.Theme2.stop()
					self.Theme3.loop=True
					self.Theme3.play()					
			elif Sound == 'Startup':
				if self.MUTE_MUSIC == False:
					self.Theme2.stop()
					self.Theme3.stop()
					self.Theme1.loop=True
					self.Theme1.play()
			elif Sound == 'Main_Theme':
				if self.MUTE_MUSIC == False:
					self.Theme1.stop()
					self.Theme3.stop()
					self.Theme2.loop=True
					self.Theme2.play()
			elif Sound == 'MonsterG':
				if random.randint(1,10) % 2 == 0:
					self.MonsterGrowl.play()
				else:
					self.MonsterGrowl2.play()


################################################################
##					 Screen Changes						 ##
################################################################

	def changeScreenAttack(self,*Args):
		self.Play_Sound('Sword')
		self.API_Refresh_GData(self.username,self.password,api_key)
		self.PopUp_List_Monsters_SP('Attack Menu','Attack_Screen')

	def changeScreenItems(self,*Args):		
		self.Play_Sound('Inventory')
		self.API_Refresh_GData(self.username,self.password,api_key)
		self.PopUp_List_Room_Items('Items. Players. Objects.','')

	def changeScreenDGPS(self,*Args):
		self.Play_Sound('Portal')
		self.returned_values = False
		self.API_DGPS(self.username,self.password,'locate',self.Warp_Location,api_key)

	def changeScreenaDGPS(self,*Args):
		self.Play_Sound('Portal')
		self.returned_values = False
		self.API_aDGPS(self.username,self.password,'locate',self.Warp_Location,api_key)

	def changeScreenPhone(self,*Args):
		self.API_Phone(self.username,self.password,'ctext','','',api_key)
		if self.ROSIE_MENU == True or self.ROSIE_MENU == 'True':
			#print('in rosie menu')
			if self.RMU == False:
				#print('in rosie menu build')
				self.Admin_Phone_Main()
				self.RMU = True
			self.root.current = 'Admin_Phone_Main'	
		else:
			self.returned_values = False
			# while self.returned_values == False:
			# 	time.sleep(.3)
			self.root.current = 'Phone_Main'

	def changeScreenROSIE(self,*Args):
		self.returned_values = False
		self.root.current = 'ROSIE_Main'		

	def changeScreenLogin(self,*Args):
		self.Play_Sound('Startup')
		self.returned_values = False
		###threading.Thread(target=self.Loading_PopUP()).start()
		self.password = ''
		self.username = ''
		self.root.current = 'Login_Page'

	def changeScreenBack(self,*Args):
		self.returned_values = False
		###threading.Thread(target=self.Loading_PopUP()).start()).start()
		self.root.current = 'Main_Page'

	def changeScreenFailed(self,*Args):
		self.root.current = 'Login_Failed'

	def changeScreenRegister(self,*Args):
		self.Play_Sound('Registration')
		self.root.current = 'Reg_Page'
	
				
################################################################
##						Scripts							 ##
################################################################

	def split_lines(self, data,scount=4,l_limit=40):
		if type(data) == int:
			return data
		if type(data) != str:
			return data
		data = str(self.unescape_r(str(data)))
		sdata = data.split(' ')
		count = len(sdata)
		if count >= scount:
			lcount = 0
			rdata = ''
			for word in sdata:
				wlen = len(word) + 1
				if lcount + wlen > l_limit:
					rdata += '\n' + word  + ' '
					lcount = wlen
				else: 
					rdata +=  word + ' '
					lcount += wlen
			return rdata
		else:
			return data

	def Update_Main_Buttons(self):
		if self.CRoom['MU'].upper() == 'Y':
			self.btnU.text = self.Paint_SVAR('Go\nU!','fg_green','bg_black')
		else:
			if self.CRoom['MU'].upper() == 'L':
				self.btnU.text = self.Paint_SVAR('Go\nU!','fg_red','bg_black')			
			else:	
				self.btnU.text = self.Paint_SVAR('Go\nU!','fg_black','bg_black')
		if self.CRoom['MD'].upper() == 'Y':
			self.btnD.text = self.Paint_SVAR('Go\nD!','fg_green','bg_black')
		else:
			if self.CRoom['MD'].upper() == 'L':
				self.btnD.text = self.Paint_SVAR('Go\nD!','fg_red','bg_black')			
			else:				
				self.btnD.text = self.Paint_SVAR('Go\nD!','fg_black','bg_black')						
		if self.CRoom['MN'].upper() == 'Y':
			self.btnN.text = self.Paint_SVAR('Go\nN!','fg_green','bg_black')
		else:
			if self.CRoom['MN'].upper() == 'L':
				self.btnN.text = self.Paint_SVAR('Go\nN!','fg_red','bg_black')		
			else:	
				self.btnN.text = self.Paint_SVAR('Go\nN!','fg_black','bg_black')			
		if self.CRoom['MS'].upper() == 'Y':
			self.btnS.text = self.Paint_SVAR('Go\nS!','fg_green','bg_black')
		else:
			if self.CRoom['MS'].upper() == 'L':
				self.btnS.text = self.Paint_SVAR('Go\nS!','fg_red','bg_black')
			else:				
				self.btnS.text = self.Paint_SVAR('Go\nS!','fg_black','bg_black')
		if self.CRoom['MW'].upper() == 'Y':
			self.btnW.text = self.Paint_SVAR('Go\nW!','fg_green','bg_black')
		else:
			if self.CRoom['MW'].upper() == 'L':
				self.btnW.text = self.Paint_SVAR('Go\nW!','fg_red','bg_black')		
			else:				
				self.btnW.text = self.Paint_SVAR('Go\nW!','fg_black','bg_black')			
		if self.CRoom['ME'].upper() == 'Y':
			self.btnE.text = self.Paint_SVAR('Go\nE!','fg_green','bg_black')
		else:
			if self.CRoom['ME'].upper() == 'L':
				self.btnN.text = self.Paint_SVAR('Go\nN!','fg_red','bg_black')			
			else:				
				self.btnE.text = self.Paint_SVAR('Go\nE!','fg_black','bg_black')
		if len(self.CRoom['items']) > 0:
			self.btnGA.text = self.Paint_SVAR('Get\nAll!','fg_green','bg_black')
		else:
			self.btnGA.text = self.Paint_SVAR('Get\nAll!','fg_black','bg_black')			
		if len(self.CRoom['monsters']) > 0:
			self.btnA.text = self.Paint_SVAR('Attack!','fg_green','bg_black')
		else:
			self.btnA.text = self.Paint_SVAR('Attack!','fg_black','bg_black')			

	def clear_screen(self):
		# Clear command as function of OS
		command = "cls" if platform.system().lower()=="windows" else "clear"

		# Action
		os.system(command)

	def Paint_Brush(self,Selected_Color):
		Selected_Color = Selected_Color.lower()
		if Selected_Color == 'reset':
			reset='[/color]'
			return reset
		if Selected_Color == 'bold':
			bold='[b]'
			return bold
		if Selected_Color == 'italics':
			italics='[i]'
			return italics
		if Selected_Color == 'underline':
			underline='[u]'
			return underline
		if Selected_Color == 'strikethrough':
			strikethrough='[s]'
			return strikethrough
		if Selected_Color == 'bold_off':
			bold_off='[/b]'
			return bold_off
		if Selected_Color == 'italics_off':
			italics_off='[/i]'
			return italics_off
		if Selected_Color == 'underline_off':
			underline_off='[/u]'
			return underline_off
		if Selected_Color == 'strikethrough_off':
			strikethrough_off='[/s]'
			return strikethrough_off
		if Selected_Color == 'fg_dblack':
			fg_dblack='[color=#000000]'
			return fg_dblack
		if Selected_Color == 'fg_black':
			fg_black='[color=#2F2F2F]'
			return fg_black			
		if Selected_Color == 'fg_red':
			fg_red='[color=#FF0000]'
			return fg_red
		if Selected_Color == 'fg_dred':
			fg_dred='[color=#990000]'
			return fg_dred		
		if Selected_Color == 'fg_lred':
			fg_lred='[color=#FF6666]'
			return fg_lred						
		if Selected_Color == 'fg_green':
			fg_green='[color=#7FFF00]'
			return fg_green
		if Selected_Color == 'fg_dgreen':
			fg_dgreen='[color=#336600]'
			return fg_dgreen		
		if Selected_Color == 'fg_lgreen':
			fg_lgreen='[color=#66FF66]'
			return fg_lgreen						
		if Selected_Color == 'fg_yellow':
			fg_yellow='[color=#FFFF00]'
			return fg_yellow
		if Selected_Color == 'fg_dyellow':
			fg_dyellow='[color=#CCCC00]'
			return fg_dyellow			
		if Selected_Color == 'fg_lyellow':
			fg_lyellow='[color=#FFFF66]'
			return fg_lyellow			
		if Selected_Color == 'fg_grey':
			fg_grey='[color=#A0A0A0]'
			return fg_grey			
		if Selected_Color == 'fg_dgrey':
			fg_dgrey='[color=#606060]'
			return fg_dgrey		
		if Selected_Color == 'fg_lgrey':
			fg_lgrey='[color=#C0C0C0]'
			return fg_lgrey						
		if Selected_Color == 'fg_purple':
			fg_purple='[color=#990099]'
			return fg_purple			
		if Selected_Color == 'fg_dpurple':
			fg_dpurple='[color=#660066]'
			return fg_dpurple	
		if Selected_Color == 'fg_lpurple':
			fg_lpurple='[color=#9933FF]'
			return fg_lpurple						
		if Selected_Color == 'fg_gold':
			fg_gold='[color=#999900]'
			return fg_gold
		if Selected_Color == 'fg_dgold':
			fg_dgold='[color=#666600]'
			return fg_dgold	
		if Selected_Color == 'fg_lgold':
			fg_lgold='[color=#CCCC00]'
			return fg_lgold								
		if Selected_Color == 'fg_orange':
			fg_orange='[color=#FF9933]'
			return fg_orange
		if Selected_Color == 'fg_dorange':
			fg_dorange='[color=#CC6600]'
			return fg_dorange
		if Selected_Color == 'fg_lorange':
			fg_lorange='[color=#FFB266]'
			return fg_lorange
		if Selected_Color == 'fg_blue':
			fg_blue='[color=#000066]'
			return fg_blue
		if Selected_Color == 'fg_dblue':
			fg_dblue='[color=#0000FF]'
			return fg_dblue
		if Selected_Color == 'fg_dcyan':
			fg_dcyan='[color=#3399FF]'
			return fg_dcyan				
		if Selected_Color == 'fg_pink':
			fg_pink='[color=#DD33DD]'
			return fg_pink			
		if Selected_Color == 'fg_dpink':
			fg_dpink='[color=#CC0066]'
			return fg_dpink	
		if Selected_Color == 'fg_lpink':
			fg_lpink='[color=#FF99FF]'
			return fg_lpink									
		if Selected_Color == 'fg_magenta':
			fg_magenta='[color=#FF00FF]'
			return fg_magenta
		if Selected_Color == 'fg_dmagenta':
			fg_dmagenta='[color=#CC00CC]'
			return fg_dmagenta		
		if Selected_Color == 'fg_lmagenta':
			fg_lmagenta='[color=#FF66FF]'
			return fg_lmagenta						
		if Selected_Color == 'fg_cyan':
			fg_cyan='[color=#00FFFF]'
			return fg_cyan
		if Selected_Color == 'fg_dcyan':
			fg_dcyan='[color=#009999]'
			return fg_dcyan	
		if Selected_Color == 'fg_lcyan':
			fg_lcyan='[color=#33FFFF]'
			return fg_lcyan	
		if Selected_Color == 'fg_brown':
			fg_brown='[color=#663300]'
			return fg_brown
		if Selected_Color == 'fg_dbrown':
			fg_dbrown='[color=#660000]'
			return fg_dbrown	
		if Selected_Color == 'fg_lbrown':
			fg_lbrown='[color=#994C00]'
			return fg_lbrown	
		if Selected_Color in ['fg_white','fg_lwhite']:
			fg_white='[color=#FFFFFF]'
			return fg_white
		if Selected_Color == 'fg_dwhite':
			fg_white='[color=#E0E0E0]'
			return fg_white			
		if Selected_Color == 'bg_black':
			bg_black=''
			return bg_black
		if Selected_Color == 'bg_red':
			bg_red=''
			return bg_red
		if Selected_Color == 'bg_green':
			bg_green=''
			return bg_green
		if Selected_Color == 'bg_yellow':
			bg_yellow=''
			return bg_yellow
		if Selected_Color == 'bg_blue':
			bg_blue=''
			return bg_blue
		if Selected_Color == 'bg_magenta':
			bg_magenta=''
			return bg_magenta
		if Selected_Color == 'bg_cyan':
			bg_cyan=''
			return bg_cyan
		if Selected_Color == 'bg_white':
			bg_white=''
			return bg_white
		if Selected_Color == 'bg_default':
			bg_default=''
			return bg_default
		else:
			bg_default=''
			return bg_default

		return

	def Show_Palet_GE(self,*Args):		
		Move = '_rr_palet {}'.format(self.ROSIE_PW)
		self.API_Send_Move(self.username,self.password,Move,api_key)

	def Show_Palet(self,func,result):
		self.Dismiss_All()
		scroll_height = 0
		result_Mar_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		result_Mar_MUDLogo = result_Mar_MUDLogo.__self__
		result_Mar_MUDLogo.allow_stretch = True
		result_Mar_MUDLogo.keep_ratio = True
		self.result_layout[27] = GridLayout(rows=3, size_hint_y=None, size=(Window.width * .9, Window.height))
		self.result_layout[27].bind(height = self.result_layout[27].setter('top'))
		self.result_layout[27] = self.result_layout[27].__self__
		self.result_layout[27].bind(height = self.result_layout[27].setter('top'))
		self.result_layout4[27] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .9, Window.height * .2))
		self.result_layout4[27] = self.result_layout4[27].__self__
		self.result_layout4[27].bind(height = self.result_layout[27].setter('top'))
		self.result_layout4[27].add_widget(result_Mar_MUDLogo)
		self.result_layout3[27] = BoxLayout(padding=3, orientation='vertical',size_hint=(Window.width - 20, Window.height * .65),size=(Window.width - 10, Window.height * .7))
		self.result_layout3[27] = self.result_layout3[27].__self__
		self.result_layout2[27] = GridLayout(cols=1, size_hint_y=None, size=(Window.width * .7, Window.height * .1))
		self.result_layout2[27] = self.result_layout2[27].__self__
		self.CMD_result[29] = Popup(title='result for {0} Call'.format(func), content=self.result_layout[27],auto_dismiss=False)
		self.CMD_result[29] = self.CMD_result[29].__self__
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__

		Palet = ['fg_red','fg_dred','fg_lred',
				'fg_blue','fg_dblue','fg_dcyan',
				'fg_green','fg_dgreen','fg_lgreen',
				'fg_yellow','fg_dyellow','fg_lyellow',
				'fg_cyan','fg_dcyan','fg_lcyan',
				'fg_magenta','fg_dmagenta','fg_lmagenta',
				'fg_pink','fg_dpink','fg_lpink',
				'fg_gold','fg_dgold','fg_lgold',
				'fg_brown','fg_dbrown','fg_lbrown',
				'fg_black','fg_dblack','fg_lblack',
				'fg_grey','fg_dgrey','fg_lgrey',
				'fg_white','fg_dwhite','fg_lwhite']

		self.Palet_List_Page_Result = {}
		self.Palet_List_Page_btn = {}
		self.Palet_List_Page_MSG_Details = {}
		i = 0
		if result != False or result != None or result != '' or result.upper() != 'NULL' or result != {} or result != '{}' :
			for color in Palet:

				self.Palet_List_Page_Result[i] = GridLayout(cols=2, size_hint_y=None, size=(Window.width * .95, Window.height * .25))
				self.Palet_List_Page_MSG_Details[i] = Label(text=self.pm('-=*=-||||||--++==<<  ',color) + self.pm('{}'.format(color),'fg_white') + self.pm('  >>==++--||||||-=*=-\n\n'.format(color),color),halign='left',font_size='14sp', markup = True,size=(Window.width * .45, Window.height * .2))				
				self.Palet_List_Page_MSG_Details[i] = self.Palet_List_Page_MSG_Details[i].__self__
				self.Palet_List_Page_Result[i].add_widget(self.Palet_List_Page_MSG_Details[i])
				self.Palet_List_Page_btn[i] = Button(text=self.pm('-=*=-||||||--++==<<  ',color) + self.pm('{}'.format(color),'fg_white') +self.pm('  >>==++--||||||-=*=-\n\n'.format(color),color),markup=True, size = (Window.width * .45, Window.height * .2))
				self.Palet_List_Page_btn[i] = self.Palet_List_Page_btn[i].__self__
				self.Palet_List_Page_Result[i].add_widget(self.Palet_List_Page_btn[i])
				if (scroll_height < (Window.height / 2)):
					scroll_height = scroll_height + 120
				i += 1

		Main_result = GridLayout(rows=i, size_hint_y=None, size=(Window.width, Window.height * .9))
		Main_result.bind(minimum_height = Main_result.setter('height'))
		Main_result = Main_result.__self__
		for x in range(0,i):
			Main_result.add_widget(self.Palet_List_Page_Result[x])

		scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, self.result_layout[27].height - 30), size = (Window.width, scroll_height)) 
		#The pos of 0,0 ensures scrlFBtns stays at the bottom. Place at negative coordinates if you want it to extend off-screen.
		scrlFBtns.add_widget(Main_result)
		self.result_layout3[27].add_widget(scrlFBtns)
		# lblmain = Label(text = 'List of your Orders', halign = 'center', y = (Window.height - 10), width = Window.width,size=(2,.15), color = (1,1,1,1))
		self.result_layout[27].add_widget(self.result_layout4[27])
		# self.result_layout[27].add_widget(lblmain)
		self.result_layout[27].add_widget(self.result_layout3[27])
		self.result_layout2[27].add_widget(back)
		self.result_layout[27].add_widget(self.result_layout2[27])

		self.CMD_result[29].open()

	def Paint_SVAR(self,SVAR,FGC,BGC):
		SVAR_MOD='{0}{1}{2}{3}'.format(self.Paint_Brush(FGC),self.Paint_Brush(BGC),SVAR,self.Paint_Brush('reset'))
		return SVAR_MOD

	def MPaint_SVAR(self,SVAR):
		color_wheel = ['fg_red','fg_green','fg_blue','fg_magenta','fg_cyan','fg_white']
		finished_string = ''
		split_string = SVAR.split(' ')
		x = 0
		for word in split_string:
			finished_string += '{0}{1}{2}{3}'.format(self.Paint_Brush(color_wheel[x]),self.Paint_Brush('bg_black'),SVAR,self.Paint_Brush('reset'))
			x += 1
			if x == len(color_wheel):
				x = 0
		return finished_string

	def login_script(self, *Args):
		self.PLogin(self.username,self.password,api_key)
		self.Play_Sound('Main_Theme')

	def ROSIE_Buffer(self,Move,api_key):
		self.API_Send_Move(self.username,self.password,"{} {}".format(Move,self.ROSIE_PW),api_key)

	def Logout_Script(self,*Args):
		self.PLogout(self.username,self.password,api_key)

	def reg_script(self, *Args):
		self.API_Register(self.username,self.password,self.FN,self.LN,self.EA,self.Class_Select,api_key)

	def eat_a_pickle(self):
		try:
			with open('Cucumber.pickle',"rb") as pickle_in:
				Cucumber = self.Cucumber = pickle.load(pickle_in)
				return Cucumber
		except:
			with open('Cucumber.pickle', 'w+') as pickle_out:
				pickle_out.write('new')
				pickle_out.close()
				return 'new'

	def store_a_pickle(self,Cucumber):
		with open('Cucumber.pickle', 'w+') as pickle_out:
			pickle_out.write(Cucumber)
			pickle_out.close()
			return output_return

	def hint_clear(self,*Args):
		self.hint_text = ''
		self.text = ''

	def OnMute(self,stype):
		if stype == 'Music':

			if self.MUTE_MUSIC == False:
				# self.Phone_Main_btnMusic.text=self.pm("Turn\non\nMusic","fg_pink")
				self.MDD_Menu_dd_Music.text=self.pm("Turn on Music","fg_pink")
				# try:
				# 	self.Admin_Phone_btnMusic.text=self.pm("Turn\non\nMusic","fg_pink")
				# except:
				# 	pass				
				self.MUTE_MUSIC = True
				self.Theme1.stop()
				self.Theme2.stop()
			elif self.MUTE_MUSIC == True:
				# self.Phone_Main_btnMusic.text=self.pm("Turn\noff\nMusic","fg_green")
				self.MDD_Menu_dd_Music.text=self.pm("Turn off Music","fg_green")
				# try:
				# 	self.Admin_Phone_btnMusic.text=self.pm("Turn\noff\nMusic","fg_green")
				# except:
				# 	pass				
				self.MUTE_MUSIC = False
				self.Theme2.play()

		elif stype == 'SoundFX':
			if self.MUTE_SOUND == False:
				# self.Phone_Main_btnSound.text=self.pm("Turn\non\nSounds","fg_pink")
				self.MDD_Menu_dd_Sound.text=self.pm("Turn on Sounds","fg_pink")
				# try:
				# 	# self.Admin_Phone_btnSound.text=self.pm("Turn\non\nSounds","fg_pink")
				# except:
				# 	pass
				self.MUTE_SOUND = True	
			elif self.MUTE_SOUND == True:
				# self.Phone_Main_btnSound.text=self.pm("Turn\noff\nSounds","fg_green")
				self.MDD_Menu_dd_Sound.text=self.pm("Turn off Sounds","fg_green")
				# try:
				# 	self.Admin_Phone_btnSound.text=self.pm("Turn\noff\nSounds","fg_green")
				# except:
				# 	pass
				self.MUTE_SOUND = False

	def on_username(self, inst, val):
		self.username = re.sub('Enter Username : ','',inst.text)
		_username = self.username

	def on_move(self, inst, val):
		self.move = re.sub('Enter Move : ','',inst.text)
		_username = self.username

	def on_D(self, inst, val):
		self.Warp_Location[0] = re.sub('Enter Move : ','',inst.text)

	def on_Z(self, inst, val):
		self.Warp_Location[1] = re.sub('Enter Move : ','',inst.text)

	def on_X(self, inst, val):
		self.Warp_Location[2] = re.sub('Enter Move : ','',inst.text)

	def on_Y(self, inst, val):
		self.Warp_Location[3] = re.sub('Enter Move : ','',inst.text)


	def on_rrsmD(self, inst, val):
		self.rrsm_Location[0] = re.sub('Enter Move : ','',inst.text)

	def on_rrsmZ(self, inst, val):
		self.rrsm_Location[1] = re.sub('Enter Move : ','',inst.text)

	def on_rrsmX(self, inst, val):
		self.rrsm_Location[2] = re.sub('Enter Move : ','',inst.text)

	def on_rrsmY(self, inst, val):
		self.rrsm_Location[3] = re.sub('Enter Move : ','',inst.text)


	def onWarpLocation(self, inst, val):
		self.Play_Sound('Portal')		
		# self.Warp_Location = [self.Char_POS[0],self.Char_POS[1],self.Char_POS[2],self.Char_POS[3]]
		self.API_DGPS(self.username,self.password,'warp',self.Warp_Location,api_key)
		self.changeScreenBack()

	def onaWarpLocation(self, inst, val):
		self.Play_Sound('Portal')
		self.API_DGPS(self.username,self.password,'awarp',self.Warp_Location,api_key)
		self.changeScreenBack()

	def on_password(self, inst, val):
		self.password = re.sub('Enter Password : ','',inst.text)
		self.password = hashlib.md5(self.password.encode('utf-8')).hexdigest()
		_password = self.password
	
	def on_FN(self, inst, val):
		self.FN = re.sub('Enter Password : ','',inst.text)		

	def on_LN(self, inst, val):
		self.LN = re.sub('Enter Password : ','',inst.text)		
		
	
	def on_EA(self, inst, val):
		self.EA = re.sub('Enter Password : ','',inst.text)		
		
	def on_target(self, inst, val):
		self.STarget = re.sub('Enter Password : ','',inst.text)			

	def on_MSG(self, inst, val):
		self.sMSG = inst.text			

################################################################
##						API CALLS						   ##
################################################################

	def OnRegister(self, req, result):
		
		result = self.unescape_r(result)
		returns = []
		# json_result = json.loads(result)
		self.Dismiss_All()
		if result['Status'] == 'Success':
			self.Dismiss_One(1)
			self.result_PopUP('Registration Details','Registration Succesful!\nLogging In.')
			self.PLogin(self.username, self.password,api_key)
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])	
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']				

		else:
			self.Dismiss_One(1)
			self.result_PopUP('Registration Details','Registration Failed!\n	Reason :\n	  {}'.format(result['Status']),norepeat=True)
		self.returned_values = True
	
	def OnSet_FSpell(self, req, result):
		returns = []
		self.Dismiss_One(1)
		if result['Status'] == 'Success':
			self.result_PopUP('Saved Spell',result)
		else:
			self.result_PopUP('Save Favorite Failed','Save Favorite Failed')

	def OnLogin(self, req, result):
		returns = []
		##print(str(json.dumps(result)))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			self.Play_Sound('Main_Theme')
			self.API_DGPS(self.username,self.password,'flocate',None,api_key)
			self.ROOM_INFO.text = result['Room_Details']
			self.ROSIE_MENU = result['ROSIE']
			self.ROSIE_PW = result['ROSIE_PW']
			if self.ROSIE_MENU == True or self.ROSIE_MENU == 'True' or self.ROSIE_MENU == 'true':
				self.MDD_btnROSIE = Button(text=self.pm("R.O.S.I.E",'fg_magenta'), markup=True, size_hint_y=None, height=120,font_size='10sp')
				self.MDD_btnROSIE.bind(on_press=(lambda *args: self.changeScreenROSIE('New Call','Enter the number you wish to reach.')))			
				self.MDD_Menu_dd_dropdown['Settings'].add_widget(self.MDD_btnROSIE)
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])			
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'F_Spells' in result.keys():
				#print(result['F_Spells'])
				self.Fav_Spells = result['F_Spells']					
				self.Update_Fav_Spells_BTNs()
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']				
			self.changeScreenBack()
		else:
			self.changeScreenFailed()
		self.returned_values = True			

	def OnLogout(self, req, result):
		returns = []
		self.username = self.password = ''
		self.changeScreenLogin()
		self.returned_values = True

	def OnRefresh(self, req, result):
		result = self.unescape_r(result)
		if result['Status'] == 'Success':
			self.RoomDetails = str(result['Room_Details'])
			self.ROOM_INFO.text = self.RoomDetails
			self.MoveDetails = str(result['Response'])
			self.AliveDetails = str(result['Alive'])
			self.returned_values = True
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])	
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])		
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])	
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']				
			if 'F_Spells' in result.keys():
				#print(result['F_Spells'])
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass	


	def OnSendMove(self, req, result,backone=False):
		result = self.unescape_r(result)			
		returns = []
		self.Dismiss_One(1)
		self.Dismiss_One(4)
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			self.RoomDetails = str(result['Room_Details'])
			self.ROOM_INFO.text = self.RoomDetails
			self.MoveDetails = str(result['Response'])
			self.AliveDetails = str(result['Alive'])
			self.returned_values = True
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])	
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])		
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])	
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']				
			if 'F_Spells' in result.keys():
				#print(result['F_Spells'])
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
			self.result_PopUP('Move Details:',self.MoveDetails,backone=backone)
		elif 'Failed_Logged_Out' in result['Status']:
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		elif 'Failed' in result['Status']:			
			if 'Reason' in result.keys():
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)),backone=backone)
			else:
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)),backone=backone)
		else:
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']),backone=backone)
		self.returned_values = True

	def OnSendMove_Muted(self, req, result):
		self.Dismiss_One(1)
		self.Dismiss_One(4)
		result = self.unescape_r(result)
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			self.RoomDetails = str(result['Room_Details'])
			self.ROOM_INFO.text = self.RoomDetails
			self.MoveDetails = str(result['Response'])
			self.AliveDetails = str(result['Alive'])
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])			
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']				
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass
			self.returned_values = True
		elif 'Failed' in result['Status']:			
			if 'Reason' in result.keys():
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)),backone=backone)
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)),backone=backone)
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']),backone=backone)
		self.returned_values = True

	def OnSay(self,Type):
		self.API_Send_Move(self.username,self.password,'{0} {1}'.format(Type,self.sMSG),api_key)

	def OnDisplayRoom(self, req, result):
		result = self.unescape_r(result)
		self.Dismiss_All()
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			self.RoomDetails = str(result['Room_Details'])
			self.ROOM_INFO.text = self.RoomDetails
			self.returned_values = True
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])	
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])	
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']				
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'F_Spells' in result.keys():
				#print(result['F_Spells'])
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass				
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		elif 'Failed' in result['Status']:			
			if 'Reason' in result.keys():
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)))
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)))
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def OnPhone(self, req, result):
		result = self.unescape_r(result)
		returns = []
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			_type = str(result['Type']).lower()
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])	
			if _type == 'mread':
				pass
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])	
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']				
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass				
			if _type == 'stext':
				self.MoveDetails = str(result['Response'])
				self.Dismiss_One(1)
				self.result_PopUP('Text Message Sent.',self.MoveDetails )
				self.changeScreenBack()
			elif _type == 'sreply':
				self.MoveDetails = str(result['Response'])
				self.Dismiss_One(1)
				self.result_PopUP('Text Message Sent.',self.MoveDetails )
				self.changeScreenBack()				
			elif _type == 'ctext':
				try:
					self.Admin_Phone_Main_New_MSGs.text = str(result['Response'])
				except:
					pass
				self.Phone_Main_New_MSGs.text = str(result['Response'])			
			elif _type == 'scall':
				self.MoveDetails = str(result['Response'])
				self.Dismiss_One(1)
				self.result_PopUP('Dialing Call...',self.MoveDetails)
				self.changeScreenBack()
			elif _type == 'dtext':
				self.MoveDetails = str(result['Response'])
				self.Dismiss_One(1)
				self.result_PopUP('Text Message Deleted.',self.MoveDetails)
				self.changeScreenBack()
			elif _type == 'rtext':
				self.MyTexts = json.loads(result['Response'])
				if self.MyTexts != False:
					self.result_PopUP_Read_PMSGs('Text Messages',self.MyTexts)
				elif self.MyTexts != {} or self.MyTexts !='' or self.MyTexts != None or self.MyTexts.upper() !='NULL':
					self.MyTexts = json.loads(result['Response'])
				else: 
					self.result_PopUP_Read_PMSGs('Text Messages','No New Messages.')
					self.changeScreenBack()
			elif _type == 'vtext':
				pass
			self.RoomDetails = str(result['Room_Details'])
			self.ROOM_INFO.text = self.RoomDetails
			self.AliveDetails = str(result['Alive'])				
			self.returned_values = True
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		elif 'Failed' in result['Status']:			
			self.Dismiss_One(1)
			if 'Reason' in result.keys():
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)))
			else:
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)))
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def OnDGPS(self, req, result):
		self.Play_Sound('Portal')
		result = self.unescape_r(result)
		self.Dismiss_All()
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			self.Play_Sound('Portal')
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']				
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass				
			_type = result['Type']
			if _type == 'locate':
				self.RoomDetails = str(result['Room_Details'])
				self.ROOM_INFO.text = self.RoomDetails
				self.Char_POS = self.pos_process(result['Response'])
				self.AliveDetails = str(result['Alive'])
				self.returned_values = True
				self.result_PopUP_DGPS('DGPS',self.Char_POS)
			elif _type == 'flocate':
				self.RoomDetails = str(result['Room_Details'])
				self.ROOM_INFO.text = self.RoomDetails
				self.Char_POS = self.pos_process(result['Response'])
				self.AliveDetails = str(result['Alive'])
				self.returned_values = True
				# self.result_PopUP_DGPS('DGPS',self.Char_POS)
			elif _type == 'warp' or _type == 'warp_home'or _type == 'awarp':
				self.RoomDetails = str(result['Room_Details'])
				self.ROOM_INFO.text = self.RoomDetails
				self.MoveDetails = str(result['Response'])
				self.AliveDetails = str(result['Alive'])
				self.returned_values = True
				self.Dismiss_One(1)
				self.result_PopUP('Warp Gun Tunnel',self.MoveDetails)
				self.changeScreenBack()
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		elif 'Failed' in result['Status']:			
			if 'Reason' in result.keys():
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)))
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)))
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def OnList_Inv(self, req, result):
		result = self.unescape_r(result)
		self.Play_Sound('Inventory')
		self.Dismiss_All()
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			if result['Response'] != False:
				self.MoveDetails = json.loads(result['Response'])
				self.PopUP_List_Inv('Inventory : ',self.MoveDetails)	
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Inventory : ','You dont have any items.')
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])			
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']		
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass				
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		elif 'Failed' in result['Status']:			
			if 'Reason' in result.keys():
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)))
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)))
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def OnShop(self, req, result):
		result = self.unescape_r(result)
		self.Play_Sound('Inventory')
		self.Dismiss_All()
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']		
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']				
			if result['Response'] != False:
				self.PopUp_List_Store('Frank Corp Store',result['Response'])
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Frank Corp Store : ','An Error occured with the command.')				
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		elif 'Failed' in result['Status']:			
			if 'Reason' in result.keys():
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)))
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)))
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def OnLSpell(self, req, result):
		self.Play_Sound('Magic_Menu')
		result = self.unescape_r(result)
		self.Dismiss_All()
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			if result['Response'] != False:
				self.PopUp_List_Spells('Spell Book : ',result['Response'])
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Spell Book : ','An Error occured with the command.')
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])				
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']		
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass				
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		elif 'Failed' in result['Status']:			
			self.Dismiss_One(1)
			if 'Reason' in result.keys():
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)))
			else:
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)))
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def OnSetFavSpell(self, num, Spell,Spell_Data):
		if 'attack' in Spell_Data['m_type'].lower():
			if 'area' in Spell_Data['m_type'].lower():
				s_type = 'Area_Attack'
				scolor = 'fg_red'
			else:							
				s_type = 'Attack'
				scolor = 'fg_red'
			aord = 'Attack'

		elif 'enchant' in Spell_Data['m_type'].lower() and 'monster' in Spell_Data['m_type'].lower():
			if 'area' in Spell_Data['m_type'].lower():
				s_type = 'Area_Attack'
				scolor = 'fg_magenta'
			else:							
				s_type = 'Attack'
				scolor = 'fg_orange'
			aord = 'Attack'
		elif 'charm' in Spell_Data['m_type'].lower() and 'monster' in Spell_Data['m_type'].lower():
			if 'area' in Spell_Data['m_type'].lower():
				s_type = 'Area_Attack'
				scolor = 'fg_magenta'
			else:							
				s_type = 'Attack'
				scolor = 'fg_orange'
			aord = 'Attack'
		else:	
			aord = 'Defense'
			if 'enchant' in Spell_Data['m_type'].lower():
				scolor = 'fg_magenta'
			elif 'heal' in Spell_Data['m_type'].lower():
				scolor = 'fg_cyan'
			elif 'shield' in Spell_Data['m_type'].lower():
				scolor = 'fg_dcyan'
			elif 'spawn_a' in Spell_Data['m_type'].lower() or 'spawn_wm' in Spell_Data['m_type'].lower() or 'spawn_i' in Spell_Data['m_type'].lower():
				scolor = 'fg_black'
			elif 'spawn_c' in Spell_Data['m_type'].lower():
				scolor = 'fg_yellow'
			elif 'spawn_m' in Spell_Data['m_type'].lower():
				scolor = 'fg_red'
			else:
				scolor = 'fg_dgreen'

			if 'area' in Spell_Data['m_type'].lower() and 'player' in Spell_Data['m_type'].lower():
				s_type = 'D_Area'
			elif 'target' in Spell_Data['m_type'].lower() and 'player' in Spell_Data['m_type'].lower():							
				s_type = 'D_Target'
			else:
				s_type = 'Defense'
		
		num = int(self.F_Num)

		if num in [0,1] and aord == 'Defense':
			self.Dismiss_One(1)
			self.result_PopUP('{} must be set to an Attack Spell'.format(aord,num),self.pm('Slot : {2} - Accepts Attack Spell Only. {1} is an {0} spell.'.format(aord,Spell.title(),num),scolor))
			return
		elif num in [2,3] and aord == 'Attack':
			self.Dismiss_One(1)
			self.result_PopUP('{} must be set to an Defense Spell'.format(aord,num),self.pm('Slot : {2} - Accepts Defense Spell Only. {1} is an {0} spell.'.format(aord,Spell.title(),num),scolor))
			return
		else:
			self.Play_Sound('Cast_Magic')
			Spell = self.unescape_r(Spell)
			if num not in self.Fav_Spells.keys():
				self.Fav_Spells[num] = {}
			self.Fav_Spells[num]["Spell"] = Spell_Data['name'].rstrip().lstrip()
			self.Fav_Spells[num]["Type"] = s_type
			self.Fav_Spells[num]["Data"] = Spell_Data
			self.API_Set_F_Spells(self.username,self.password,self.Fav_Spells,api_key)
			self.Update_Fav_Spells_BTNs()
			self.Dismiss_One(1)
			self.result_PopUP('Set {} Favorite {}'.format(aord,num),self.pm('You set {} Spell : {}\n As Favorite {}.'.format(aord,Spell.title(),num),scolor))
		
		
				
	def OnRRLM(self, req, result):
		self.Play_Sound('Monster')
		result = self.unescape_r(result)
		self.Dismiss_All()
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			if result['Response'] != False:
				self.PopUP_List_RRLM('R.O.S.I.E. Spawn Monsters Menu : ',result['Response'])
			else:
				self.Dismiss_One(1)
				self.result_PopUP('R.O.S.I.E. Spawn Monsters Menu : ','An Error occured with the command.')
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])				
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']		
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass				
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		elif 'Failed' in result['Status']:			
			if 'Reason' in result.keys():
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)))
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)))
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def OnRRLC(self, req, result):
		result = self.unescape_r(result)
		self.Dismiss_All()
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			if result['Response'] != False:
				self.PopUP_List_RRLC('R.O.S.I.E. Spawn Companions Menu : ',result['Response'])
			else:
				self.Dismiss_One(1)
				self.result_PopUP('R.O.S.I.E. Spawn Companions Menu : ','An Error occured with the command.')
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])				
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']		
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass				
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		elif 'Failed' in result['Status']:			
			self.Dismiss_One(1)
			if 'Reason' in result.keys():
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,100)))
			else:
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),4,100)))
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def OnRRLI(self, req, result):
		result = self.unescape_r(result)
		self.Dismiss_All()
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			if result['Response'] != False:
				self.PopUP_List_RRGI('R.O.S.I.E. Give Items Menu : ',result['Response'])
			else:
				self.Dismiss_One(1)
				self.result_PopUP('R.O.S.I.E. Give Items Menu : ','An Error occured with the command.')
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])				
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']		
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']	
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass							
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()
		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def OnList_Crafts(self, req, result):
		result = self.unescape_r(result)
		returns = []
		##print(str(result))
		# json_result = json.loads(result)
		if result['Status'] == 'Success':
			if result['Response'] != False:
				self.MoveDetails = json.loads(result['Response'])
				self.PopUP_List_Crafts('Inventory : ',self.MoveDetails)
			else:
				self.Dismiss_One(1)
				self.result_PopUP('Inventory : ','You dont know any crafts.')
			if 'P_Stats' in result.keys():
				self.OnStats(result['P_Stats'])	
			if 'Char_POS' in result.keys():			
				self.Char_POS = self.pos_process(result['Char_POS'])				
			if 'CRoom' in result.keys():
				self.CRoom = result['CRoom']
				self.Update_Main_Buttons()
			if 'Player_Details' in result.keys():
				self.Player_Details = result['Player_Details']		
			if 'F_Spells' in result.keys():
				self.Fav_Spells = result['F_Spells']
			if 'Token' in result.keys():
				if result['Token'] == 'Valid':
					pass
				elif len(re.findall(r'\d',result['Token'])) == len(result['Token']):
					self.store_a_pickle(result['Token'])
					self.Cucumber = result['Token']
				else:
					pass
				
		elif 'Failed_Logged_Out' in result['Status']:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason: Connection Timed Out\n Logging Back In.')
			self.login_script()

		elif 'Failed' in result['Status']:			
			self.Dismiss_One(1)
			if 'Reason' in result.keys():
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(result['Reason'],4,80)))
			else:
				self.result_PopUP('Move Details:','Move Failed!\n	Reason:\n {}'.format(self.split_lines(json.dumps(result,indent=4),80)))

		else:
			self.Dismiss_One(1)
			self.result_PopUP('Move Details:','Move Failed!\n	Reason :\n	  {}'.format(result['Status']))
		self.returned_values = True

	def pos_process(self,Data):
		if type(Data) == list:
			if len(Data) == 1:
				Data = Data[1]
			else: 
				pass
		if type(Data) == str:
			if '.' in Data:
				Data = Data.split('.')
			elif '[' in Data:
				Data = re.sub(r'\[|\]\"\'','',Data).split(',')
			elif Data == "" or Data == None:
				Data = ["0","0","0","0"]
		return Data

	def Build_SFAV_Menu(self):
		self.SFAV_Menu1_8 = DropDown()
		self.SFAV_Menu9_16 = DropDown()		
		self.SFAV_btns = {} 
		for x in range(0,17):
			self.SFAV_btns[x] = Button(text=self.pm("F-{}".format(x),'fg_black'),markup=True, size_hint_y=None, height=150,font_size='12sp')
			self.SFAV_btns[x].bind(on_press=lambda *args,fn=x: self.Set_F_Num(fn))
			if x < 8:
				self.SFAV_Menu1_8.add_widget(self.SFAV_btns[x])
			
			else:
				self.SFAV_Menu9_16.add_widget(self.SFAV_btns[x])
		self.SFAV_Menu1_8.bind(on_select=self.SFAV_Menu1_8._real_dismiss)				
		self.SFAV_Menu9_16.bind(on_select=self.SFAV_Menu9_16._real_dismiss)

	def Set_F_Num(self,x):
		self.F_Num = str(x)

	def Build_MDD_Menu(self):
		##### Build MDD Menu Buttons #####
		self.MDD_Menu_dd_dropdown = {}
		Buttons = ['Character','Phone','Settings','Fav_A','Fav_B']
		for x in Buttons:
			self.MDD_Menu_dd_dropdown[x] = DropDown()
			
		##### Character Menu Buttons #####

		self.MDD_Menu_dd_DGPS = Button(text="DGPS",markup=True, size_hint_y=None, height=120,font_size='10sp')
		self.MDD_Menu_dd_DGPS.bind(on_press=lambda *args: self.result_PopUP_DGPS('Frank Corp Warp Menu.','Warp Almost Anywhere With Frank Corp.'))		
		self.MDD_Menu_dd_Phone = Button(text=self.pm("Phone",'fg_yellow'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_Phone.bind(on_press=self.changeScreenPhone)
		self.MDD_Menu_dd_Crafts = Button(text=self.pm("Crafts Menu",'fg_green'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_Crafts.bind(on_press=(lambda *args: self.API_List_Crafts(self.username,self.password,api_key)))
		self.MDD_Menu_dd_SB = Button(text=self.pm("Spell Book!",'fg_green'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_SB.bind(on_press=lambda *args:self.API_LSpell(self.username,self.password,api_key))	
		self.MDD_Menu_dd_Say = Button(text=self.pm("Say",'fg_yellow'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_Say.bind(on_press=self.result_PopUP_Player_Speaks)
		self.MDD_Menu_dd_Rest = Button(text=self.pm("Rest",'fg_yellow'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_Rest.bind(on_press=self.Execute_Rest)			 
		self.MDD_Menu_dd_I = Button(text=self.pm("Inventory",'fg_yellow'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_I.bind(on_press=self.Execute_Inv)
		self.MDD_Menu_dd_WM = Button(text=self.pm("Warp Monsters",'fg_red'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_WM.bind(on_press=(lambda *args: self.Execute_API_SM('warp monsters')))
		self.MDD_Menu_dd_WH = Button(text=self.pm("Warp Home",'fg_cyan'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_WH.bind(on_press=(lambda *args: self.Execute_API_SM('warp home')))
		self.MDD_Menu_dd_dropdown['Character'].add_widget(self.MDD_Menu_dd_DGPS)
		self.MDD_Menu_dd_dropdown['Character'].add_widget(self.MDD_Menu_dd_Phone)
		self.MDD_Menu_dd_dropdown['Character'].add_widget(self.MDD_Menu_dd_I)
		self.MDD_Menu_dd_dropdown['Character'].add_widget(self.MDD_Menu_dd_Crafts)
		self.MDD_Menu_dd_dropdown['Character'].add_widget(self.MDD_Menu_dd_SB)				
		self.MDD_Menu_dd_dropdown['Character'].add_widget(self.MDD_Menu_dd_Say)
		self.MDD_Menu_dd_dropdown['Character'].add_widget(self.MDD_Menu_dd_Rest)
		self.MDD_Menu_dd_dropdown['Character'].add_widget(self.MDD_Menu_dd_WM)				
		self.MDD_Menu_dd_dropdown['Character'].add_widget(self.MDD_Menu_dd_WH)
		##### Phone Menu Buttons ###
		self.MDD_Menu_dd_Store = Button(text=self.pm(re.sub(' ','\n',"Shop Frank Corp"),'fg_green'),markup=True, size_hint_y=None, height=120,font_size='10sp')   
		self.MDD_Menu_dd_Store.bind(on_press=(lambda *args: self.API_Store(self.username,self.password,'api_list',api_key)))
		self.MDD_Menu_dd_Read = Button(text=self.pm("Read New",'fg_yellow'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_Read.bind(on_press=(lambda *args: self.API_Phone(self.username,self.password,'rtext','new','',api_key)))
		self.MDD_Menu_dd_ReadAll = Button(text=self.pm("Read All",'fg_yellow'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_ReadAll.bind(on_press=(lambda *args: self.API_Phone(self.username,self.password,'rtext','all','',api_key)))
		self.MDD_Menu_dd_NMsg = Button(text=self.pm(re.sub(' ','\n',"Send New Message"),'fg_yellow'),markup=True, size_hint_y=None, height=120,font_size='10sp')   
		self.MDD_Menu_dd_NMsg.bind(on_press=(lambda *args: self.result_PopUP_Send_PMSGs('New Message','Enter your Message.')))
		self.MDD_Menu_dd_NInvite = Button(text=self.pm(re.sub(' ','\n',"Send House Invite"),'fg_yellow'),markup=True, size_hint_y=None, height=120,font_size='10sp')   
		self.MDD_Menu_dd_NInvite.bind(on_press=(lambda *args: self.PopUp_Send_Invite('New Invite','Who Do You Want to Invite?')))
		self.MDD_Menu_dd_Call = Button(text=self.pm("New Call",'fg_yellow'),markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_Call.bind(on_press=(lambda *args: self.result_PopUP_Send_Call('New Call','Enter the number you wish to reach.')))
		self.MDD_Menu_dd_dropdown['Phone'].add_widget(self.MDD_Menu_dd_Read)
		self.MDD_Menu_dd_dropdown['Phone'].add_widget(self.MDD_Menu_dd_ReadAll)
		self.MDD_Menu_dd_dropdown['Phone'].add_widget(self.MDD_Menu_dd_NMsg)
		self.MDD_Menu_dd_dropdown['Phone'].add_widget(self.MDD_Menu_dd_Call)
		self.MDD_Menu_dd_dropdown['Phone'].add_widget(self.MDD_Menu_dd_Store)
		self.MDD_Menu_dd_dropdown['Phone'].add_widget(self.MDD_Menu_dd_NInvite)

		##### Settings Menu Buttons #####

		self.MDD_Menu_dd_Logout = Button(text="Quit",markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_Logout.bind(on_press=self.Logout_Script)
		self.MDD_Menu_dd_Sound = Button(text="Play Sounds?",markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_Sound.bind(on_press=(lambda *args: self.OnMute('SoundFX')))
		self.MDD_Menu_dd_Music = Button(text="Play Music?",markup=True, size_hint_y=None, height=120,font_size='10sp')      
		self.MDD_Menu_dd_Music.bind(on_press=(lambda *args: self.OnMute('Music')))		   
		self.MDD_Menu_dd_dropdown['Settings'].add_widget(self.MDD_Menu_dd_Sound)
		self.MDD_Menu_dd_dropdown['Settings'].add_widget(self.MDD_Menu_dd_Music)
		self.MDD_Menu_dd_dropdown['Settings'].add_widget(self.MDD_Menu_dd_Logout)
		##### Fav 0-15 Menu Buttons   ###\
		self.Favspell = {}
		for i in range(0,17):
			self.Favspell[i] = Button(text="Fav {}".format(i),markup=True, size_hint_y=None, height=60)
			if int(i) <= 7:
				self.MDD_Menu_dd_dropdown['Fav_A'].add_widget(self.Favspell[i])
			elif int(i) >= 8:
				self.MDD_Menu_dd_dropdown['Fav_B'].add_widget(self.Favspell[i])
		# self.MDD_Menu_dd_dropdown['C_Fav'].add_widget(self.xxx)
		self.MDD_Menu_dd_btn = {}
		self.MDD_Layout = {}
		for y in range(0,5):
			self.MDD_Menu_dd_btn[y] = {}
			self.MDD_Layout[y] = GridLayout(cols=6)
			for x in Buttons:
				self.MDD_Menu_dd_btn[y][x] = Button(text=x, size_hint=(.8,3))
				self.MDD_Menu_dd_btn[y][x].bind(on_release=self.MDD_Menu_dd_dropdown[x].open)				
				self.MDD_Layout[y].add_widget(self.MDD_Menu_dd_btn[y][x])
		for x in Buttons:
			self.MDD_Menu_dd_dropdown[x].bind(on_touch_down=self.MDD_Menu_dd_dropdown[x]._real_dismiss)

	def Update_Fav_Spells_BTNs(self):
		for i, Spell_data in self.Fav_Spells.items():
			z = int(i)
			if len(self.Fav_Spells[i]) == 0:
				fs1_text = 'Fav1\nNot\nSet!'
			Btn_Txt = ''
			words = self.Fav_Spells[i]['Spell'].split(' ')
			if len(words) > 2:
				for word in words:
					if len(word) > 0:
						Btn_Txt += '{}.'.format(word[0].upper())
			else:
				Btn_Txt = self.Fav_Spells[i]['Spell']
			if 'Data' in self.Fav_Spells[i].keys():
				if type(self.Fav_Spells[i]['Data']) == dict:
					if 'enchant' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'lg_magenta'
						bcolor = 'fg_magenta'
					elif 'heal' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_cyan'
						bcolor = 'fg_lcyan'
					elif 'charm' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_orange'
						bcolor = 'fg_lorange'
					elif 'shield' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_dcyan'
						bcolor = 'fg_dblue'
					elif 'spawn_i' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_gold'
						bcolor = 'fg_lgold'
					elif 'spawn_wm' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_dpink'
						bcolor = 'fg_pink'
					elif 'spawn_a' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_yellow'
						bcolor = 'fg_dyellow'
					elif 'spawn_c' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_lbrown'
						bcolor = 'fg_dbrown'
					elif 'targeted_attack' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_red'
						bcolor = 'fg_dred'
					elif 'area_attack' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_purple'
						bcolor = 'fg_dpurple'
					elif 'spawn_m' in self.Fav_Spells[i]['Data']['m_type'].lower():
						scolor = 'fg_red'
						bcolor = 'fg_lred'
					else:
						bcolor = 'fg_black'
					Btn_Txt = self.Fav_Spells[i]['Spell']
					self.Favspell[z].font_size='10sp'	
					if self.Fav_Spells[i]['Data']['m_type'].lower() in ['enchant_monster_target','charm_monster_target','targeted_attack']:
						self.Favspell[z].text = self.pm(Btn_Txt,bcolor) 
						self.Favspell[z].bind(on_press=lambda *Args,Z=i: self.PopUp_List_Monsters_SP('Cast',Z))
						
					elif self.Fav_Spells[i]['Data']['m_type'].lower() in ['enchant_monster_area','charm_monster_area','area_attack']:
						self.Favspell[z].text = self.pm(Btn_Txt,bcolor)
						self.Favspell[z].on_press=(lambda *Args,Move='cast Spell:{}%Target:{}%'.format(Spell_data['Spell'],'all'): self.API_Send_Move(self.username,self.password,Move,api_key))
					
					elif self.Fav_Spells[i]['Data']['m_type'].lower() in ['enchant_player_area','area_heal','area_shield']:
						self.Favspell[z].text = self.pm(Btn_Txt,bcolor)
						self.Favspell[z].on_press=(lambda *Args,Move='cast Spell:{}%Target:{}%'.format(Spell_data['Spell'],'all'): self.API_Send_Move(self.username,self.password,Move,api_key))
					elif self.Fav_Spells[i]['Data']['m_type'].lower() in ['enchant_player_target','targeted_heal','targeted_shield']:
						self.Favspell[z].text = self.pm(Btn_Txt,bcolor)
						self.Favspell[z].on_press=(lambda *Args,spell=Spell_data['Spell']: self.PopUp_Spell_Target_Player('Friend',spell))					
					else:
						self.Favspell[z].text = self.pm(Btn_Txt,bcolor)
						self.Favspell[z].on_press=(lambda *Args,spell=Spell_data['Spell']: self.PopUp_Spell_Target_Player('Friend',spell))					

			z += 1

	def Build_Stats_Display(self):
		self.Stats_displaym = {}
		self.Stats_display1 = {}
		self.Stats_display2 = {}
		self.Stats_display3 = {}
		self.Stats_display4 = {}
		self.Stats_display5 = {}
		self.Stats_Display_HP_W1 = {}
		self.Stats_Display_PF_W1 = {}
		self.Stats_Display_AT_W1 = {}
		self.Stats_Display_DF_W1 = {}
		self.Stats_Display_CRDT_W1 = {}
		self.Stats_Display_AMMO_W1 = {}
		self.Stats_Display_MP_W1 = {}
		self.Stats_Display_EXP_W1 = {}
		self.Stats_Display_NXT_W1 = {}
		self.Stats_Display_LVL_W1 = {}
		for i in range(0,6):
			self.Stats_displaym[i] = GridB(rows=5, size_hint_y=None, size=(Window.width  * .9, (Window.height * .18)))
			self.Stats_displaym[i] = self.Stats_displaym[i].__self__
			self.Stats_display1[i] = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .03)))
			self.Stats_display1[i] = self.Stats_display1[i].__self__
			self.Stats_display2[i] = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .03)))
			self.Stats_display2[i] = self.Stats_display2[i].__self__
			self.Stats_display3[i] = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .03)))
			self.Stats_display3[i] = self.Stats_display3[i].__self__
			self.Stats_display4[i] = GridLayout(cols=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .03)))
			self.Stats_display4[i] = self.Stats_display4[i].__self__
			self.Stats_display5[i] = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .03)))
			self.Stats_display5[i] = self.Stats_display5[i].__self__

			self.Stats_Display_HP_W1[i] = Label(text='HP:',halign='center',font_size='11sp', markup = True)
			self.Stats_Display_HP_W1[i] = self.Stats_Display_HP_W1[i].__self__

			self.Stats_Display_PF_W1[i] = Label(text='WM:',halign='center',font_size='11sp', markup = True)
			self.Stats_Display_PF_W1[i] = self.Stats_Display_PF_W1[i].__self__

			self.Stats_Display_AT_W1[i] = Label(text='AT:',halign='center',font_size='11sp', markup = True)
			self.Stats_Display_AT_W1[i] = self.Stats_Display_AT_W1[i].__self__

			self.Stats_Display_DF_W1[i] = Label(text='DF:',halign='center',font_size='11sp', markup = True)
			
			self.Stats_Display_DF_W1[i] = self.Stats_Display_DF_W1[i].__self__

			self.Stats_Display_CRDT_W1[i] = Label(text='CRDT:',halign='center',font_size='11sp', markup = True)
			
			self.Stats_Display_CRDT_W1[i] = self.Stats_Display_CRDT_W1[i].__self__

			self.Stats_Display_MP_W1[i] = Label(text='MP:',halign='center',font_size='11sp', markup = True)
			
			self.Stats_Display_MP_W1[i] = self.Stats_Display_MP_W1[i].__self__

			self.Stats_Display_AMMO_W1[i] = Label(text='AMMO:',halign='center',font_size='11sp', markup = True)
			
			self.Stats_Display_AMMO_W1[i] = self.Stats_Display_AMMO_W1[i].__self__

			self.Stats_Display_EXP_W1[i] = Label(text='EXP:',halign='center',font_size='11sp', markup = True)
			
			self.Stats_Display_EXP_W1[i] = self.Stats_Display_EXP_W1[i].__self__

			self.Stats_Display_NXT_W1[i] = Label(text='Next Level:',halign='center',font_size='11sp', markup = True)
			
			self.Stats_Display_NXT_W1[i] = self.Stats_Display_NXT_W1[i].__self__

			self.Stats_Display_LVL_W1[i] = Label(text='Level:',halign='center',font_size='11sp', markup = True)
			
			self.Stats_Display_LVL_W1[i] = self.Stats_Display_LVL_W1[i].__self__

			self.Stats_display1[i].add_widget(self.Stats_Display_LVL_W1[i])
			self.Stats_display1[i].add_widget(self.Stats_Display_HP_W1[i])

			self.Stats_display2[i].add_widget(self.Stats_Display_AT_W1[i])
			self.Stats_display2[i].add_widget(self.Stats_Display_DF_W1[i])			

			self.Stats_display3[i].add_widget(self.Stats_Display_EXP_W1[i])
			self.Stats_display3[i].add_widget(self.Stats_Display_CRDT_W1[i])

			self.Stats_display4[i].add_widget(self.Stats_Display_AMMO_W1[i])
			self.Stats_display4[i].add_widget(self.Stats_Display_MP_W1[i])
			self.Stats_display4[i].add_widget(self.Stats_Display_PF_W1[i])

			self.Stats_display5[i].add_widget(self.Stats_Display_NXT_W1[i])

			self.Stats_displaym[i].add_widget(self.Stats_display1[i])
			self.Stats_displaym[i].add_widget(self.Stats_display2[i])
			self.Stats_displaym[i].add_widget(self.Stats_display3[i])
			self.Stats_displaym[i].add_widget(self.Stats_display4[i])
			self.Stats_displaym[i].add_widget(self.Stats_display5[i])

	def pm(self,string,color):
		return self.Paint_SVAR(string,color,'bg_black')

	def OnStats(self,Stats_Return):
		Stats_Return = self.unescape_r(Stats_Return)
		self.Char_Stats = Stats_Return
		for i in range(0,6):
			#print('Updating stats for : {}'.format(i))
			# self.pm('|','fg_yellow') + self.pm('
			self.Stats_Display_PF_W1[i].text = self.pm('|','fg_magenta') + self.pm(' WM:','fg_yellow') + ' {} '.format(Stats_Return['WM']) + self.pm('/','fg_dcyan') + ' {} '.format(Stats_Return['MWM']) + self.pm('|','fg_magenta')			
			self.Stats_Display_AMMO_W1[i].text = self.pm('|','fg_magenta') + self.pm(' Ammo:','fg_yellow') + ' {} '.format(Stats_Return['AMMO']) + self.pm('/','fg_dcyan') + ' {} '.format(Stats_Return['MAMMO']) + self.pm('|','fg_magenta')			
			self.Stats_Display_MP_W1[i].text = self.pm('|','fg_magenta') + self.pm(' MP:','fg_yellow') + ' {} '.format(Stats_Return['MP']) + self.pm('/','fg_dcyan') + ' {} '.format(Stats_Return['MMP']) + self.pm('|','fg_magenta')			
			self.Stats_Display_CRDT_W1[i].text = self.pm('|','fg_magenta') + self.pm(' CRDT:','fg_yellow') + ' {} '.format(Stats_Return['CRDT']) + self.pm('|','fg_magenta')	
			
			self.Stats_Display_HP_W1[i].text = self.pm('|','fg_magenta') + self.pm(' HP:','fg_yellow') + ' {} '.format(Stats_Return['HP']) + self.pm('/','fg_dcyan') + ' {} '.format(Stats_Return['MHP']) + self.pm('|','fg_magenta')
			self.Stats_Display_AT_W1[i].text = self.pm('|','fg_magenta') + self.pm(' Attack:','fg_yellow') + ' {} '.format(Stats_Return['AT']) + self.pm('|','fg_magenta')			
			self.Stats_Display_DF_W1[i].text = self.pm('|','fg_magenta') + self.pm(' Defense:','fg_yellow') + ' {} '.format(Stats_Return['DF']) + self.pm('|','fg_magenta')	
					
			self.Stats_Display_EXP_W1[i].text = self.pm('|','fg_magenta') + self.pm(' XP:','fg_yellow') + ' {} '.format(Stats_Return['EXP']) + self.pm('|','fg_magenta')	
			self.Stats_Display_NXT_W1[i].text = self.pm('|','fg_magenta') + self.pm(' Next Lvl @','fg_yellow') + ' {} '.format(Stats_Return['NXT']) + self.pm('|','fg_magenta')	
			self.Stats_Display_LVL_W1[i].text = self.pm('|','fg_magenta') + self.pm('{} '.format(self.username.title()),'fg_dcyan') + self.pm('- Level: ','fg_yellow') + ' {} '.format(Stats_Return['LVL']) + self.pm('|','fg_magenta')	
	
	def PLogin(self, _username,_password,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/plogin'.format(api_url), on_success=self.OnLogin, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def PLogout(self, _username,_password,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/plogout'.format(api_url), on_success=self.OnLogout, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_Send_Move(self, _username,_password,move,_api_key):
		self.repeat_cmd = move
		if 'cast' in move:
			self.Play_Sound('Cast_Magic')
		elif 'hit' in move or 'attack' in move:
			self.Play_Sound('Sword')
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'move': move,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnSendMove, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_Send_Move_Muted(self, _username,_password,move,_api_key):
		self.repeat_cmd = move
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'move': move,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnSendMove_Muted, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_ROSIE_Speaks(self, _username,_password,MSG,_APW,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'move': '_rr_broadcast {} {}'.format(_APW,MSG),'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnSendMove, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True
		
	def API_ROSIE_SM(self, _username,_password,Monster,_api_key):
		RR_LOC = '{}.{}.{}.{}'.format(self.rrsm_Location[0],self.rrsm_Location[1],self.rrsm_Location[2],self.rrsm_Location[3])
		Move = '_rr_mspawn {0} {1} {2} {3}'.format(self.ROSIE_PW,RR_LOC,'monster',Monster)
		params = urllib.parse.urlencode({'username': _username,'password': _password,'api_key': _api_key, 'move': Move,'Monster': Monster.lower(),'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnSendMove, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True
		
	def display_room(self, _username,_password,move,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'move': move,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnDisplayRoom, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_Phone(self, _username,_password,_type,_target,_msg,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'type': _type, 'target': _target, 'message': _msg,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/phone'.format(api_url), on_success=self.OnPhone, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_DGPS(self, _username,_password,_type,_target,_api_key):
		self.Dismiss_All()
		_Ttarget = '{}.{}.{}.{}'.format(self.Warp_Location[0],self.Warp_Location[1],self.Warp_Location[2],self.Warp_Location[3])
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'type': _type, 'target': _Ttarget,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/dgps'.format(api_url), on_success=self.OnDGPS, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_Store(self, _username,_password,Item,_api_key):
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		if 'buy' in Item: 
			Item = re.sub('buy ','',Item).lstrip().rstrip()					 
			params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'Item':Item,'u_token':self.Cucumber})
			req = UrlRequest('{}/MaR_MUD/api/store'.format(api_url), on_success=self.OnSendMove,
			req_body=params,req_headers=headers,verify=False)
		else:
			params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'Item':Item,'u_token':self.Cucumber})
			req = UrlRequest('{}/MaR_MUD/api/store'.format(api_url), on_success=self.OnShop,
			req_body=params,req_headers=headers,verify=False)

		req.wait()
		self.returned_values = True

	def API_LSpell(self, _username,_password,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'Item':'api_list','u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}					 
		req = UrlRequest('{}/MaR_MUD/api/lspell'.format(api_url), on_success=self.OnLSpell,
		req_body=params,req_headers=headers,verify=False)
		
		req.wait()
		self.returned_values = True

	def API_aDGPS(self, _username,_password,_type,_target,_api_key):

		_Ttarget = '{}.{}.{}.{}'.format(self.Warp_Location[0],self.Warp_Location[1],self.Warp_Location[2],self.Warp_Location[3])
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'APW':self.ROSIE_PW, 'type': 'awarp', 'target': _Ttarget,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/dgps'.format(api_url), on_success=self.OnDGPS, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_List_Inv(self, _username,_password,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/list_inv'.format(api_url), on_success=self.OnList_Inv, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_ROSIE_UW(self, _username,_password,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'move':'_rr_ {}'.format(self.ROSIE_PW),'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnSendMove, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_ROSIE_SM(self, _username,_password,Monster,_api_key):
		RR_LOC = '{}.{}.{}.{}'.format(self.rrsm_Location[0],self.rrsm_Location[1],self.rrsm_Location[2],self.rrsm_Location[3])
		Move = '_rr_mspawn {0} {1} {2} {3}'.format(self.ROSIE_PW,RR_LOC,'monster',Monster)
		params = urllib.parse.urlencode({'username': _username,'password': _password,'api_key': _api_key, 'move': Move,'Monster': Monster,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnSendMove, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_ROSIE_SC(self, _username,_password,Companion,_api_key):
		RR_LOC = '{}.{}.{}.{}'.format(self.rrsm_Location[0],self.rrsm_Location[1],self.rrsm_Location[2],self.rrsm_Location[3])
		Move = '_rr_cspawn {0} {1} {2} {3}'.format(self.ROSIE_PW,'companion',RR_LOC,Monster)
		params = urllib.parse.urlencode({'username': _username,'password': _password,'api_key': _api_key, 'move': Move,'Companion': Monster,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnSendMove, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_ROSIE_GI(self, _username,_password,Item,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'move':'_rr_give {0} {1}'.format(self.ROSIE_PW,Item),'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnSendMove, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_ROSIE_SI(self, _username,_password,OPlayer,Item,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'move':'_rr_senditem {0} {1} {2}'.format(self.ROSIE_PW,OPlayer,Item),'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/send_move'.format(api_url), on_success=self.OnSendMove, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_ROSIE_LM(self, _username,_password,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'APW':self.ROSIE_PW,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/rr_lm'.format(api_url), on_success=self.OnRRLM, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_ROSIE_LC(self, _username,_password,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'APW':self.ROSIE_PW,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/rr_lc'.format(api_url), on_success=self.OnRRLC, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_ROSIE_LI(self, _username,_password,Item,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'APW':self.ROSIE_PW,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/rr_li'.format(api_url), on_success=self.OnRRLI, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_Set_F_Spells(self, _username,_password,F_Spells,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'APW':self.ROSIE_PW,'F_Spells':str(json.dumps(self.Fav_Spells)),'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/set_fspells'.format(api_url), on_success=self.OnSet_FSpell, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True		

	def API_List_Crafts(self, _username,_password,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/list_crafts'.format(api_url), on_success=self.OnList_Crafts, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_Register(self, _username,_password,FN,LN,EA,Class_Select,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key, 'FN':FN, 'LN':LN, 'EA':EA,"Class_Select":self.Class_Select,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/register'.format(api_url), on_success=self.OnRegister, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True

	def API_Refresh_GData(self, _username,_password,_api_key):
		params = urllib.parse.urlencode({'username': _username,'password':_password,'api_key':_api_key,'u_token':self.Cucumber})
		headers = {'Content-type': 'application/x-www-form-urlencoded',
						 'Accept': 'text/plain'}
		req = UrlRequest('{}/MaR_MUD/api/refresh_gdata'.format(api_url), on_success=self.OnRefresh, req_body=params,
		req_headers=headers,verify=False)
		req.wait()
		self.returned_values = True		


##################################################################################
## ROSIE STUFF
##################################################################################


	def Admin_Phone_Main(self,*args):
		Window.softinput_mode = 'pan'
		self.Admin_Phone_Main_sm = Screen(name='Admin_Phone_Main')
		self.Admin_Phone_Main_sm = self.Admin_Phone_Main_sm.__self__

		self.icon = './data/MaR_MUD_Icon.png'
		self.Admin_Phone_Main_MaR_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		self.Admin_Phone_Main_MaR_MUDLogo.allow_stretch = True
		self.Admin_Phone_Main_MaR_MUDLogo.keep_ratio = True
		self.Admin_Phone_Main_MaR_MUDLogo = self.Admin_Phone_Main_MaR_MUDLogo.__self__
		self.Admin_Phone_Main_PG1 = GridLayout(rows=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Admin_Phone_Main_PG1 = self.Admin_Phone_Main_PG1.__self__
		self.Admin_Phone_Main_PG2 = GridLayout(rows=6, size_hint_y=None, size=(Window.width  * .95, (Window.height * .7)))
		self.Admin_Phone_Main_PG2 = self.Admin_Phone_Main_PG2.__self__
		self.Admin_Phone_Main_G1 = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .125)))
		self.Admin_Phone_Main_G1 = self.Admin_Phone_Main_G1.__self__
		self.Admin_Phone_Main_G2 = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .125)))
		self.Admin_Phone_Main_G2 = self.Admin_Phone_Main_G2.__self__
		self.Admin_Phone_Main_G3 = GridLayout(cols=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Admin_Phone_Main_G3 = self.Admin_Phone_Main_G3.__self__
		self.Admin_Phone_Main_G4 = GridLayout(cols=5, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Admin_Phone_Main_G4 = self.Admin_Phone_Main_G4.__self__
		self.Admin_Phone_Main_G5 = GridLayout(cols=5, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Admin_Phone_Main_G5 = self.Admin_Phone_Main_G5.__self__
		self.Admin_Phone_Main_G6 = GridLayout(cols=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.Admin_Phone_Main_G6 = self.Admin_Phone_Main_G6.__self__

		self.Admin_Phone_Main_spacer = BoxLayout(padding=.2,spacing=.2, orientation='horizontal',size_hint=(1, 30),pos_hint={'center_x': .5, 'center_y': .5})

		layout = GridLayout(rows=3, size_hint_y=None, size=(Window.width, Window.height))
		layout = layout.__self__
		layout2 = GridLayout(rows=2, size_hint_y=None, size=(Window.width, Window.height * .15))
		layout2 = layout2.__self__
		self.Admin_Phone_Main_sm.add_widget(layout)
		self.root.add_widget(self.Admin_Phone_Main_sm)
		
		self.Admin_Phone_Main_Text_Area = ScrolllabelLabel(text='Welcome to the MaR_MUD Communications\n Enjoy your phone.')
		self.Admin_Phone_Main_Text_Area = self.Admin_Phone_Main_Text_Area.__self__
		self.Admin_Phone_Main_New_MSGs = Label(text='{}'.format(''),halign='left',font_size='12sp',size=(Window.width * .8,Window.height * .2), markup = True)
		self.Admin_Phone_Main_New_MSGs = self.Admin_Phone_Main_New_MSGs.__self__

		# self.Admin_Phone_Main_btnCrafts = Button(text=self.pm("Crafts\nMenu",'fg_green'),markup=True,size_hint = (1,1))
		# self.Admin_Phone_Main_btnCrafts.bind(on_press=(lambda *args: self.API_List_Crafts(self.username,self.password,api_key)))
		# self.Admin_Phone_Main_btnWH = Button(text=self.pm("Warp\nHome",'fg_cyan'),markup=True,size_hint = (1,1))
		# self.Admin_Phone_Main_btnWH.bind(on_press=(lambda *args: self.Execute_API_SM('warp home')))
		# self.Admin_Phone_Main_btnWM = Button(text=self.pm("Warp\nMonsters",'fg_red'),markup=True,size_hint = (1,1))
		# self.Admin_Phone_Main_btnWM.bind(on_press=(lambda *args: self.Execute_API_SM('warp monsters')))

		self.Admin_Phone_Main_btnRead = Button(text=self.pm("Read\nNew",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Admin_Phone_Main_btnRead.bind(on_press=(lambda *args: self.API_Phone(self.username,self.password,'rtext','new','',api_key)))
		self.Admin_Phone_Main_btnReadAll = Button(text=self.pm("Read\nAll",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Admin_Phone_Main_btnReadAll.bind(on_press=(lambda *args: self.API_Phone(self.username,self.password,'rtext','all','',api_key)))

		self.Admin_Phone_Main_btnNMsg = Button(text=self.pm("New\nMessage",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Admin_Phone_Main_btnNMsg.bind(on_press=(lambda *args: self.result_PopUP_Send_PMSGs('New Message','Enter your Message.')))
		self.Admin_Phone_Main_btnNInvite = Button(text=self.pm("New\nHouse\nInvite",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Admin_Phone_Main_btnNInvite.bind(on_press=(lambda *args: self.PopUp_Send_Invite('New Invite','Who Do You Want to Invite?')))
		self.Admin_Phone_Main_btnNMsg = self.Admin_Phone_Main_btnNMsg.__self__
		self.Admin_Phone_Main_btnCall = Button(text=self.pm("New\nCall",'fg_yellow'),markup=True,size_hint = (1,1))
		self.Admin_Phone_Main_btnCall.bind(on_press=(lambda *args: self.result_PopUP_Send_Call('New Call','Enter the number you wish to reach.')))
		self.Admin_Phone_Main_btnCall = self.Admin_Phone_Main_btnCall.__self__
		# self.Admin_Phone_btnStore = Button(text=self.pm("Shop\nFrank\nCorp",'fg_green'),markup=True,size_hint = (1,1))
		# self.Admin_Phone_btnStore.bind(on_press=(lambda *args: self.API_Store(self.username,self.password,'api_list',api_key)))
		# self.Admin_Phone_btnStore = self.Admin_Phone_btnStore.__self__
		# self.Admin_Phone_btnSound = Button(text="Play\nSounds?",size_hint = (1,1),markup=True)
		# self.Admin_Phone_btnSound.bind(on_press=(lambda *args: self.OnMute('SoundFX')))
		# self.Admin_Phone_btnSound = self.Admin_Phone_btnSound.__self__
		# self.Admin_Phone_btnMusic = Button(text="Play\nMusic?",size_hint = (1,1),markup=True)
		# self.Admin_Phone_btnMusic.bind(on_press=(lambda *args: self.OnMute('Music')))
		# self.Admin_Phone_btnMusic = self.Admin_Phone_btnMusic.__self__

		# btnDGPS = Button(text=self.pm("DGPS",'fg_cyan'),markup=True,size_hint = (.2,1))
		# btnDGPS.bind(on_press=lambda *args: self.result_PopUP_DGPS('Frank Corp Warp Menu.','Warp Almost Anywhere With Frank Corp.'))
		# self.Admin_Phone_Main_G6.add_widget(btnDGPS)

		btnLogout = Button(text="Quit",size_hint = (.2,1))
		btnLogout.bind(on_press=self.Logout_Script)
		self.Admin_Phone_Main_G4.add_widget(btnLogout)

		# btnSB = Button(text=self.pm("Spell\nBook!",'fg_green'),markup=True,size_hint = (.2,1))
		# # btnA.bind(on_press=self.Execute_A)
		# btnSB.bind(on_press=lambda *args:self.API_LSpell(self.username,self.password,api_key))	
		# self.Admin_Phone_Main_G6.add_widget(btnSB)

		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.Dismiss_All)
		back = back.__self__


		self.Admin_Phone_Main_G1.add_widget(self.Admin_Phone_Main_Text_Area)
		self.Admin_Phone_Main_G2.add_widget(self.Admin_Phone_Main_New_MSGs)
		
		self.Admin_Phone_Main_G3.add_widget(self.Admin_Phone_Main_btnRead)
		self.Admin_Phone_Main_btnROSIE = Button(text=self.pm("R.O.S.I.E",'fg_magenta'),markup=True,size_hint = (1.5,1))
		self.Admin_Phone_Main_btnROSIE.bind(on_press=(lambda *args: self.changeScreenROSIE('New Call','Enter the number you wish to reach.')))
		self.Admin_Phone_Main_btnROSIE = self.Admin_Phone_Main_btnROSIE.__self__
		self.Admin_Phone_Main_G3.add_widget(self.Admin_Phone_Main_btnROSIE)
		self.Admin_Phone_Main_G3.add_widget(self.Admin_Phone_Main_btnReadAll)
		
		# self.Admin_Phone_Main_G4.add_widget(self.Admin_Phone_btnSound)
		# self.Admin_Phone_Main_G4.add_widget(self.Admin_Phone_btnMusic)

		self.Admin_Phone_Main_G4.add_widget(back)
		self.Admin_Phone_Main_G4.add_widget(self.Admin_Phone_Main_btnCall)
		self.Admin_Phone_Main_G4.add_widget(self.Admin_Phone_Main_btnNMsg)
		self.Admin_Phone_Main_G4.add_widget(self.Admin_Phone_Main_btnNInvite)

		# self.Admin_Phone_Main_G5.add_widget(self.Admin_Phone_btnStore)
		# self.Admin_Phone_Main_G5.add_widget(self.Admin_Phone_Main_btnCra
		# self.Admin_Phone_Main_G5.add_widget(self.Admin_Phone_Main_btnWM)
		# self.Admin_Phone_Main_G5.add_widget(self.Admin_Phone_Main_btnWH)
		layout2.add_widget(self.Admin_Phone_Main_MaR_MUDLogo)
		layout.add_widget(self.MDD_Layout[3])
		layout.add_widget(layout2)
		# layout2.add_widget(self.Admin_Phone_Main_G1)
		self.Admin_Phone_Main_PG2.add_widget(self.Admin_Phone_Main_G1)
		self.Admin_Phone_Main_PG2.add_widget(self.Admin_Phone_Main_G2)
		self.Admin_Phone_Main_PG2.add_widget(self.Admin_Phone_Main_G3)
		self.Admin_Phone_Main_PG2.add_widget(self.Admin_Phone_Main_G4)
		self.Admin_Phone_Main_PG2.add_widget(self.Admin_Phone_Main_G6)
		# self.Admin_Phone_Main_PG2.add_widget(self.Admin_Phone_Main_G5)
		layout.add_widget(self.Admin_Phone_Main_PG2)

	def ROSIE_Main(self,*args):
		Window.softinput_mode = 'pan'
		self.ROSIE_Main_sm = Screen(name='ROSIE_Main')
		self.ROSIE_Main_sm = self.ROSIE_Main_sm.__self__

		self.icon = './data/MaR_MUD_Icon.png'
		self.ROSIE_Main_MaR_MUDLogo = Image(source='./data/MaR_MUD_Logo.png')
		self.ROSIE_Main_MaR_MUDLogo.allow_stretch = True
		self.ROSIE_Main_MaR_MUDLogo.keep_ratio = True
		self.ROSIE_Main_MaR_MUDLogo = self.ROSIE_Main_MaR_MUDLogo.__self__
		self.ROSIE_Main_PG1 = GridLayout(rows=3, size_hint_y=None, size=(Window.width  * .8, (Window.height * .15)))
		self.ROSIE_Main_PG1 = self.ROSIE_Main_PG1.__self__
		self.ROSIE_Main_PG2 = GridLayout(rows=5, size_hint_y=None, size=(Window.width  * .95, (Window.height * .85)))
		self.ROSIE_Main_PG2 = self.ROSIE_Main_PG2.__self__
		self.ROSIE_Main_G1 = GridLayout(cols=1, size_hint_y=None, size=(Window.width  * .8, (Window.height * .125)))
		self.ROSIE_Main_G1 = self.ROSIE_Main_G1.__self__
		self.ROSIE_Main_G2 = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .125)))
		self.ROSIE_Main_G2 = self.ROSIE_Main_G2.__self__
		self.ROSIE_Main_G3 = GridLayout(cols=2, size_hint_y=None, size=(Window.width  * .8, (Window.height * .2)))
		self.ROSIE_Main_G3 = self.ROSIE_Main_G3.__self__
		self.ROSIE_Main_G4 = GridLayout(cols=5, size_hint_y=None, size=(Window.width  * .8, (Window.height * .2)))
		self.ROSIE_Main_G4 = self.ROSIE_Main_G4.__self__
		self.ROSIE_Main_G5 = GridLayout(cols=6, size_hint_y=None, size=(Window.width  * .8, (Window.height * .2)))
		self.ROSIE_Main_G5 = self.ROSIE_Main_G5.__self__

		self.ROSIE_Main_spacer = BoxLayout(padding=.2,spacing=.2, orientation='horizontal',size_hint=(1, 30),pos_hint={'center_x': .5, 'center_y': .5})

		layout = GridLayout(rows=3, size_hint_y=None, size=(Window.width, Window.height))
		layout = layout.__self__
		layout2 = GridLayout(rows=2, size_hint_y=None, size=(Window.width, Window.height * .15))
		layout2 = layout2.__self__
		self.ROSIE_Main_sm.add_widget(layout)
		self.root.add_widget(self.ROSIE_Main_sm)
		
		self.ROSIE_Main_Text_Area = ScrolllabelLabel(text='Welcome to the R.O.S.I.E.\n The Admin Tool brought to you by Frank Corp.\nYou can Spawn Items/Monsters/Crafts/Reset World Data.\nJust ask R.O.S.I.E. will do the rest.')
		self.ROSIE_Main_Text_Area = self.ROSIE_Main_Text_Area.__self__
		
		self.ROSIE_Main_btnGiveItems = Button(text=self.pm("Give\nItems\nMenu",'fg_blue'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnGiveItems.bind(on_press=(lambda *args: self.API_ROSIE_LI(self.username,self.password,'',api_key)))
		
		self.ROSIE_Main_btnGAS = Button(text=self.pm("Give\nAll\nSpells",'fg_green'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnGAS.bind(on_press=(lambda *args,Move='_rr_gas': self.ROSIE_Buffer(Move,api_key)))

		self.ROSIE_Main_btnGAC = Button(text=self.pm("Give\nAll\nCrafts",'fg_green'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnGAC.bind(on_press=(lambda *args,Move='_rr_gac': self.ROSIE_Buffer(Move,api_key)))

		self.ROSIE_Main_btnAW = Button(text=self.pm("Admin\nWarp\nMenu",'fg_cyan'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnAW.bind(on_press=(lambda *args: self.result_PopUP_aDGPS('Admin Warp Menu!!!\nBrought to You by R.O.S.I.E and Frank Corp.','Warping Anywhere?')))

		self.ROSIE_Main_btnSM = Button(text=self.pm("Spawn\nMonsters\nMenu",'fg_red'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnSM.bind(on_press=(lambda *args: self.API_ROSIE_LM(self.username,self.password,api_key)))

		self.ROSIE_Main_btnSC = Button(text=self.pm("Spawn\nCompanions\nMenu",'fg_magenta'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnSC.bind(on_press=(lambda *args: self.API_ROSIE_LC(self.username,self.password,api_key)))		

		self.ROSIE_Main_btnUW = Button(text=self.pm("Update\nWorld",'fg_magenta'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnUW.bind(on_press=(lambda *args: self.API_ROSIE_UW(self.username,self.password,api_key)))

		self.ROSIE_Main_btnRSay = Button(text=self.pm("ROSIE\nSpeak\nAll",'fg_magenta'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnRSay.bind(on_press=(lambda *args: self.result_PopUP_ROSIE_Speaks('ROSIE Speaks, The MaR_MUD PA System.','')))		

		self.ROSIE_Main_btnColors1 = Button(text=self.pm("ROSIE\nShow\nColor\nPalet\nApp",'fg_magenta'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnColors1.bind(on_press=(lambda *args: self.Show_Palet('Here are the colors available for text in the App.','Here are the colors available for text in the game.')))		

		self.ROSIE_Main_btnColors2 = Button(text=self.pm("ROSIE\nShow\nColor\nPalet\nGE",'fg_magenta'),markup=True,size_hint = (1,1))
		self.ROSIE_Main_btnColors2.bind(on_press=lambda *Args: self.Show_Palet_GE())
				
		back = Button(text=self.pm("Back",'fg_lred'),markup=True,size_hint = (1,3))
		back.bind(on_press=self.changeScreenBack)
		back = back.__self__

		self.ROSIE_Main_G1.add_widget(self.ROSIE_Main_Text_Area)
				
		self.ROSIE_Main_G4.add_widget(self.ROSIE_Main_btnSC)
		self.ROSIE_Main_G4.add_widget(self.ROSIE_Main_btnGAS)
		self.ROSIE_Main_G4.add_widget(self.ROSIE_Main_btnGiveItems)
		self.ROSIE_Main_G4.add_widget(self.ROSIE_Main_btnGAC)
		self.ROSIE_Main_G4.add_widget(self.ROSIE_Main_btnSM)
		# self.ROSIE_Main_G4.add_widget(self.ROSIE_Main_btnNInvite)

		self.ROSIE_Main_G5.add_widget(self.ROSIE_Main_btnColors1)
		self.ROSIE_Main_G5.add_widget(self.ROSIE_Main_btnColors2)
		self.ROSIE_Main_G5.add_widget(self.ROSIE_Main_btnUW)
		self.ROSIE_Main_G5.add_widget(back)
		self.ROSIE_Main_G5.add_widget(self.ROSIE_Main_btnAW)
		self.ROSIE_Main_G5.add_widget(self.ROSIE_Main_btnRSay)
		
		layout2.add_widget(self.ROSIE_Main_MaR_MUDLogo)
		layout.add_widget(layout2)
		# layout2.add_widget(self.ROSIE_Main_G1)
		self.ROSIE_Main_PG2.add_widget(self.ROSIE_Main_G1)
		# self.ROSIE_Main_PG2.add_widget(self.ROSIE_Main_G2)
		# self.ROSIE_Main_PG2.add_widget(self.ROSIE_Main_G3)
		self.ROSIE_Main_PG2.add_widget(self.ROSIE_Main_G4)
		self.ROSIE_Main_PG2.add_widget(self.ROSIE_Main_G5)
		layout.add_widget(self.ROSIE_Main_PG2)

	def escape_m(self,VAR):
		if type(VAR) == str:
			VAR = re.sub("'",'-003399SQ-',VAR)
			VAR = re.sub('"','-003399QM-',VAR)
			VAR = re.sub(';','-003399SM-',VAR)
			VAR = re.sub(',','-003399CM-',VAR)
		return VAR

	def unescape_r(self,VAR):
		if type(VAR) == str:
			VAR = re.sub('-003399SQ-',"'",VAR)
			VAR = re.sub('-003399QM-','"',VAR)
			VAR = re.sub('-003399SM-',';',VAR)
			VAR = re.sub('-003399CM-',',',VAR)
		return VAR
if __name__ == "__main__":
	MaR_MUDApp().run()
