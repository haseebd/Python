import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class ScreenOne(Screen):
    
    def __init__ (self,**kwargs):
        super (ScreenOne, self).__init__(**kwargs)
        
        my_box1 = BoxLayout(orientation='vertical')
        my_box2 = BoxLayout(orientation='horizontal')
        
        my_label1 = Label(text="HD Coding Presents", size_hint_y=None, font_size="15sp", height = 150)
        my_label2 = Label(text="Four\nHundred", font_size="100sp", halign="center", valign="middle")
        my_label3 = Label(text="Score Tracker", font_size="25sp")
        my_label4 = Label(text="by Haseeb Durrani", font_size="15sp")
        
        
        my_button1 = Button(text="Screen 2",size_hint_y=None, size_y=75)
        my_button1.bind(on_press=self.changer1)
        my_button2 = Button(text="Screen 3",size_hint_y=None, size_y=75)
        my_button2.bind(on_press=self.changer2)
        
        
        my_box1.add_widget(my_label1)
        my_box1.add_widget(my_label2)
        my_box1.add_widget(my_label3)
        my_box1.add_widget(my_label4)
        
        my_box1.add_widget(my_box2)
        
        my_box2.add_widget(my_button1)
        my_box2.add_widget(my_button2)
        
        self.add_widget(my_box1)
    
    def changer1(self,*args):
        self.manager.current = 'screen2'
    def changer2(self,*args):
        self.manager.current = 'screen3'

class ScreenTwo(Screen):
    
    def __init__(self,**kwargs):
        super (ScreenTwo,self).__init__(**kwargs)
        
        box = BoxLayout(orientation='vertical')
        layout = GridLayout(cols = 8, size_hint=(1, 4))
        box.add_widget(layout)
        
        box2 = BoxLayout(orientation='horizontal')
        box.add_widget(box2)
        
        box3 = BoxLayout(orientation='horizontal')
        box.add_widget(box3)
        
        # Player 1 Name Input
        self.txt1 = TextInput(text='', font_size = "20sp", padding_y = 25, multiline=False)
        layout.add_widget(self.txt1)
        # Ok button to Enter Player 1 Name
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.p1name)
        layout.add_widget(btn1)
        # Player 2 Name Input
        self.txt2 = TextInput(text='', font_size = "20sp", padding_y = 25, multiline=False)
        layout.add_widget(self.txt2)
        # Ok button to Enter Player 2 Name
        btn2 = Button(text="OK")
        btn2.bind(on_press=self.p2name)
        layout.add_widget(btn2)
        # Player 3 Name Input
        self.txt3 = TextInput(text='', font_size = "20sp", padding_y = 25, multiline=False)
        layout.add_widget(self.txt3)
        # Ok button to Enter Player 3 Name
        btn3 = Button(text="OK")
        btn3.bind(on_press=self.p3name)
        layout.add_widget(btn3)
        # Player 4 Name Input
        self.txt4 = TextInput(text='', font_size = "20sp", padding_y = 25, multiline=False)
        layout.add_widget(self.txt4)
        # Ok button to Enter Player 4 Name
        btn4 = Button(text="OK")
        btn4.bind(on_press=self.p4name)
        layout.add_widget(btn4)
        
        # Player Number and Name Labels
        self.lbl1 = Label(text="Player 1:")
        layout.add_widget(self.lbl1)
        self.lbl2 = Label(text="P1", font_size = "20sp")
        layout.add_widget(self.lbl2)
        self.lbl3 = Label(text="Player 2:")
        layout.add_widget(self.lbl3)
        self.lbl4 = Label(text="P2", font_size = "20sp")
        layout.add_widget(self.lbl4)
        self.lbl5 = Label(text="Player 3:")
        layout.add_widget(self.lbl5)
        self.lbl6 = Label(text="P3", font_size = "20sp")
        layout.add_widget(self.lbl6)
        self.lbl7 = Label(text="Player 4:")
        layout.add_widget(self.lbl7)
        self.lbl8 = Label(text="P4", font_size = "20sp")
        layout.add_widget(self.lbl8)
        
        # Score Labels
        self.lbl9 = Label(text="Score:")
        layout.add_widget(self.lbl9)
        self.lbl10 = Label(text="0", font_size = "50sp")
        layout.add_widget(self.lbl10)
        self.lbl11 = Label(text="Score:")
        layout.add_widget(self.lbl11)
        self.lbl12 = Label(text="0", font_size = "50sp")
        layout.add_widget(self.lbl12)
        self.lbl13 = Label(text="Score:")
        layout.add_widget(self.lbl13)
        self.lbl14 = Label(text="0", font_size = "50sp")
        layout.add_widget(self.lbl14)
        self.lbl15 = Label(text="Score:")
        layout.add_widget(self.lbl15)
        self.lbl16 = Label(text="0", font_size = "50sp")
        layout.add_widget(self.lbl16)
        
        # Call Input
        self.lbl17 = Label(text="Call:")
        layout.add_widget(self.lbl17)
        self.txt5 = TextInput(text='', font_size = "50sp", multiline=False)
        layout.add_widget(self.txt5)
        self.lbl18 = Label(text="Call:")
        layout.add_widget(self.lbl18)
        self.txt6 = TextInput(text='', font_size = "50sp",  multiline=False)
        layout.add_widget(self.txt6)
        self.lbl19 = Label(text="Call:")
        layout.add_widget(self.lbl19)
        self.txt7 = TextInput(text='', font_size = "50sp", multiline=False)
        layout.add_widget(self.txt7)
        self.lbl20 = Label(text="Call:")
        layout.add_widget(self.lbl20)
        self.txt8 = TextInput(text='', font_size = "50sp",  multiline=False)
        layout.add_widget(self.txt8)
        
        
        btn5 = Button(text="Yes", background_color=(0.0, 1.0, 0.0, 1.0))
        btn5.bind(on_press=self.p1yes)
        layout.add_widget(btn5)
        
        btn6 = Button(text="No", background_color=(1.0, 0.0, 0.0, 1.0))
        btn6.bind(on_press=self.p1no)
        layout.add_widget(btn6)
        
        btn7 = Button(text="Yes", background_color=(0.0, 1.0, 0.0, 1.0))
        btn7.bind(on_press=self.p2yes)
        layout.add_widget(btn7)
        
        btn8 = Button(text="No", background_color=(1.0, 0.0, 0.0, 1.0))
        btn8.bind(on_press=self.p2no)
        layout.add_widget(btn8)
        
        btn9 = Button(text="Yes", background_color=(0.0, 1.0, 0.0, 1.0))
        btn9.bind(on_press=self.p3yes)
        layout.add_widget(btn9)
        
        btn10 = Button(text="No", background_color=(1.0, 0.0, 0.0, 1.0))
        btn10.bind(on_press=self.p3no)
        layout.add_widget(btn10)
        
        btn11 = Button(text="Yes", background_color=(0.0, 1.0, 0.0, 1.0))
        btn11.bind(on_press=self.p4yes)
        layout.add_widget(btn11)
        
        btn12 = Button(text="No", background_color=(1.0, 0.0, 0.0, 1.0))
        btn12.bind(on_press=self.p4no)
        layout.add_widget(btn12)
        
        resetnames_button = Button(text="Reset\nNames",size_hint_y=None, size_y=70)
        resetnames_button.bind(on_press=self.resetnames)
        box2.add_widget(resetnames_button)
        
        resetcalls_button = Button(text="Reset\nCalls",size_hint_y=None, size_y=70)
        resetcalls_button.bind(on_press=self.resetcalls)
        box2.add_widget(resetcalls_button)
        
        resetall_button = Button(text="Reset\nGame",size_hint_y=None, size_y=70)
        resetall_button.bind(on_press=self.resetall)
        box2.add_widget(resetall_button)
        
        self.lbl21 = Label(text="Total Calls:", size_hint_y=None, size_y=100)
        box2.add_widget(self.lbl21)
        
        self.lbl22 = Label(text="", size_hint_y=None, size_y=100)
        box2.add_widget(self.lbl22)
        
        checkcalls_button = Button(text="Check Calls",size_hint_y=None, size_y=70)
        checkcalls_button.bind(on_press=self.checkcalls)
        box2.add_widget(checkcalls_button)
        
        my_button1 = Button(text="Screen 1",size_hint_y=None, size_y=100)
        my_button1.bind(on_press=self.changer1)
        box3.add_widget(my_button1)
        my_button2 = Button(text="Screen 3",size_hint_y=None, size_y=100)
        my_button2.bind(on_press=self.changer2)
        box3.add_widget(my_button2)
        
        
        
        
        
        self.add_widget(box)
    
    
    
    
    # button click function
    
    def resetnames(self,btn):
        self.lbl2.text = "P1"
        self.lbl4.text = "P2"
        self.lbl6.text = "P3"
        self.lbl8.text = "P4"
    
    def resetcalls(self,btn):
        
        self.txt5.text = ""
        self.txt6.text = ""
        self.txt7.text = ""
        self.txt8.text = ""
        self.lbl22.text = ""
    
    def resetall(self,btn):
        self.lbl2.text = "P1"
        self.lbl4.text = "P2"
        self.lbl6.text = "P3"
        self.lbl8.text = "P4"
        self.lbl10.text = "0"
        self.lbl12.text = "0"
        self.lbl14.text = "0"
        self.lbl16.text = "0"
        self.txt1.text = ""
        self.txt2.text = ""
        self.txt3.text = ""
        self.txt4.text = ""
        self.txt5.text = ""
        self.txt6.text = ""
        self.txt7.text = ""
        self.txt8.text = ""
    
    def checkcalls(self,btn):
        try:
            calls_total = int(self.txt5.text) + int(self.txt6.text) + int(self.txt7.text) + int(self.txt8.text)
            self.lbl22.text = str(calls_total)
            
            if calls_total < 11:
                self.txt5.text = ""
                self.txt6.text = ""
                self.txt7.text = ""
                self.txt8.text = ""
            else:
                pass
        except:
            pass
    
    
    # Ok Buttons to confirm player name input
    def p1name(self,btn):
        if len(self.txt1.text) > 0:
            self.lbl2.text = self.txt1.text
            self.txt1.text = ""

    def p2name(self,btn):
        if len(self.txt2.text) > 0:
            self.lbl4.text = self.txt2.text
            self.txt2.text = ""

    def p3name(self,btn):
        if len(self.txt3.text) > 0:
            self.lbl6.text = self.txt3.text
            self.txt3.text = ""

    def p4name(self,btn):
        if len(self.txt4.text) > 0:
            self.lbl8.text = self.txt4.text
            self.txt4.text = ""

# Yes/No Buttons to calculate player after a hand
    def p1yes(self,btn):
    
        try:
            if int(self.txt5.text) == 5 or int(self.txt5.text) == 10:
                self.lbl10.text = str(int(self.lbl10.text) + 10)
            elif int(self.txt5.text) == 7 or int(self.txt5.text) == 14:
                 self.lbl10.text = str(int(self.lbl10.text) + 14)
            else:
                self.lbl10.text = str(int(self.lbl10.text) + int(self.txt5.text))
        except:
            self.txt5.text = ""
    
        self.txt5.text = ""
    
    def p1no(self,btn):
        try:
            if int(self.txt5.text) == 5 or int(self.txt5.text) == 10:
                self.lbl10.text = str(int(self.lbl10.text) - 10)
            elif int(self.txt5.text) == 7 or int(self.txt5.text) == 14:
                self.lbl10.text = str(int(self.lbl10.text) - 14)
            else:
                self.lbl10.text = str(int(self.lbl10.text) - int(self.txt5.text))
        except:
            self.txt5.text = ""
        
        self.txt5.text = ""
    
    def p2yes(self,btn):
        try:
            if int(self.txt6.text) == 5 or int(self.txt6.text) == 10:
                self.lbl12.text = str(int(self.lbl12.text) + 10)
            elif int(self.txt6.text) == 7 or int(self.txt6.text) == 14:
                self.lbl12.text = str(int(self.lbl12.text) + 14)
            else:
                self.lbl12.text = str(int(self.lbl12.text) + int(self.txt6.text))
        except:
            self.txt6.text = ""
        
        self.txt6.text = ""
    
    def p2no(self,btn):
        try:
            if int(self.txt6.text) == 5 or int(self.txt6.text) == 10:
                self.lbl12.text = str(int(self.lbl12.text) - 10)
            elif int(self.txt6.text) == 7 or int(self.txt6.text) == 14:
                self.lbl12.text = str(int(self.lbl12.text) - 14)
            else:
                self.lbl12.text = str(int(self.lbl12.text) - int(self.txt6.text))
        except:
            self.txt6.text = ""
        
        self.txt6.text = ""
    
    def p3yes(self,btn):
        try:
            if int(self.txt7.text) == 5 or int(self.txt7.text) == 10:
                self.lbl14.text = str(int(self.lbl14.text) + 10)
            elif int(self.txt7.text) == 7 or int(self.txt7.text) == 14:
                self.lbl14.text = str(int(self.lbl14.text) + 14)
            else:
                self.lbl14.text = str(int(self.lbl14.text) + int(self.txt7.text))
        except:
            self.txt7.text = ""
        
        self.txt7.text = ""
    
    def p3no(self,btn):
        try:
            if int(self.txt7.text) == 5 or int(self.txt7.text) == 10:
                self.lbl14.text = str(int(self.lbl14.text) - 10)
            elif int(self.txt7.text) == 7 or int(self.txt7.text) == 14:
                self.lbl14.text = str(int(self.lbl14.text) - 14)
            else:
                self.lbl14.text = str(int(self.lbl14.text) - int(self.txt7.text))
        except:
            self.txt7.text = ""
        
        self.txt7.text = ""
    
    def p4yes(self,btn):
        try:
            if int(self.txt8.text) == 5 or int(self.txt8.text) == 10:
                self.lbl16.text = str(int(self.lbl16.text) + 10)
            elif int(self.txt8.text) == 7 or int(self.txt8.text) == 14:
                self.lbl16.text = str(int(self.lbl16.text) + 14)
            else:
                self.lbl16.text = str(int(self.lbl16.text) + int(self.txt8.text))
        except:
            self.txt8.text = ""
        
        self.txt8.text = ""
    
    def p4no(self,btn):
        try:
            if int(self.txt8.text) == 5 or int(self.txt8.text) == 10:
                self.lbl16.text = str(int(self.lbl16.text) - 10)
            elif int(self.txt8.text) == 7 or int(self.txt8.text) == 14:
                self.lbl16.text = str(int(self.lbl16.text) - 14)
            else:
                self.lbl16.text = str(int(self.lbl16.text) - int(self.txt8.text))
        except:
            self.txt8.text = ""
        
        self.txt8.text = ""
    
    def changer1(self,*args):
        self.manager.current = 'screen1'
    
    def changer2(self,*args):
        self.manager.current = 'screen3'

class ScreenThree(Screen):
    
    def __init__ (self,**kwargs):
        super (ScreenThree, self).__init__(**kwargs)
        
        my_box1 = BoxLayout(orientation='vertical')
        my_box2 = BoxLayout(orientation='horizontal')
        
        my_label1 = Label(text="Coming Soon .....", font_size="30sp", size_hint_y=None, height = 100)
        
        my_button1 = Button(text="Screen 1",size_hint_y=None, size_y=100)
        my_button1.bind(on_press=self.changer1)
        my_button2 = Button(text="Screen 2",size_hint_y=None, size_y=100)
        my_button2.bind(on_press=self.changer2)
        
        my_box1.add_widget(my_label1)
        
        my_box1.add_widget(my_box2)
        
        my_box2.add_widget(my_button1)
        my_box2.add_widget(my_button2)
        
        self.add_widget(my_box1)
    
    def changer1(self,*args):
        self.manager.current = 'screen1'
    
    def changer2(self,*args):
        self.manager.current = 'screen2'


class Four100(App):
    def build(self):
        my_screenmanager = ScreenManager()
        screen1 = ScreenOne(name='screen1')
        screen2 = ScreenTwo(name='screen2')
        screen3 = ScreenThree(name='screen3')
        my_screenmanager.add_widget(screen1)
        my_screenmanager.add_widget(screen2)
        my_screenmanager.add_widget(screen3)
        return my_screenmanager

if __name__ == '__main__':
    Four100().run()
