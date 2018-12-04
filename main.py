from PIL import Image, ImageDraw
from random import choice ,randint

def getinput():
    dimensions = input("Please enter your dimensions - separate by comma\n")
    dimensions = dimensions.split(',')
    return dimensions;

def makemaze(width, height):

    visited = []
    visited.append([0,0])
    print(visited)

    def walk(x,y):

        north = [x-1, y]
        east = [x, y+1]
        south = [x+1, y]
        west = [x, y-1]

        directions = [north, east, south, west]
        d = choice(directions)

        if d in visited or \
                d[0] < 0 or \
                d[0] > width - 1 or \
                d[1] < 0 or \
                d[1] > height - 1:
            d = choice(directions)
        else:
            print(d)

            visited.append(d)
            print(visited)

        if len(visited) < width * height:
            walk(d[0], d[1])

    walk(0,0)

def draw(x, y):
    print(str(x) + " " + str(y))

    output = ""
    for i in range(int(y)):
        for j in range(int(x)):
            output += str(decideTile())
        output += "\n"

    print(output)

def decideTile():
    tile = randint(0,1)
    if tile == 0:
        return " "
    elif tile == 1:
        return "X"

if __name__ == '__main__':
    #dimensions = getinput()
    width,height = 4,4# dimensions[0],dimensions[1]

    makemaze(width,height)