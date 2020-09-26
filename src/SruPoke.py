# A window is opened and two dots (a small red and a big blue dot) move in the window.
# The dots bounce off whenever they touch the edge of the window.
# The dots teleport to random positions on each mouse click.
# Scoreboard is displayed.
# GAME OVER is displayed once the dots collide.

from uagame import Window
from pygame import QUIT, Color, MOUSEBUTTONUP
from random import randint
from pygame.time import Clock, get_ticks
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle
from math import sqrt

def main():

	game=Game()
	game.play()

class Game:
	
	def __init__(self):

		self.window=Window('Poke the Dots', 500, 400)
		self.adjust_window()
		self.close_selected=False
		self.small_dot=Dot(self.window, 'red', [50,50], 30, [1,2])
		self.big_dot=Dot(self.window, 'blue', [200,100], 40, [2,1])
		self.frame_rate=90
		self.clock=Clock()
		self.small_dot.randomize()
		self.big_dot.randomize()
		self.score=0
		self.continue_game=True

	def adjust_window(self):

		self.window.set_bg_color('black')
		self.window.set_font_name('Times New Roman')
		self.window.set_font_size(50)
		self.window.set_font_color('white')

	def draw(self):

		self.window.clear()
		self.draw_score()
		self.small_dot.draw()
		self.big_dot.draw()
		if not self.continue_game:
			self.draw_game_over()
		self.window.update()

	def play(self):

		while not self.close_selected:
			self.handle_events()
			self.draw()
			self.update()
		self.window.close()


	def handle_events(self):

		event_list=get_events()
		for event in event_list:
			if event.type==QUIT:
				self.close_selected=True
			elif self.continue_game and event.type==MOUSEBUTTONUP:
				self.handle_mouse_click()

	def handle_mouse_click(self):

		self.small_dot.randomize()
		self.big_dot.randomize()

	def draw_score(self):

		string='Score: ' + str(self.score)
		self.window.draw_string(string, 0, 0)

	def update(self):

		if self.continue_game:
			self.small_dot.move()
			self.big_dot.move()
			self.clock.tick(self.frame_rate)
			self.score=get_ticks() // 1000 #milliseconds to seconds


		if self.small_dot.intersects(self.big_dot):
			self.continue_game=False

	def draw_game_over(self):

		string='GAME OVER'
		font_color=self.small_dot.get_color()
		bg_color=self.big_dot.get_color()
		original_font_color=self.window.get_font_color()
		original_bg_color=self.window.get_bg_color()

		self.window.set_font_color(font_color)
		self.window.set_bg_color(bg_color)
		height=self.window.get_height() - self.window.get_font_height()
		self.window.draw_string(string, 0, height)

		self.window.set_font_color(original_font_color)
		self.window.set_bg_color(original_bg_color)

class Dot:

	def __init__(self, window, color, center, radius, velocity):

		self.window=window
		self.color=color
		self.center=center
		self.radius=radius
		self.velocity=velocity

	def draw(self):

		surface=self.window.get_surface()
		color=Color(self.color)
		draw_circle(surface, color, self.center, self.radius)

	def move(self):

		size=[self.window.get_width(), self.window.get_height()]
		for index in range(0,2):
			self.center[index]=self.center[index]+self.velocity[index]
			if (self.center[index]+self.radius >= size[index]) or (self.center[index]-self.radius <= 0):
				self.velocity[index] = -self.velocity[index]

	def randomize(self):
		
		size=[self.window.get_width(), self.window.get_height()]
		for index in range(0,2):
			self.center[index]=randint(self.radius, size[index]-self.radius)

	def intersects(self, dot):

		distance = sqrt((self.center[0] - dot.center[0])**2 + (self.center[1] - dot.center[1])**2)
		return distance <= self.radius + dot.radius

	def get_color(self):

		return self.color

main()