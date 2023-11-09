from tkmodule import App, AppFrame
from widgets import tesButton
from tkinter import Label

def demo():
    """Normal Style"""
    Label(frm, text='Normal', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=0, column=0, padx=20, pady=15)
    tesButton(frm, text='Open', background='green', backgroundidx=None, textcolor='white').grid(row=0, column=1, padx=10)
    tesButton(frm, text='Save', background='royal blue', icon='./icons/save.png', iconoffset=5).grid(row=0, column=2, padx=10)

    """Simple Style"""
    Label(frm, text='Simple', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=1, column=0, padx=20, pady=15)
    tesButton(frm, text='Simple', background='red', backgroundidx=0, textcolor='white', animation='border', style='simple').grid(row=1, column=1)
    tesButton(frm, text='Simple', background='green', backgroundidx=1, bordercolor='black', bordercoloridx=0, animation='background', style='simple').grid(row=1, column=2)
    tesButton(frm, text='Style', background='dark blue', backgroundidx=2, textcolor='white', style='simple').grid(row=1, column=3, padx=(8,8))

    'Transparent Style'
    Label(frm, text='Transparent', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=2, column=0, padx=20, pady=15)
    tesButton(frm, text='New Game', textcolor='white', bordercolor='red', style='transparent').grid(row=2, column=1)
    tesButton(frm, text='Delete', textcolor='white', bordercolor='blue', bordercoloridx=2, style='transparent').grid(row=2, column=2)
    tesButton(frm, text='Settings', textcolor='white', bordercolor='green', bordercoloridx=3, style='transparent').grid(row=2, column=3)

    '''Underline Style'''
    Label(frm, text='Underline', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=3, column=0, padx=20, pady=15)
    tesButton(frm, text='Photo', background='#37474f', textcolor='orange', style='underline', animation='border').grid(row=3, column=1)
    tesButton(frm, text='Music', background='red', backgroundidx=1, textcolor='white', style='underline', animation='background').grid(row=3, column=2)
    tesButton(frm, text='Video', background='sea blue', backgroundidx=0, textcolor='yellow', style='underline').grid(row=3, column=3)

    '''Reverse Style'''
    Label(frm, text='Reverse', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=4, column=0, padx=20, pady=15)
    tesButton(frm, text='Open File', icon='./icons/add_file.png', iconoffset=5, textposition='center', background='blue', backgroundidx=2, textcolor='white', style='reverse').grid(row=4, column=1)
    tesButton(frm, text='Save File', icon='./icons/save.png', iconoffset=5, textposition='center', background='gray', backgroundidx=9, textcolor='#424242', style='reverse', animation='border').grid(row=4, column=2)

    '''Record Style'''
    Label(frm, text='Record', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=5, column=0, padx=20, pady=15)
    tesButton(frm, text='Click Me', background='orange',  backgroundidx=2, style='record').grid(row=5, column=1)

    '''Roll Style'''
    Label(frm, text='Roll', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=6, column=0, padx=20, pady=15)
    tesButton(frm, text='Settings', icon='./icons/settings.png', iconoffset=5, textposition='c', textoffset=10,  widthmax=160, widthmini=45, background='gray', backgroundidx=2, textcolor='white', style='roll', animation='background').grid(row=6, column=1, padx=10, sticky='w')

    '''Animagtion-1 Style'''
    Label(frm, text='Animation-1', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=7, column=0, padx=20, pady=15)
    tesButton(frm, text='Play', background='red', backgroundidx=0, textcolor='white', animation='background').grid(row=7, column=1)
    tesButton(frm, text='Exit', background='dark blue', backgroundidx=2, textcolor='white', animation='background').grid(row=7, column=2, padx=(8,8))

    '''Animagtion-2 Style'''
    Label(frm, text='Animation-2', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=8, column=0, padx=20, pady=15)
    tesButton(frm, text='Click Me', textcolor='white', bordercolor='red', bordercoloridx=0, animation='border', style='transparent').grid(row=8, column=1)
    tesButton(frm, text='Load', background='green', backgroundidx=2, textcolor='white', bordercolor='black', bordercoloridx=0, animation='border').grid(row=8, column=2)
    tesButton(frm, text='Restart', textcolor='white', background='blue', backgroundidx=0, bordercolor='black', bordercoloridx=0, animation='border').grid(row=8, column=3)

    '''Transparent Style Two'''
    Label(frm, text='Transparent2', width=12, bg='#424242', fg='white', font=('Verdana', 20, 'italic'), anchor='e').grid(row=9, column=0, padx=20, pady=15)
    tesButton(frm, text='Delete 2', textcolor='white', bordercolor='blue', bordercoloridx=2, style='transparent2', animation='border').grid(row=9, column=1)
    tesButton(frm, text='Settings 2', textcolor='white', bordercolor='green', bordercoloridx=2, style='transparent2', animation='background').grid(row=9, column=2)

if __name__ == '__main__':
    app = App('Demo-2', size='1400x800')
    frm = AppFrame(app)
    demo()
    app.mainloop()
