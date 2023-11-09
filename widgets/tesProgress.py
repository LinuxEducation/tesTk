from src.rectangle import Rectangle
from tkinter import Frame
import time
import random

class tesProgress:
	def __init__(
			self, container, width: int = 80, height: int = 40, radius: int = 8, length: int = 8, style: int = 4, color: str = '#2b2d31', loop: int = 1):

		self.container = container
		self.width = width
		self.height = height
		self.radius = radius
		self.color = color
		self.length = length
		self.loop = loop
		self.rectangles_list = []
		self.create_canvas(container)
		self.run_animation(style)

	def create_canvas(self, container):
		"""centered frame for rectangle shape"""
		frame = Frame(container, background=container['bg']) ; frame.pack(expand=True)
		"""create rectangle widgets"""
		for position in range(self.length):
			rectangle = Rectangle(frame, self.width, self.height, self.radius, self.color)
			rectangle.grid(row=0, column=position, padx=4, sticky='n')
			self.rectangles_list.append(rectangle)

	def random_position(self, nlist=[]):
		while len(nlist) < self.length:
			number = random.randint(0,self.length-1)
			if number not in nlist:
				nlist.append(number)
		return nlist

	def run_animation(self, style):
		x=.6
		for idx in self.random_position():
			rectangle = self.rectangles_list[idx]
			rectangle.draw_shape_inside()
			rectangle.draw_shadow_shape()
			self.container.update()
			time.sleep(x)
			if x > .1:
				x -= .1
		'''pause'''
		time.sleep(.5)

		#2/ draw border line
		for rectangle in self.rectangles_list:
			rectangle.draw_border_lines()
			rectangle.draw_border_radius()
			self.container.update()
			time.sleep(0.1)
		'''pause'''
		time.sleep(.5)

		'''display the selected animation style'''
		if style == 1 or str(style).lower() == 'one':
			self._style_one()
		if style == 2 or str(style).lower() == 'two':
			self._style_two()
		if style == 3 or str(style).lower() == 'three':
			self._style_three()
		if style == 4 or str(style).lower() == 'four':
			self._style_four()

		'''final animation'''
		for idx in self.random_position():
			rectangle = self.rectangles_list[idx]
			rectangle.delete('widgetshape')
			self.container.update()
			time.sleep(.15)
		time.sleep(.2)
		self.container.destroy()


	def _style_one(self):
		for _ in range(self.loop):
			'''change color rectangle'''
			for rectangle in self.rectangles_list[:-1]:
				rectangle.settings(background='red')
				""" Very Importand! For a single rectangle, the window must be refreshed"""
				self.container.update()
				time.sleep(.1)
			'''back to the oryginal color'''
			for rectangle in self.rectangles_list[:-1]:
				rectangle.settings(background='#2b2d31')

			'''change color mobile rectangle '''
			rectangle = self.rectangles_list[-1]
			rectangle.settings(background='green')

			'''move last rectangle'''
			for x in range(10, 60):
				rectangle.grid_configure(padx=(x,0))
				self.container.update()
				time.sleep(.001)
			for x in reversed(range(10, 60)):
				rectangle.grid_configure(padx=(x,0))
				self.container.update()
				time.sleep(.01)
	
			'''finish and clear last (green) rectangle'''
			rectangle.settings(background='#2b2d31')


	def _style_two(self):
		for _ in range(self.loop):
			'''change color rectangle'''
			for rectangle in self.rectangles_list[:-1]:
				rectangle.settings(background='red')
				self.container.update()
				time.sleep(.1)
			'''restore all first shapes'''
			for rectangle in self.rectangles_list[:-1]:
				rectangle.settings(background='#2b2d31')

			'''change color mobile rectangle '''
			rectangle = self.rectangles_list[-1]
			rectangle.settings(background='green')

			for x in range(10, 60):
				rectangle.grid_configure(padx=(x,0))
				self.container.update()
				time.sleep(.001)
			for x in reversed(range(10, 60)):
				rectangle.grid_configure(padx=(x,0))
				self.container.update()
				time.sleep(.01)
	
			'''finish and clear last (green) recgtangles'''
			rectangle.settings(background='#2b2d31')

			'''change color'''
			if _ < self.loop:
				for rectangle in self.rectangles_list[:-1][::-1]:
					rectangle.settings(background='green')
					self.container.update()
					time.sleep(.1)

			'''finish and clear all rectangle'''
			for rectangle in self.rectangles_list[:-1]:
				rectangle.settings(background='#2b2d31')
				self.container.update()
			time.sleep(.2)	


	def _style_three(self):
		for _ in range(self.loop):
			'''change color'''
			for rectangle in self.rectangles_list[:-1]:
				rectangle.settings(background='red')
				self.container.update()
				time.sleep(.1)
				'''restore'''
				rectangle.settings(background='#2b2d31')

			'''mobile rectangle '''
			rectangle = self.rectangles_list[-1]
			rectangle.settings(background='green')

			for x in range(10, 60):
				rectangle.grid_configure(padx=(x,0))
				self.container.update()
				time.sleep(.001)
			for x in reversed(range(10, 60)):
				rectangle.grid_configure(padx=(x,0))
				self.container.update()
				time.sleep(.01)
	
			rectangle.settings(background='#2b2d31')


	def _style_four(self):
		for _ in range(self.loop):
			'''change color rectangle'''
			for rectangle in self.rectangles_list[:-1]:
				rectangle.settings(background='red')
				self.container.update()
				time.sleep(.1)

			'''back to the oryginal color'''
			for rectangle in self.rectangles_list[:-1]:
				rectangle.settings(background='#2b2d31')

			'''finish and change the last rectangle color'''
			rectangle = self.rectangles_list[-1]
			colors = rectangle.get_colors('green')[:-2]
			for color in colors + colors[::-1]:
				rectangle.itemconfig('shapeinside', fill=color, outline=color)
				self.container.update()
				time.sleep(.03)
			rectangle.itemconfig('shapeinside', fill='#2b2d31', outline='#2b2d31')
