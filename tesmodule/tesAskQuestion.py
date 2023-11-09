from widgets import tesButtonfrom tkinter import Frame, Label, Topleveldef widget_settings(type_: str = None) -> dict:	settings_yes = {		'width': 180,		'height': 40,		'radius': 11,		'backgroundidx': 2,		'bordercoloridx': 3,		'fontsize': 16,		'background': 'green',		'bordercolor': 'black',		'text': 'Yes',		'textcolor': 'white',		'fonttype': 'Verdana',		'style': 'simple'}	settings_no = {		'width': 180,		'height': 40,		'radius': 11,		'backgroundidx': 2,		'bordercoloridx': 3,		'fontsize': 16,		'background': 'red',		'bordercolor': 'black',		'text': 'No',		'textcolor': 'white',		'fonttype': 'Verdana',		'style': 'simple'}	if type_ == 'yes':		return settings_yes	if type_ == 'no':		return settings_noclass tesAskQuestion(Toplevel):	def __init__(self,				 container = None,				 title: str = 'Question - Action',				 message: str = 'This file already exists! Are you sure?'):		Toplevel.__init__(self, container, background='#585858')		self.geometry('600x200')		self.minsize(400, 150)		self.title(title)		self.answer = False		self.create_UI(message)		self.wait_window()	def create_UI(self, message):		self.create_frames()		self.insert_label(message)		self.insert_widgets()	def create_frames(self):		self.menu = Frame(self, background='#424242')		self.menu.pack(side='bottom', fill='x')	def insert_label(self, message):		msg = Label(self, text=message, bg='#585858', font=('Arial', 15), wraplength=400, fg='white')		msg.pack(expand=True)	def insert_widgets(self):		yes = tesButton(self.menu, **widget_settings('yes'), command=lambda: self.set_answer(True))		yes.pack(side='right', padx=(8, 5), pady=8)		no = tesButton(self.menu, **widget_settings('no'), command=lambda: self.set_answer(False))		no.pack(side='right')	def set_answer(self, set_answer):		if set_answer:			self.answer = True		self.destroy()