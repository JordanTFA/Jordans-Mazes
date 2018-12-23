<<<<<<< HEAD
from random import choice, randint, shuffle
=======
from random import choice ,randint, shuffle
>>>>>>> origin/master


def makemaze(width, height):
    visited = []
    popped = []
    result = []
    print("D: [0,0]\n")

    def walk(x, y):

        outOfBounds = []
        v = []
        visited.append([x, y])

        north = [x, y - 1]
        east = [x + 1, y]
        south = [x, y + 1]
        west = [x - 1, y]

        directions = [north, east, south, west]

        for index in range(3, -1, -1):
            xx, yy = directions[index]
            if xx < 0 or xx >= width or yy < 0 or yy >= height:
                del directions[index]
                outOfBounds.append([xx, yy])

            if [xx, yy] in visited or [xx, yy] in popped:
                v.append([xx, yy])
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
            popped.append(visited[-1])
            print("Popped: ", popped)
            visited.pop()
            d = visited[-1]
            visited.pop()
            print("D: ", d)
            print()

            walk(d[0], d[1])

    walk(0, 0)

    for r in result:
        print(r)
<<<<<<< HEAD


def drawmaze(width, height):
    hw = "|  "
    hp = "   "

    vw = "+--"
    vp = "+  "

    row = ""

    # print()
    # print(("+--" * width) + "+")
    # grid[width][height]
    row += hw + hw + hp + hp + hp + hw + "\n"
    row += vp + vp + vw + vp + vp + vp + "\n"
    # print(row)

    grid = []
    for row in range(height): grid += [["t"] * width]

    grid[2][2] = "E"

    msg = "\n"
    for row in grid:
        for t in row:
            msg += t
        msg += "\n"

    print(msg)
    # print(("+--" * width) + "+")
    # for i in range(height):
    # print (horz[i])
    # if i < len(vert):
    # print(vert[i])
    # for i in range(height):
    # print(("+--" * width) + "+")
    # print("|  " * (width + 1))

    # Print floor
    # print(("+--" * width) + "+")
=======
    
def drawmaze(width, height):
    
    hw = "|  "
    hp = "   "
    
    vw = "+--"
    vp = "+  "
    
    row = ""

    #print()
    #print(("+--" * width) + "+")
    #grid[width][height] 
    row += hw + hw + hp + hp + hp + hw + "\n"
    row += vp + vp + vw + vp + vp + vp + "\n"
    #print(row)

    grid = []
    for row in range(height): grid += [["t"]*width]
    
    msg = "\n"
    for row in grid:
        for t in row:
            msg+=t
        msg+="\n"
    
    print(msg)
    #print(("+--" * width) + "+")
    #for i in range(height):
        #print (horz[i])
        #if i < len(vert):
            #print(vert[i])
    #for i in range(height):
        #print(("+--" * width) + "+")
        #print("|  " * (width + 1))

    #Print floor
    #print(("+--" * width) + "+")
>>>>>>> origin/master

    print()
    print("+--+--+--+--+--+")
    print("|  |           |")
    print("+  +  +--+  +  +")
    print("|     |     |  |")
    print("+--+  +--+--+  +")
    print("|  |  |     |  |")
    print("+  +  +  +  +  +")
    print("|        |  |  |")
    print("+--+--+--+--+--+")
<<<<<<< HEAD


if __name__ == '__main__':
    width, height = 5, 4
    makemaze(width, height)
    drawmaze(width, height)
=======
if __name__ == '__main__':

    width, height = 5,4
    makemaze(width, height)
    drawmaze(width, height)
>>>>>>> origin/master
