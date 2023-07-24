import sys
from pygame import *

def parabol(x):
	return (x - 100) ** 2 + 100

window = display.set_mode((500, 500))
clock = time.Clock()
window.fill((255, 255, 255))
run = True
x = 85
while run:
	for e in event.get():
		if e.type == QUIT:
			run = False
	# window.fill((255, 255, 255))
	draw.circle(window, (255, 0, 0), (x, parabol(x)), 1)
	print(x, parabol(x))
	x += 0.01

	display.update()
	clock.tick(120)

quit()
sys.exit()
