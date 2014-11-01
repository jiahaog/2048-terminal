import gamegrid2048
from os import system
import keypress


# Initialize Variables
game = gamegrid2048.gameGrid()
game.newNumber()
game.newNumber()
no_of_moves = 0
moveLog = []


def firstScreen():
    system('clear')
    print game
    print 'Get to 2048!'
    print 'Use WASD to shift'


def gameLoop():
    game_running = True

    while game_running:

        # Maps keypress and appends it to a log
        inp = keypress.readMove()
        moveLog.append(inp)

        # Shifts tiles with input
        game.shift(inp)

        # print stuff
        system('clear')
        print game
        print 'Moves: %s' % game.no_of_moves
        print 'Largest No: %i' % game.largest_num()

        # Check for game over
        if not game.check_game_over():
            print 'Game Over!'
            print 'Moves:'
            print moveLog
            game_running = False


def game2048():

    firstScreen()
    gameLoop()

game2048()
