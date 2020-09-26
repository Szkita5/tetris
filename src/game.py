import random
import numpy as np
import pygame


minos_x = 10
minos_y = 20



# Array of all shapes, (x,y) positions of all 4 minos relative to top left corner for each rotation. 0 is spawn rotation, moving clockwise.
I = np.asarray([[(0,1),(1,1),(2,1),(3,1)],[(2,0),(2,1),(2,2),(2,3)],[(0,2),(1,2),(2,2),(3,2)],[(1,0),(1,1),(1,2),(1,3)]])
J = np.asarray([[(0,0),(0,1),(1,1),(2,1)],[(1,0),(2,0),(1,1),(1,2)],[(0,1),(1,1),(2,1),(2,2)],[(1,0),(1,1),(1,2),(0,2)]])
L = np.asarray([[(0,1),(1,1),(2,1),(2,0)],[(1,0),(1,1),(1,2),(2,2)],[(0,1),(0,2),(1,1),(2,1)],[(0,0),(1,0),(1,1),(1,2)]])
O = np.asarray([[(1,0),(2,0),(1,1),(2,1)],[(1,0),(2,0),(1,1),(2,1)],[(1,0),(2,0),(1,1),(2,1)],[(1,0),(2,0),(1,1),(2,1)]])
S = np.asarray([[(0,1),(1,1),(1,0),(2,0)],[(1,0),(1,1),(2,1),(2,2)],[(0,2),(1,2),(1,1),(2,1)],[(0,0),(0,1),(1,1),(1,2)]])
T = np.asarray([[(0,1),(1,1),(1,0),(2,1)],[(1,0),(1,1),(1,2),(2,1)],[(0,1),(1,1),(2,1),(1,2)],[(0,1),(1,0),(1,1),(1,2)]])
Z = np.asarray([[(0,0),(1,0),(1,1),(2,1)],[(1,1),(1,2),(2,0),(2,1)],[(0,1),(1,1),(1,2),(2,2)],[(0,1),(0,2),(1,0),(1,1)]])

shapes = [S, Z, I, O, J, L, T]
colors = [(255,255,255),(0,0,255),(255,165,0),(255,255,0),(0,255,0),(128,0,128),(255,0,0)]

class Board():
	def __init__(self):
		# Board is 22 mino tall and 10 mino wide. Only bottom 20 rows are visible
		# Board itself is a selection of coloured squares
		self.board = np.zeros((minos_x, minos_y + 2, 3), dtype = np.int)

	def is_valid(self, Piece):
		pass
		#1: check if piece out of bounds
		#2: check for piece collision




class Piece():
	def __init__(self, x, y, shape):
		self.x = x
		self.y = y
		self.shape = shape
		self.rotation = 0
		# positions of all 4 minos
		self.positions = [(self.x + self.shape[self.rotation,0,0], self.y + self.shape[self.rotation,0,1]),
						(self.x + self.shape[self.rotation,1,0], self.y + self.shape[self.rotation,1,1]),
						(self.x + self.shape[self.rotation,2,0], self.y + self.shape[self.rotation,2,1]),
						(self.x + self.shape[self.rotation,3,0], self.y + self.shape[self.rotation,3,1])]
		self.color = colors[shapes.index(self.shape)]




#pixel size of each block
block_size = 30

display_width = 600
display_height = 800

top_x = 20
top_y = 20


pygame.init()
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()

play_board = Board()

print(play_board.board.shape)

crashed = False

while not crashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	for i in range(play_board.board.shape[0]):
		for j in range(play_board.board.shape[1]):
			#pygame.draw.rect(display, play_board[i, j], ())
			pass


	# Draw grid lines
	for i in range(minos_x + 1):
		pygame.draw.line(display, (128,128,128), (top_x + i*block_size, top_y + 0), (top_x + i*block_size, top_y + minos_y*block_size), 1)

	for i in range(minos_y + 1):
		pygame.draw.line(display, (128,128,128), (top_x + 0, top_y + i*block_size), (top_x + minos_x*block_size ,top_y + i*block_size), 1)

	

	pygame.display.update()
	clock.tick(60)

pygame.quit()