from debris import Debris
import sprite_constants

class Small_Meteor(Debris):

    def __init__(self, pos):
        self.size = sprite_constants.SIZES["SMALL"]
        self.health = 50
        super().__init__(self, pos)
        