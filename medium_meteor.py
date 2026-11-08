from debris import Debris
import sprite_constants

class Medium_Meteor(Debris):

    def __init__(self, pos):
        self.size = sprite_constants.SIZES["MEDIUM"]
        self.health = 100
        super().__init__(pos)