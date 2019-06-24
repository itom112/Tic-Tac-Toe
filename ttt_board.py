import os

brd = [[1, 2, 3,], 
		 [4, 5, 6,],
		 [7, 8, 9,]]


def board():
	os.system('clear')
	print('')
	print('  ', brd[0][0], brd[0][1], brd[0][2], '', sep=' | ')
	print('   -------------')
	print('  ', brd[1][0], brd[1][1], brd[1][2], '', sep=' | ')
	print('   -------------')
	print('  ', brd[2][0], brd[2][1], brd[2][2], '', sep=' | ')
	print('\n')

board()





