from tkmodule import App, AppLabel
from widgets import tesFrame
import time

def animation(e):
    lf1.widget_animation()

app = App('LabelFrame')
app.update()
time.sleep(0.3)
lf1 = tesFrame(app, width=600, height=400, radius=40, style='labelFrame', text='LabelFrame', textcolor='white', animation='border') ; lf1.pack(expand=True)
lf2 = tesFrame(lf1.tkinterframe, width=280, height=60, background='#585858') ; lf2.pack(expand=True)
AppLabel(lf2.tkinterframe, text='~ ! [ ) @ # $ ) [ % ^ & * +/- ', fontsize=15).pack(expand=True)

lf1.bind('<Enter>', animation)
app.mainloop()
