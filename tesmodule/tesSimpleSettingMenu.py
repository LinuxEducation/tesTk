import osimport jsonfrom tkinter import Toplevel, PhotoImage, Frame, Label, Entryfrom widgets import tesSimpleButtonclass MenuFrame(Frame):	def __init__(self, container: Toplevel):		Frame.__init__(self, container, background='#585858', padx=5)		self.pack(fill='both', expand=True)		self.columnconfigure(0, weight=2)class MenuSeparator(Frame):	def __init__(self, container=None, title: str = 'Category', title_color: str = 'white', line_color: str = '#424242'):		Frame.__init__(self, container, bg=container['background'])		self.columnconfigure(1, weight=2)		self.insert(title, title_color, line_color)	def insert(self, title, title_color, line_color) -> None:		Label(self,			  text=title,			  background=self['background'],			  foreground=title_color,			  font=('Arial', 11, 'italic')			  ).grid(row=0, column=0, sticky='w')		Frame(self, background=line_color).grid(row=0, column=1, sticky='ew', padx=(3, 0))class tesSimpleSettingMenu(Toplevel):	def __init__(			self,			container=None,			window_x: int = 500,			window_y: int = 300,			title: str = 'Setting Menu',			setting_data: dict[str, tuple] = None,			setting_file: str = 'default_setting_menu.json',			setting_save: bool | int = True,			command=None):		# object attribute		self.container = container		self.window_x = window_x		self.window_y = window_y		self.title_ = title		self.setting_data = setting_data		self.setting_file = setting_file		self.setting_save = setting_save		self.command = command		self.setting_menu_list = []		self._create_window()		self._run_settings()		self.wait_window()	def _create_window(self):		Toplevel.__init__(self, self.container, background='#424242')		self.iconphoto(False, PhotoImage(file='./icons/tesTk_window3.png'))		self.geometry(f'{self.window_x}x{self.window_y}')		self.title(self.title_)	def _run_settings(self):		if not self.setting_data:			self._tip_message()		else:			if self.setting_save:				if os.path.exists(self.setting_file):					setting_data = self._load_settings()					self._create_ui_menu(setting_data)				else:					self._create_ui_menu(self.setting_data)					self._save_settings()			else:				self._create_ui_menu(self.setting_data)	def _create_ui_menu(self, setting_data, i=0) -> None:		frame = MenuFrame(self)		for tags, value in setting_data.items():			if 'separator' in tags.lower():				separator = MenuSeparator(frame, title=value, line_color='#00838F')				separator.grid(row=i, column=0, sticky='nsew', columnspan=2, pady=(5, 2))				separator.tags = tags				separator.any_text = value				self.setting_menu_list.append(separator)				i += 1				continue			label = Label(frame,						  bg='#6E6E6E',						  fg='white',						  font=('Arial', 11),						  text=value[-1],						  anchor='w')			label.grid(row=i,					   column=0,					   pady=1,					   padx=(0, 3),					   sticky='ew')			entry = Entry(frame,						  font=('Arial', 11),						  highlightthickness=0,						  bg='#424242',						  width=5,						  relief='flat',						  fg='white')			entry.grid(row=i, column=1)			entry.insert(0, str(value[0]))			if str(value[0]) == 'None':				entry.configure(state='disabled')			entry.tags = tags			entry.value = value[0]			entry.any_text = value[-1]			self.setting_menu_list.append(entry)			i += 1		b1 = tesSimpleButton(self, text='Cancel', background='red', width=100, height=28, radius=5, fontsize=12)		b1.pack(side='right', padx=2, pady=3)		b1.command = self.destroy		b2 = tesSimpleButton(self, text='Accept', background='green', width=100, height=28, radius=5, fontsize=12)		b2.pack(side='right')		b2.command = self	def _tip_message(self) -> None:		self.geometry('650x250')		message = 'SimpleMenuSettings expects dict object:  {tags: [\'true/false\', \'some text\']}'		Label(self, text=message, font=('Arial', 14)).pack(expand=True)	def _save_settings(self) -> None:		with open(self.setting_file, 'w') as file:			json.dump(self.get_settings(), file, indent=4)	def _load_settings(self) -> dict:		with open(self.setting_file, 'r') as file:			settings = json.load(file)		return settings	def get_settings(self) -> dict:		menu_settings = {}		for obj in self.setting_menu_list:			if 'separator' not in obj.tags.lower():				try:					menu_settings[obj.tags] = [obj.get(), obj.any_text]				except:					menu_settings[obj.tags] = [obj.value, obj.any_text]			else:				menu_settings[obj.tags] = obj.any_text		return menu_settings	def _remember_menu_settings(self) -> None:		""" if the settings window is closed, all widgets in it will be deleted """		for obj in self.setting_menu_list:			if isinstance(obj, Entry):				obj.value = obj.get()	def __str__(self):		return 'SimpleSettingMenu ->  Window Destroyed!'	def __call__(self):		if self.setting_save:			self._save_settings()		self._remember_menu_settings()		self.destroy()		if self.command:			self.command()			return		print(self)