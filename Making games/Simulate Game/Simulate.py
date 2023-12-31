import random, sys, time, pygame
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FLASHSPEED = 500
FLASHDELAY = 200
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHTRED = (255, 0, 0)
RED = (155, 0, 0)
BRIGHTGREEN = (0, 255, 0)
GREEN = (0, 155, 0)
BRIGHTBLUE = (0, 0, 255)
BLUE = (0, 0, 155)
BRIGHTYELLOW = (255, 255, 0)
YELLOW = (155, 155, 0)
DARKGRAY = (40, 40, 40)
bgColor = BLACK

XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) /2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)

YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)
REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, BEEP1, BEEP2, BEEP3, BEEP4

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('Simulate')
	BASICFONT = pygame.font.Font('freesansbold.ttf', 16)

	infoSurf = BASICFONT.render('Match the pattern by clicking on the buutton or using the Q, W, A, S keys.', True, DARKGRAY)
	infoRect = infoSurf.get_rect()
	infoRect.topleft = (10, WINDOWHEIGHT - 25)

	BEEP1 = pygame.mixer.Sound('beep1.ogg')
	BEEP2 = pygame.mixer.Sound('beep2.ogg')
	BEEP3 = pygame.mixer.Sound('beep3.ogg')
	BEEP4 = pygame.mixer.Sound('beep4.ogg')
	
	pattern = []
	currentStep = 0
	lastClickTime = 0
	score = 0
	waitingForInput = False

	checkForQuit()

	while True:
		clicked = None
		DISPLAYSURF.fill(bgColor)
		DISPLAYSURF.blit(infoSurf, infoRect)
		scoreSurf = BASICFONT.render("Score: " + str(score), True, WHITE)
		scoreRect = scoreSurf.get_rect()
		scoreRect.topleft = (WINDOWWIDTH - 100, 10)
		DISPLAYSURF.blit(scoreSurf, scoreRect)
		checkForQuit()
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_q:
					clicked = YELLOW			
				elif event.key == K_w:
					clicked = BLUE
				elif event.key == K_a:
					clicked = RED
				elif event.key == K_s:
					clicked = GREEN
			if event.type == MOUSEBUTTONUP:
				clicked = getButtonClick(*event.pos)

		drawButtons()

		if not waitingForInput:
			pygame.display.update()
			pygame.time.wait(1000)
			pattern.append(random.choice([YELLOW, RED, GREEN, BLUE]))
			for color in pattern:
				flashButtonAnimation(color)
				pygame.time.wait(FLASHDELAY)
			waitingForInput = True
		else:
			if clicked and clicked == pattern[currentStep]:
				flashButtonAnimation(clicked)
				# pygame.time.wait(500)
				currentStep += 1
				clicked = None
				lastClickTime = time.time()
				if currentStep == len(pattern):
					changeBackgroundAnimation()
					score += 1
					currentStep = 0
					waitingForInput = False
			elif (clicked and clicked != pattern[currentStep]) or (currentStep != 0 and time.time() - TIMEOUT > lastClickTime):
				gameOverAnimation()
				pygame.time.wait(2000)
				score = 0
				currentStep = 0
				waitingForInput = False
				pattern = []
				pygame.time.wait(1000)
				changeBackgroundAnimation()

		pygame.display.update()
		FPSCLOCK.tick(FPS)

def terminate():
	pygame.quit()
	sys.exit()

def checkForQuit():
	for event in pygame.event.get(QUIT):
		terminate()
	for event in pygame.event.get(KEYUP):
		if event.key == K_ESCAPE:
			terminate()
		pygame.event.post(event)

def flashButtonAnimation(color, animationSpeed=50):
	if color == YELLOW:
		sound = BEEP1
		flashColor = BRIGHTYELLOW
		rectangle = YELLOWRECT
	elif color == BLUE:
		sound = BEEP2
		flashColor = BRIGHTBLUE
		rectangle = BLUERECT
	elif color == RED:
		sound = BEEP3
		flashColor = BRIGHTRED
		rectangle = REDRECT
	elif color == GREEN:
		sound = BEEP4
		flashColor = BRIGHTGREEN
		rectangle = GREENRECT

	origSurf = DISPLAYSURF.copy()
	flashSurf = pygame.Surface((BUTTONSIZE, BUTTONSIZE))
	flashSurf = flashSurf.convert_alpha()
	r, g, b = flashColor
	sound.play()
	for start, end, step in ((0, 255, 1), (255, 0, -1)):
		for alpha in range(start, end, animationSpeed * step):
			checkForQuit()
			DISPLAYSURF.blit(origSurf, (0, 0))
			flashSurf.fill((r, g, b, alpha))
			DISPLAYSURF.blit(flashSurf, rectangle) #rectangle.topleft)
			pygame.display.update()
			FPSCLOCK.tick(FPS)
	DISPLAYSURF.blit(origSurf, (0, 0))		

def drawButtons():
	pygame.draw.rect(DISPLAYSURF, YELLOW, YELLOWRECT)
	pygame.draw.rect(DISPLAYSURF, BLUE, BLUERECT)
	pygame.draw.rect(DISPLAYSURF, RED, REDRECT)
	pygame.draw.rect(DISPLAYSURF, GREEN, GREENRECT)

def changeBackgroundAnimation(animationSpeed=40):	
	global bgColor
	newBgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

	newBgSurf = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))
	newBgSurf = newBgSurf.convert_alpha()
	r, g, b = newBgColor
	for alpha in range(0, 255, animationSpeed):
		checkForQuit()
		DISPLAYSURF.fill(bgColor)

		newBgSurf.fill((r, g, b, alpha))
		DISPLAYSURF.blit(newBgSurf, (0, 0))

		drawButtons()

		pygame.display.update()
		FPSCLOCK.tick(FPS)
	bgColor = newBgColor

def gameOverAnimation(color=WHITE, animationSpeed=50):
	origSurf = DISPLAYSURF.copy()
	flashSurf = pygame.Surface(DISPLAYSURF.get_size())
	flashSurf = flashSurf.convert_alpha()
	BEEP1.play()
	BEEP2.play()
	BEEP3.play()
	BEEP4.play()
	r, g, b = color
	for i in range(3):
		for start, end, step in ((0, 255, 1), (255, 0, -1)):
			for alpha in range(start, end, animationSpeed * step):
				checkForQuit()
				flashSurf.fill((r, g, b, alpha))
				DISPLAYSURF.blit(origSurf, (0, 0))
				DISPLAYSURF.blit(flashSurf, (0, 0))
				drawButtons()
				pygame.display.update()
				FPSCLOCK.tick(FPS)

def getButtonClick(x, y):
	if YELLOWRECT.collidepoint((x, y)):
		return YELLOW
	elif BLUERECT.collidepoint((x, y)):
		return BLUE
	elif REDRECT.collidepoint((x, y)):
		return RED
	elif GREENRECT.collidepoint((x, y)):
		return GREEN
	return None


if __name__ == '__main__':
	main()

