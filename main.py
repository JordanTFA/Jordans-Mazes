from PIL import Image, ImageDraw
from random import choice ,randint, shuffle

def makemaze(width, height):

    visited = []
    popped = []
    result = []
    print("D: [0,0]\n")

    def walk(x,y):

        outOfBounds = []
        v = []
        visited.append([x,y])

        north = [x, y - 1]
        east = [x + 1, y]
        south = [x, y + 1]
        west = [x - 1, y]

        directions = [north, east, south, west]

        for index in range(3,-1,-1):
            xx,yy = directions[index]
            if xx < 0 or xx >= width or yy < 0 or yy >= height:
                del directions[index]
                outOfBounds.append([xx,yy])

            if [xx,yy] in visited or [xx,yy] in popped:
                v.append([xx,yy])
                if directions:
                    del directions[index]

        # Valid tile - let's continue
        if directions:
            d = choice(directions)
            result.append(str(visited[-1]) + " <-> " + str(d))

            print("Out of Bounds: ", outOfBounds)
            print("Visited tiles: ", v)
            print("Available directions : ", directions)
            print("D: ", d)
            print("Result: ", result[-1])
            print()

            if (len(visited) + len(popped)) < ((height * width) - 1):
                walk(d[0], d[1])

        # No neighbours - time to backtrack...
        else:
            print("No Neighbours")
            print("Visited: ", visited)
            print("Popped: ", popped)
            popped.append(visited[-1])
            visited.pop()
            d = visited[-1]
            visited.pop()
            print("D: ", d)
            print()

            walk(d[0], d[1])
    walk(0,0)

    for r in result:
        print(r)

def drawmaze(width, height):
    for i in range(0, width):
        for j in range(0, height):
            print("*")

if __name__ == '__main__':

    width, height = 20, 20
    #makemaze(width, height)
    drawmaze(width, height)