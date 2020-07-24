# A window is opened and two dots (a small red and a big blue dot) move in the window.
# The dots bounce off whenever they touch the edge of the window.

from uagame import Window
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

def main():

	window=create_window()
	game=create_game(window)

	play_game(game)
	window.close()

def create_window():

	window=Window('Poke the Dots', 500, 400)
	window.set_bg_color('black')
	return window

def create_game(window):

	game=Game()
	game.window=window
	game.close_selected=False
	game.small_dot=create_dot(window, 'red', [50,50], 30, [1,2])
	game.big_dot=create_dot(window, 'blue', [200,100], 40, [2,1])
	game.frame_rate=90
	game.clock=Clock()

	return game

def create_dot(window, color, center, radius, velocity):

	dot=Dot()
	dot.window=window
	dot.color=color
	dot.center=center
	dot.radius=radius
	dot.velocity=velocity

	return dot

def play_game(game):

	while not game.close_selected:
		handle_events(game)
		draw_game(game)
		update_game(game)

def handle_events(game):

	event_list=get_events()
	for event in event_list:
		if event.type==QUIT:
			game.close_selected=True

def draw_game(game):

	game.window.clear()
	draw_dot(game.small_dot)
	draw_dot(game.big_dot)
	game.window.update()

def draw_dot(dot):
	
	surface=dot.window.get_surface()
	color=Color(dot.color)
	draw_circle(surface, color, dot.center, dot.radius)

def update_game(game):

	move_dot(game.small_dot)
	move_dot(game.big_dot)
	game.clock.tick(game.frame_rate)
	
def move_dot(dot):

	size=[dot.window.get_width(), dot.window.get_height()]
	for index in range(0,2):
		dot.center[index]=dot.center[index]+dot.velocity[index]
		if (dot.center[index]+dot.radius >= size[index]) or (dot.center[index]-dot.radius <= 0):
			dot.velocity[index] = -dot.velocity[index]

class Game:
	pass

class Dot:
	pass

main()