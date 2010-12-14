from pyglet import window
from pyglet import clock
from pyglet import font
from random import *
from math import *


class Sprite(object):
	
	def __get_left(self):
		return self.x
	left = property(__get_left)
	
	def __get_right(self):
		return self.x + self.image.width
	right = property(__get_right)
	
	def __get_top(self):
		return self.y + self.image.height
	top = property(__get_top)
	
	def __get_bottom(self):
		return self.y
	bottom = property(__get_bottom)
	
	def __init__(self, image_file, image_data=None, **kwargs):
		
		self.image_file = image_file
		if image_data is None:
			self.image = helper.load_image(image_file)
		else:
			self.image = image_data
		self.x = 0
		self.y = 0
		self.dead = False
		self.__dict__.update(kwargs)
		
	def draw(self):
		self.image.blit(self.x, self.y)
	
	def update(self):
		pass
	
	def intersect(self, sprite):
		"""Do the sprites intersect?
		@param sprite - the sprite to test
		"""
		return not ((self.left > sprite.right)
			or (self.right < sprite.left)
			or (self.top < sprite.bottom)
			or (self.bottom > sprite.top))
			
	def collide(self, sprite_list):
		"""Collision detection, returns a list of collisions"""
		
		lst_return  = [] 
		for sprite in sprite_list:
			if (self.intersect(sprite)):
				lst_return.append(sprite)
		return lst_return
