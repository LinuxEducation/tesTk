from src.widget_composition import WidgetComposition
from tkinter import Label, ttk
from .tesButton import tesButton

class tesCombobox(WidgetComposition):
    def __init__(self,
                 container,
                 value_list: list[str] = ['Combobox'],
                 command=None,
                 **kw):
        super().__init__(container, **kw)
        self.value_list: list[str] = value_list
        self.command = command

        self.set_color()
        self.draw_widget()
        self._insert_tkinter_frame_widget()
        self._grid_settings()
        self._insert_value()
        self._insert_value_list()
        self._event_combobox_button()
        self._insert_expand_button()

    def _widget_settings(self, type_: str = None) -> dict:
        #value box
        value_settings = {'master':     self.tkinterframe,
                          'background': self.background,
                          'foreground': 'white',
                          'font':       ('Verdana', 14),
                          'text':       self.value}
        #list box
        list_settings = {'master':      self.tkinterframe,
                         'background':  self.background,
                         'foreground':  'white',
                         'font':        ('Verdana', 11),
                         'anchor':      'w'}
        #button box
        button_settings = {'container':     self.tkinterframe,
                           'command':       self.__expand_nofification,
                           'text':          '\u2B9F',
                           'fontsize':      11,
                           'textcolor':     '#FAFAFA',
                           'background':    self.background,
                           'bordercolor':   self.background,
                           'border':        1,
                           'width':         36,
                           'height':        32,
                           'radius':        7,
                           'shadow':        False}

        if type_ == 'value':
            return value_settings
        if type_ == 'list':
            return list_settings
        if type_ == 'button':
            return button_settings

    def _grid_settings(self) -> None:
        self.tkinterframe.columnconfigure(0, weight=2)

    def _insert_value(self) -> None:
        self.value = self.value_list[0]
        self.tesCombobox_title = Label(**self._widget_settings('value'))
        self.tesCombobox_title.grid(row=0, column=0, sticky='w', pady=(1, 3))

    def _insert_separator(self,):
        ttk.Separator(self.tkinterframe, orient='horizontal').grid(row=1, padx=(3,0), pady=(3,3), sticky='we')

    def _insert_value_list(self):
        self.widget_list = []
        self._insert_separator()
        for i in range(1, len(self.value_list)):
            tesCombobox_item = Label(text=self.value_list[i], **self._widget_settings('list'))
            tesCombobox_item.grid(row=i+1, column=0, sticky='nesw', pady=(0,0), padx=(3,0))
            self.widget_list.append(tesCombobox_item)
            tesCombobox_item.bind('<Enter>', self._event_value_list)
            tesCombobox_item.bind('<Leave>', self._event_value_list)
            tesCombobox_item.bind('<Button-1>', self._event_value_list)
            tesCombobox_item.bind('<Button-1>', self, add='+')

    def _set_value(self, event):
        self.value = event.widget['text']
        self.tesCombobox_title['text'] = self.value
        value_list = self.value_list.copy()
        value_list.remove(self.value)
        for widget, value in zip(self.widget_list, value_list):
            widget['text'] = value

    def _event_value_list(self, event) -> None:
        if 'Enter' in str(event):
            event.widget.config(background='white', foreground='black')
        if 'Leave' in str(event):
            event.widget.config(background=self.background, foreground='white')
        if 'Button' in str(event):
            self._set_value(event)

    def _insert_expand_button(self) -> None:
        self.expand_button = tesButton(**self._widget_settings('button'))
        self.expand_button.grid(row=0, column=1, sticky='e')
        self.expand_button.bind('<Enter>', self._event_combobox_button)
        self.expand_button.bind('<Leave>', self._event_combobox_button)

    def _event_combobox_button(self, event=None):
        if 'Enter' in str(event):
            event.widget.itemconfig('borderline', fill='gray')
            event.widget.itemconfig('borderradius', outline='gray')
        if 'Leave' in str(event):
            event.widget.itemconfig('borderline', fill=self.background)
            event.widget.itemconfig('borderradius', outline=self.background)


    def __expand_nofification(self) -> None:
        height_tesCombobox = (len(self.value_list)-1) * 25 + 44 + 10 #<- height ttk.Separstor
        if int(self.wget('height')) < height_tesCombobox:
            self.settings(height=height_tesCombobox)
            self.resize_frame()
            self.expand_button.settings(text='\u2B9D')
        else:
            self.settings(height=44)
            self.resize_frame()
            self.expand_button.settings(text='\u2B9F')

    def get(self) -> str:
        return self.value

    def __call__(self, event):
        self.command() if self.command else print(self.__str__())

    def __str__(self):
        return 'tesCombobox: ' + self.get()
