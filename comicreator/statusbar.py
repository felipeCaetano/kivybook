from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty


class StatusBar(BoxLayout):
    counter = NumericProperty(0)
    previous_conter = 0

    def on_counter(self, instance, value):
        if value == 0:
            self.msg_text = "Drawing space cleared"
        elif value -1 == self.__class__.previous_conter:
            self.msg_text = "Widget added"
        elif value + 1 == self.previous_conter:
            StatusBar.msg_text = "Widget removed"
        self.previous_conter = value