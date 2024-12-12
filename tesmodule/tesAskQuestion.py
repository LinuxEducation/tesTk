from widgets import tesButtonfrom tkinter import Frame, Label, Topleveldef widget_settings(type_: str = None) -> dict:	settings_yes = {		'width': 180,		'height': 38,		'radius': 11,		'backgroundidx': 2,		'bordercoloridx': 3,		'fontsize': 16,		'background': 'green',		'bordercolor': 'black',		'text': 'Yes',		'textcolor': 'white',		'fonttype': 'Verdana',		'style': 'simple'}	settings_no = {		'width': 180,		'height': 38,		'radius': 11,		'backgroundidx': 2,		'bordercoloridx': 3,		'fontsize': 16,		'background': 'red',		'bordercolor': 'black',		'text': 'No',		'textcolor': 'white',		'fonttype': 'Verdana',		'style': 'simple'}	if type_ == 'yes':		return settings_yes	if type_ == 'no':		return settings_noclass FrameControlPanel(Frame):	def __init__(self, container: Toplevel):		Frame.__init__(self, container, background='#424242')		self.pack(side='bottom', fill='x')class tesAskQuestion(Toplevel):	def __init__(self,				 title: str = 'Question - Action',				 message: str = 'This file already exists! Are you sure?'):		Toplevel.__init__(self, background='#585858')		self.geometry('600x200')		self.minsize(400, 150)		self.title(title)		self.panel = FrameControlPanel(self)		self.create_UI(message)		self.selection = False		self.wait_window()	def create_UI(self, message) -> None:		self.insert_label(message)		self.insert_buttons()	def insert_label(self, message) -> None:		Label(self, text=message, bg='#585858', font=('Arial', 15), wraplength=400, fg='white').pack(expand=True)	def insert_buttons(self) -> None:		tesButton(self.panel, **widget_settings('yes'), command=lambda: self.set_selection(True)).pack(side='right', padx=(8, 5), pady=8)		tesButton(self.panel, **widget_settings('no'), command=self.set_selection).pack(side='right')	def set_selection(self, selection: bool = False) -> None:		if selection:			self.selection = True		self.destroy()	def __bool__(self):		return self.selection