import readGame

#######################################################
# These are some Helper functions which you have to use 
# and edit.
# Must try to find out usage of them, they can reduce
# your work by great deal.
#
# Functions to change:
# 1. is_corner(self, pos):
# 2. is_validMove(self, oldPos, direction):
# 3. getNextPosition(self, oldPos, direction):
# 4. getNiextState(self, oldPos, direction):
##########i#############################################
class game:
	def __init__(self, filePath):
        	self.gameState = readGame.readGameState(filePath)
                self.nodesExpanded = 0
		self.trace = []
	
	def is_corner(self, pos):
		########################################
		# You have to make changes from here
		# check for if the new positon is a corner or not
		# return true if the position is a corner

		#check if the peg has gone beyond the board limits
		if pos[0] < 0 or pos[0] > 6 or pos[1] < 0 or pos[1] > 6:
			return True

		#check if the peg has gone into the walls
		if self.gameState[pos[0]][pos[1]] == -1:
			return True
		else:
			return False	
	
	
	def getNextPosition(self, oldPos, direction):
		#########################################
		# YOU HAVE TO MAKE CHANGES HERE
		# See DIRECTION dictionary in config.py and add
		# this to oldPos to get new position of the peg if moved
		# in given direction , you can remove next line

		#Just add direction to old position. It is multiplied by scalar i.e 2 as the direction is in 1 unit
		x = oldPos[0] + 2*direction[0]
		y = oldPos[1] + 2*direction[1]
		newPos = (x,y)
		return newPos
	
	
	def is_validMove(self, oldPos, direction):
		#########################################
		# DONT change Things in here
		# In this we have got the next peg position and
		# below lines check for if the new move is a corner

		#Check if the move has gone beyond the board limits ot hit the walls
		newPos = self.getNextPosition(oldPos, direction)
		if self.is_corner(newPos):
			return False	
		#########################################
		
		########################################
		# YOU HAVE TO MAKE CHANGES BELOW THIS
		# check for cases like:
		# if new move is already occupied

		#The new position of the peg should be empty. This check ensures the same
		if self.gameState[newPos[0]][newPos[1]] == 1:
			return False

		#Check for presence of intermediate peg i.e the peg between old position and new position
                if oldPos[0] == newPos[0]:
                        if oldPos[1] > newPos[1]: #move to west
                                if self.gameState[oldPos[0]][newPos[1]+1] == 0:
					return False
                        else: # move to east
                                if self.gameState[oldPos[0]][newPos[1]-1] == 0:
					return False
                elif oldPos[1] == newPos[1]:
                        if oldPos[0] > newPos[0]: #move north
                                if self.gameState[newPos[0]+1][newPos[1]] == 0:
					return False
                        else: #move south
                                if self.gameState[newPos[0]-1][newPos[1]] == 0:
					return False
                else:
                        print "Error !!!Invalid move"
                        exit(1)

		# or new move is outside peg Board
		# Remove next line according to your convenience
		return True
	
	def getNextState(self, oldPos, direction):
		###############################################
		# DONT Change Things in here
		self.nodesExpanded += 1
		if not self.is_validMove(oldPos, direction):
			print "Error, You are not checking for valid move"
			exit(0)
		###############################################
		
		###############################################
		# YOU HAVE TO MAKE CHANGES BELOW THIS
		# Update the gameState after moving peg
		# eg: remove crossed over pegs by replacing it's
		# position in gameState by 0
		# and updating new peg position as 1

		#Remove the intermediate peg by marking it to zero
	 	newPos = self.getNextPosition(oldPos, direction)
		if oldPos[0] == newPos[0]:
			if oldPos[1] > newPos[1]:
				self.gameState[oldPos[0]][newPos[1]+1] = 0
			else:
				self.gameState[oldPos[0]][newPos[1]-1] = 0	
		elif oldPos[1] == newPos[1]:
			if oldPos[0] > newPos[0]:
				self.gameState[newPos[0]+1][newPos[1]] = 0
			else:
				self.gameState[newPos[0]-1][newPos[1]] = 0
		else:
			print "Error !!!Invalid move"
			exit(1)

		#Remove peg from old position
		self.gameState[oldPos[0]][oldPos[1]] = 0;

		#Put a peg in new position
		self.gameState[newPos[0]][newPos[1]] = 1;
		return self.gameState	

