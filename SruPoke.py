# A window is opened and two dots (a small red and a big blue dot) move in the window.
# The dots bounce off whenever they touch the edge of the window.

from uagame import Window
from pygame import QUIT, Color
from pygame.time import Clock
from pygame.event import get as get_events
from pygame.draw import circle as draw_circle

def main():

	window=create_window()
	clock=Clock()

	color=['blue','red']
	radius=[40,30]
	center=[[200,100],[50,50]]
	velocity=[[2,1],[1,2]]

	play_game(window, color, center, radius, velocity, clock)
	window.close()

def create_window():

	window=Window('Poke the Dots', 500, 400)
	window.set_bg_color('black')
	return window

def create_game():
	pass 

def create_dot():
	pass

def play_game(window, color, center, radius, velocity, clock):

	close_selected=False

	while not close_selected:
		close_selected=handle_events()
		draw_game(window, color, center, radius)
		update_game(window, center, radius, velocity, clock)

def handle_events():

	closed=False
	event_list=get_events()
	for event in event_list:
		if event.type==QUIT:
			closed=True

	return closed

def draw_game(window, color, center, radius):

	window.clear()
	draw_dot(window, color, center, radius)
	window.update()

def draw_dot(window, color_string, center, radius):

	for index in range(0,2):
		surface=window.get_surface()
		color=Color(color_string[index])
		draw_circle(surface, color, center[index], radius[index])

def update_game(window, center, radius, velocity, clock):

	frame_rate=90
	move_dot(window, center[0], radius[0], velocity[0])
	move_dot(window, center[1], radius[1], velocity[1])
	clock.tick(frame_rate)
	
def move_dot(window, center, radius, velocity):

	size=[window.get_width(), window.get_height()]
	for index in range(0,2):
		center[index]=center[index]+velocity[index]
		if center[index]+radius >= size[index] or center[index]-radius <= 0:
			velocity[index] = -velocity[index]

main()