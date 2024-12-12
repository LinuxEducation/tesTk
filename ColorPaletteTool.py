from tkinter import Tk, Toplevel, Frame, Label, PhotoImage, StringVar
from widgets import tesButton, tesLabel, tesCombobox
from func.color_palette import get_colors
from tkmodule import AppInformation
from tesmodule import tesShowInfo
import time
import random

OS_ITEMS = 32

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Color Palette - Tool')
        self.geometry('1400x800')
        self.iconphoto(False, PhotoImage(file='./icons/tesTk_window3.png'))
        self.minsize(1400, 750)
        self['background'] = '#585858'
        self.app_window_size = 'default'
        self.hexcode_info = None
        self.bind('<Configure>', self.default_app_size)

    def run(self) -> None:
        self.menu = AppMenu(self)
        self.create_color_palette_frame()
        self.display_color_palette()
        self.create_app_status()

    def create_color_palette_frame(self) -> None:
        self.frame = Frame(self, background=self['background'])
        self.frame.pack(expand=True, pady=(5, 20))

    def display_color_palette(self, style: str = 'Material Color') -> None:
        self.number_label = []
        self.title_label = []

        colors = get_colors(style)
        settings = {'background':   '#585858',
                    'font':         ('Verdana', 12),
                    'foreground':   'white',
                    'padx':         10,
                    'anchor':       'se'}

        # number -row
        for index_number in range(list(colors.values())[0].__len__()):
            n = Label(self.frame, text=index_number, **settings, width=1)
            n.grid(row=0, column=index_number + 1)
            self.number_label.append(n)

        # title -column
        for color_name in colors:
            t = Label(self.frame, text=color_name, **settings, width=12)
            t.grid()
            self.title_label.append(t)

        # colors -grid
        for color_position_y in range(colors.__len__()):
            # color name position in the row
            pos = list(colors)[color_position_y]
            for color_position_x in range(list(colors.values())[0].__len__()):
                # color code position in the column
                col = colors[pos][color_position_x]
                tl = tesLabel(self.frame, background=col, width=75, height=44, radius=8, border=0)
                tl.grid(row=color_position_y + 1, column=color_position_x + 1, padx=0, pady=1)
                tl.bind('<Enter>', self._set_color)
                tl.bind('<Leave>', self._set_color)
                tl.bind('<Button-1>', self._get_char)
                tl.bind('<Button-1>', self.menu, add='+')

    def create_app_status(self) -> None:
        self.status = Label(self, text='Ready To Work', bg=self['bg'], fg='white', anchor='w')
        self.status.pack(fill='x', padx=10, pady=(0, 5))

    def default_app_size(self, event) -> None:
        if event.widget == app:
            size = self.get_ui_geometry()[2]
            if size > 1400:
                for item in self.title_label + self.number_label:
                    if not item.grid_info():
                        item.grid()
                if not self.menu.menu_items:
                    self.menu.display_menu()
                    self.menu.menu_items = True

    def _set_color(self, event) -> None:
        c = event.widget.grid_info()['column']
        r = event.widget.grid_info()['row']
        if 'Enter' in str(event) and 'frame' in str(event.widget):
            self.number_label[c - 1]['foreground'] = 'orange'
            self.title_label[r - 1]['foreground'] = 'orange'
        if 'Leave' in str(event) and 'frame' in str(event.widget):
            self.number_label[c - 1]['foreground'] = 'white'
            self.title_label[r - 1]['foreground'] = 'white'

    def _get_char(self, event) -> None:
        char = event.widget.wget('background').upper()
        self.clipboard_clear()
        self.clipboard_append(char)
        self.menu.tesl.insert(char)
        self.menu.tesl.widget_animation()
        self.status['text'] = 'Copied:  ' + char
        if not self.hexcode_info:
            tesShowInfo('Widget Colors', 'Hex Code copied to Clipboard. Use: Ctrl+V')
            self.hexcode_info = True

    def get_ui_geometry(self) -> tuple[float, float, float, float]:
        resolution_x = self.winfo_screenwidth()
        resolution_y = self.winfo_screenheight()
        window_x = self.winfo_width()
        window_y = self.winfo_height()
        return resolution_x, resolution_y, window_x, window_y

    def remove_color_palette_label(self) -> None:
        for items in self.title_label + self.number_label:
            items.grid_remove()

    def glue_app_window(self, mini_size: int = 756, position: str = 'rightM') -> None:
        time.sleep(.15)
        if self.get_ui_geometry()[2] < self.get_ui_geometry()[0]:
            if position == 'rightM':
                offset = self.get_ui_geometry()[0] - mini_size
                self.app_window_size = 'medium'
            if position == 'leftM':
                offset = '0'
                self.app_window_size = 'medium'
            if position == 'leftS':
                offset = '0'
                mini_size = 600
                self.menu.delete_menu_widgets()
            if position == 'rightS':
                mini_size = 600
                offset = self.get_ui_geometry()[0] - mini_size
                self.menu.delete_menu_widgets()
            self.remove_color_palette_label()
            self.minsize(mini_size, self.get_ui_geometry()[1] - OS_ITEMS)
            self.geometry(f'{mini_size}x{self.get_ui_geometry()[1]}+{offset}+0')


class AppMenu(Frame):
    def __init__(self, container):
        Frame.__init__(self, container)
        self['background'] = '#424242'
        self.pack(side='right', fill='y', padx=1, pady=1)
        self.display_menu()
        self.menu_items = True
        self.timer = 5
        self.timer2 = 0
        self.app_notification()

    def display_menu(self) -> None:
        combobox_list = ['Material Color', 'Flat Color', 'Web Color']
        label_settings = {'background':         '#424242',
                          'foreground':         '#BDBDBD',
                          'font': ('Verdana',   11),
                          'anchor':             'w'}

        button_settings = {'text':              'Display Tip',
                           'textposition':      'center',
                           'background':        'gray',
                           'backgroundidx':     0,
                           'bordercolor':       'black',
                           'bordercoloridx':    5,
                           'textcolor':         'white',
                           'style':             'simple',
                           'animation':         'border',
                           'fontsize':          15,
                           'radius':            11}

        glue_button_settings = {'text':             None,
                                'width':            46,
                                'height':           32,
                                'radius':           7,
                                'bordercolor':      '#6E6E6E',
                                'background':       'gray',
                                'backgroundidx':    0,
                                'style':            'simple',
                                'iconposition':     'center'}

        x = Frame(self, bg='#424242')
        x.pack(padx=15, pady=(20, 0))
        tesButton(x, **glue_button_settings, icon='./icons/pos_leftMedium.png', command=lambda: app.glue_app_window(position='leftM')).pack(side='left', padx=(0, 5))
        tesButton(x, **glue_button_settings, icon='./icons/pos_leftSmall.png', command=lambda: app.glue_app_window(position='leftS')).pack(side='left', padx=(0, 5))
        tesButton(x, **glue_button_settings, icon='./icons/pos_rightSmall.png', command=lambda: app.glue_app_window(position='rightS')).pack(side='left', padx=(0, 5))
        tesButton(x, **glue_button_settings, icon='./icons/pos_rightMedium.png', command=lambda: app.glue_app_window(position='rightM')).pack(side='left')

        #Color Palette
        color = Label(self, text='Color Palette', **label_settings)
        self.combo = tesCombobox(self, width=200, animation='border', background='#424242', bordercolor='black', bordercoloridx=5, radius=11, value_list=combobox_list, command=self.change_color_palette)
        #Hex Code
        self.hex_value = StringVar(self, 'Hex')
        self.hex = Label(self, textvariable=self.hex_value, **label_settings)
        self.tesl = tesLabel(self, background='gray', radius=11, bordercolor='black', bordercoloridx=5, animation='background', text='#0000', textposition='w', textcolor='white', fontsize=14)
        #How To Use
        use = Label(self, text='How To Use', **label_settings)
        tips = tesButton(self, **button_settings, command=self.display_tip)
        self.powered_by = Label(self, text='PoweredBy | tesTk', **label_settings)
        self.powered_by.bind('<Button-1>', self.display_poweredBy)

        #Display Method
        color.pack(fill='x', pady=(5, 0), padx=22)
        self.combo.pack(padx=15)
        self.hex.pack(fill='x', pady=(5, 0), padx=22)
        self.tesl.pack()
        use.pack(fill='x', pady=(5, 0), padx=22)
        tips.pack(padx=15)
        self.powered_by.pack(side='bottom', fill='x', pady=(0, 5), padx=15)

    def delete_menu_widgets(self) -> None:
        for item in self.winfo_children():
            item.pack_forget()
        self.configure(width=1)
        self.menu_items = False

    def clipboard_notification(self) -> None:
        self.hex_value.set('Copied to Clipboard')
        if self.timer > 0:
            self.after(400, self.clipboard_notification)
            self.timer -= 1
        else:
            self.hex_value.set('Hex')
            self.timer = 5

    def app_notification(self) -> None:
        if self.timer2 > 10:
            index = random.randint(7, 9)
            name = random.choices(get_colors("Material Color", True))[0]
            color = get_colors("Material Color").get(name)[index]
            title = "CreatedBy | LinuxEdu" if self.powered_by['text'] == "PoweredBy | tesTk" else "PoweredBy | tesTk"
            self.powered_by.configure(foreground=color, text=title)
            self.timer2 = 0
        self.after(1000, self.app_notification)
        self.timer2 += 1

    def change_color_palette(self) -> None:
        for item in app.frame.winfo_children():
            item.destroy()
        style = self.combo.get()
        app.display_color_palette(style)
        if app.app_window_size == 'medium':
            app.remove_color_palette_label()

    def display_tip(self, image: str = './images/tips_tricks.png') -> None:
        time.sleep(0.1)
        Tips(self, 1225, 344, 'How To Use').display_tip(image)

    def display_poweredBy(self, event):
        time.sleep(0.1)
        AppInformation(app)

    def __call__(self, event):
        if self.timer == 5:
            self.clipboard_notification()
        else:
            self.timer = 4

class Tips(Toplevel):
    def __init__(self, container, window_x: int = 1200, window_y: int = 700, title: str = None):
        Toplevel.__init__(self, container, width=window_x, height=window_y, bg='#585858')
        self.iconphoto(False, PhotoImage(file='./icons/tesTk_window.png'))
        self.title(title)
        self.geometry(f'{window_x}x{window_y}')
        if title == 'How To Use':
            self.maxsize(window_x, window_y)

    def display_tip(self, image) -> None:
        self.image = PhotoImage(file=image)
        Label(self, image=self.image, borderwidth=0).pack(padx=1, pady=1)


if __name__ == '__main__':
    app = App()
    app.run()
    app.mainloop()
