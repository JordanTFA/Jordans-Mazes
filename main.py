from PIL import Image, ImageDraw

def getinput():
    dimensions = input("Please enter your dimensions - separate by comma\n")
    dimensions = dimensions.split(',')
    return dimensions;

def draw(x, y):
    print(str(x) + " " + str(y))

if __name__ == '__main__':
    dimensions = getinput()
    x = dimensions[0]
    y = dimensions[1]
    draw(x,y)