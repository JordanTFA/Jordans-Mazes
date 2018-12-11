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
            xx,yy=directions[index]
            if xx < 0 or xx >= width or yy < 0 or yy >= height:
                del directions[index]
                outOfBounds.append([xx,yy])
                if [xx,yy] in visited:
                    v.append([xx,yy])

        d = choice(directions)

        print("Out of Bounds: " + str(outOfBounds) +
              "\nVisited tiles: " + str(v) +
              "\nAvailable directions : " + str(directions) +
              "\nD: " + str(d) +
              "\n")


        # d = choice(directions)
        # while not inBounds(d):
        #     print("Initial Out of bounds: " + str(d) + ", Directions: " + str(directions))
        #
        #     if len(directions) > 1:
        #         directions.remove(d)
        #         print("Removed: " + str(d))
        #         d = choice(directions)
        #
        #     else:
        #         print("Out of neighbours - Now we backtrack...")
        #         popped.append(visited[-1])
        #         visited.pop()
        #         d = visited[-1]
        #         print("New D: " + str(d))
        #         walk(d[0], d[1])
        #
        # while d in visited:
        #
        #     #print("Visited: " + str(d))
        #
        #     if len(directions) > 1:
        #         directions.remove(d)
        #         d = choice(directions)
        #
        #     else:
        #         print("Out of neighbours - Now we backtrack...")
        #         visited.pop()
        #         d = visited[-1]
        #         print("New D: " + str(d))
        #         walk(d[0], d[1])
        #
        #     if not inBounds(d):
        #
        #         if len(directions) > 1:
        #             directions.remove(d)
        #             print("Removed: " + str(d))
        #             d = choice(directions)
        #
        #         else:
        #             print("Out of neighbours - Now we backtrack...")
        #             visited.pop()
        #             d = visited[-1]
        #             print("New D: " + str(d))
        #             walk(d[0], d[1])

        #print("D: " + str(d))

        if len(visited) < (width * height):
            walk(d[0], d[1])

    walk(0,0)

    print("Finished: " + str(len(visited)) + " " + str(visited))

def inBounds(d):

    if d[0] < 0 or \
            d[0] > width - 1 or \
            d[1] < 0 or \
            d[1] > height - 1:
        return False
    else:
        return True

if __name__ == '__main__':

    width,height = 4,4
    makemaze(width,height)