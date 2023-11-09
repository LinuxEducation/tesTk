from src.widget_composition import WidgetComposition
from tkinter import Label

class tesFrame(WidgetComposition):
    def __init__(self, container, style: str = None, **kw):
        WidgetComposition.__init__(self, container, **kw)
        self.style = style
        self.set_color()
        self.set_style(style, container)
        self.draw_widget()
        self._insert_tkinter_frame_widget()

        ''' ToDo
            - if labelFrame title is large, tkinterframe inside tesFrame must change
            - change the position of the title: right, right down... 
        '''


    def set_style(self, style, container) -> None:
        if style == 'labelFrame':
            self.background = container['background']
            self._label_style()
        if self.animation:
            self.widget_animation()

    def _label_style(self) -> None:
        settings = {'background':   self.background,
                    'text':         self.text,
                    'fg':           self.textcolor,    
                    'font':         ('Havletica', self.fontsize),
                    'padx':         4}

        self.create_window(self.radius, 0, window=Label(**settings), anchor='w')

    def _tkinter_frame_position(self, offset=0) -> tuple[float, float]:
        """button arc is a 1/2 radius                       ./create_arc()    -> canvas methos
           anchor parameter have a default value: center    ./create_window() -> canvas method"""
        x = self.width/2
        y = self.height/2
        if self.style == 'labelFrame':
            offset = self.fontsize / 4
        return x-self.shadow, y-self.shadow + offset

    def _tkinter_frame_geometry(self, offset=0) -> dict:
        if self.style == 'labelFrame':
            offset = self.fontsize / 2
        geometry = {'width':  self.width-self.radius,
                    'height': self.height-self.radius - offset}
        return geometry

    def pack(self, **kwargs) -> None:
        WidgetComposition.pack(self, kwargs)
        if self.style == 'labelFrame':
            WidgetComposition.pack_configure(self, pady=(self.fontsize/2, 0))

    def grid(self, **kwargs) -> None:
        WidgetComposition.grid(self, kwargs)
        if self.style == 'labelFrame':
            WidgetComposition.grid_configure(self, pady=(self.fontsize/2, 0))
