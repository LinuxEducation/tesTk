from tkinter import Tk, Label, Frame

class AppFrame(Frame):
    def __init__(self, container):
        Frame.__init__(self, container, background=container['bg'])
        self.pack(expand=True)

class AppLabel(Label):
    def __init__(self, container, text, fontsize=22):
        Label.__init__(self, container)
        settings = {'background':   container['background'],
                    'text':         text,
                    'font':         ('Verdana', fontsize),
                    'foreground':   'white'}
        self.config(**settings)
        self.pack(expand=True)

class App(Tk):
    def __init__(self, title=None, color='#424242', size='1400x600', resolution: bool = False):
        Tk.__init__(self)
        self.title(title)
        self.geometry(size)
        self['background'] = color
        if resolution:
            self.insert_label()
            self.bind('<Configure>', self.set_resolution)

    def message(self):
        AppLabel(self, text="This Window is a 'Container' for other code")

    def insert_label(self):
        self.resolution = Label(self, fg='white', bg='#424242', font=('Arial', 12, 'italic'), text='resolution')
        self.resolution.place(relx=0, rely=1, anchor='sw')

    def set_resolution(self, event=None):
        window_x = self.winfo_width()
        window_y = self.winfo_height()
        self.resolution.configure(text=f'{window_x}x{window_y}')


if __name__ == '__main__':
    app = App('Window Container')
    app.message()
    app.mainloop()
