
NONE, EAST, SOUTH, WEST, NORTH = range(0,5)

def left(direction):
    return((direction+2)%4)+1

def right(direction):
    return (direction%4)+1

def reverse(direction):
    return ((direction+1)%4)+1
