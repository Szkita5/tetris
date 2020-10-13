import random
import numpy as np
import pygame


minos_x = 10
minos_y = 20



# Array of all shapes, (x,y) positions of all 4 minos relative to top left corner for each rotation. 0 is spawn rotation, moving clockwise.
I = np.asarray([[(0,2),(1,2),(2,2),(3,2)],[(2,0),(2,1),(2,2),(2,3)],[(0,1),(1,1),(2,1),(3,1)],[(1,0),(1,1),(1,2),(1,3)]])
J = np.asarray([[(0,2),(0,1),(1,1),(2,1)],[(1,2),(2,2),(1,1),(1,0)],[(0,1),(1,1),(2,1),(2,0)],[(1,2),(1,1),(1,0),(0,0)]])
L = np.asarray([[(0,1),(1,1),(2,1),(2,2)],[(1,2),(1,1),(1,0),(2,0)],[(0,1),(0,0),(1,1),(2,1)],[(0,2),(1,2),(1,1),(1,0)]])
O = np.asarray([[(1,2),(2,2),(1,1),(2,1)],[(1,2),(2,2),(1,1),(2,1)],[(1,2),(2,2),(1,1),(2,1)],[(1,2),(2,2),(1,1),(2,1)]])
S = np.asarray([[(0,1),(1,1),(1,2),(2,2)],[(1,2),(1,1),(2,1),(2,0)],[(0,0),(1,0),(1,1),(2,1)],[(0,2),(0,1),(1,1),(1,0)]])
T = np.asarray([[(0,1),(1,1),(1,2),(2,1)],[(1,2),(1,1),(1,0),(2,1)],[(0,1),(1,1),(2,1),(1,0)],[(0,1),(1,2),(1,1),(1,0)]])
Z = np.asarray([[(0,2),(1,2),(1,1),(2,1)],[(1,1),(1,0),(2,2),(2,1)],[(0,1),(1,1),(1,0),(2,0)],[(0,1),(0,0),(1,2),(1,1)]])

shapes = np.asarray([I, J, L, O, S, T, Z])
colors = np.asarray([(255,255,255),(0,0,255),(255,165,0),(255,255,0),(0,255,0),(128,0,128),(255,0,0)])

class Board():
	def __init__(self):
		# Board is 22 mino tall and 10 mino wide. Only bottom 20 rows are visible
		# Board itself is a selection of coloured squares
		self.board = np.zeros((minos_x, minos_y + 2, 3), dtype = np.int)
		

	def is_valid(self, check_piece):
		valid = True

		for i in range(4):
			# Get position of each mino
			x, y = check_piece.positions[i]

			# Check for out of bounds
			if x < 0 or x >= minos_x:
				valid = False
				continue

			if y < 0 or y >= minos_y:
				valid = False
				continue

			# Check for collison
			if self.board[x, y].any() != 0:
				valid = False
				continue

		
		return valid



class Piece():
	def __init__(self, x, y, seed):
		self.x = x
		self.y = y
		self.seed = seed
		self.shape = shapes[seed]
		self.color = colors[seed]
		self.rotation = 0
		self.stuck_counter = 0
		# positions of all 4 minos
		self.positions = np.asarray([(self.x + self.shape[self.rotation,0,0], self.y + self.shape[self.rotation,0,1]),
						(self.x + self.shape[self.rotation,1,0], self.y + self.shape[self.rotation,1,1]),
						(self.x + self.shape[self.rotation,2,0], self.y + self.shape[self.rotation,2,1]),
						(self.x + self.shape[self.rotation,3,0], self.y + self.shape[self.rotation,3,1])])

	def update_positions(self):
		self.positions = np.asarray([(self.x + self.shape[self.rotation,0,0], self.y + self.shape[self.rotation,0,1]),
						(self.x + self.shape[self.rotation,1,0], self.y + self.shape[self.rotation,1,1]),
						(self.x + self.shape[self.rotation,2,0], self.y + self.shape[self.rotation,2,1]),
						(self.x + self.shape[self.rotation,3,0], self.y + self.shape[self.rotation,3,1])])
	
	def move_left(self):
		self.x -= 1
		self.update_positions()
		if play_board.is_valid(self):
			self.stuck_counter = 0
			return 0
		else: 
			self.x += 1
			self.update_positions()
			return 1

	def move_right(self):		
		self.x += 1
		self.update_positions()
		if play_board.is_valid(self):
			self.stuck_counter = 0
			return 0
		else: 
			self.x -= 1
			self.update_positions()
			return 1

	def move_down(self):
		self.y -= 1
		self.update_positions()
		if play_board.is_valid(self):
			self.stuck_counter = 0
			return 0
		else:
			self.y += 1
			self.update_positions()
			self.stuck_counter += 1
			return 1

	def move_up(self):
		self.y += 1
		self.update_positions()
		if play_board.is_valid(self):
			self.stuck_counter = 0
			return 0
		else:
			self.y -= 1
			self.update_positions()
			return 1
			

	def drop(self):
		while (self.move_down() == 0):
			pass

	def rotate(self):
		pass


# Create a Bag class that holds the seeds, and returns a piece from the bag
class Bag():

	def __init__(self, bags_number):
		self.bags_number = bags_number
		self.refill_bags()
		
		self.next_piece = self.get_new_piece()

	def refill_bags(self):
		self.bags = []
		for i in range(self.bags_number):
			self.bags.append([0,1,2,3,4,5,6])

		print(self.bags)

	def get_new_piece(self):
		# Find random seed form the bags
		bag = random.randint(0, self.bags_number-1)

		# Cannot chose from empty array
		success = False
		tries = 0
		while (not success):
			tries = tries + 1
			try:
				seed = random.choice(self.bags[bag])
				success = True
			except IndexError:
				bag = (bag+1) % 3
				if (tries == 3):
					self.refill_bags()
		
		# Remove seed from bags
		self.bags[bag].remove(seed)
		print(self.bags)

		
		if seed == 0:
			return Piece(3, 17, seed)	#ToDo: Need to set y to 18
		else:
			return Piece(3, 18, seed)	#ToDo: Need to set y to 19

	def peek_next_piece(self):
		return self.next_piece

	def get_next_piece(self):
		out = self.next_piece
		self.next_piece = self.get_new_piece()
		return out


#pixel size of each block
block_size = 30
display_width = 600
display_height = 800
top_x = 20
top_y = 60
next_x = top_x + 11 * block_size
next_y = top_y + 2 * block_size

def draw_board():
	# Draw the board minos
	for i in range(play_board.board.shape[0]):
		for j in range(play_board.board.shape[1]):
			pygame.draw.rect(display, play_board.board[i, j], ((top_x + i*block_size, top_y + (minos_y-1)*block_size - (j*block_size)),(block_size,block_size)))

	# Draw the active piece minos
	for i in range(4):
		pygame.draw.rect(display, active_piece.color, ((top_x + active_piece.positions[i,0] * block_size, top_y + (minos_y-1)*block_size - (active_piece.positions[i,1]*block_size)),(block_size, block_size)))

	# Draw next piece
	for i in range(4):
		pygame.draw.rect(display, next_piece.color, ((next_x + next_piece.positions[i,0] * block_size, next_y + (minos_y-1)*block_size - (next_piece.positions[i,1]*block_size)),(block_size, block_size)))

	# Draw grid lines
	for i in range(minos_x + 1):
		pygame.draw.line(display, (128,128,128), (top_x + i*block_size, top_y + 0), (top_x + i*block_size, top_y + minos_y*block_size), 1)

	for i in range(minos_y + 1):
		pygame.draw.line(display, (128,128,128), (top_x + 0, top_y + i*block_size), (top_x + minos_x*block_size ,top_y + i*block_size), 1)

	pygame.display.flip()



######################################################################################################################
pygame.init()

display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()



#####################################################################################################################

piece_bags = Bag(3)
play_board = Board()
active_piece = piece_bags.get_new_piece()
next_piece = piece_bags.peek_next_piece()


play_board.is_valid(active_piece)



fall_time = 0
fall_speed = 1.0

run = True

while run:

	fall_time += clock.get_rawtime()

	if fall_time/100 >= fall_speed:
		fall_time = 0
		active_piece.move_down()

		# If piece is stuck for 3 consecutive ticks without movement, it gets added to the board and a new piece is generated
		if active_piece.stuck_counter == 2:
			for i in range(4):
				play_board.board[active_piece.positions[i,0], active_piece.positions[i,1]] = active_piece.color

			active_piece = piece_bags.get_new_piece()
			next_piece = piece_bags.peek_next_piece()



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				active_piece.move_left()
				draw_board()
			if event.key == pygame.K_RIGHT:
				active_piece.move_right()
				draw_board()
			if event.key == pygame.K_DOWN:
				active_piece.move_down()
				draw_board()
			if event.key == pygame.K_SPACE:
				active_piece.drop()
				draw_board()

	
	draw_board()

	

	pygame.display.update()
	clock.tick(60)

pygame.quit()