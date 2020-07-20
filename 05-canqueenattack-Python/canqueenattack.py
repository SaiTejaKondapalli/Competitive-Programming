# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and
# diagonally.

def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	if qR == oR or qC == oC:
		return True
	elif (qR == qC and oR == oC):
		return True
	elif (qR + qC == oR + oC) or (qR == oR + 1 and qC == oC + 1) or (qR == oR - 1 and qC == oC - 1):
		return True
	return False