from src.widget import WidgetShape, WidgetSetting

class Rectangle(WidgetShape, WidgetSetting):
    def draw_widget(self) -> None:
        WidgetShape.draw_widget(self)

    def widget_animation(self) -> None:
        WidgetSetting.widget_animation(self)
