import pygame, sys, math

def convert_point_3D_to_2D(x, y, z):
	if z == 0:
		return (x, y)
	else:
		x_convert = x + z * math.cos(math.pi / 4)
		y_convert = y - z * math.sin(math.pi / 4)
		return (x_convert, y_convert)

win = pygame.display.set_mode((500, 500))
win.fill(pygame.Color('white'))
clock = pygame.time.Clock()
front_cube = [convert_point_3D_to_2D(*point) for point in [(0, 0, 0), (100, 0, 0), (100, 100, 0), (0, 100, 0)]]
back_cube = [convert_point_3D_to_2D(*point) for point in [(0, 0, 100), (100, 0, 100), (100, 100, 100), (0, 100, 100)]]
line1 = [convert_point_3D_to_2D(100, 100, 0), convert_point_3D_to_2D(100, 100, 100)]
line2 = [convert_point_3D_to_2D(100, 200, 0), convert_point_3D_to_2D(100, 200, 100)]
line3 = [convert_point_3D_to_2D(200, 100, 0), convert_point_3D_to_2D(200, 100, 100)]
line4 = [convert_point_3D_to_2D(200, 200, 0), convert_point_3D_to_2D(200, 200, 100)]
while True:
	[sys.exit() for event in pygame.event.get(pygame.QUIT)]

	for i in range(len(front_cube) - 1):
		start = tuple(map(lambda x: x + 100, front_cube[i]))
		end = tuple(map(lambda x: x + 100, front_cube[i + 1]))
		pygame.draw.line(win, (0, 0, 255), start, end, 5)
	start = tuple(map(lambda x: x + 100, front_cube[3]))
	end = tuple(map(lambda x: x + 100, front_cube[0]))
	pygame.draw.line(win, (0, 0, 255), start, end, 5)

	for i in range(len(back_cube) - 1):
		start = tuple(map(lambda x: x + 100, back_cube[i]))
		end = tuple(map(lambda x: x + 100, back_cube[i + 1]))
		pygame.draw.line(win, (0, 0, 255), start, end, 5)
	start = tuple(map(lambda x: x + 100, back_cube[3]))
	end = tuple(map(lambda x: x + 100, back_cube[0]))
	pygame.draw.line(win, (0, 0, 255), start, end, 5)

	pygame.draw.line(win, (0, 0, 255), line1[0], line1[1], 5)
	pygame.draw.line(win, (0, 0, 255), line2[0], line2[1], 5)
	pygame.draw.line(win, (0, 0, 255), line3[0], line3[1], 5)
	pygame.draw.line(win, (0, 0, 255), line4[0], line4[1], 5)

	pygame.display.update()
	clock.tick(60)