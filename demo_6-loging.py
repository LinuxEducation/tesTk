from tkmodule import App, AppLabel
from widgets import tesFrame, tesButton, tesEntry
from tkinter import Label, PhotoImage

class LoginPanel:
    def create_UI(self, app):
        frame = {'width':       340,
                 'height':      360,
                 'radius':      30,
                 'background':  '#39404a',
                 'bordercolor': '#263238'}
        
        entry = {'width':           250,
                 'height':          40,
                 'radius':          11,
                 'background':      '#D8D8D8',
                 'bordercolor':     '#A4A4A4',
                 'iconposition':    'w'}

        button = {'width':          250,
                 'height':          40,
                 'radius':          11,
                 'background':      'red',
                 'backgroundidx':   3,
                 'bordercolor':     'red',
                 'border':          1,
                 'text':            'Sign In',
                 'textcolor':       'white',
                 'command':         self.logged,
                 'animation':       'border'}
  
        self.lg = tesFrame(app, **frame) ; self.lg.pack(expand=True)
        self.icon = PhotoImage(file='./icons/user1.png') ; Label(self.lg.tkinterframe, image=self.icon, background='#39404a').pack(pady=(10,20))
        self.log = tesEntry(self.lg.tkinterframe,  icon='./icons/user3.png', text='Login', **entry) ; self.log.pack(pady=(0,5))
        self.pas = tesEntry(self.lg.tkinterframe, icon='./icons/key1.png', text='*****', **entry) ; self.pas.pack()
        tesButton(self.lg.tkinterframe, **button).pack(pady=20)

    def logged(self, event=None):
        if self.log.get() and self.pas.get():
            self.lg.destroy()
            self.__create_UI()
            app.unbind('<Return>')

    @staticmethod
    def __create_UI():
        AppLabel(app, text="This Window is a 'Container' for other code")


app = App('Login Panel', '#313338')
ui = LoginPanel()
ui.create_UI(app)
app.bind('<Return>', ui.logged)
app.mainloop()
