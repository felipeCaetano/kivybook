from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ListProperty

class GeneralTools(BoxLayout):
    group_mode = False
    translation = ListProperty(None)

    def clear(self, instance):
        self.drawing_space.clear_widgets()

    def remove(self, instance):
        ds = self.drawing_space
        if len(ds.children) > 0:
            ds.remove_widget(ds.children[0])

    def group(self, instance, value):
        if value == 'down':
            self.group_mode = True
        else:
            self.group_mode = False
            self.unselect_all()

    def color(self, instance):
        ...

    def gestures(self, instance):
        ...

    def unselect_all(self):
        [child.unselect() for child in self.drawing_space.children]

    def on_translation(self, instance, value):
        [child.translate(*self.translation) for child in
         self.drawing_space.children if child.selected]
