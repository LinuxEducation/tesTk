from tkmodule import App, AppFrame
from widgets import tesButton, tesEntry, tesLabel
from tkinter import Label


idx = 0 ; output_ = ''
def label_update(input_='Label'):
    l2.widget_animation()
    global idx, output_
    if len(input_) == idx:
        idx = 0; output_ = ''
        return None
    output_ += input_[idx]
    l2.insert(output_)
    idx += 1

def recording():
    if 'Recording' not in l1.get():
        l1.insert('Recording')
        l1.widget_animation()
        return None
    l1.insert('Stop')
    l1.widget_animation()


app = App('Demo-2')
frm = AppFrame(app)

'''Button'''
Label(frm, text='Button', bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=0, column=0, padx=20, pady=15)
tesButton(frm, text='Recording', background='#424242', textcolor='white', bordercolor='red', animation='border', style='record', command=recording).grid(row=0, column=1)
tesButton(frm, text='About', background='red', border=1, animation='border', backgroundidx=1, textcolor='white', command=label_update).grid(row=0, column=2, padx=(8, 8))
tesButton(frm, text='\u23FB', width=50, radius=45, background='green', bordercolor='black', textcolor='black', command=quit).grid(row=0, column=3)
tesButton(frm, text='Accept', background='yellow', backgroundidx=1, textcolor='blue', bordercolor='black', bordercoloridx=0, animation='background').grid(row=1, column=1)
tesButton(frm, text='Cancel', background='dark blue', backgroundidx=2, border=1, animation='background', textcolor='white').grid(row=1, column=2, padx=(8,8))
tesButton(frm, text='Settings', icon='./icons/settings.png', iconoffset=10, textposition='c', textoffset=15, widthmax=160, widthmini=55, width=160, background='gray', backgroundidx=2, textcolor='white', style='roll', animation='background').grid(row=1, column=3)
tesButton(frm, text='Open', icon='./icons/add_file.png', textposition='center', iconoffset=5, width=160, widthmax=190, background='blue', backgroundidx=2, textcolor='white', style='reverse', animation='border').grid(row=1, column=4)

'''Entry'''
Label(frm, text='Entry', bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='w').grid(row=2, column=0, pady=15)
tesEntry(frm, background='green', textcolor='white', bordercolor='black', bordercoloridx=0, animation='border', text='Search..', iconposition='center', style='underline').grid(row=2, column=1)
tesEntry(frm, background='#f44336', iconposition='w', textcolor='white', bordercolor='black', text='Tkinter Entry', iconoffset=3, icon='./icons/user.png').grid(row=3, column=1)
tesEntry(frm, background='white', iconposition='e', textcolor='black', bordercolor='black', text='Search....', iconoffset=-3, icon='./icons/search3.png').grid(row=3, column=2)

'''Label'''
Label(frm, text='Label', bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='w').grid(row=4, column=0, pady=15)
l1 = tesLabel(frm, background='royal blue', textcolor='white', bordercolor='black', bordercoloridx=0, animation='border',text='Ready To Work') ; l1.grid(row=4, column=1)
l2 = tesLabel(frm, background='orange', backgroundidx=3, animation='background', textcolor='black', bordercolor='black', text='Load...', textposition='center') ;l2.grid(row=4, column=2)

app.mainloop()
