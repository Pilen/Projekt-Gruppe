import sys, math
import pygame

def distance_between(r0, r1):
    return math.sqrt((r1.x-r0.x)*(r1.x-r0.x) + (r1.y-r0.y)*(r1.y-r0.y))

def quit():
    print "GAME OVER"
    sys.exit(0)
