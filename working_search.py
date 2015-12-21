import pegSolitaireUtils
import copy
import readGame
import Queue
from config import DIRECTION

def recursive_dls(game_obj, pos, curr_depth, limit_depth, count):

	result = False
	if count == 1:
		if pos[0]%2 == 1 and pos[1]%2 == 1:
			return True
		else:
			return False

	if curr_depth > limit_depth:
		return False

	for i in range(7):
		for j in range(7):
			if (game_obj.gameState[i][j] == 1):
				if game_obj.is_validMove((i,j), DIRECTION['N']) and game_obj.gameState[i-1][j] == 1:
					dup_array = copy.deepcopy(game_obj.gameState)
					newPos = game_obj.getNextPosition((i,j), DIRECTION['N'])
					game_obj.gameState = game_obj.getNextState((i,j), DIRECTION['N'])
					result = recursive_dls(game_obj, newPos, curr_depth + 1, limit_depth, count - 1)
					
					if result == True:
						game_obj.trace.insert(0,newPos)
						game_obj.trace.insert(0,(i,j))
						return True
					else:
						game_obj.gameState = dup_array 

        			if game_obj.is_validMove((i,j), DIRECTION['S']) and game_obj.gameState[i+1][j] == 1:
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

        			if game_obj.is_validMove((i,j), DIRECTION['E']) and game_obj.gameState[i][j+1] == 1:
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

				if game_obj.is_validMove((i,j), DIRECTION['W']) and game_obj.gameState[i][j-1] == 1:
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

                                if game_obj.is_validMove((i,j), DIRECTION['N']):
                                        dup_array = copy.deepcopy(game_obj.gameState)
                                        newPos = game_obj.getNextPosition((i,j), DIRECTION['N'])
                                        game_obj.gameState = game_obj.getNextState((i,j), DIRECTION['N'])
                                        result = recursive_dls(game_obj, newPos, curr_depth + 1, limit_depth, count)

                                        if result == True:
                                                game_obj.trace.insert(0,newPos)
                                                game_obj.trace.insert(0,(i,j))
						return True
                                        else:
                                                game_obj.gameState = dup_array

                                if game_obj.is_validMove((i,j), DIRECTION['S']):
                                        dup_array = copy.deepcopy(game_obj.gameState)
                                        newPos = game_obj.getNextPosition((i,j), DIRECTION['S'])
                                        game_obj.gameState = game_obj.getNextState((i,j), DIRECTION['S'])
                                        result = recursive_dls(game_obj, newPos, curr_depth + 1, limit_depth, count)

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
                                        result = recursive_dls(game_obj, newPos, curr_depth + 1, limit_depth, count)

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
                                        result = recursive_dls(game_obj, newPos, curr_depth + 1, limit_depth, count)

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
	'''depth = 18;
	result = False
	while depth < 50:
		for i in range(7):
			for j in range(7):
				if pegSolitaireObject.gameState[i][j] == 1:
					result = recursive_dls(pegSolitaireObject, (i,j), 0, depth)
					if result == True:
						print "Success at depth " + depth
						break
		depth += 1'''
	count = readGame.count_pegs(pegSolitaireObject)
	result = recursive_dls(pegSolitaireObject, (0,0), 0, 20, count)
	return result


 
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
	heuristic_func = [[0 for x in range(7)] for x in range(7)]	
	for i in range(7):
		for j in range(7):
			val = 0
			val = val + abs(j - 3)
			val = val + abs(i - 3)
			heuristic_func[i][j] = val

        cost = [[0 for x in range(7)] for x in range(7)]
        for i in range(7):
                for j in range(7):
                        cost[i][j] = 0

        q = Queue.PriorityQueue()

        for i in range(7):
                for j in range(7):
                        if game_obj.gameState[i][j] == 1:
                                q.put((heuristic_func[i][j],i,j))

        while not q.empty():
                item = q.get()
                if game_obj.gameState[item[1]][item[2]] != 1:
                        continue

                if (item[1],item[2]) == (3,3) and count_pegs == 1:
			print "Early return"
                        break

                if game_obj.is_validMove((item[1],item[2]), DIRECTION['N']):
                        newPos = game_obj.getNextPosition((item[1],item[2]), DIRECTION['N'])
                        cost[newPos[0]][newPos[1]] = cost[item[1]][item[2]] + abs(3 - item[1]) + abs(3 - item[2])
                        q.put((cost[newPos[0]][newPos[1]] + heuristic_func[newPos[0]][newPos[1]], newPos[0], newPos[1]))
                        game_obj.gameState = game_obj.getNextState((item[1],item[2]), DIRECTION['N'])
			if game_obj.gameState[item[1]-1][item[2]] == 1:
				count_pegs = count_pegs - 1

                if game_obj.is_validMove((item[1],item[2]), DIRECTION['S']):
                        newPos = game_obj.getNextPosition((item[1],item[2]), DIRECTION['S'])
                        cost[newPos[0]][newPos[1]] = cost[item[1]][item[2]] + abs(3 - item[1]) + abs(3 - item[2])
                        q.put((cost[newPos[0]][newPos[1]] + heuristic_func[newPos[0]][newPos[1]], newPos[0], newPos[1]))
                        game_obj.gameState = game_obj.getNextState((item[1],item[2]), DIRECTION['S'])
                        if game_obj.gameState[item[1]+1][item[2]] == 1:
                                count_pegs = count_pegs - 1


                if game_obj.is_validMove((item[1],item[2]), DIRECTION['E']):
                        newPos = game_obj.getNextPosition((item[1],item[2]), DIRECTION['E'])
                        cost[newPos[0]][newPos[1]] = cost[item[1]][item[2]] + abs(3 - item[1]) + abs(3 - item[2])
                        q.put((cost[newPos[0]][newPos[1]] + heuristic_func[newPos[0]][newPos[1]], newPos[0], newPos[1]))
                        game_obj.gameState = game_obj.getNextState((item[1],item[2]), DIRECTION['E'])
                        if game_obj.gameState[item[1]][item[2]+1] == 1:
                                count_pegs = count_pegs - 1


                if game_obj.is_validMove((item[1],item[2]), DIRECTION['W']):
                        newPos = game_obj.getNextPosition((item[1],item[2]), DIRECTION['W'])
                        cost[newPos[0]][newPos[1]] = cost[item[1]][item[2]] + abs(3 - item[1]) + abs(3 - item[2])
                        q.put((cost[newPos[0]][newPos[1]] + heuristic_func[newPos[0]][newPos[1]], newPos[0], newPos[1]))
                        game_obj.gameState = game_obj.getNextState((item[1],item[2]), DIRECTION['W'])
                        if game_obj.gameState[item[1]][item[2]-1] == 1:
                                count_pegs = count_pegs - 1


	if q.empty():
		print "False"
		return False
	else:
		print "True ",cost[3][3]
		return True


def aStarTwo(pegSolitaireObject):
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
	return True

