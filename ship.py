from in_space import In_Space

class Ship(In_Space):

    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.pos = [0,0,0]