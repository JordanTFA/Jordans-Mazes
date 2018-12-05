from PIL import Image, ImageDraw
from random import choice ,randint, shuffle

def getinput():
    dimensions = input("Please enter your dimensions - separate by comma\n")
    dimensions = dimensions.split(',')
    return dimensions;

def makemaze(width, height):

    visited = []
    visited.append([0,0])
    print(visited)

    def walk(x,y):

        north = [x - 1, y]
        east = [x, y + 1]
        south = [x + 1, y]
        west = [x, y - 1]

        directions = [north, east, south, west]
        d = choice(directions)

        while not inRange(d):
             print("Initial Out of bounds: " + str(d))
             d = choice(directions)

        while d in visited:

            print("Visited: " + str(d))

            if not directions:
                print("Out of neighbours - Now we backtrack...")
            elif not inRange(d):
                print("Out of bounds: " + str(d) + ", Directions: " + str(directions))
                directions.remove(d)
                print("Removed: " + str(d))
            else:
                d = choice(directions)

                print("Directions: " + str(directions))


        print("D: " + str(d))
        visited.append(d)

        if len(visited) < width * height:
            walk(d[0], d[1])

    walk(0,0)


    print("Finished: " + str(len(visited)) + str(visited))
# def getNeighbour(x,y, visited):
#
#     north = [x - 1, y]
#     east = [x, y + 1]
#     south = [x + 1, y]
#     west = [x, y - 1]
#
#     directions = [north, east, south, west]
#     d = choice(directions)
#
#     d = checkInRange(d)
#     while d[0] < 0 or \
#         d[0] > width - 1 or \
#         d[1] < 0 or \
#         d[1] > height - 1:
#
#         d = choice(directions)
#
#     while d in visited:
#         d = choice(directions)
#     #d = checkVisited(d,directions,visited)
#
#     return d

def inRange(d):

    if d[0] < 0 or \
            d[0] > width - 1 or \
            d[1] < 0 or \
            d[1] > height - 1:
        return False
    else:
        return True

# def checkVisited(d,directions, visited):
#
#     if not d:
#         print("No neighbours")
#     if d in visited:
#         print(d)
#         d = choice(directions)
#         checkVisited(d, directions, visited)
#
#     return d

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