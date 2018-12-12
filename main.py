from PIL import Image, ImageDraw
from random import choice ,randint, shuffle

def makemaze(width, height):

    visited = []
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

            if [xx,yy] in visited:
                v.append([xx,yy])
                if directions:
                    del directions[index]

        # Valid tile - let's continue
        if directions:
            d = choice(directions)

            print("Out of Bounds: ", outOfBounds)
            print("Visited tiles: ", v)
            print("Available directions : ", directions)
            print("D: ", d)

            print(str(visited[-1]) + " <-> " + str(d) + "\n")

            if len(visited) < (width * height):
                walk(d[0], d[1])

        # No neighbours - time to backtrack...
        else:
            print("No Neighbours")
            visited.pop()
    walk(0,0)

    print("Finished: " + str(len(visited)) + " " + str(visited))

if __name__ == '__main__':

    width, height = 4, 4
    makemaze(width, height)