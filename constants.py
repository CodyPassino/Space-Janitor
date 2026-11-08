import pygame

# Display settings
RESOLUTION = (1200, 800)
DELTA_TIME = 0.1
FPS = 60

# Space panels
SPACE_X = {
    "STATION" : 1,
    "PANEL_NUM": 8,
    "FORCE_METEOR": 4
}

SPACE_Y = {
    "STATION" : 1,
    "PANEL_NUM": 8,
    "FORCE_METEOR": 4 
}

# Ship settings
SHIP_TURN_SPEED = 20 # Num of pixels, left right and down
SHIP_SPEED = 10 # Num of pixels to zoom in

# Directions
UP = 1
DOWN = -1
RIGHT = -1
LEFT = 1
STILL = 0

# Debris
POS = {
    "X": 0,
    "Y": 1,
    "Z": 2
}
