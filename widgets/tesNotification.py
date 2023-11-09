from abc import ABC, abstractmethod
from .tesFrame import tesFrame
from .tesButton import tesButton
from tkinter import Frame, Label, PhotoImage

class Notification(tesFrame, ABC):
    @abstractmethod
    def _insert_icon(self, icon): pass

    @abstractmethod
    def _insert_title(self, title): pass

    @abstractmethod
    def _insert_subtitle(self, subtitle): pass

    @abstractmethod
    def _insert_message(self, message): pass

class BasicNotification(Notification, ABC):
    def __init__(self, container, icon='./icons/notifi.png', title='Title', subtitle='Subtitle - short message', message='Message - longer message'):
        tesFrame.__init__(self, container, width=500, height=80, background='#2E2E2E')
        self._insert_icon(icon)
        self._insert_title(title)
        self._insert_subtitle(subtitle)
        self._insert_message(message)
        self._grid_settings()
        self._event_settings()
        self._insert_expand_button()
        self.close_button = None

    def _grid_settings(self) -> None:
        self.tkinterframe.columnconfigure(1, weight=2)
        self.pack_configure(pady=(4, 0))

    def _insert_icon(self, icon: str) -> None:
        self.icon = PhotoImage(file=icon).subsample(1, 1)
        Label(self.tkinterframe, bg='#2b2d31', image=self.icon).grid(row=0, column=0, rowspan=2)

    def _insert_title(self, title: str) -> None:
        Label(self.tkinterframe, bg='#2E2E2E', text=title, font=('Verdana', 14, 'italic', 'bold'), fg='#ff9800', ).grid(row=0, column=1, sticky='w', padx=(5, 0))

    def _insert_subtitle(self, subtitle: str) -> None:
        Label(self.tkinterframe, bg='#2E2E2E', text=subtitle, font=('Verdana', 13), fg='white').grid(row=1, column=1, sticky='w', padx=(5, 0), pady=(0,3))

    def _insert_message(self, message: str) -> None:
        Label(self.tkinterframe, bg='#2E2E2E', text=message, font=('Verdana', 13), fg='white', justify='left').grid(row=2, column=1, sticky='w', padx=(5, 0))

    ''' logic of expand button
        if the button is pressed, the notification is rolled out
    '''
    def _insert_expand_button(self) -> None:
        self.expand_button = tesButton(self.tkinterframe, command=self.__expand_nofification, 
                                       text='\u2BC6', fontsize=10, textcolor='#FAFAFA', background='#2E2E2E', bordercolor='#2E2E2E', border=1, width=25, height=25, radius=0, shadow=None)
        self.expand_button.grid(row=1, column=2, padx=(0, 10))

    def __expand_nofification(self) -> None:
        if int(self.wget('height')) < 160:
            self.settings(height=160)
            self.resize_frame()
            self.expand_button.settings(text='\u2BC5')
        else:
            self.settings(height=80)
            self.resize_frame()
            self.expand_button.settings(text='\u2BC6')

    ''' logic of close button
        button is created if the cursor is inside the notification
    '''

    def __show_button(self, event: str) -> None:
        if not self.close_button:
            self.close_button = tesButton(self.tkinterframe, command=self.__destroy_notification, text='\u2718', textcolor='#FAFAFA', fontsize=10,
                                          background='#2E2E2E', bordercolor='#2E2E2E', border=1, width=25, height=25, radius=8, shadow=None)
            self.close_button.grid(row=0, column=2, padx=(0, 10))
        self.close_button.grid()

    def __hide_button(self, event: str) -> None:
        self.close_button.grid_remove()
        
    def __destroy_notification(self) -> None:
        self.destroy()

    def _event_settings(self) -> None:
        self.tkinterframe.bind('<Enter>', self.__show_button)
        self.tkinterframe.bind('<Leave>', self.__hide_button)  

class SimpleMessage(BasicNotification):
    def _insert_expand_button(self):
        return None

    def _insert_message(self, message):
        return None

class StandardMessage(BasicNotification):
    pass

class PlayerNotification(BasicNotification):
    def __init__(self, container, icon='./icons/notifi.png', title='Title', subtitle='Subtitle - short message'):
        BasicNotification.__init__(self, container, icon, title, subtitle)
        self._insert_player()

    def _insert_player(self) -> None:
        control_panel = Frame(self.tkinterframe, bg='#2E2E2E')
        self.prev = tesButton(control_panel, text='<', textcolor='white', background='black', backgroundidx=3, border=1, width=50, height=30, radius=10, animation='border')
        self.play = tesButton(control_panel, text='Play', textcolor='white', background='black', backgroundidx=3, border=1, width=150, height=40, radius=16, animation='border', command=self.__change_status)
        self.next = tesButton(control_panel, text='>', textcolor='white', background='black', backgroundidx=3, border=1, width=50, height=30, radius=10, animation='border')
        
        control_panel.grid(row=2, columnspan=2, pady=(20, 0))
        self.prev.grid(row=0, column=0)
        self.play.grid(row=0, column=1, padx=(5, 5))
        self.next.grid(row=0, column=2)
    
    def _insert_message(self, message):
        return None

    @staticmethod
    def __change_status():
        print('not yet implemented')

class ReportNotification(BasicNotification, ABC):
    def __init__(self, container, icon: str = './icons/notifi.png', title: str = 'Title', subtitle: str = 'Subtitle - short message', report: list = 'Report'):
        BasicNotification.__init__(self, container, icon, title, subtitle)
        self._insert_report(report)

    def _insert_report(self, report) -> None:
        for i in range(len(report)):
            Label(self.tkinterframe, text=report[i], bg='#2E2E2E', fg='#BDBDBD').grid(row=i+2, column=1, sticky='w', padx=(8, 0))

    def _insert_message(self, message):
        return None

class MissedNotification(ReportNotification):
    pass

class WeatherNotification(ReportNotification):
    pass

class tesNotification:
    @staticmethod
    def type(type_: str = 'standard', container=None, **kw) -> Notification:
        if type_ == 'simple':
            return SimpleMessage(container, **kw)
        if type_ == 'standard':
            return StandardMessage(container, **kw)
        if type_ == 'player':
            return PlayerNotification(container, **kw)
        if type_ == 'weather':
            return WeatherNotification(container, **kw)
        if type_ == 'missed':
            return MissedNotification(container, **kw)
