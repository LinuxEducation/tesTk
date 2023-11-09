from tkmodule import App
from widgets import tesFrame, tesLabel
import time

app = App()
frame = tesFrame(app, width=550, height=550,radius=50, background='#424242', bordercolor='black', border=2)
frame.pack(expand=True)

tesLabel(frame.tkinterframe, width=250, text='Hello My frend!', textposition='nw', textoffset=3, background='white').pack(anchor='nw', pady=(0, 8))
tesLabel(frame.tkinterframe, width=250, text='Hi! How are you?', textposition='nw', background='orange').pack(anchor='ne', pady=(0, 8))
tesLabel(frame.tkinterframe, width=450, height=80, text='I\'m fine!\nCan We talk about Your new job?', textposition='nw', background='white').pack(anchor='nw', pady=(0, 8))
tesLabel(frame.tkinterframe, width=450, height=80, text='Of course! What exactly would you like to\nknow?', textposition='nw', background='orange').pack(anchor='ne', pady=(0, 8))
tesLabel(frame.tkinterframe, width=460, height=80, text='I heard that you are a python programmer.\nHow much time did you spend learning?', textposition='nw', background='white').pack(anchor='nw', pady=(0, 8))
tesLabel(frame.tkinterframe, width=450, height=100, text='Over one year.\nBut I have been interested in it for more\nthan ten years', textposition='nw', background='orange').pack(anchor='ne', pady=(0, 8))

app.mainloop()


