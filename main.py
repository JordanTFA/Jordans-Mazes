from PIL import Image, ImageDraw
from random import choice ,randint, shuffle

def makemaze(width, height):

    visited = []
    popped = []
    visited.append([0,0])
    print("Visited: " + str(visited))

    def walk(x,y):

        north = [x - 1, y]
        east = [x, y + 1]
        south = [x + 1, y]
        west = [x, y - 1]

        directions = [north, east, south, west]

        # for xx,yy in directions:
        #     if xx < 0 or xx >= width or yy < 0 or yy >= height:
        #         directions.remove([xx,yy])
        #         print("Removing " + str([xx,yy]) + ", Directions left = " + str(directions))

        d = choice(directions)
        while not inBounds(d):
            print("Initial Out of bounds: " + str(d) + ", Directions: " + str(directions))

            if len(directions) > 1:
                directions.remove(d)
                print("Removed: " + str(d))
                d = choice(directions)

            else:
                print("Out of neighbours - Now we backtrack...")
                popped.append(visited[-1])
                visited.pop()
                visited.append(d)
                print("New D: " + str(d))
                walk(d[0], d[1])

        while d in visited:

            print("Visited: " + str(d))

            if len(directions) > 1:
                directions.remove(d)
                d = choice(directions)

            else:
                print("Out of neighbours - Now we backtrack...")
                popped.append(visited[-1])
                visited.pop()
                d = visited[-1]
                visited.append(d)
                print("New D: " + str(d))
                walk(d[0], d[1])

            if not inBounds(d):

                if len(directions) > 1:
                    directions.remove(d)
                    print("Removed: " + str(d))
                    d = choice(directions)

                else:
                    print("Out of neighbours - Now we backtrack...")
                    popped.append(visited[-1])
                    visited.pop()
                    d = visited[-1]
                    visited.append(d)
                    print("New D: " + str(d))
                    walk(d[0], d[1])

        print("D: " + str(d))
        visited.append(d)


        if (len(visited) + len(popped)) < width * height:
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