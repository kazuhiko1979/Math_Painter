class Rectangle:

	def __init__(self, x, y, height, width, color):
		self.color = color
		self.width = width
		self.height = height
		self.y = y
		self.x = x

	def draw(self, canvas):
		"""Draws itself into the canvas"""
		# Change a slice of the array with new value
		canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:

	def __init__(self, x, y, side, color):
		self.color = color
		self.side = side
		self.y = y
		self.x = x

	def draw(self, canvas):
		"""Draw itself into the canvas"""
		# Changes a slice of the array with new values
		canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color
