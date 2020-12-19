import kivy
import kivymd
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.size = (330, 560)
kivy.lang.builder.Builder.load_file("style.kv")


class My_Layout(Widget):
    text = kivy.properties.ObjectProperty('0')
    font_size = kivy.properties.NumericProperty(70)

    def clear(self):
        self.text= self.text[:-1] 

    def all_clear(self):
        self.text = ''
        self.font_size = 70

    def press(self, button):
        mode = 'None'

        if len(str(self.text)) > 11:
            mode = 'stop'

        if self.text == '0' or self.text == 0 and mode != 'stop' or self.text == "Error":
            self.text = button
        else:
            if mode == 'stop':
                pass
            else:
                self.text = f"{self.text}{button}"

        if len(str(self.text)) == 8:
            self.font_size -= 20

    def press_zero(self):
        self.text = f"{self.text}00"

    def operation(self, sign):
        if self.text == '0' or self.text == 0 or self.text == '+'\
                            or self.text == '÷' or self.text == '×'\
                            or self.text == '−' or self.text == '%':
            self.text = f"{sign}"

        else:
            self.text = f"{self.text}{sign}"

        if len(str(self.text)) == 8:
            self.font_size -= 20

    def decimal(self):
        if self.text[-1] is '.':
            pass
        else:
            self.text = f"{self.text}."

    def equal(self):
        try:
            if '+' in self.text:
                num_list = self.text.split('+')
                answer = 0
                for i in num_list:
                    answer = answer + float(i)
                    self.text = str(answer)

            if '−' in self.text:
                num_list = self.text.split('−')
                answer = 0
                for i in num_list:
                    if num_list.index(i) == 0:
                        answer = i
                    else:
                        answer = float(answer) - float(i)
                    self.text = str(answer)

            if '×' in self.text:
                num_list = self.text.split('×')
                answer = 0
                for i in num_list:
                    if num_list.index(i) == 0:
                        answer = i
                    else:
                        answer = float(answer) * float(i)
                    self.text = str(answer)

            if '÷' in self.text:
                num_list = self.text.split('÷')
                answer = 0
                for i in num_list:
                    if num_list.index(i) == 0:
                        answer = i
                    else:
                        answer = float(answer) / float(i)
                    self.text = str(answer)

            if '%' in self.text:
                num_list = self.text.split('%')
                answer = 0
                for i in num_list:
                    if num_list.index(i) == 0:
                        answer = i
                    else:
                        answer = (float(answer)/100) * float(i)
                    self.text = str(answer)

            if len(str(self.text)) == 8:
                self.font_size -= 20

        except:
            self.text = "Error"


class main_app(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Pink'
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        app = My_Layout()
        return app


main_app().run()
