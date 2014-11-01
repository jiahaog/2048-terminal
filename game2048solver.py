# solver file for 2048 to test effectiveness of a particular sequence of moves


import gamegrid2048
from os import system
from random import randrange


# Initialise
game = gamegrid2048.gameGrid()
game.newNumber()
game.newNumber()
directions = ['up', 'down', 'left', 'right']
fps = 30
no_of_moves = 0
moveLog = []

# First Screen
system('clear')
print game
print 'Get to 2048!'
print 'Use WASD to shift'


# code loop
while True:

    # checkInput and shift
    # inp = keypress.readMove()
    inp = directions[randrange(4)]
    moveLog.append(inp)
    game.shift(inp)

    # print stuff
    # os.system('clear')
    # print game
    # print 'Moves: %s' %game.no_of_moves
    # print 'Largest No: %i' %game.largest_num()
    if not game.check_game_over():
        break
    # sleep(1/fps)


print 'Game Over'
print 'Moves: %s' % game.no_of_moves
print 'Largest No: %i' % game.largest_num()
