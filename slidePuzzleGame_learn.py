import pygame, sys, random
from pygame.locals import *

BOARDWIDTH = 4 # số ô theo chiều ngang
BOARDHEIGHT = 4 # số ô theo chiều dọc
TILESIZE = 80 # kích thước 1 ô vuông
WINDOWWIDTH = 640 # chiều rộng cửa sổ tính = pixel
WINDOWHEIGHT = 480 # chiều cao cửa sổ tính bằng pixel
FPS = 30 # 30 khung hình trên giây
BORDERSIZE = 5
BLANK = None # vị trí không có ô số

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

# BUTTONCOLOR = WHITE
# BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('Slide Puzzle')
	BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

	RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 90)

	NEW_SURF, NEW_RECT = makeText('New Game', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 60)

	SOLVE_SURF, SOLVE_RECT = makeText('Solve', TEXTCOLOR, TILECOLOR, WINDOWWIDTH - 120, WINDOWHEIGHT - 30)

	mainBoard, solutionSeq = generateNewPuzzle(80)
	SOLVEDBOARD = getStartingBoard()
	getStartingBoard()
	allMoves = []

	while True:
		move = None
		message = 'Click tile or press arrow keys to slide.'
		if mainBoard == SOLVEDBOARD:
			message = 'Solved'
		drawBoard(mainBoard, message)		
		checkForQuit()
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				tileX, tileY = getSpotClicked(mainBoard, event.pos[0], event.pos[1])
				if (tileX, tileY) == (None, None):
					if RESET_RECT.collidepoint(event.pos):
						resetAnimation(mainBoard, allMoves)
						allMoves = []
					elif NEW_RECT.collidepoint(event.pos):
						mainBoard, solutionSeq = generateNewPuzzle(80)
						allMoves = []
					elif SOLVE_RECT.collidepoint(event.pos):
						resetAnimation(mainBoard, solutionSeq + allMoves)
						solutionSeq = []
						allMoves = []
				else:
					blankx, blanky = getBlankPosition(mainBoard)
					if (tileX, tileY) == (blankx, blanky + 1):
						move = UP
					if (tileX, tileY) == (blankx, blanky - 1):
						move = DOWN
					if (tileX, tileY) == (blankx + 1, blanky):
						move = LEFT
					if (tileX, tileY) == (blankx - 1, blanky):
						move = RIGHT
					
			elif event.type == KEYUP:
				if event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
					move = UP
				if event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
					move = DOWN
				if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
					move = LEFT
				if event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
					move = RIGHT

		if move:
			slideAnimation(mainBoard, move, 'Sliding...', 8)
			makeMove(mainBoard, move)
			allMoves.append(move)

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

def getStartingBoard():
	counter = 1
	board = []
	for x in range(BOARDWIDTH):
		column = []
		for y in range(BOARDHEIGHT):
			column.append(counter)
			counter += BOARDWIDTH
		board.append(column)
		counter -= BOARDWIDTH * BOARDHEIGHT - 1
	board[BOARDWIDTH - 1][BOARDHEIGHT - 1] = None
	# print(board)
	return board

def makeText(text, color, bgcolor, top, left):
	textSurf = BASICFONT.render(text, True, color, bgcolor)
	textRect = textSurf.get_rect()
	textRect.topleft = (top, left)
	return (textSurf, textRect)

def getLeftTopOfTile(tileX, tileY):
	left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
	top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
	return (left, top)

def drawTile(tilex, tiley, number, adjx=0, adjy=0):
	left, top = getLeftTopOfTile(tilex, tiley)
	pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))
	textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
	textRect = textSurf.get_rect()
	textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) +adjy
	DISPLAYSURF.blit(textSurf, textRect) 

def drawBoard(board, message):
	"""
	vẽ message, bảng và 3 nút reset, new game, solve
	"""
	DISPLAYSURF.fill(BGCOLOR)

	if message:
		textSurf, textRect = makeText(message, MESSAGECOLOR, BGCOLOR, 5, 5)
		DISPLAYSURF.blit(textSurf, textRect)

	for tilex in range(BOARDWIDTH):
		for tiley in range(BOARDHEIGHT):
			if board[tilex][tiley]:
				drawTile(tilex, tiley, board[tilex][tiley])

	left, top = getLeftTopOfTile(0, 0)
	width = BOARDWIDTH * TILESIZE + BOARDWIDTH - 1
	height = BOARDHEIGHT * TILESIZE + BOARDHEIGHT - 1
	pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - BORDERSIZE - 1, top - BORDERSIZE - 1, width + (BORDERSIZE + 1) * 2, height + (BORDERSIZE + 1) * 2), 5)

	DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
	DISPLAYSURF.blit(NEW_SURF, NEW_RECT)
	DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)

def getBlankPosition(board):
	"""
	lấy ra vị trí ô trống
	"""
	for x in range(BOARDWIDTH):
		for y in range(BOARDHEIGHT):
			if board[x][y] == None:
				return (x, y)

def makeMove(board, move):
	blankx, blanky = getBlankPosition(board)
	if move == UP:
		board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
	if move == DOWN:
		board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
	if move == LEFT:
		board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
	if move == RIGHT:
		board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]

def isValidMove(board, move):
	""" kiểm tra có di chuyển được theo hướng move không """
	blankx, blanky = getBlankPosition(board)
	return (move == UP and blanky != len(board[0]) - 1) or \
		   (move == DOWN and blanky != 0) or \
	       (move == LEFT and blankx != len(board) - 1) or \
	       (move == RIGHT and blankx != 0)

def getRandomMove(board, lastMove=None):
	validMoves = [UP, DOWN, LEFT, RIGHT]

	if lastMove == UP or not isValidMove(board, DOWN):
		validMoves.remove(DOWN)
	if lastMove == DOWN or not isValidMove(board, UP):
		validMoves.remove(UP)
	if lastMove == LEFT or not isValidMove(board, RIGHT):
		validMoves.remove(RIGHT)
	if lastMove == RIGHT or not isValidMove(board, LEFT):
		validMoves.remove(LEFT)

	return random.choice(validMoves)

def slideAnimation(board, move, message, animationSpeed):
	blankx, blanky = getBlankPosition(board)
	if move == UP:
		x = blankx
		y = blanky + 1
	elif move == DOWN:
		x = blankx
		y = blanky - 1
	elif move == LEFT:
		x = blankx + 1
		y = blanky
	elif move == RIGHT:
		x = blankx - 1
		y = blanky

	drawBoard(board, message)
	baseSurf = DISPLAYSURF.copy()
	left, top = getLeftTopOfTile(x, y)
	pygame.draw.rect(baseSurf, BGCOLOR, (left, top, TILESIZE, TILESIZE))

	for i in range(0, TILESIZE, animationSpeed):
		DISPLAYSURF.blit(baseSurf, (0, 0))
		if move == UP:
			drawTile(x, y, board[x][y], 0, -i)
		elif move == DOWN:
			drawTile(x, y, board[x][y], 0, i)
		elif move == LEFT:
			drawTile(x, y, board[x][y], -i, 0)
		elif move == RIGHT:
			drawTile(x, y, board[x][y], i, 0)

		pygame.display.update()
		FPSCLOCK.tick(FPS)

def generateNewPuzzle(numSlides):
	sequence = []
	board = getStartingBoard()
	drawBoard(board, '')
	pygame.display.update()
	pygame.time.wait(500)
	lastMove = None
	for i in range(numSlides):
		lastMove = getRandomMove(board, lastMove)
		slideAnimation(board, lastMove, 'Generating new puzzle...', int(TILESIZE / 3))
		makeMove(board, lastMove)
		sequence.append(lastMove)
	# print(board)
	# print(sequence)
	return (board, sequence)

def getSpotClicked(board, mousex, mousey):
	for tileX in range(BOARDWIDTH):
		for tileY in range(BOARDHEIGHT):
			left, top = getLeftTopOfTile(tileX, tileY)
			rect = pygame.Rect(left, top, TILESIZE, TILESIZE)
			if rect.collidepoint(mousex, mousey):
				return (tileX, tileY)
	return (None, None)

def resetAnimation(board, allMoves):
	allMoves.reverse()
	for move in allMoves:
		if move == UP:
			oppositeMove = DOWN
		elif move == DOWN:
			oppositeMove = UP
		elif move == LEFT:
			oppositeMove = RIGHT
		elif move == RIGHT:
			oppositeMove = LEFT
		slideAnimation(board, oppositeMove, '', int(TILESIZE / 2))
		makeMove(board, oppositeMove)		

if __name__ == '__main__':
	main()