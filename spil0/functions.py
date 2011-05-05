import sys, math
import pygame
import data

def distance_between(r0, r1):
    return math.sqrt((r1.x-r0.x)*(r1.x-r0.x) + (r1.y-r0.y)*(r1.y-r0.y))

def quit():
    print "GAME OVER"
    if data.player.__dict__.has_key("gold"):
        print "You gathered %i gold." % data.player.gold
    sys.exit(0)

