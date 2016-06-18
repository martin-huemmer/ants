__author__ = 'martinhummer'

# walk in the direction according to heading
def north(pos):
    pos[0] = pos[0] + 0
    pos[1] = pos[1] + 1
    return pos

def northEast(pos):
    pos[0] = pos[0] + 1
    pos[1] = pos[1] + 1
    return pos

def east(pos):
    pos[0] = pos[0] + 1
    pos[1] = pos[1] + 0
    return pos

def southEast(pos):
    pos[0] = pos[0] + 1
    pos[1] = pos[1] - 1
    return pos

def south(pos):
    pos[0] = pos[0] + 0
    pos[1] = pos[1] - 1
    return pos

def southWest(pos):
    pos[0] = pos[0] - 1
    pos[1] = pos[1] - 1
    return pos

def west(pos):
    pos[0] = pos[0] - 1
    pos[1] = pos[1] - 0
    return pos

def northWest(pos):
    pos[0] = pos[0] - 1
    pos[1] = pos[1] + 1
    return pos

# function to call walking in direction of heading
directions = { 0 : north,
                   45 : northEast,
                   90 : east,
                   135: southEast,
                   180: south,
                   225: southWest,
                   270: west,
                   315: northWest
}
