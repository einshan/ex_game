from sys import exit
from random import randint
class Scene(object):
	
	def enter(self):
		print "Welcome to adventure games."
		exit(1)
		
class Engine(object):
	
	def __init__(self,scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current.scene = self.scene_map.opening_scene()
		
		while True:
			print "\n--------------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene()
		
class Death(Scene):
	
	quips = [
	"You died .You kinda suck at this.",
	"You mom would be proud...if she were smarter.",
	"Such a luser.",
	"I have a small puppy that's better at this."
	]
	
	
	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]
		
		exit(1)

class Central_Corridor(Scene):
	
	def enter(self):
		pass
		
class Laster_Weapon_Armory(Scene):

	def enter(self):
		pass
		
class The_Bridge(Scene):

	def enter(self):
		pass
		
class Escape_Pod(Scene):

	def enter(self):
		pass

class Map(Scene):

	def __init__(self,start_scene):
		pass 
		
	def next_scene(self,scene_name):
		pass
		
	def opening_scene(self):
		pass
		
a_map = Map('Central_Corridor')
a_game = Engine(a_map)
a_game.play()
