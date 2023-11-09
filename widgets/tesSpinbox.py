from src.widget_composition import WidgetCompositionfrom tkinter import Entryfrom .tesButton import tesButtonclass tesSpinbox(WidgetComposition):    def __init__(            self,            container,            textcolor: str = 'white',            background_b: str = 'black',            backgroundidx_b: int = 4,            bordercolor_b: str = 'black',            bordercoloridx_b: int = 3,            value: int = 0,            step: int = 1,            mini: int = 0,            maxi: int = 100,            tags: str | tuple[str, str] = ('tesSpinbox', 'name'),            **kw):        super().__init__(container, textcolor=textcolor, **kw)        self.background_b = background_b        self.backgroundidx_b = backgroundidx_b        self.bordercolor_b = bordercolor_b        self.bordercoloridx_b = bordercoloridx_b        self.step = step        self.mini = mini        self.maxi = maxi        self._value = value        self._previous_value = value        self._tags = tags        self.set_color()        self.draw_widget()        self._insert_tkinter_frame_widget()        self._insert_tkinter_entry_widget()        self._insert_testk_button_widget()        self.insert(value)        self._grid_settings()        self.set_style()    def set_style(self) -> None:        if self.animation == 'border':            self.tkinterentry.bind('<Double-1>', self._animtion_style)    def _animtion_style(self, event) -> None:        if self.color_number_idx == 0:            self.widget_animation()    def _grid_settings(self) -> None:        self.tkinterframe.columnconfigure(0, weight=2)    def _insert_tkinter_entry_widget(self) -> None:        """Tkinter Entry Object"""        self.tkinterentry = Entry(self.tkinterframe, **self._tkinter_entry_settings())        self.tkinterentry.grid(row=0, column=0, sticky='we', padx=(0, 3))    def _tkinter_entry_settings(self) -> dict:        settings = {'background':           self.background,                    'fg':                   self.textcolor,                    'font':                 ('Havletica', 15),                    'highlightthickness':   0,                    'relief':               'flat'}        return settings    def _testk_button_settinngs(self) -> dict:        settings = {'container':     self.tkinterframe,                    'fontsize':      18,                    'textcolor':     '#FAFAFA',                    'background':    self.background_b,                    'backgroundidx': self.backgroundidx_b,                    'bordercolor':   self.bordercolor_b,                    'bordercoloridx': self.bordercoloridx_b,                    'border':        1,                    'width':         34,                    'height':        30,                    'radius':        7,                    'shadow':        False,                    'style':         'simple',                    'animation':    'border'}        return settings    def _insert_testk_button_widget(self) -> None:        tesButton(text='-', **self._testk_button_settinngs(), command=self._value_down).grid(row=0, column=1, sticky='e', pady=(2, 0))        tesButton(text='+', **self._testk_button_settinngs(), command=self._value_upp).grid(row=0, column=2, sticky='e', pady=(2, 0))    def _value_validation(self):        """ important -> Tkinter Entry returns a string object type            object must be iterable """        if not self.tkinterentry.get():            return False        for sign in self.tkinterentry.get():            if sign == '-':                if len(self.tkinterentry.get()) < 2:                    return False                if sign in self.tkinterentry.get()[1:]:                    return False                continue            if not sign.isdigit():                return False        return True    def _value_upp(self):        if self._value_validation():            value = self.get()            self._previous_value = value            if value + self.step < self.maxi:                value += self.step            else:                value = self.maxi            self.insert(value)    def _value_down(self):        if self._value_validation():            value = self.get()            self._previous_value = value            if value - self.step > self.mini:                value -= self.step            else:                value = self.mini            self.insert(value)    def insert(self, value: int = 0) -> None:        if not isinstance(value, int):            raise ValueError("Incorect value! Expected type: 'int'")        self.delete()        self.tkinterentry.insert(0, value)    def get(self) -> int | str:        if self._value_validation():            value = int(self.tkinterentry.get())            return value        return "[Error] Incorrect value! Expected type: 'int'"    @property    def previous_value(self) -> int:        return self._previous_value    @previous_value.setter    def previous_value(self, value) -> None:        if not isinstance(value, int):            raise ValueError("Incorect value! Expected type: 'int'")        self._previous_value = value    @property    def tags(self) -> str | tuple[str, str]:        return self._tags    def delete(self) -> None:        self.tkinterentry.delete(0, 'end')