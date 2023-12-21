from tkmodule import App
from widgets import tesText
from widgets import tesLabel
from widgets import tesWidgetBox, tesSmallButton

app = App(color='#424242', title='tesWidgetBox', size='900x500', resolution=True)
# tesTk WidgetBox
box = tesWidgetBox(app, title='tesBox', fontsize=15, radius=11, width=340, height_max=220, background='#0cc0df', button_color='green')
box.pack(expand=True)
# Tkinter Text
txt = tesText(box.tkinterframe, shadow=False, border=0, background='white', width=320, height=100, radius=7)
txt.pack(pady=5)
txt.tkintertext.delete(0.0, 'end')
txt.tkintertext.insert(0.0, 'This is tesWidgetBox. You can set the title, maximum width and maximum height of the widget and put all other widgets in it. ')
# tesTk SmallButton
but = tesSmallButton(box.tkinterframe, style=None, background='#0cc0df', backgroundidx=None, iconposition='center',  width=58, height=60, border=0, icon='./images/Tk-logo-blue_small.png')
but.pack(side='right', anchor='e', padx=(0, 5), pady=(0, 5))
# tesTk Label
lab = tesLabel(box.tkinterframe, shadow=False, border=0, radius=7, fontsize=9, width=260, height=32, background='#ffde59', text='tesTk is Tkinter\'s modern widgets design')
lab.pack(side='left', anchor='w', padx=(5, 0), pady=(5, 8))
app.mainloop() 
