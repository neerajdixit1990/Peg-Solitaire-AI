import pegSolitaireUtils
import copy
import readGame
import Queue
from config import DIRECTION


#This is the recursive function used for exploring the search trees for Iterative Deepening Search
def recursive_dls(game_obj, pos, curr_depth, limit_depth, count):

	result = False
	#Check for goal state
	if count == 1:
		if pos[0]%2 == 1 and pos[1]%2 == 1:
			return True
		else:
			return False

	#if the depth of recursion goes beyond limit we return False
	if curr_depth > limit_depth:
		return False

	for i in range(7):
		for j in range(7):
			if (game_obj.gameState[i][j] == 1):
				if game_obj.is_validMove((i,j), DIRECTION['N']):
					#If this is valid move, make a copy of the gameState so that we can restore
					#the gameState in case of a failure
					dup_array = copy.deepcopy(game_obj.gameState)
					newPos = game_obj.getNextPosition((i,j), DIRECTION['N'])
					#update the game state with the new move
					game_obj.gameState = game_obj.getNextState((i,j), DIRECTION['N'])
					result = recursive_dls(game_obj, newPos, curr_depth + 1, limit_depth, count - 1)
					
					if result == True:
						#Trace the path if we succeed !!!
						game_obj.trace.insert(0,newPos)
						game_obj.trace.insert(0,(i,j))
						return True
					else:
						#restore game State
						game_obj.gameState = dup_array 

        			if game_obj.is_validMove((i,j), DIRECTION['S']):
					dup_array = copy.deepcopy(game_obj.gameState)
                			newPos = game_obj.getNextPosition((i,j), DIRECTION['S'])
                			game_obj.gameState = game_obj.getNextState((i,j), DIRECTION['S'])
                                        result = recursive_dls(game_obj, newPos, curr_depth + 1, limit_depth, count - 1)
                			
					if result == True:
                                                game_obj.trace.insert(0,newPos)
						game_obj.trace.insert(0,(i,j))
						return True
					else:
						game_obj.gameState = dup_array 

        			if game_obj.is_validMove((i,j), DIRECTION['E']):
					dup_array = copy.deepcopy(game_obj.gameState)
                			newPos = game_obj.getNextPosition((i,j), DIRECTION['E'])
                			game_obj.gameState = game_obj.getNextState((i,j), DIRECTION['E'])
                                        result = recursive_dls(game_obj, newPos, curr_depth + 1, limit_depth, count - 1)

                			if result == True:
                                                game_obj.trace.insert(0,newPos)
                                                game_obj.trace.insert(0,(i,j))
						return True
					else:
						game_obj.gameState = dup_array

				if game_obj.is_validMove((i,j), DIRECTION['W']):
					dup_array = copy.deepcopy(game_obj.gameState)
                			newPos = game_obj.getNextPosition((i,j), DIRECTION['W'])
                			game_obj.gameState = game_obj.getNextState((i,j), DIRECTION['W'])
                                        result = recursive_dls(game_obj, newPos, curr_depth + 1, limit_depth, count - 1)

                			if result == True:
                                                game_obj.trace.insert(0,newPos)
                                                game_obj.trace.insert(0,(i,j))
						return True
					else:
						game_obj.gameState = dup_array

	return False
	
	
def ItrDeepSearch(pegSolitaireObject):
	#################################################
	# Must use functions:
	# getNextState(self,oldPos, direction)
	# 
	# we are using this function to count,
	# number of nodes expanded, If you'll not
	# use this grading will automatically turned to 0
	#################################################
	#
	# using other utility functions from pegSolitaireUtility.py
	# is not necessary but they can reduce your work if you 
	# use them.
	# In this function you'll start from initial gameState
	# and will keep searching and expanding tree until you 
	# reach goal using Iterative Deepning Search.
	# you must save the trace of the execution in pegSolitaireObject.trace
	# SEE example in the PDF to see what to save
	#
	#################################################
	depth = 1;
	#The max number of pegs on the given board is 33. So max depth can be 33
	while depth <= 33:
		count = readGame.count_pegs(pegSolitaireObject)
		result = recursive_dls(pegSolitaireObject, (0,0), 0, depth, count)
		if result == True:
			break
		#increment depth every time we fail
		depth = depth + 1
	return result


#In the given pegSolitaire game, the pegs present on odd locations (x-axis & y-axis is odd number)
#can reach the goal state

#The peg present at (2,2) or (2,3) or (3,2) can never reach the goal state of (3,3)
#So we penalize these pegs with DOUBLE (multiply by scalar 2) the manhattan distance
#By doing this we ensure that these search trees will explored only when there is no
#path found from the pegs more probable to reach the goal State

#This will surely trim out some of the un-necessary search trees

def heuristic_two(x,y):
	heuristic = 0;
	if x%2 == 1:
		heuristic = heuristic + abs(3-x)
	else:
		heuristic = heuristic + 2*abs(3-x)

	if y%2 == 1:
		heuristic = heuristic + abs(3-x)
	else:
		heuristic = heuristic + 2*abs(3-y)
	return heuristic



#This is a naive Manhattan Distance heuristic
#This is sum of paths from the goal state (3,3)
def heuristic_one(x,y):
	heuristic = abs(3-x) + abs(3-y)
	return heuristic
 
def aStarOne(game_obj):
	#################################################
        # Must use functions:
        # getNextState(self,oldPos, direction)
        # 
        # we are using this function to count,
        # number of nodes expanded, If you'll not
        # use this grading will automatically turned to 0
        #################################################
        #
        # using other utility functions from pegSolitaireUtility.py
        # is not necessary but they can reduce your work if you 
        # use them.
        # In this function you'll start from initial gameState
        # and will keep searching and expanding tree until you 
	# reach goal using A-Star searching with first Heuristic
	# you used.
        # you must save the trace of the execution in pegSolitaireObject.trace
        # SEE example in the PDF to see what to return
        #
        #################################################
	count_pegs = readGame.count_pegs(game_obj)

	#Initialize the priority Queue
	#The least cost node would be expanded first
        q = Queue.PriorityQueue()
	found_sol = False

	#Put all the current gamestates in the queue
        for i in range(7):
                for j in range(7):
                        if game_obj.gameState[i][j] == 1:
				obj_copy = copy.deepcopy(game_obj)
                                q.put((heuristic_one(i,j),obj_copy,count_pegs,i,j))

	#Repeat until q is not empty
        while not q.empty():
		#Extract the current game state parameters from the queue
                item = q.get()
		curr_count = item[2]
		curr_obj = item[1]
		game_obj.nodesExpanded += 1
		curr_cost = item[0]

		#Check for goal state
                if (item[3],item[4]) == (3,3) and curr_count == 1:
			found_sol = True
			game_obj.trace = curr_obj.trace
                        break

        	for i in range(7):
                	for j in range(7):
				if curr_obj.gameState[i][j] == 1:
                			if curr_obj.is_validMove((i,j), DIRECTION['N']):
						#If the move is valid, we save a copy of the object and all
						#its parameters as we are exploring the search trees in parallel
						newPos = curr_obj.getNextPosition((i,j), DIRECTION['N'])
						new_obj = copy.deepcopy(curr_obj)

						#copy game state
						new_obj.gameState = copy.deepcopy(curr_obj.gameState)
						new_obj.gameState = new_obj.getNextState((i,j), DIRECTION['N'])
		
						#copy trace
						new_obj.trace = copy.deepcopy(curr_obj.trace)
						new_obj.trace.append((i,j))
						new_obj.trace.append(newPos)
		
						#Put it back in the queue with modified cost and heuristic
						q.put((curr_cost + 2 + heuristic_one(newPos[0], newPos[1]), new_obj, curr_count - 1, newPos[0], newPos[1]))

					if curr_obj.is_validMove((i,j), DIRECTION['S']):
                        			newPos = curr_obj.getNextPosition((i,j), DIRECTION['S'])
                        			new_obj = copy.deepcopy(curr_obj)
                                                new_obj.gameState = copy.deepcopy(curr_obj.gameState)
                        			new_obj.gameState = new_obj.getNextState((i,j), DIRECTION['S'])
                                        	new_obj.trace = copy.deepcopy(curr_obj.trace)
                                        	new_obj.trace.append((i,j))
                                        	new_obj.trace.append(newPos)
                        			q.put((curr_cost + 2 + heuristic_one(newPos[0], newPos[1]), new_obj, curr_count - 1, newPos[0], newPos[1]))

					if curr_obj.is_validMove((i,j), DIRECTION['E']):
                        			newPos = curr_obj.getNextPosition((i,j), DIRECTION['E'])
                        			new_obj = copy.deepcopy(curr_obj)
                                                new_obj.gameState = copy.deepcopy(curr_obj.gameState)
                        			new_obj.gameState = new_obj.getNextState((i,j), DIRECTION['E'])
                                        	new_obj.trace = copy.deepcopy(curr_obj.trace)
                                        	new_obj.trace.append((i,j))
                                        	new_obj.trace.append(newPos)
                        			q.put((curr_cost + 2 + heuristic_one(newPos[0], newPos[1]), new_obj, curr_count - 1, newPos[0], newPos[1]))
	
					if curr_obj.is_validMove((i,j), DIRECTION['W']):	
						newPos = curr_obj.getNextPosition((i,j), DIRECTION['W'])
                        			new_obj = copy.deepcopy(curr_obj)
                                                new_obj.gameState = copy.deepcopy(curr_obj.gameState)
                        			new_obj.gameState = new_obj.getNextState((i,j), DIRECTION['W'])
                        			new_obj.trace = copy.deepcopy(curr_obj.trace)
                                        	new_obj.trace.append((i,j))
                                        	new_obj.trace.append(newPos)
						q.put((curr_cost + 2 + heuristic_one(newPos[0], newPos[1]), new_obj, curr_count - 1, newPos[0], newPos[1]))
	
	return found_sol


def aStarTwo(game_obj):
	#################################################
        # Must use functions:
        # getNextState(self,oldPos, direction)
        # 
        # we are using this function to count,
        # number of nodes expanded, If you'll not
        # use this grading will automatically turned to 0
        #################################################
        #
        # using other utility functions from pegSolitaireUtility.py
        # is not necessary but they can reduce your work if you 
        # use them.
        # In this function you'll start from initial gameState
        # and will keep searching and expanding tree until you 
        # reach goal using A-Star searching with second Heuristic
        # you used.
        # you must save the trace of the execution in pegSolitaireObject.trace
        # SEE example in the PDF to see what to return
        #
        #################################################


	#This funtion is exactly same as previous function except for the
	#change in heuristic function

        count_pegs = readGame.count_pegs(game_obj)

        q = Queue.PriorityQueue()
        found_sol = False

        for i in range(7):
                for j in range(7):
                        if game_obj.gameState[i][j] == 1:
                                obj_copy = copy.deepcopy(game_obj)
                                q.put((heuristic_two(i,j),obj_copy,count_pegs,i,j))

        while not q.empty():
                item = q.get()
                curr_count = item[2]
                curr_obj = item[1]
                game_obj.nodesExpanded += 1
                curr_cost = item[0]

                if (item[3],item[4]) == (3,3) and curr_count == 1:
                        found_sol = True
                        game_obj.trace = curr_obj.trace
                        break

                for i in range(7):
                        for j in range(7):
                                if curr_obj.gameState[i][j] == 1:
                                        if curr_obj.is_validMove((i,j), DIRECTION['N']):
                                                newPos = curr_obj.getNextPosition((i,j), DIRECTION['N'])
                                                new_obj = copy.deepcopy(curr_obj)
                                                new_obj.gameState = copy.deepcopy(curr_obj.gameState)
                                                new_obj.gameState = new_obj.getNextState((i,j), DIRECTION['N'])
                                                new_obj.trace = copy.deepcopy(curr_obj.trace)
                                                new_obj.trace.append((i,j))
                                                new_obj.trace.append(newPos)
                                                q.put((curr_cost + 2 + heuristic_two(newPos[0], newPos[1]), new_obj, curr_count - 1, newPos[0], newPos[1]))

                                        if curr_obj.is_validMove((i,j), DIRECTION['S']):
                                                newPos = curr_obj.getNextPosition((i,j), DIRECTION['S'])
                                                new_obj = copy.deepcopy(curr_obj)
                                                new_obj.gameState = copy.deepcopy(curr_obj.gameState)
                                                new_obj.gameState = new_obj.getNextState((i,j), DIRECTION['S'])
                                                new_obj.trace = copy.deepcopy(curr_obj.trace)
                                                new_obj.trace.append((i,j))
                                                new_obj.trace.append(newPos)
                                                q.put((curr_cost + 2 + heuristic_two(newPos[0], newPos[1]), new_obj, curr_count - 1, newPos[0], newPos[1]))

                                        if curr_obj.is_validMove((i,j), DIRECTION['E']):
                                                newPos = curr_obj.getNextPosition((i,j), DIRECTION['E'])
                                                new_obj = copy.deepcopy(curr_obj)
                                                new_obj.gameState = copy.deepcopy(curr_obj.gameState)
                                                new_obj.gameState = new_obj.getNextState((i,j), DIRECTION['E'])
                                                new_obj.trace = copy.deepcopy(curr_obj.trace)
                                                new_obj.trace.append((i,j))
                                                new_obj.trace.append(newPos)
                                                q.put((curr_cost + 2 + heuristic_two(newPos[0], newPos[1]), new_obj, curr_count - 1, newPos[0], newPos[1]))

                                        if curr_obj.is_validMove((i,j), DIRECTION['W']):
                                                newPos = curr_obj.getNextPosition((i,j), DIRECTION['W'])
                                                new_obj = copy.deepcopy(curr_obj)
                                                new_obj.gameState = copy.deepcopy(curr_obj.gameState)
                                                new_obj.gameState = new_obj.getNextState((i,j), DIRECTION['W'])
                                                new_obj.trace = copy.deepcopy(curr_obj.trace)
                                                new_obj.trace.append((i,j))
                                                new_obj.trace.append(newPos)
                                                q.put((curr_cost + 2 + heuristic_two(newPos[0], newPos[1]), new_obj, curr_count - 1, newPos[0], newPos[1]))

        return found_sol

