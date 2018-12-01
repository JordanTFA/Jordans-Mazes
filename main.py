from PIL import Image, ImageDraw
import random

def getinput():
    dimensions = input("Please enter your dimensions - separate by comma\n")
    dimensions = dimensions.split(',')
    return dimensions;

def draw(x, y):
    print(str(x) + " " + str(y))

    output = ""
    for i in range(int(y)):
        for j in range(int(x)):
            output += str(decideTile())
        output += "\n"

    print(output)

def decideTile():
    tile = random.randint(0,1)
    if tile == 0:
        return " "
    elif tile == 1:
        return "X"

if __name__ == '__main__':
    dimensions = getinput()
    x = dimensions[0]
    y = dimensions[1]
    draw(x,y)