from abc import ABC, abstractmethod
from src.exception import BadParameter, BadAnimationParameter, BadType
from tkinter import Canvas, PhotoImage

''' This code is an example of how to fight a single pixel. 
    All canvas methods that draw a shape do it differently! '''

WIS = HIS = 2


class WidgetShape(Canvas, ABC):
    def __init__(
            self,
            container,
            width=200,
            height=44,
            radius=11,
            background='gray',
            backgroundidx=None,
            border=1,
            bordercolor='black',
            bordercoloridx=None,
            shadow=True,
            shadowcolor='#151515',
            text=None,
            textcolor='black',
            textposition='center',
            textoffset = 0,
            fonttype = 'Verdana',
            fontsize=16,
            icon=None,
            iconposition='w',
            iconoffset = 0,
            animation=None):
        Canvas.__init__(self, container, width=width, height=height, bg=container['bg'], highlightthickness=0)
        self.container = container
        self.width = width
        self.height = height
        self.radius = radius
        self.background = background
        self.backgroundidx = backgroundidx
        self.border = border
        self.bordercolor = bordercolor
        self.bordercoloridx = bordercoloridx
        self.shadowcolor = shadowcolor
        self.shadow = shadow
        self.text = text
        self.textcolor = textcolor
        self.textposition = textposition
        self.textoffset = textoffset
        self.iconposition = iconposition
        self.iconoffset = iconoffset

        self.fonttype = fonttype
        self.fontsize = fontsize
        self.animation = animation
        self.color_number_idx = 0

        self.icon = icon
        if self.icon:
            self.icon = PhotoImage(file=self.icon).subsample(WIS, HIS)

        self.background_name = background
        self.bordercolor_name = bordercolor

        self.animation_speed = 30

    def set_canvas_color(self, color: str) -> None:
        Canvas.configure(self, background=color)

    @abstractmethod
    def draw_widget(self) -> None:
        """Draw only the basic shape. Each widget must be implemented differently"""
        self.draw_shape_inside()
        if self.shadow:
            self.draw_shadow_shape()
        if self.border:
            self.draw_border_lines()
            self.draw_border_radius()

    def __get_shape_points(self, method: str, shadow: int = 1) -> tuple:
        if self.shadow == True:
            shadow = 3

        if self.border < 1:
            self.border = 1
            self.bordercolor = self.background

        fix = 0
        off = offset = 1
        if self.border % 2:
            fix = 0.5
            off = 0

        '''arc method
        '''
        arc1 = self.border / 2 + fix, self.border / 2 + fix, self.radius + self.border / 2 + fix, self.radius + self.border / 2 + fix
        arc2 = self.width - arc1[-1] - shadow, arc1[1], self.width - self.border / 2 - fix - shadow, arc1[-1]
        arc3 = arc2[0], self.height - self.radius - self.border / 2 + fix - shadow, arc2[
            2], self.height - self.border / 2 + fix - shadow
        arc4 = arc1[0], arc3[1], arc1[2], arc3[-1]

        '''line method
        '''
        line1 = arc1[2] - self.radius / 2, arc1[0] + off, arc2[0] + self.radius / 2, arc1[0] + off
        line2 = arc2[2], arc2[3] - self.radius / 2, arc3[2], arc3[1] + self.radius / 2
        line3 = arc3[0] + self.radius / 2, arc3[-1], arc4[2] - self.radius / 2, arc4[-1]
        line4 = arc1[0] + off, arc3[1] + self.radius / 2, arc1[0] + off, arc1[-1] - self.radius / 2

        '''shadow method
        '''
        shadow1 = self.width - 2, self.radius / 2, self.width - 2, self.height - self.radius / 2
        shadow2 = self.radius / 2, self.height - 2, self.width - self.radius / 2, self.height - 2
        shadow3 = self.width - self.radius - 2, self.height - self.radius - 2, self.width - 2, self.height - 2

        if method == 'arc':
            return arc1, arc2, arc3, arc4
        if method == 'line':
            return line1, line2, line3, line4
        if method == 'shadow':
            return shadow1, shadow2, shadow3
        if method == 'diode':
            return arc2[0], arc2[3]
        if method == 'underline':
            return line3[0] + 1, line3[1] - 1, line3[2] - 1, line3[3] - 1

    def draw_shape_inside(self) -> None:
        for point, corner in zip(self.__get_shape_points('arc'), [90, 0, 270, 180]):
            self.create_arc(point, start=corner, style='chord', width=self.border, fill=self.background,
                            outline=self.background, tags=('widgetshape', 'shapeinside'))
        self.create_polygon(self.__get_shape_points('line'), width=self.border, fill=self.background,
                            outline=self.background, tags=('widgetshape', 'shapeinside'))

    def draw_border_lines(self) -> None:
        for line in self.__get_shape_points('line'):
            self.create_line(line, width=self.border, fill=self.bordercolor, tags=('widgetshape', 'borderline'))

    def draw_border_radius(self, mystyle: str = 'arc') -> None:
        for point, corner in zip(self.__get_shape_points('arc'), [90, 0, 270, 180]):
            self.create_arc(point, start=corner, style=mystyle, width=self.border, outline=self.bordercolor,
                            fill=self.bordercolor, tags=('widgetshape', 'borderradius'))

    def draw_underline_style(self) -> None:
        self.create_line(self.__get_shape_points('underline'), width=self.border, fill=self.textcolor, tags='underline')
    draw_underline = draw_underline_style

    def draw_shadow_shape(self) -> None:
        for line in self.__get_shape_points('shadow')[:-1]:
            self.create_line(line, width=3, fill=self.shadowcolor, tags='widgetshape')
        self.create_arc(self.__get_shape_points('shadow')[-1], start=270, style='arc', width=3,
                        outline=self.shadowcolor, fill=self.bordercolor, tags='widgetshape')

    def insert_text(self) -> None:
        x = self.width / 2
        y = self.height / 2
        if self.textposition == 'w':
            x = self.border
            y = self.height / 2
        if self.textposition == 'sw':
            x = self.border
            y = self.height - 1
        if self.textposition == 'nw':
            x = self.border
            y = 0
        if self.textposition == 'e':
            x = self.width - self.border - 1
            y = self.height / 2
        if self.textposition == 'se':
            x = self.width - self.border
            y = self.height - 1
        if self.textposition == 'ne':
            x = self.width - self.border
            y = 0
        if self.textposition == 'n':
            y = 0
        if self.textposition == 's':
            y = self.height - 1
        self.create_text(x + self.textoffset, y, text=self.text, fill=self.textcolor, font=(f'{self.fonttype}', self.fontsize), anchor=self.textposition, tags='text')

    def insert_image(self) -> None:
        shadow = 0
        if self.shadow:
            shadow = 3
        x = self.width / 2
        y = self.height / 2
        if self.iconposition == 'w':
            x = self.border
            y = self.height / 2
        if self.iconposition == 'e':
            x = self.width - self.border - shadow
            y = self.height / 2
        if self.iconposition == 'sw':
            x = self.border
            y = self.height - self.border - shadow
        if self.iconposition == 'nw':
            x = self.border
            y = 0
        if self.iconposition == 'se':
            x = self.width - self.border - shadow
            y = self.height - self.border - shadow
        if self.iconposition == 'ne':
            x = self.width - self.border - shadow
            y = 0
        self.create_image(x+self.iconoffset, y, image=self.icon, anchor=self.iconposition, tags='icon')

    def draw_recording_diode(self, size: int) -> None:
        x = self.__get_shape_points('diode')[0] + self.radius / 2 - size / 2 -1
        y = self.__get_shape_points('diode')[1] - self.radius / 2 - size / 2
        self.create_oval(x, y, x + size, y + size, fill=self.diode_status, outline=self.bordercolor, tags='recorddiode')
    draw_diode = draw_recording_diode

    def change_image_position(self, position) -> None:
        WidgetShape.delete(self, 'icon')
        self.iconposition = position
        self.insert_image()

    def change_text_position(self, position) -> None:
        WidgetShape.delete(self, 'text')
        self.textposition = position
        self.insert_text()

class WidgetSetting(ABC):

    def resize_canvas(self, kwargs) -> None:
        if 'width' in kwargs.keys():
            self.configure(width=kwargs['width'])
        if 'height' in kwargs.keys():
            self.configure(height=kwargs['height'])
    resize_widget = resize_canvas

    def clear_canvas(self, tag: str = 'widgetshape') -> None:
        """ tags: 'widgetshape, shapeinside' are the ground, background layer.
            it's very important to remove only this object because the widget has many layers """
        WidgetShape.delete(self, tag)
    clear_widget = clear_canvas

    def set_shape_attributes(self, **kwargs) -> None:
        """validation of parameters"""
        for key, value in kwargs.items():
            if key not in self.__dict__:
                raise BadParameter(key)
            if not value:
                self.__dict__[key] = value
            if type(value) != type(self.__dict__[key]):
                raise BadType(value, str(type(self.__dict__[key])))
            '''update the widget attributes'''
            self.__dict__[key] = value

        if 'background' in kwargs.keys() or 'bordercolor' in kwargs.keys():
            if 'background' in kwargs.keys():
                self.background_name = kwargs['background']
            if 'bordercolor' in kwargs.keys():
                self.bordercolor_name = kwargs['bordercolor']
            #set kolor jest zawsze gdy zmieniamy backgroun lub bordercolor
            self.set_color()

        if 'backgroundidx' in kwargs.keys():
            self.backgroundidx = kwargs['backgroundidx']
            self.set_color()
        if 'bordercoloridx' in kwargs.keys():
            self.set_color()
            self.bordercoloridx = kwargs['bordercoloridx']

        if 'width' in kwargs or 'height' in kwargs:
            '''if the size has been changed, the canvas must be cleared and draw again'''
            self.resize_widget(kwargs)

        self.clear_widget()
        self.draw_widget()
    settings = set_shape_attributes

    @staticmethod
    def get_colors(color: str = None) -> dict | list | str:
        """expects real color name"""
        animation_colors = {'red':    ['#b71c1c', '#c62828', '#d32f2f', '#e53935', '#f44336', '#ef5350', '#e57373', '#ef9a9a', '#ffcdd2', '#ffebee'],
                      'pink':         ['#880e4f', '#ad1457', '#c2185b', '#d81b60', '#e91e63', '#ec407a', '#f06292', '#f48fb1', '#f8bbd0', '#fce4ec'],
                      'indigo':       ['#4a148c', '#6a1b9a', '#7b1fa2', '#8e24aa', '#9c27b0', '#ab47bc', '#ba68c8', '#ce93d8', '#e1bee7', '#f3e5f5'],
                      'purple':       ['#311b92', '#4527a0', '#512da8', '#5e35b1', '#673ab7', '#7e57c2', '#9575cd', '#b39ddb', '#d1c4e9', '#ede7f6'],
                      'dark blue':    ['#1a237e', '#283593', '#303f9f', '#3949ab', '#3f51b5', '#5c6bc0', '#7986cb', '#9fa8da', '#c5cae9', '#e8eaf6'],
                      'blue':         ['#0d47a1', '#1565c0', '#1976d2', '#1e88e5', '#2196f3', '#42a5f5', '#64b5f6', '#90caf9', '#bbdefb', '#e3f2fd'],
                      'blue2':        ['#01579b', '#0277bd', '#0288d1', '#039be5', '#03a9f4', '#29b6f6', '#4fc3f7', '#81d4fa', '#b3e5fc', '#e1f5fe'],
                      'sea blue':     ['#006064', '#00838f', '#0097a7', '#00acc1', '#00bcd4', '#26c6da', '#4dd0e1', '#80deea', '#b2ebf2', '#e0f7fa'],
                      'cyprus':       ['#004d40', '#00695c', '#00796b', '#00897b', '#009688', '#26a69a', '#4db6ac', '#80cbc4', '#b2dfdb', '#e0f2f1'],
                      'green':        ['#1b5e20', '#2e7d32', '#388e3c', '#43a047', '#4caf50', '#66bb6a', '#81c784', '#a5d6a7', '#c8e6c9', '#e8f5e9'],
                      'lawn green':   ['#33691e', '#558b2f', '#689f38', '#7cb342', '#8bc34a', '#9ccc65', '#aed581', '#c5e1a5', '#dcedc8', '#f1f8e9'],
                      'olive green':  ['#827717', '#9e9d24', '#afb42b', '#c0ca33', '#cddc39', '#d4e157', '#dce775', '#e6ee9c', '#f0f4c3', '#f9fbe7'],
                      'yellow':       ['#f57f17', '#f9a825', '#fbc02d', '#fdd835', '#ffeb3b', '#ffee58', '#fff176', '#fff59d', '#fff9c4', '#fffde7'],
                      'orange':       ['#ff6f00', '#ff8f00', '#ffa000', '#ffb300', '#ffc107', '#ffca28', '#ffd54f', '#ffe082', '#ffecb3', '#fff8e1'],
                      'dark orange':  ['#e65100', '#ef6c00', '#f57c00', '#fb8c00', '#ff9800', '#ffa726', '#ffb74d', '#ffcc80', '#ffe0b2', '#fff3e0'],
                      'hd orange':    ['#bf360c', '#d84315', '#e64a19', '#f4511e', '#ff5722', '#ff7043', '#ff8a65', '#ffab91', '#ffccbc', '#fbe9e7'],
                      'brown':        ['#3e2723', '#4e342e', '#5d4037', '#6d4c41', '#795548', '#8d6e63', '#a1887f', '#bcaaa4', '#d7ccc8', '#efebe9'],
                      'black':        ['#000000', '#151515', '#1C1C1C', '#2E2E2E', '#424242', '#585858', '#6E6E6E', '#848484', '#A4A4A4', '#BDBDBD'],
                      'gray':         ['#424242', '#585858', '#6E6E6E', '#848484', '#A4A4A4', '#BDBDBD', '#D8D8D8', '#E6E6E6', '#F2F2F2', '#FAFAFA'],
                      'anthracite':   ['#263238', '#37474f', '#455a64', '#546e7a', '#607d8b', '#78909c', '#90a4ae', '#b0bec5', '#cfd8dc', '#eceff1']}
        if not color:
            return animation_colors
        return animation_colors[color]

    def set_color(self, background_color_set: bool = False, bordercolor_set: bool = False) -> None:
        ''' if *idx is set and color name is in the dictionary...
            get char from the list '''
        if type(self.backgroundidx) is int:
            if self.background_name not in self.get_colors().keys():
                raise BadAnimationParameter(self.background_name)
            self.background = self.get_colors(self.background_name)[self.backgroundidx]
            background_color_set = True
        if type(self.bordercoloridx) is int:
            if self.bordercolor_name not in self.get_colors().keys():
                raise BadAnimationParameter(self.bordercolor_name)
            self.bordercolor = self.get_colors(self.bordercolor_name)[self.bordercoloridx]
            bordercolor_set = True

        if self.animation == 'background':
            ''' if *idx is not set, set the value to 0 '''
            if not background_color_set:
                if self.background_name not in self.get_colors().keys():
                    raise BadAnimationParameter(self.background_name)
                self.backgroundidx = 0
                self.background = self.get_colors(self.background_name)[self.backgroundidx]
        if self.animation == 'border':
            if not bordercolor_set:
                if self.bordercolor_name not in self.get_colors().keys():
                    raise BadAnimationParameter(self.bordercolor_name)
                self.bordercoloridx = 0
                self.bordercolor = self.get_colors(self.bordercolor_name)[self.bordercoloridx]

    def set_animation_colors(self) -> None:
        if self.animation == 'background':
            self.colors = self.get_colors(self.background_name)[self.backgroundidx:7] \
                          + self.get_colors(self.background_name)[self.backgroundidx:self.backgroundidx + 6][::-1]
        if self.animation == 'border':
            self.colors = self.get_colors(self.bordercolor_name)[self.bordercoloridx:7] \
                          + self.get_colors(self.bordercolor_name)[self.bordercoloridx:self.bordercoloridx + 6][::-1]

    @abstractmethod
    def widget_animation(self) -> None:
        if self.color_number_idx == 0:
            self.set_animation_colors()
        if self.color_number_idx <= self.colors.__len__() - 1:
            if self.animation == 'background':
                self.itemconfig('shapeinside', fill=self.colors[self.color_number_idx],
                                outline=self.colors[self.color_number_idx])
            if self.animation == 'border':
                self.itemconfig('borderline', fill=self.colors[self.color_number_idx])
                self.itemconfig('borderradius', outline=self.colors[self.color_number_idx])
            self.color_number_idx += 1
            self.after(self.animation_speed, self.widget_animation)
        else:
            self.color_number_idx = 0

    def wget(self, key: str = None):
        if not key:
            return self.__dict__
        return self.__dict__[key]
