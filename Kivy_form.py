import re
from subfile import Student, save_student, load_student
def valid_email(email):
    pattern = r"^[\w]+@[\w]+\.[\w]{2,}$"
    return re.match(pattern, email) is not None

def generate_id(prefix,existing_id):
    if not existing_id:
        return f"{prefix}001"
    next_id = [int(i[len(prefix):]) for i in existing_id]
    return f"{prefix}{max(next_id)+1:03d}"

student_list = load_student()

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.screenmanager import Screen, ScreenManager

class BorderLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.after:
            Color(1,1,1,1)
            self.border = Line(rectangle=(self.x, self.y, self.width, self.height), width=1.5)
        self.bind(pos = self.update_border, size = self.update_border)

    def update_border(self, *args):
        self.border.rectangle = (self.x, self.y, self.width, self.height)

class PageColor(Screen):
    def __init__(self,page_color=(0,0,0.06,1), **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*page_color)
            self.rect = Rectangle(pos = self.pos, size = self.size)
            self.bind(pos = self.update_rect, size = self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class Home(PageColor):
    def __init__(self, **kwargs):
        super().__init__(page_color= (0,0.3,0,1),**kwargs)
        layout = FloatLayout()
        label = Label(text="AFOY ACADEMY", font_size=65, bold=True, color=(1,0.84,0,1),
                      pos_hint= {'center_x':0.5, 'center_y':0.55})
        layout.add_widget(Label(text="REGISTRATION FORM", font_size=35, bold=True,color=(1,0.84,0,1),
                                pos_hint= {'center_x':0.5, 'center_y':0.36}))
        btn = Button(text="Next", size_hint=(0.07,0.06),pos_hint= {'right':0.85, "center_y":0.1})
        btn.bind(on_press=self.go_to_next)
        layout.add_widget(label)
        layout.add_widget(btn)
        self.add_widget(layout)

    def go_to_next(self, instance):
        self.manager.transition.direction = "left"
        self.manager.current = "Next"

class Next(PageColor):
    def __init__(self, **kwargs):
        super().__init__(page_color = (0.20,0.27,0.33,1), **kwargs)
        layout = FloatLayout()
        layout.add_widget(Label(text = "Fill in with appropriate information", size_hint=(0.07,None),
                                pos_hint= {'x':0.25, 'center_y':0.94}, font_size=20))
        email_box = BorderLayout(orientation="vertical", size_hint=(0.7,0.15),
                                 pos_hint= {'center_x':0.50, 'center_y':0.70},spacing= 10)
        email_box.add_widget(Label(text="Enter your email", size_hint_y=None, height=25))
        self.email = TextInput(hint_text="Enter your email", size_hint_y=None, height=40,multiline=False)
        email_box.add_widget(self.email)
        layout.add_widget(email_box)
        name = BorderLayout(orientation="vertical", size_hint=(0.7,0.15),
                            pos_hint= {'center_x':0.50, 'center_y':0.40},spacing= 10)
        name.add_widget(Label(text="Enter your name", size_hint_y=None, height=25))
        self.name_input = TextInput(hint_text="Enter your name", size_hint_y=None, height=40,multiline=False)
        name.add_widget(self.name_input)
        layout.add_widget(name)
        self.status = Label(text="",size_hint=(0.4,0.06),pos_hint= {'center_x':0.5, 'center_y':0.30},
                            color=(1,1,1,1))
        layout.add_widget(self.status)
        sub_btn= Button(text="Next", size_hint= (0.07,0.06),pos_hint= {'center_x':0.85, 'center_y':0.1})
        sub_btn.bind(on_press=self.check_email)
        layout.add_widget(sub_btn)
        btn = Button(text= "Back",size_hint=(0.07,0.06),pos_hint= {'right':0.15, "center_y":0.1})
        btn.bind(on_press=self.go_home)
        layout.add_widget(btn)
        view= ScrollView()
        view.add_widget(layout)
        self.add_widget(view)

    def check_email(self,instance):
        if valid_email(self.email.text.strip()):
            reg_data.email = self.email.text.strip()
            reg_data.name_input = self.name_input.text.strip()

            self.status.text = "email is valid"
            self.manager.current = "After"
        else:
            self.status.text = "please enter a valid email"

    def go_home(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "Home"

class After(PageColor):
    def __init__(self,**kwargs):
        super().__init__(page_color = (0.25,0.10,0.03,1), **kwargs)
        layout = FloatLayout()
        layout.add_widget(Label(text="Fill in with appropriate information", size_hint=(0.07, None),
                                pos_hint={'x': 0.25, 'center_y': 0.94}, font_size=20))
        course= BorderLayout(orientation="vertical", size_hint=(0.7,0.15),
                              pos_hint={'center_x': 0.50, 'center_y': 0.70}, spacing=10)
        course.add_widget(Label(text= "Enter your course", size_hint_y=None, height=25))
        self.course= TextInput(hint_text= "enter your course", size_hint_y=None, height=40,multiline = False)
        course.add_widget(self.course)
        layout.add_widget(course)
        sb_comb= BorderLayout(orientation="vertical", size_hint=(0.7,0.15),
                              pos_hint={'center_x': 0.50, 'center_y': 0.40}, spacing=10)
        sb_comb.add_widget(Label(text="Enter your subject Combination", size_hint_y=None, height=25))
        self.sb_comb= TextInput(hint_text="enter your course combination",size_hint_y=None, height=40,multiline=False)
        sb_comb.add_widget(self.sb_comb)
        layout.add_widget(sb_comb)
        button= Button(text="back",size_hint=(0.07,0.06),pos_hint= {'right':0.15, "center_y":0.1})
        button.bind(on_press=self.go_back)
        layout.add_widget(button)
        btn = Button(text = "submit", size_hint = (0.09,0.06),pos_hint= {'right':0.5, "center_y":0.05})
        btn.bind(on_press=self.submit)
        layout.add_widget(btn)
        self.add_widget(layout)

    def submit(self,instance):
        existing_id = [s.reg_id for s in student_list]
        reg_id = generate_id("AFO3EXMFT", existing_id)

        student = Student(reg_data.email, reg_data.name_input,
                          self.course.text.strip(),self.sb_comb.text.strip(),reg_id)
        student_list.append(student)
        save_student(student_list)
        end_screen = self.manager.get_screen("End")
        end_screen.status.text = (f"Registered Sucessfully,"
                                  f"\n   Dear: {reg_data.name_input},"
                                  f"\nYour ID : {reg_id} ")
        self.manager.current = "End"

    def go_back(self,instance):
        self.manager.transition.direction = "right"
        self.manager.current = "Next"

class End(PageColor):
    def __init__(self,**kwargs):
        super().__init__(page_color= (0,0,0.08,1), **kwargs)
        layout = BoxLayout(orientation="vertical", spacing=30,size_hint=(1,1))
        self.status = Label(text="",color=(1,1,1,1), bold = True, font_size = 30)
        layout.add_widget(self.status)
        self.add_widget(layout)

class RegistrationData:
    def __init__(self):
        self.email = ""
        self.name_input = ""
        self.course = ""
        self.sb_comb= ""
reg_data= RegistrationData()

class Form(App):
    def build(self):
        note = ScreenManager()
        note.add_widget(Home(name = "Home"))
        note.add_widget(Next(name = "Next"))
        note.add_widget(After(name = "After"))
        note.add_widget(End(name = "End"))
        return note

if __name__ == "__main__":
    Form().run()