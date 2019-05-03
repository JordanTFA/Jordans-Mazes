from random import choice

pairs = []

def makeMaze(width, height):
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
            pairs.append((visited[-1],d))

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

def drawMaze(width, height):
    hw = "|  "
    hp = "   "

    vw = "+--"
    vp = "+  "

    grid = []
    for row in range(height * 2):
        if row % 2 != 0:
            grid += [[vw] * width + ["+"]]
        else:
            grid += [[hw] * width + ["|"]]

    for a,b in pairs:
        low = min(a,b)
        high = max(a,b)
        if a[0] == b[0]: # Vertical movement
            grid[high[0]][high[1]] = vp
        if a[1] == b[1]: # Horizontal movement
            grid[low[0]][low[1]] = hp

    msg = "\n"

    msg += ("+--" * width) + "+\n"

    for row in grid:
        for t in row:
            msg += t
        msg += "\n"

    print(msg)

    row = ""

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
    width, height = 4,4
    makeMaze(width, height)
    drawMaze(width, height)