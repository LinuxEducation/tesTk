from tkinter import Tk, Frame, Label, PhotoImage
from widgets import tesButton, tesSmallButton, tesSpinbox, tesEntry, tesWidgetBox
from func.color_palette import get_colors
from func.icon_database import icon_database
from func.setting_data import write_user_settings, read_user_settings
from tkmodule import AppInformation
from tesmodule import tesShowInfo, tesSimpleSettingMenu as SM
import time
import random
import os


def widget_settings(type_: str = None) -> dict:
    label_settings = {'background': '#424242',
                      'foreground': '#BDBDBD',
                      'font': ('Verdana', 9),
                      'anchor': 'w'}

    spinbox_settings = {'background': 'black',
                        'backgroundidx': 5,
                        'animation': 'border',
                        'width': 200,
                        'height': 42,
                        'shadow': 0}

    board_settings = {'width': 25,
                      'height': 25,
                      'radius': 1,
                      'text': None,
                      'shadow': None}

    button_settings = {'background': 'black',
                       'backgroundidx': 5,
                       'animation': 'border',
                       'width': 220,
                       'height': 55,
                       'style': 'simple',
                       'text': 'GetSettings',
                       'icon': './icons/xyz.png',
                       'iconposition': 'w',
                       'iconoffset': 25}

    widget_settings = {'width': 200,
                       'height': 44,
                       'radius': 11,
                       'backgroundidx': 1,
                       'bordercoloridx': 3,
                       'background': 'sea blue',
                       'bordercolor': 'black',
                       'border': 1,
                       'text': 'widget',
                       'textcolor': 'white',
                       'fontsize': 16,
                       'fonttype': 'Arial',
                       'style': 'simple',
                       'animation': 'border',
                       'textposition': 'center',
                       'textoffset': 5,
                       'iconoffset': 5}

    box_settings = {'fontsize': 11,
                    'radius': 11,
                    'width': 220,
                    'background': 'black',
                    'backgroundidx': 4,
                    'bordercolor': 'gray',
                    'bordercoloridx': 2,
                    'animation': 'border'}

    hexentry_settings = {'text': '#',
                         'icon': './icons/accept.png',
                         'iconposition': 'e',
                         'width': 110,
                         'height': 27,
                         'shadow': None,
                         'radius': 6,
                         'fontsize': 12,
                         'textcolor': 'white'}

    if type_ == 'label':
        return label_settings
    if type_ == 'spinbox':
        return spinbox_settings
    if type_ == 'button':
        return button_settings
    if type_ == 'board':
        return board_settings
    if type_ == 'widget':
        return widget_settings
    if type_ == 'box':
        return box_settings
    if type_ == 'hexentry':
        return hexentry_settings


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Widget Creator - Tool')
        self.geometry('1400x1000')
        self.iconphoto(False, PhotoImage(file='./icons/tesTk_window3.png'))
        self['background'] = '#585858'
        self.clicked = 0
        self.widget_icon_active = False
        self.settings_info = None
        self.font_format = ''

    def run(self) -> None:
        self.menu = AppMenu(self)
        self.insert_widget()
        self.insert_app_status()
        self.insert_board_colors()
        self.insert_hex_widget()
        self.app_service()
        self.load_user_settings()

    def insert_widget(self) -> None:
        self.widget = tesButton(self, **widget_settings('widget'), command=self.increment_widget_value)
        self.widget.pack(expand=True)
        self.widget.path = None

    def load_user_settings(self) -> None:
        if os.path.exists('bg_menu_settings.json'):
            self.change_widgets_settings('bg_menu_settings.json')
        if os.path.exists('fg_menu_settings.json'):
            self.change_widgets_settings('fg_menu_settings.json')
        if os.path.exists('global_settings.json'):
            self.change_widgets_settings('global_settings.json')

    def change_widgets_settings(self, settings_file: str) -> None:
        # change:  shadow, font format, icon position
        settings = read_user_settings(settings_file=settings_file)
        font_format = ''

        for tags, value in settings.items():
            if settings_file == 'bg_menu_settings.json':
                value_ = int(value[0] == 'True' or value[0] == '1')
                # draw shadow
                if tags == 'shadow':
                    self.update_settings(shadow=value_)

            if settings_file == 'fg_menu_settings.json':
                value_ = int(value[0] == 'True' or value[0] == '1')
                # Position of the icon
                if tags == 'iconposition':
                    self.widget.settings(iconposition=value[0])
                # font style
                if tags == 'bold':
                    if value_:
                        font_format += 'bold '
                if tags == 'italic':
                    if value_:
                        font_format += 'italic '
                if tags == 'underline':
                    if value_:
                        font_format += 'underline'
                self.update_settings(fontformat=font_format.strip())

            if settings_file == 'global_settings.json':
                if tags == 'width':
                    self.update_settings(width=value)
                    s1 = self.menu.items_tracked[0]
                    s1.insert(value)
                if tags == 'height':
                    self.update_settings(height=value)
                    s2 = self.menu.items_tracked[1]
                    s2.insert(value)
                if tags == 'radius':
                    self.update_settings(radius=value)
                    s3 = self.menu.items_tracked[2]
                    s3.insert(value)
                if tags == 'background':
                    self.update_settings(background=value)
                    e1 = self.menu.items_tracked[8]
                    e1.insert(value)
                if tags == 'backgroundidx':
                    self.update_settings(backgroundidx=value)
                    s4 = self.menu.items_tracked[3]
                    s4.insert(value)
                if tags == 'bordercolor':
                    self.update_settings(bordercolor=value)
                    s5 = self.menu.items_tracked[9]
                    s5.insert(value)
                if tags == 'bordercoloridx':
                    self.update_settings(bordercoloridx=value)
                    e2 = self.menu.items_tracked[4]
                    e2.insert(value)
                if tags == 'text':
                    self.update_settings(text=value)
                    e3 = self.menu.items_tracked[10]
                    e3.insert(value)
                if tags == 'textcolor':
                    self.update_settings(textcolor=value)
                    e4 = self.menu.items_tracked[11]
                    e4.insert(value)
                if tags == 'fonttype':
                    self.update_settings(fonttype=value)
                    e2 = self.menu.items_tracked[12]
                    e2.insert(value)
                if tags == 'fontsize':
                    self.update_settings(fontsize=value)
                    s6 = self.menu.items_tracked[5]
                    s6.insert(value)
                if tags == 'textoffset':
                    self.update_settings(textoffset=value)
                    s7 = self.menu.items_tracked[6]
                    s7.insert(value)
                if tags == 'textposition':
                    self.update_settings(textposition=value)
                    e6 = self.menu.items_tracked[-1]
                    e6.insert(value)
                if tags == 'iconoffset':
                    self.update_settings(iconoffset=value)
                    s8 = self.menu.items_tracked[7]
                    s8.insert(value)
                if tags == 'icon':
                    if value[0] == 'True':
                        button = self.menu.b4
                        button.diode_status = 'red'
                        button._record_style()
                        self.set_icon_activ()

    def set_icon_activ(self) -> None:
        self.widget_icon_active = True if self.widget_icon_active is False else False
        if self.widget_icon_active:
            self.insert_widget_icon()
        else:
            self.delete_widget_icon()

    def insert_widget_icon(self) -> None:
        name = self.menu.get_widget_tite()
        if name in icon_database():
            path = icon_database(name)
            self.widget.icon = PhotoImage(file=path).subsample(2, 2)
            self.widget.path = path
            self.widget.clear_widget('icon')
            self.widget.insert_image()
            if not os.path.exists('global_settings.json'):
                settings = {'icon': ['True', self.widget.path]}
                write_user_settings(settings_data=settings, settings_file='global_settings.json')
            else:
                settings = read_user_settings('global_settings.json')
                settings['icon'] = ['True', self.widget.path]
                write_user_settings(settings_data=settings, settings_file='global_settings.json')
            self.status['text'] = 'Update'

    def delete_widget_icon(self) -> None:
        self.widget.icon = None
        self.widget.itemconfig('icon', image='')
        settings = read_user_settings('global_settings.json')
        settings['icon'] = ['False', None]
        write_user_settings(settings_data=settings, settings_file='global_settings.json')
        self.status['text'] = 'Update'

    def change_icon_position(self, position) -> None:
        if self.widget_icon_active:
            self.widget.change_image_position(position)
            if os.path.exists('fg_menu_settings.json'):
                settings = read_user_settings('fg_menu_settings.json')
                settings['iconposition'] = [position, settings['iconposition'][-1]]
                write_user_settings(settings_data=settings, settings_file='fg_menu_settings.json')
            self.status['text'] = 'Update'

    def insert_app_status(self) -> None:
        self.status = Label(self, text='Ready To Work', bg=self['bg'], fg='white', anchor='w')
        self.status.pack(side='left', padx=10, pady=(0, 5))

    def insert_board_colors(self) -> None:
        self.buttons_items = []
        for color in '#484848', '#585858', '#6E6E6E', '#848484', '#A4A4A4', '#BDBDBD', '#D8D8D8', '#E6E6E6':
            button = tesButton(self, background=color, **widget_settings('board'))
            button.pack(side='right', padx=(0, 10), pady=(0, 10))
            button.command = lambda c=color: self.change_board_color(color=c)
            self.buttons_items.append(button)

    def insert_hex_widget(self) -> None:
        self.hex_entry = tesEntry(self, **widget_settings('hexentry'))
        self.hex_entry.command = lambda: self.change_board_color(self.hex_entry.get())
        self.hex_entry.tkinterentry.bind('<Return>', lambda event: self.change_board_color(self.hex_entry.get()))
        self.hex_entry.pack(side='right', padx=(0, 10), pady=(0, 10))

    def change_board_color(self, color) -> None:
        """The Board is the basis of the application"""
        try:
            self.configure(background=color)
            self.status.configure(background=color)
            self.widget.set_canvas_color(color)
            self.hex_entry.set_canvas_color(color)
            for button in self.buttons_items:
                button.set_canvas_color(color)
        except:
            pass

    def app_service(self, save_settings=None) -> None:
        for item in self.menu.items_tracked:
            if isinstance(item.get(), int):
                if item.get() != item.previous_value:
                    if item.tags == 'width':
                        value = item.get()
                        self.update_settings(width=value)
                    if item.tags == 'height':
                        value = item.get()
                        self.update_settings(height=value)
                    if item.tags == 'radius':
                        value = item.get()
                        self.update_settings(radius=value)
                    if item.tags == 'backgroundidx':
                        value = item.get()
                        if value < 10 and value > -11:
                            self.update_settings(backgroundidx=value)
                    if item.tags == 'bordercoloridx':
                        value = item.get()
                        if value < 10 and value > -11:
                            self.update_settings(bordercoloridx=value)

                    """ To track widgets we need:
                        the previous_vale -the tesSpinbox attributes
                        get() method, background_name and bordercolor_name - tesEntry and tesButton attribute
                    """

                    item.previous_value = item.get()
                    save_settings = True
                    self.status['text'] = 'Update'

            if isinstance(item.get(), str):
                if item.tags == 'background':
                    if item.get() in get_colors('Material Color'):
                        value = item.get()
                        if self.widget.background_name != item.get():
                            self.update_settings(background=value)
                            self.status['text'] = 'Update'
                            save_settings = True

            if isinstance(item.get(), str):
                if item.tags == 'bordercolor':
                    if item.get() in get_colors('Material Color'):
                        value = item.get()
                        if self.widget.bordercolor_name != item.get():
                            self.update_settings(bordercolor=value)
                            self.status['text'] = 'Update'
                            save_settings = True

            if isinstance(item.get(), str):
                if item.tags == 'text':
                    name = item.get()
                    if item.get() != self.widget.text:
                        if self.widget_icon_active:
                            if name.lower() in icon_database():
                                if self.widget.path != icon_database(name):
                                    self.insert_widget_icon()
                        self.widget.itemconfigure('text', text=name)
                        self.widget.text = name
                        self.status['text'] = 'Update'
                        save_settings = True

            if isinstance(item.get(), str):
                if item.tags == 'fonttype':
                    if item.get() != self.widget.wget('fonttype'):
                        value = item.get()
                        try:
                            self.update_settings(fonttype=value)
                            self.status['text'] = 'Update'
                        except:
                            pass
                        save_settings = True

            if isinstance(item.get(), int):
                if item.tags == 'fontsize':
                    if item.get() != self.widget.wget('fontsize'):
                        value = item.get()
                        self.update_settings(fontsize=value)
                        self.status['text'] = 'Update'
                        save_settings = True

            if isinstance(item.get(), str):
                if item.tags == 'textcolor':
                    if item.get() != self.widget.wget('textcolor'):
                        value = item.get()
                        try:
                            self.update_settings(textcolor=value)
                            self.status['text'] = 'Update'
                        except:
                            pass
                        save_settings = True

            if isinstance(item.get(), str):
                if item.tags == 'textposition':
                    if item.get() != self.widget.wget('textposition'):
                        value = item.get()
                        if value in ('nw', 'n', 'ne', 'w', 'e', 'sw', 's', 'se', 'c', 'center'):
                            self.update_settings(textposition=value)
                            self.status['text'] = 'Update'
                            save_settings = True

            if isinstance(item.get(), int):
                if item.tags == 'textoffset':
                    if item.get() != self.widget.wget('textoffset'):
                        value = item.get()
                        self.update_settings(textoffset=value)
                        self.status['text'] = 'Update'
                        save_settings = True

            if isinstance(item.get(), int):
                if item.tags == 'iconoffset':
                    if item.get() != self.widget.wget('iconoffset'):
                        value = item.get()
                        self.update_settings(iconoffset=value)
                        self.status['text'] = 'Update'
                        save_settings = True

        if save_settings:
            global_settings = {}
            for item in self.menu.items_tracked:
                global_settings[item.tags] = item.get()
            if self.widget_icon_active:
                global_settings['icon'] = ['True', self.widget.path]
            else:
                global_settings['icon'] = ['False', None]
            write_user_settings(settings_data=global_settings, settings_file='global_settings.json')

        self.after(200, self.app_service)

    def update_settings(self, **kw) -> None:
        """Tkinter has refresh problem and leaves artifacts"""
        self.widget.clear_widget('text')
        self.widget.clear_widget('icon')
        self.widget.settings(**kw)

    def increment_widget_value(self) -> None:
        self.clicked += 1
        self.status['text'] = 'Clicked:  ' + str(self.clicked)

    def get_widget_settings(self) -> None:
        settings = 'settings = {\n'
        for item in self.menu.items_tracked:
            key = f'\'{item.tags}\':'
            val = item.get()
            if isinstance(val, str):
                val = f"\'{val}\'"
            settings += f'\t{key:20}{val},\n'
        if self.widget_icon_active:
            # path to file
            key = '\'icon\':'
            val = f'\'{self.widget.path}\','
            settings += f'\t{key:20}{val}\n'
            # icon position
            key = '\'iconposition\':'
            val = f'\'{self.widget.iconposition}\','
            settings += f'\t{key:20}{val}\n'

        # widget shadow
        key = '\'shadow\':'
        val = f'{self.widget.shadow},'
        settings += f'\t{key:20}{val}\n'
        # font format
        key = '\'fontformat\':'
        val = f'\'{self.widget.fontformat}\','
        settings += f'\t{key:20}{val}\n'
        # widget animation
        key = '\'animation\':'
        val = f'\'border\','
        settings += f'\t{key:20}{val}\n'
        # widget style
        key = '\'style\':'
        val = '\'simple\'}'
        settings += f'\t{key:20}{val}\n'

        self.clipboard_clear()
        self.clipboard_append(settings)
        if self.status['text'] != 'Copied!  Use: Ctrl+V':
            self.status['text'] = 'Copied!  Use: Ctrl+V'
        if not self.settings_info:
            tesShowInfo('Widget Settings', 'Settings copied to Clipboard. Use: Ctrl+V')
            self.settings_info = True


class AppMenu(Frame):
    def __init__(self, container):
        Frame.__init__(self, container)
        self['background'] = '#424242'
        self.pack(side='right', fill='y', padx=0, pady=0)
        self.app_information()
        self.display_menu()
        self.menu_items = True
        self.timer = 5
        self.timer2 = 0
        self.app_notification()

    def get_widget_tite(self) -> str:
        """title is the name of the icon in the database"""
        for item in self.items_tracked:
            if item.tags == 'text':
                name = item.get().lower()
                return name

    def display_menu(self) -> None:
        self.resize_x = PhotoImage(file="./icons/resize_x2.png").subsample(2, 2)
        self.resize_y = PhotoImage(file="./icons/resize_y.png").subsample(2, 2)
        self.rotate = PhotoImage(file="./icons/rotate.png").subsample(2, 2)

        background_data = {'separator': 'Background',
                           'shadow': [True, 'Draw the \'shadow\' of the Widget'],
                           'border': [None, 'Draw the \'border\' of the Widget']}

        foreground_data = {'separator': 'Icon position',
                           'iconposition': ['w', 'Precise position of the \'icon\':  c, w, n, e, s, sw, nw, se, ne'],
                           'separator2': 'Font format',
                           'bold': [False, 'Use \'bold\' font'],
                           'italic': [False, 'Use \'italic\' font'],
                           'underline': [False, 'Use \'undeline\' font']}

        # Geometry Box
        gf = tesWidgetBox(self,
                          title='Geometry',
                          height_max=239,
                          button_color='red',
                          button_color_idx=2,
                          **widget_settings('box'))
        gf.pack(anchor='e', padx=10, pady=(10, 7))

        # Background Box
        bg = tesWidgetBox(self,
                          title='Background',
                          height_max=176,
                          button_color='sea blue',
                          button_color_idx=1,
                          **widget_settings('box'),
                          widget_box_setting=lambda: SM(self,
                                                        window_x=450,
                                                        window_y=250,
                                                        setting_data=background_data,
                                                        setting_file='bg_menu_settings.json',
                                                        title='Background Settings',
                                                        command=lambda: app.change_widgets_settings(
                                                            'bg_menu_settings.json')))
        bg.pack(anchor='e', padx=10, pady=(0, 7))
        bg.resize_widget_box()

        # Bordercolor Box
        bc = tesWidgetBox(self,
                          title='Bordercolor',
                          height_max=176,
                          button_color='black',
                          button_color_idx=3,
                          **widget_settings('box'))
        bc.pack(anchor='e', padx=10, pady=(0, 7))

        # Foreground Box
        fg = tesWidgetBox(self,
                          title='Foreground',
                          height_max=397,
                          button_color='orange',
                          button_color_idx=1,
                          **widget_settings('box'),
                          widget_box_setting=lambda: SM(self,
                                                        window_x=470,
                                                        window_y=250,
                                                        setting_data=foreground_data,
                                                        setting_file='fg_menu_settings.json',
                                                        title='Foreground Settings',
                                                        command=lambda: app.change_widgets_settings(
                                                            'fg_menu_settings.json')))
        fg.pack(anchor='e', padx=10, pady=(0, 7))
        fg.resize_widget_box()

        # Foreground Offset Box
        pg = tesWidgetBox(self, title='Foreground Offset',
                          height_max=176,
                          button_color='lawn green',
                          button_color_idx=1,
                          **widget_settings('box'))
        pg.pack(anchor='e', padx=10)
        pg.resize_widget_box()

        # Geometry
        Label(gf.tkinterframe, text='width', image=self.resize_x, compound='right', padx=7,
              **widget_settings('label')).pack(anchor='w', pady=(4, 0))
        s1 = tesSpinbox(gf.tkinterframe, tags='width', value=200, maxi=600, mini=100, step=10,
                        **widget_settings('spinbox'))
        s1.pack()
        Label(gf.tkinterframe, text='height', image=self.resize_y, compound='right', padx=7,
              **widget_settings('label')).pack(anchor='w')
        s2 = tesSpinbox(gf.tkinterframe, tags='height', value=44, **widget_settings('spinbox'))
        s2.pack()
        Label(gf.tkinterframe, text='radius', image=self.rotate, compound='right', padx=7,
              **widget_settings('label')).pack(anchor='w')
        s3 = tesSpinbox(gf.tkinterframe, tags='radius', value=11, **widget_settings('spinbox'))
        s3.pack()

        # Background
        Label(bg.tkinterframe, text='color', **widget_settings('label')).pack(padx=(7, 0), pady=(4, 0), anchor='w')
        e1 = tesEntry(bg.tkinterframe, tags='background', text='sea blue', textcolor='white',
                      **widget_settings('spinbox'))
        e1.pack()
        Label(bg.tkinterframe, text='number', **widget_settings('label')).pack(padx=7, anchor='w')
        s4 = tesSpinbox(bg.tkinterframe, tags='backgroundidx', value=1, mini=0, maxi=9, **widget_settings('spinbox'))
        s4.pack()

        # Bordercolor
        Label(bc.tkinterframe, text='color', **widget_settings('label')).pack(padx=(7, 0), anchor='w', pady=(4, 0))
        e2 = tesEntry(bc.tkinterframe, tags='bordercolor', text='black', textcolor='white',
                      **widget_settings('spinbox'))
        e2.pack()
        Label(bc.tkinterframe, text='number', **widget_settings('label')).pack(padx=7, anchor='w')
        s5 = tesSpinbox(bc.tkinterframe, tags='bordercoloridx', value=3, mini=0, maxi=9, **widget_settings('spinbox'))
        s5.pack()

        # Foreground
        Label(fg.tkinterframe, text='title', **widget_settings('label')).pack(padx=(7, 0), anchor='w', pady=(4, 0))
        e3 = tesEntry(fg.tkinterframe, tags='text', text='widget', textcolor='white', **widget_settings('spinbox'))
        e3.pack()
        Label(fg.tkinterframe, text='color', **widget_settings('label')).pack(padx=(7, 0), anchor='w')
        e4 = tesEntry(fg.tkinterframe, tags='textcolor', text='white', textcolor='white', **widget_settings('spinbox'))
        e4.pack()

        # font
        Label(fg.tkinterframe, text='font', **widget_settings('label')).pack(padx=(7, 0), anchor='w')
        e5 = tesEntry(fg.tkinterframe, tags='fonttype', text='Arial', textcolor='white', **widget_settings('spinbox'))
        e5.pack()
        s6 = tesSpinbox(fg.tkinterframe, tags='fontsize', value=16, mini=8, maxi=100, **widget_settings('spinbox'))
        s6.pack()

        # tex position
        Label(fg.tkinterframe, text='text position', **widget_settings('label')).pack(padx=(7, 0), anchor='w')
        e6 = tesEntry(fg.tkinterframe, tags='textposition', text='center', textcolor='white',
                      **widget_settings('spinbox'))
        e6.pack()

        # icon position
        Label(fg.tkinterframe, text='icon position', **widget_settings('label')).pack(padx=7, anchor='w')
        b1 = tesSmallButton(fg.tkinterframe, icon='./icons/pos_leftSmall.png', width=44, height=28,
                            iconposition='center')
        b1.command = lambda pos='w': app.change_icon_position(pos)
        b1.pack(side='left', padx=(7, 0))
        b2 = tesSmallButton(fg.tkinterframe, icon='./icons/pos_centerSmall.png', width=44, height=28,
                            iconposition='center')
        b2.command = lambda pos='center': app.change_icon_position(pos)
        b2.pack(side='left', padx=(6, 0))
        b3 = tesSmallButton(fg.tkinterframe, icon='./icons/pos_rightSmall.png', width=44, height=28,
                            iconposition='center', )
        b3.command = lambda pos='e': app.change_icon_position(pos)
        b3.pack(side='left', padx=(6, 0))
        self.b4 = tesSmallButton(fg.tkinterframe, width=44, height=28, style='record', radius=10, iconoffset=8,
                            icon='./icons/home2.png')
        self.b4.command = app.set_icon_activ
        self.b4.pack(side='left', padx=(7, 0))

        # offset position
        Label(pg.tkinterframe, text='text', **widget_settings('label')).pack(padx=7, anchor='w', pady=(3, 0))
        s7 = tesSpinbox(pg.tkinterframe, tags='textoffset', value=5, mini=-100, maxi=100, **widget_settings('spinbox'))
        s7.pack()
        Label(pg.tkinterframe, text='icon', **widget_settings('label')).pack(padx=7, anchor='w')
        s8 = tesSpinbox(pg.tkinterframe, tags='iconoffset', value=5, mini=-100, maxi=100, **widget_settings('spinbox'))
        s8.pack()

        tesButton(self, command=app.get_widget_settings, **widget_settings('button')).pack(side='bottom', pady=(0, 5))
        self.items_tracked = [s1, s2, s3, s4, s5, s6, s7, s8, e1, e2, e3, e4, e5, e6]

    def app_information(self) -> None:
        self.powered_by = Label(self, text='PoweredBy | tesTk', **widget_settings('label'))
        self.powered_by.bind('<Button-1>', self.display_poweredBy)
        self.powered_by.pack(side='bottom', fill='x', pady=(0, 10), padx=15)

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

    def display_poweredBy(self, event) -> None:
        time.sleep(0.1)
        AppInformation(app)


if __name__ == '__main__':
    app = App()
    app.run()
    app.mainloop()
