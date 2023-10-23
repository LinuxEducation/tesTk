## tesTk - Tkinter Widget's

> tesTk is Tkinter's modern widgets design. It is based on the tkinter canvas widget. You can use tesTk just like tkinter.

<p align="center">
  <a href="https://youtu.be/kXv28X6IoRs"><img src="/logo/tesTk.gif" width='30%' title="tesTk-logo"></a>
</p>

## WidgetCreatorTool

> Tool for basic widget configuration. Widget shape, background and foreground layer, font style and size, setting images and their positions. Easy and fast generation of widget parameters.

<p align="center">
  <img src="/images/WidgetCreatorTool.png" width='50%' height='30%'>
</p>

``example``

```py
from tkmodule import App
from widgets import tesButton

settings = {
	'width':            200,
	'height':           44,
	'radius':           11,
	'backgroundidx':    1,
	'bordercoloridx':   3,
	'fontsize':         18,
	'background':       'sea blue',
	'bordercolor':      'black',
	'text':             'Widget',
	'textcolor':        'white',
	'fonttype':         'Arial',
	'icon':             './icons/tk_smal.png',
	'iconposition':     'w',
	'iconoffset':       5,
	'style':            'simple'}

app = App()
tesButton(app, **settings).pack(expand=True)
app.mainloop()
```

## ColorPaletteTool

> A tool for visualization and color selection. ColorPalette has styles, you can add new colors or get them directly in the program. You can get a color with this tool or set a color in your program by specifying a name color and color number (idx).

<p align="center">
  <img src="/images/ColorPaletteTool.png" width='50%'>
</p>

``example``

```py
from func.color_palette import get_colors

colors = get_colors('Material Color')
print(colors)

tesButton(..., background='dark blue', backgroundidx=2).pack()
tesLabel(..., bordercolor='red', bordercoloridx=5).grid()
tesEntry(..., background='#424242', bordercolor='orange').pack()
tesFrame(..., bordercolor='black', bordercoloridx=0).pack()
```

## tesButton - widget

> The tesButton has many custom styles. The basic styles are: rounded corners, shadows, borders. Other available styles are: roll, transparent, reverse, underline, background animation and borders. Some styles can be combined: reverse + border animation, roll + background animation and borders.

<p align="center">
  <a href="/images/buttons-org.png"><img src="/images/buttons-mini.png" width='50%'></a> 
</p>

``example``

```py
from widgets import tesButton

tesButton(container, text='Open File', icon='./icons/open.png', command=function).pack()
tesButton(..., text='transparent', bordercolor='red', style='transparent').pack()
tesButton(..., text='record', background='green', radius=10, style='record').grid()
tesButton(..., text='animation', bordercolor='lawn green', bordercoloridx=0, animation='border').place()
tesButton(..., text='reverse', textcolor='white', background='gray', style='reverse').pack()
tesButton(..., text='roll', icon='./icons/settings.png', textposition='w', widthmax=160, widthmini=55, style='roll').grid()
tesButton(..., text='underline', background='#37474f', textcolor='orange', style='underline', animation='border').pack()
```

## tesSimpleButton, tesSmallButton - widget

> tesSimpleButton and tesSmallButton is designed for simple or small controls.

``example``

```py
from widgets import tesSmallButton, tesSimpleButton

tesSmallButton(container).pack()
tesSimpleButton(..., text='Click Me', command=func).grid()
```

## tesEntry - widget

> The tesEntry allows you to insert icons, set the underline style and enable border animation.

<p align="center">
  <img src="/images/entry.png" width='50%'></a> 
</p>

``example``

```py
from widgets import tesEntry

tesEntry(..., bordercolor='black', bordercoloridx=0, animation='border', text='Search').grid()
tesEntry(..., text='login', icon='./icons/user.png', iconposition='w').pack()
tesEntry(..., background='blue', textcolor='white', fontsize=18, style='underline').place()
```

## tesFrame - widget

> Widget tesFrame or tesLabelFrame, a frame for other widgets. Supports border animation.

<p align="center">
  <img src="/images/frame.png" width='40%'>
</p>

``example``

```py
from widget import tesFrame

lf = tesFrame(container, style='labelFrame', animation='border') ; lf.pack()
     tesFrame(lf.tkinterframe, width=280, height=60, background='gray').pack()
```

## tesCombobox - widget

> Widget tesCombobox... Supports.

<p align="center">
  <img src="/images/tesCombobox.png" width='50%'>
</p>

``example``

```py
from widget import tesCombobox

os_list = ['Windows', 'GNU Linux', 'Mac OSX']
tesCombobox(container, value_list=os_list, command=func).pack()
```

## tesSpinbox - widget

> Widget tesSpinbox... Supports.

<p align="center">
  <img src="/images/tesSpinbox.png" width='50%'>
</p>

``example``

```py
from widget import tesSpinbox

tesSpinbox(container, mini=0, maxi=100, step=10, value=20).pack()
```

## tesNotification - widget

> tesNotification is a notification system. It supports border animation, resizing and closing.

<p align="center">
  <img style="display: inline-block" src="/images/notification1.png" width='30%'>
  <img style="display: inline-block" src="/images/notification2.png" width='30%'>
  <img style="display: inline-block" src="/images/notification3.png" width='30%''>
</p>

``example``

```py
from widgets import tesNotufication

tesNotification().type('missed', container, icon='./icons/missed.png', title='Missed Call', subtitle='784604058', report=['list objects']).pack()
tesNotification().type('weather', container, icon='./icons/weather.png' ,title='Weather', subtitle='Rain and strong wind', report=['list objects']).pack()
tesNotification().type('player', container, icon='./icons/music.png', title='Paused', subtitle='Kings Of Leon - Sex on Fire')pack()
```

## tesProgress - widget

> Process, animation of work. Multiple animation styles, progress bar length, rectangle styles.

<p align="center">
  <a><img style="display: inline-block" src="/images/progress3.png" width='45%'></a>
  <a><img style="display: inline-block" src="/images/progress2.png" width='45%'></a>
</p>

``example``

```py
from tkmodule import App
from widgets import tesProgress

window = App('DemoProgress', '#313338')
tesProgress(window, 160, 70, 16, 7, style=4, loop=3)
window.mainloop()
```

## tesLabel - widget

> Supports background animation or borders and sets text positions.

``example``

```py
from widgets import tesLabel

tesLabel(..., text='Ready To Work', bordercolor='black', animation='border',).grid()
tesLabel(..., text='Loading', background='orange', backgroundidx=3, animation='background', textposition='center').pack()
```

## tesTk - tkinter module

> tesTk also supports modules based only on the tkinter library. App and AppInformation module.

<p align="center">
  <img style="display: inline-block" src="/images/app_information.png" width='50%'>
</p>

``example``

```py
from tkmodule import App, AppInformation
from widgets import tesSmallButton

app = App()
'''AppInformation expects data type dict'''
tesSmallButton(app, command=AppInformation).pack(expand=True)
app.mainloop()
```

Sample Demos

<p align="center">
  <img style="display: inline-block" src="/images/chat.png" width='20%'>
  <img style="display: inline-block" src="/images/notification.png" width='20%'>
  <img style="display: inline-block" src="/images/widget_button-org.png" width='20%'>
</p>
