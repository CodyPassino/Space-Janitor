import constants

class In_Space():

    def __init__(self):
        self.hi = "hi"

    def get_x(self):
        return self.pos[constants.POS["X"]]
        
    def get_y(self):
        return self.pos[constants.POS["Y"]]
        
    def get_z(self):
        return self.pos[constants.POS["Z"]]