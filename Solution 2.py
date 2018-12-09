from random import choice


# we gonna hash tuples with this
def cordhash(cord):
    return (cord[0] << 16) + cord[1]


WIDTH = 4
HEIGHT = 4
SIZE = WIDTH * HEIGHT
VISITED = set()
RESULT = []
INDEX = 0
# first position
chosen = (0, 0)
while True:
    VISITED.add(cordhash(chosen))
    # if we reach SIZE==0 we are done
    SIZE -= 1
    if not SIZE:
        break

    go_back = True
    while go_back:
        X, Y = last = chosen

        outside = []
        visited = []
        directions = []

        # testings
        x = X - 1
        cord = (x, Y)
        if x < 0:
            outside.append(cord)
        elif cordhash(cord) in VISITED:
            visited.append(cord)
        else:
            directions.append(cord)
        x = X + 1
        cord = (x, Y)
        if x == WIDTH:
            outside.append(cord)
        elif cordhash(cord) in VISITED:
            visited.append(cord)
        else:
            directions.append(cord)

        y = Y - 1
        cord = (X, y)
        if y < 0:
            outside.append(cord)
        elif cordhash(cord) in VISITED:
            visited.append(cord)
        else:
            directions.append(cord)
        y = Y + 1
        cord = (X, y)
        if y == HEIGHT:
            outside.append(cord)
        elif cordhash(cord) in VISITED:
            visited.append(cord)
        else:
            directions.append(cord)

        print('Out of bounds:', outside)
        print('Visited:', visited)
        print('Directions:', directions)
        if directions:
            chosen = choice(directions)
            INDEX = len(RESULT) - 1
            RESULT.append((last, chosen), )
            go_back = False
            print('D:', chosen)
        else:
            chosen = RESULT[INDEX][1]
            INDEX -= 1
            print('Falling back to:', chosen)
        print()
print('Result:')
print('\n'.join(['%s <-> %s' % step for step in RESULT]))