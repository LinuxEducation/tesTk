from src.widget import *
from tkinter import Entry, END


class tesEntry(WidgetShape, WidgetSetting):
    def __init__(
            self,
            container,
            iconposition=None,
            style: str = 'default',
            command=None,
            tags: str | tuple[str, str] = ('tesEntry', 'name'),
            **kw):
        WidgetShape.__init__(self, container, iconposition=iconposition, **kw)
        self.style = style
        self._tags = tags
        self.command = command
        self.set_color()
        self.draw_widget()
        self._insert_tkinter_entry_widget()
        self.set_style()
        self._event()

    def draw_widget(self) -> None:
        WidgetShape.draw_widget(self)
        if self.icon:
            self.insert_image()

    def set_style(self) -> None:
        if self.style == 'underline':
            self.tkinterentry.bind('<Enter>', self._underline_style)
            self.tkinterentry.bind('<Leave>', self._underline_style)
        if self.animation == 'border':
            self.tkinterentry.bind('<Double-1>', self._animtion_style)

    def widget_animation(self) -> None:
        if self.animation == 'background':
            raise 'not yet implemented'
        WidgetSetting.widget_animation(self)

    def _underline_style(self, event) -> None:
        if 'Enter' in str(event):
            self.draw_underline()
        if 'Leave' in str(event):
            # tesEntry object has its own delete method
            WidgetShape.delete(self, 'underline')

    def _animtion_style(self, event) -> None:
        if self.color_number_idx == 0:
            self.widget_animation()

    def _event(self) -> None:
        if self.icon:
            self.tag_bind('icon', '<Button-1>', self)

    def _tkinter_entry_position(self) -> tuple[float, float]:
        """button arc is a 1/2 radius                       ./create_arc()    -> canvas methos
           anchor parameter have a default value: center    ./create_window() -> canvas method"""
        x = self.width / 2
        y = self.height / 2 - 1
        self.offset = 0
        if self.iconposition == 'w':
            self.offset = 32 + 5
            x = x + 32 / 2 - 2
        if self.iconposition == 'e':
            self.offset = 32 + 5
            x = x - 32 / 2 - 5
        return x, y

    def _tkinter_entry_geometry(self) -> dict:
        bag = 2 #POPRAW TO!!!
        geometry = {'width': self.width - self.radius - self.offset -bag,
                    'height': self.height - self.border * 2 - 4}
        return geometry

    def _tkinter_entry_settings(self) -> dict:
        settings = {'background': self.background,
                    'fg': self.textcolor,
                    'font': ('Havletica', self.fontsize),
                    'highlightthickness': 0,
                    'relief': 'flat'}
        return settings

    def _insert_tkinter_entry_widget(self) -> None:
        """Tkinter Entry Object"""
        self.tkinterentry = Entry(**self._tkinter_entry_settings())
        self.tkinterentry.insert(0, self.text)
        """Tkinter Canvas Method"""
        self.create_window(self._tkinter_entry_position(), **self._tkinter_entry_geometry(), window=self.tkinterentry)

    def get(self) -> str:
        value = self.tkinterentry.get()
        return value

    def insert(self, value: str) -> None:
        self.delete()
        self.tkinterentry.insert(0, value)

    def delete(self) -> None:
        self.tkinterentry.delete(0, END)

    def settings(self, **kwargs):
        WidgetSetting.settings(self, **kwargs)
        self._insert_tkinter_entry_widget()

    @property
    def tags(self) -> str | tuple[str, str]:
        return self._tags

    def __call__(self, event):
        self.command() if self.command else print(self.__str__())

    def __str__(self):
        if not self.get():
            return 'tesEntry: ' + 'empty'
        return 'tesEntry: ' + self.get()
