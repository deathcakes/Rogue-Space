from pyglet import window
from pyglet import clock
from pyglet import font
from random import *
from math import *


class MainWindow(window.Window):
	
	def __init__(self, *args, **kwargs):
		# Let all of the standard stuff pass through
		window.Window.__init__(self, fullscreen=1, *args, **kwargs)
		
	
	def main_loop(self):
		
		
		ft = font.load('Arial', 12)
		fps_text = font.Text(ft, y = 10)
		
		
		while not self.has_exit:
			self.dispatch_events()
			self.clear()
			
			clock.tick()
			
			fps_text.text = ("fps: %d") % (clock.get_fps())
			fps_text.draw()
			
			self.flip()
			
if __name__ == "__main__":
	go = MainWindow()
	go.main_loop()
