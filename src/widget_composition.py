from abc import ABC
from src.widget import WidgetShape, WidgetSetting
from tkinter import Frame
import math

class WidgetComposition(WidgetShape, WidgetSetting, ABC):
    def draw_widget(self) -> None:
        WidgetShape.draw_widget(self)

    def widget_animation(self) -> None:
        if self.animation == 'background':
            raise 'background animation are not currently supported...'
        WidgetSetting.widget_animation(self)

    def resize_tkinter_frame(self) -> None:
        self.coords('tkinterframe', self._tkinter_frame_position())
        self.itemconfig('tkinterframe', self._tkinter_frame_geometry())
    resize_frame = resize_tkinter_frame

    def resize_widget_composition(self, size):
        self.height = size
        self.configure(height=size)
        self.clear_widget()
        self.draw_widget()
        self.resize_tkinter_frame()


    def _insert_tkinter_frame_widget(self) -> None:
        """Tkinter Frame Object"""
        self.tkinterframe = Frame(**self._tkinter_frame_settings())
        """Tkinter Canvas Method"""
        self.create_window(self._tkinter_frame_position(), **self._tkinter_frame_geometry(), window=self.tkinterframe, tags='tkinterframe')

    def _tkinter_frame_position(self) -> tuple[float, float]:
        """widget arc is a 1/2 radius                       ./create_arc()    -> canvas method
           anchor parameter have a default value: center    ./create_window() -> canvas method"""
        x = self.width/2
        y = self.height/2
        return x-self.shadow, y-self.shadow

    def calculate_max_point(self, offset: int = 4) -> int:
        radius = self.radius // 2
        c = math.sqrt(radius ** 2 * 2) / 2
        max_position = (radius - c) * 2
        return max_position + offset

    def _tkinter_frame_geometry(self) -> dict:
        position = self.calculate_max_point()
        geometry = {'width':  self.width-position-1,
                    'height': self.height-position}
        return geometry

    def _tkinter_frame_settings(self) -> dict:
        settings = {'background':           self.background,
                    'highlightthickness':   0,
                    'relief':               'flat'}
        return settings
