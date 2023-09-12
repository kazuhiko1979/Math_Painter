from PIL import Image
import numpy as np

class Canvas:
	"""Object where all shapes are going to be drawn"""
	def __init__(self, height, width, color):
		self.color = color
		self.height = height
		self.width = width

		# Create a 3d numpy of zeros
		self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
		# change [0,0,0] with user given values for color
		self.data[:] = self.color

	def make(self, imagepath):
		"""Converts the current array into an image file"""
		img = Image.fromarray(self.data, 'RGB')
		img.save(imagepath)


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

canvas = Canvas(height=20, width=30, color=(255, 255, 255))
r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas)

s1 = Square(x=1, y=3, side=3, color=(0, 100, 222))
s1.draw(canvas)
canvas.make('canvas.png')