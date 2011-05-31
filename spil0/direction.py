import random as rand

NONE, EAST, SOUTH, WEST, NORTH = range(0,5)

def left(direction):
    return((direction+2)%4)+1

def right(direction):
    return (direction%4)+1

def reverse(direction):
    return ((direction+1)%4)+1

def random():
    return rand.randint(1,4)

def to_vector(direction, distance):
    if direction == EAST:
        return [distance,0]
    elif direction == SOUTH:
        return [0,distance]
    elif direction == WEST:
        return [-distance,0]
    elif direction == NORTH:
        return [0,-distance]
    else:
        return [0,0]
    
