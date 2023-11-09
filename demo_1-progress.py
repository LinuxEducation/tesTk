from tkmodule import App
from widgets import tesProgress

if __name__ == '__main__':
	window = App('DemoProgress', '#313338')
	tesProgress(window, 160, 70, 16, 7, style=4, loop=3)
	window.mainloop()
