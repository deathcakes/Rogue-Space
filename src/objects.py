from pyglet import window
from pyglet import clock
from pyglet import font
from random import *
from math import *

class base_item:
	pass

class base_door:
	"""Defines door properties, can be opened/closed"""
	pass

class open_door(base_door):
	"""What do you think"""
	pass

class closed_door(base_door):
	"""Self explanatory"""
	pass

class broken_door(base_door):
	"""Door that is closed and has to be cut through with a welding torch"""
	pass

class base_chest:
	"""Object that can contain other objects or items"""
	pass

class locker(base_chest):
	"""Smallest chest implementation"""
	pass

class cupboard(base_chest):
	"""Larger chest implementation"""
	pass

class vault(base_chest):
	"""Largest chest implementation"""
	pass

class get_random_item:
	"""Obtains a random item based on level"""
