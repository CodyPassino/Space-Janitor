from debris import Debris
import sprite_constants

class Large_Meteor(Debris):

    def __init__(self, pos):
        self.size = sprite_constants.SIZES["LARGE"]
        self.health = 200
        super().__init__(pos)