from pyglet import window
from pyglet import clock
from pyglet import font
from random import *
from math import *


import helpers
import objects
import mobs



class level_properties:
	"""Stores properties of levels"""
	
	def __init__(self, depth, max_x, max_y, min_x, min_y, max_rooms, max_mobs, max_items, max_mob_level, max_item_level):
		
		self.depth = depth
		self.max_x = max_x
		self.max_y = max_y
		self.min_x = min_x
		self.min_y = min_y
		self.max_rooms = max_rooms
		self.max_mobs = max_mobs
		self.max_items = max_items
		self.max_mob_level = max_mob_level
		self.max_item_level = max_item_level
		
		
class level(object):
	"""Level class, defines size, monster and object type and room/scenery frequency"""
		
	def __init__(self, level_properties):
		
		self.props = level_properties
		
		# Generate occupation map
		
		self.occupied_tiles = {}
		
		for y in range(self.props.min_y, self.props.max_y):
			for x in range(self.props.min_x, self.props.max_x):
				self.occupied_tiles[(x, y)] = None
				
		self.items = {}
		self.mobs = {}
		
		self.rooms = {}
				
	def get_rooms(self):
		"""Needs to be able to have proportions of rooms within the level"""
		self.max_rooms = self.props.max_rooms
		
		self.max_room_basic = int((self.max_rooms/100)*70)
		self.max_room_long = int((self.max_rooms/100)*10)
		self.max_room_hangar = int((self.max_rooms/100)*2)
		self.max_room_lab = int((self.max_rooms/100)*9)
		self.max_room_workshop = int((self.max_rooms/100)*9)
		
	
	def is_occupied(self, x, y):
		"""Checks whether a tile is occupied"""
		for k, v in self.occupied_tiles:
			if k == y:
				if v == x:
					if self.occupied_tiles[(x, y)] == None:
						return 0
					else:
						return 1
	
	def set_occupied(self, x, y, tile):
		"""Sets a tile as occupied, given a tuple or list of x and y coordinates"""
		for k, v in self.occupied_tiles:
			if k == y:
				if v == x:
					if self.is_occupied(x, y) == 0:
						self.occupied_tiles[(x, y)] = tile
						return 0
					else:
						return 1
			


class base_room(object):
	"""Base class for the room object"""
	
	def __get_type(self):
		return self.__r_type
	r_type = property(__get_type)
	
	def __init__(self, r_type, level):
		"""Only way to set type is through init call"""
		self.__r_type = r_type
		self.objects = []
		self.monsters = []
				
		# Dimensions measured from bottom left hand corner
		self.width = 0
		self.height = 0
		
		# What level the room is being created on
		self.level = level
		
		self.__occupied_tiles = {}
	
	def set_dimensions(self, width, height):
		"""Sets the occupied tiles dictionary to contain the correct number of tiles"""
		self.width = width
		self.height = height
		for y in range(self.height):
			for x in range(self.width):
				self.__occupied_tiles[(x, y)] = None
	
	def set_walls(self):
		"""Puts a simple bordering wall around the room"""
		
		for x in range(self.width):
			if self.is_occupied == 0:
				self.set_occupied(x, 0, "Wall")
				self.set_occupied(x, self.height, "Wall")
	
		for y in range(self.height):
			if self.is_occupied == 0:
				self.set_occupied(0, y, "Wall")
				self.set_occupied(self.width, y, "Wall")

					
	def get_objects(self):
		pass
	
	def get_monsters(self):
		pass
	
	def is_occupied(self, x, y):
		"""Determines whether a tile is occupied or not"""
		for k, v in self.__occupied_tiles:
			if k == y:
				if v == x:
					if self.__occupied_tiles[(x, y)] == None:
						return 0
					else:
						return 1
	def set_occupied(self, x, y, tile):
		"""Sets a tile as occupied within a room"""
		for k, v in self.__occupied_tiles:
			if k == y:
				if v == x:
					if self.is_occupied(x, y) == 0:
						self.__occupied_tiles[(x, y)] = tile
						return 0
					else:
						return 1
		
		
class room_basic(base_room):
	"""Simple rectangular room of a small size"""
	
	def __init__(self, level):
		"""Makes the basic room object"""
		base_room.__init__(self, BASIC_ROOM, level)
		
		self.setdimensions(randint(6, 10), randint(6, 10))
		self.set_walls()
		
		
		
	def get_objects(self):
		"""Populates the room with objects"""
		for i in randint(0, 3):
			if len(self.level.items) < self.level.props.max_items:
				
				item = objects.get_random_item(self.level)
			
				# Need to replace this with a way of keeping track of 2D tile allocation
				# Also needs to be able to give up creating an object if the room is full
				item.x_pos = self.width / randint(1, self.width)
				item.y_pos = self.height / randint(1, self.width)
			
				self.objects.append(item)
	
	def get_monsters(self):
		"""Populates the room with monsters"""
		for i in randint(0, 1):
			monster = mobs.get_random_monster(self.level)
			
			# See get_objects for need to keep track of tiles
			
			self.monsters.append(monster)
	

class room_long(base_room):
	"""Large narrow room of random orientation"""
	pass

class room_hangar(base_room):
	"""Very large room, sparsely populated"""
	pass

class room_lab(base_room):
	"""Small room containing items of a scientific nature"""
	pass

class room_workshop(base_room):
	"""Small room containing items of an engineering nature"""
	pass

class base_corridor:
	"""Basic class for corridors"""
	pass

class corridor_corner(base_corridor):
	"""Corner of a corridor, to enable corridors to not have to end in rooms"""
	pass

class narrow_corridor(base_corridor):
	"""Narrow corridor, mostly to connect two small rooms"""
	pass

class large_corridor(base_corridor):
	"""Wider corridor, to connect larger rooms"""
	pass

class main_corridor(base_corridor):
	"""Very large corridor, more like a long room, less than three per level"""
	pass

class make_room:
	pass

class make_corridor:
	pass


