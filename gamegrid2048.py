from DisplayEngine import *
from random import randrange
from copy import deepcopy


class gameGrid:

    display_x = 24
    display_y = 4
    frame = display(display_x, display_y)
    no_of_moves = 0

    # Master list control
    master_list = [[0 for j in range(display_x / 6)] for i in range(display_y)]

    def changeChar(self, x, y, char):
        self.master_list[y][x] = int(char)

    # Shifting based on direction, use wasd to move
    def shift(self, direction, inp_list=False):

        if not inp_list:
            inputlist = deepcopy(self.master_list)
        else:
            inputlist = deepcopy(inp_list)

        # Checks for direction and rotates list accordingly
        # All cases here, need to rewrite into a loop
        if direction == 'left':
            a = inputlist
        elif direction == 'right':
            a = [i[::-1] for i in inputlist]
        elif direction == 'up':
            a = [list(x) for x in zip(*inputlist)[::-1]]
        elif direction == 'down':
            a = [list(x) for x in zip(*inputlist[::-1])]
        else:
            inputlist = self.master_list

            return True

        # Shifted List is the list with all elements shifted to the left, without adding yet
        shifted_List = [[] for i in range(len(a[0]))]

        for j, list_j in enumerate(a):
            counter = 0
            for i, val_x in enumerate(list_j):
                if val_x:
                    shifted_List[j].append(val_x)

                else:
                    counter += 1
            for number in range(counter):
                shifted_List[j].append(0)

        added_List = [[] for i in range(len(a[0]))]

        # Need to rewrite this algorithm
        for j, list_j in enumerate(shifted_List):
                # First two same
            if list_j[0] == list_j[1]:
                added_List[j].append(list_j[0] + list_j[1])
                if list_j[2] == list_j[3]:
                    added_List[j].append(list_j[2] + list_j[3])
                    added_List[j].append(0)
                    added_List[j].append(0)
                else:
                    added_List[j].append(list_j[2])
                    added_List[j].append(list_j[3])
                    added_List[j].append(0)

            else:
                added_List[j].append(list_j[0])

                if list_j[1] == list_j[2]:
                    added_List[j].append(list_j[1] + list_j[2])
                    added_List[j].append(list_j[3])
                    added_List[j].append(0)
                else:
                    added_List[j].append(list_j[1])
                    if list_j[2] == list_j[3]:
                        added_List[j].append(list_j[2] + list_j[3])
                        added_List[j].append(0)
                    else:
                        added_List[j].append(list_j[2])
                        added_List[j].append(list_j[3])

        # Rotates everything back
        if direction == 'left':
            final = added_List
        elif direction == 'right':
            final = [i[::-1] for i in added_List]
        elif direction == 'up':
            final = [list(x) for x in zip(*added_List[::-1])]
        elif direction == 'down':
            final = [list(x) for x in zip(*added_List)[::-1]]

        # Final Assignment of masterlist
        if not inp_list:
            self.master_list = deepcopy(final)

            if self.master_list != inputlist:
                self.no_of_moves += 1

        else:
            return final

        # If grid not full, return true
        if self.check_if_full:
            if inputlist != final:
            # Create new number
                self.newNumber()

    # Creates pictorial represenation
    def __str__(self):
        b = [['[' + str(x).center(4) + ']' if x else '[' + ''.center(4) + ']' for x in self.master_list[y]]
             for y, value in enumerate(self.master_list)]

        return str(display(b))

    def check_game_over(self):
        counter = 0
        for i in ['up', 'down', 'left', 'right']:
            a = deepcopy(self.shift(i, self.master_list))
            if a == self.master_list:
                counter += 1

        if counter == 4:
            return False
        else:
            return True

    def check_if_full(self):

        occupied_coords = []
        for j, list_j in enumerate(self.master_list):
            for i, val_i in enumerate(list_j):
                if val_i:
                    occupied_coords.append([i, j])

        newCoord = [randrange(4), randrange(4)]

        n = 0
        while newCoord in occupied_coords:
            newCoord = [randrange(4), randrange(4)]
            n += 1
            if n == 1000:
                return False

        return newCoord

    # To create a class method to output coordinates of occupied blocks
    # Class method to create random characters in unoccupied blocks
    def newNumber(self, char=0):

        newCoord = self.check_if_full()

        if newCoord:
            if char == 0:

                # The appearance of 4 is only possible when max number on board
                # is >= 32
                if self.largest_num() >= 32:
                    a = randrange(2)

                    if a == 0:
                        char = 2
                    else:
                        char = 4

                else:
                    char = 2

            self.changeChar(newCoord[0], newCoord[1], char)

    # Returns the largest number in the game
    def largest_num(self):

        a = []

        for i in self.master_list:
            for j in i:
                a.append(j)

        return max(a)
