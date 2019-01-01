from random import choice ,randint, shuffle

pairs = [0,0]

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
            pairs.append(visited[-1],d)

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

def drawmaze(width, height):
    hw = "|  "
    hp = "   "

    vw = "+--"
    vp = "+  "

    grid = []
    for row in range(height * 2):
        if row % 2 != 0:
            grid += [["+--"] * width + ["+"]]
        else:
            grid += [["|  "] * width + ["|"]]

    grid[0][1] = "   "
    grid[1][1] = "+  "
    grid[0][2] = "   "

    msg = "\n"

    msg += ("+--" * width) + "+\n"

    for row in grid:
        for t in row:
            msg += t
        msg += "\n"

    print(msg)

    for a,b in pairs:
        print(a,b)

    row = ""

    # grid = []
    # for row in range(height):
    #     grid += [["+"] * width]

    # print()
    # print(("+--" * width) + "+")
    # grid[width][height]
    # row += hw + hw + hp + hp + hp + hw + "\n"
    # row += vp + vp + vw + vp + vp + vp + "\n"
    # print(("+--" * width) + "+")
    # row += hw + hw + hw + hw + hw + hw + "\n"
    # row += vw + vw + vw + vw + vw + vp + "\n"
    # row += hw + hw + hw + hw + hw + hw + "\n"
    # row += vw + vw + vw + vw + vw + vp + "\n"
    # row += hw + hw + hw + hw + hw + hw + "\n"
    # row += vw + vw + vw + vw + vw + vp + "\n"
    # row += hw + hw + hw + hw + hw + hw + "\n"
    # row += vw + vw + vw + vw + vw + vp + "\n"
    # print(row)

    #grid[2][2] = "E"


    # print(("+--" * width) + "+")
    # for i in range(height):
    # print (horz[i])
    # if i < len(vert):
    # print(vert[i])
    # for i in range(height):
    # print(("+--" * width) + "+")
    # print("|  " * (width + 1))

    # Print floor
    #     # print(("+--" * width) + "+")

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

if __name__ == '__main__':
    width, height = 3,3
    makemaze(width, height)
    drawmaze(width, height)
