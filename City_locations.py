import random
import time
import os

DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
EDIBLE = 'edible'
DESCWORDS = 'descwords'


Def locations():
    Homestate = {
        'New California Republic': {
            DESC: """After the nuclear fallout, a lot of people split up to make sheltered communities for themselves and others.
                      Then they later grew into a bunch of cities in the wastelands, which made up the New California Republic.""",
            NORTH: 'Glorburgh', 'Idostin', 'Yeka', 'Yefnard',
            EAST:  'Home','Krowood', 'Orkgate', 'Laville', 'Odonmery',
            SOUTH: 'Yhodale', 'Ipland', 'Blonio', 'Vruuville',
            WEST: 'New Vegas', 'Ovlaford', 'Houver', 'Asowell', 'Oklance',
            GROUND: ['Welcome Survivors Sign', 'Wasteland']},
        'Home': {
            DESC: 'This has been your home for 20 years ever since your parents died.',
#            WEST: 'Thief Guild',
#            EAST: 'Bakery',
#            SOUTH: 'Town Square',
#            GROUND: ['Do Not Take Sign Sign']},
