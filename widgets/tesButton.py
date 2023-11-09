from src.widget import WidgetShape, WidgetSetting
from src.exception import BadAnimationParameter
import time

class tesButton(WidgetShape, WidgetSetting):
    def __init__(
            self,
            container,
            text: str = 'tesButton',
            textcolor: str = 'white',
            widthmax: int = 200,
            widthmini: int = None,
            style: str = 'normal',
            event: str = 'ButtonRelease-1',
            command=None,
            **kw):
        WidgetShape.__init__(self, container, text=text, textcolor=textcolor, **kw)

        self.style = style
        self.widthmax = widthmax
        self.widthmini = widthmini
        self.diode_status = 'white'
        self.command = command

        self.set_color()
        self.draw_widget()
        self.set_style()
        self._event(event)

    def set_style(self) -> None:
        if self.style == 'reverse':
            self._reverse_style()
        if self.style == 'transparent':
            self._transparent_style()
        if self.style == 'transparent2':
            self._transparent_style_two()
        if self.style == 'roll':
            self._roll_style()
        if self.style == 'underline':
            self._underline_style()
        if self.style == 'record':
            self._record_style()
        if self.style == 'simple':
            self._simple_style()

    def draw_widget(self) -> None:
        WidgetShape.draw_widget(self)
        if self.icon:
            self.insert_image()
        if self.text:
            self.insert_text()

    def widget_animation(self) -> None:
        WidgetSetting.widget_animation(self)

    def _event(self, event) -> None:
        self.bind(f'<{event}>', self)
        if event == 'Enter':
            self.bind('<Button-1>', self)

    def _reverse_style(self) -> None:
        def reverse_color(event) -> None:
            if 'Enter' in str(event):
                self.itemconfigure('shapeinside', fill=self.textcolor, outline=self.textcolor)
                self.itemconfigure('text', fill=self.background)
                self.background_name = self.textcolor
            if 'Leave' in str(event):
                self.itemconfigure('shapeinside', fill=self.background, outline=self.background)
                self.itemconfigure('text', fill=self.textcolor)
                self.background_name = self.background
        self.bind('<Enter>', reverse_color)
        self.bind('<Leave>', reverse_color)

    def _transparent_style(self) -> None:
        self.itemconfigure('shapeinside', fill=self.container['background'], outline=self.container['background'])
        if self.animation == 'background':
            raise BadAnimationParameter(self.style)
        
    def _transparent_style_two(self) -> None:
        self.background_name = self.bordercolor_name
        self.backgroundidx = self.bordercoloridx
        self.itemconfigure('shapeinside', fill=self.container['background'], outline=self.container['background'])

        def show_color(event) -> None:
            if 'Enter' in str(event):
                self.itemconfigure('shapeinside',
                                   fill=self.bordercolor, outline=self.bordercolor)
            if 'Leave' in str(event):
                self.itemconfigure('shapeinside',
                                   fill=self.container['background'], outline=self.container['background'])
        self.bind('<Enter>', show_color)
        self.bind('<Leave>', show_color)

    def _roll_style(self) -> None:
        if not self.widthmini:
            self.widthmini = self.radius + 32+1
        self._text = self.text
        self.settings(width=self.widthmini, text='')

        def roll_style(event) -> None:
            if 'Enter' in str(event):
                self.settings(width=self.widthmax, text=self._text)
            if 'Leave' in str(event):
                self.settings(width=self.widthmini, text='')
        self.bind('<Enter>', roll_style)
        self.bind('<Leave>', roll_style)

    def _underline_style(self) -> None:
        def underline_style(event) -> None:
            if 'Enter' in str(event):
                self.draw_underline() 
            if 'Leave' in str(event):
                self.delete('underline')
        self.bind('<Enter>', underline_style)
        self.bind('<Leave>', underline_style)

    def _record_style(self) -> None:
        self.draw_diode(size=6)

    def _simple_style(self) -> None:
        def simple_style(event) -> None:
            if 'Enter' in str(event):
                self.backgroundidx += 2
                self.background = self.get_colors(self.background_name)[self.backgroundidx]
                self.itemconfigure('shapeinside', fill=self.background, outline=self.background)
            if 'Leave' in str(event):
                self.backgroundidx -= 2
                self.background = self.get_colors(self.background_name)[self.backgroundidx]
                self.itemconfigure('shapeinside', fill=self.background, outline=self.background)
        self.bind('<Enter>', simple_style)
        self.bind('<Leave>', simple_style)

    def _diode_status(self) -> None:
        self.diode_status = 'red' if self.diode_status == 'white' else 'white'
        self.itemconfig('recorddiode', fill=self.diode_status)

    def __call__(self, mouse):
        if self.animation in ('background', 'border'):
            if self.color_number_idx == 0:
                self.widget_animation()
        if self.style == 'record':
            self._diode_status()
        if self.command:
            self.command()
            return
        print(self.__str__())

    def __str__(self):
        if not self.text:
            self.text = 'Empty'
        return 'tesButton: ' + self.text
