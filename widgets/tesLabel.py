from src.widget import *

class tesLabel(WidgetShape, WidgetSetting):
    def __init__(self, container, **kw):
        WidgetShape.__init__(self, container, **kw)
        self.set_color()
        self.draw_widget()

    def widget_animation(self) -> None:
        if self.animation:
            WidgetSetting.widget_animation(self)

    def draw_widget(self) -> None:
        WidgetShape.draw_widget(self)
        if self.text:
            self.insert_text()

    def insert(self, value: str) -> None:
        self.text = value
        if not self.text:
            self.insert_text()
            return
        self.itemconfigure('text', text=value)

    def get(self) -> str:
        return self.text

    def delete(self) -> None:
        self.text = None
        self.itemconfigure('text', text='')
