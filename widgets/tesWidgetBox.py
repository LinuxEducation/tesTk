from src.widget_composition import WidgetCompositionfrom tkinter import Label, Frame, ttkfrom widgets import tesSmallButtonclass tesWidgetBox(WidgetComposition):    def __init__(self,                 container,                 title: str | None = 'tesBox',                 button_color: str = 'red',                 button_color_idx: int = 2,                 widget_box_setting=None,                 width_max: int = 200,                 height_max: int = 88,                 separator: bool = False,                 animation: str = None,                 **kw):        super().__init__(container, **kw)        self.width_max = width_max        self.height_max = height_max        self.title = title        self.button_color = button_color        self.button_color_idx = button_color_idx        self.widget_box_setting = widget_box_setting        self.previouse_width = self.width        self.previouse_height = self.height        self.animation = animation        self.set_color()        self.draw_widget()        self._insert_tkinter_frame_widget()        self._insert_expand_button()        if title:            self._insert_title()        if widget_box_setting:            self._insert_setting_button()        if separator:            self._insert_separator()    def _insert_separator(self,):        ttk.Separator(self.tkinterframe, orient='horizontal').pack(padx=(3, 3), fill='x')    def draw_widget(self) -> None:        WidgetComposition.draw_widget(self)    def _insert_tkinter_frame_widget(self) -> None:        WidgetComposition._insert_tkinter_frame_widget(self)        # insert frame for title and button        self.header = Frame(self.tkinterframe, background=self.background)        self.header.pack(fill='x', pady=(2, 2))    def _insert_title(self) -> None:        Label(**self._widget_settings('label')).pack(side='left', anchor='sw', padx=3)    def _insert_expand_button(self) -> None:        self.expand_button = tesSmallButton(self.header, **self._widget_settings('button'))        self.expand_button.pack(side='right', anchor='e', padx=5, pady=(2, 0))    def _insert_setting_button(self):        self.button_setting = tesSmallButton(self.header, background='gray', backgroundidx=0, width=30, height=30, icon='./icons/settings_small.png',                                             text=None, iconoffset=3, radius=5, border=0, command=self.widget_box_setting)        self.button_setting.pack(side='right', pady=(2, 0))    def resize_widget_box(self):        self.width = self.width_max if self.width < self.width_max else self.previouse_width        self.height = self.height_max if self.height < self.height_max else self.previouse_height        self.configure(width=self.width, height=self.height)        self.clear_widget()        self.draw_widget()        self.resize_tkinter_frame()        if self.height > self.previouse_height:            self.expand_button.itemconfigure('text', text='-')        else:            self.expand_button.itemconfigure('text', text='+')        if self.animation == 'border':            if self.height > self.previouse_height:                self.widget_animation()    def _widget_settings(self, type_: str = None) -> dict:        title_settings = {'master':     self.header,                          'background': self.background,                          'foreground': 'white',                          'font':       ('Verdana', self.fontsize),                          'text':       self.title}        button_settings = {'text':              '+',                           'width':             28,                           'height':            28,                           'background':        self.button_color,                           'backgroundidx':     self.button_color_idx,                           'command':           self.resize_widget_box,                           'icon':              False,                           'border':            0}        if type_ == 'label':            return title_settings        if type_ == 'button':            return button_settings