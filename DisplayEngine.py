from copy import deepcopy


class display:

    def __init__(self, x=0, y=0):
        # If input is numbers, create a blank canvas
        if isinstance(x, int):

            # Nested list that controls everything
            self.m = []

            # character for whitespace
            self.whiteSpace = '.'

            for i in range(y):
                self.m.append([])
                for j in range(x):
                    self.m[i].append(self.whiteSpace)

        # For overlays
        # Else if input is a list that produces a screen, take that screen as
        # input
        elif isinstance(x, list):
            self.m = deepcopy(x)

    # Print code to generate canvas
    def __str__(self):
        # Canvas is a string
        table = ''
        for i in self.m:
            for j in i:
                table += str(j)
            table += '\n'
        return table

    # method to individual character space
    # Redundant, can just use text method alone
    def change(self, x, y, value):
        self.m[y][x] = value

    # Old method to insert text (cannot insert multi line text)
    # def text(self,x,y,text):
    # 	text = str(text)
    # 	for i in range(len(text)):
    # 		self.change(x+i,y,text[i])

    # New method to insert text (can insert multiline text seperated by '\n')
    # x,y coordinates are top left of text chunk
    def text(self, x, y, text):
        text = str(text)
        textsplit = text.split('\n')
        for i, line in enumerate(textsplit):
            for j, char in enumerate(line):
                self.change(x + j, y + i, char)

    # Scrolls the canvas to the left
    def shift_left(self):
        new = []
        for i in range(len(self.m)):
            new.append([])
            for j in range(len(self.m[i])):
                if j + 1 < len(self.m[i]):
                    new[i].append(self.m[i][j + 1])
                else:
                    new[i].append(self.whiteSpace)
        self.m = new

    # Scrolls the canvas to the left, and warps characters scrolling out to
    # the right side
    def shift_left_warp(self):
        new = []
        for i in range(len(self.m)):
            new.append([])
            for j in range(len(self.m[i])):
                if j < len(self.m[i]) - 1:
                    new[i].append(self.m[i][j + 1])
                else:
                    new[i].append(self.m[i][len(self.m[i]) - j - 1])
        self.m = new

    # Allows output of screen as a list
    def __call__(self):
        return self.m

    # returns the x,y coordinates of a specific character
    # def find(self, char):
    # 	self.m[]

# print display([['[ 0  ]', '[ 0  ]', '[ 0  ]', '[ 0  ]'], ['[ 0  ]', '[ 0
# ]', '[ 0  ]', '[ 0  ]'], ['[ 0  ]', '[ 0  ]', '[ 0  ]', '[ 0  ]'], ['[ 0
# ]', '[ 0  ]', '[ 0  ]', '[ 0  ]']])

# default variables to initialise
# fps = 10
# displayx = 50
# displayy = 10
# frame = display(displayx,displayy)
# frame.text(5,5,'a')



# code loop
# while True:
# for i in range():
# 	os.system('clear')
# 	print frame
# 	frame.shift_left_warp()
# frame.change(0,i,'w')
# 	sleep(1/fps)
