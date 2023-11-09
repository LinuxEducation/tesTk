class BadParameter(Exception):
	def __str__(self):
		return str(self.args[0]) + ' -> Unexpected parameter! Please correct...'

class BadAnimationParameter(Exception):
	def __str__(self):
		if 'transparent' in self.args[0]:
			return str(self.args[0]) + ' -> This style does not support background animation...'
		return str(self.args[0]) + ' -> The animation expects a specific color name...'

class BadValue(Exception):
	def __str__(self):
		return str(self.args[0]) + ' -> Incorect value! Expected object: ' + str(type(self.args[0]))

class BadType(Exception):
	def __str__(self):
		return str(type(self.args[0])) + ' -> Incorect type! Expected object: ' + self.args[1]
