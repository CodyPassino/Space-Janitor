from debris import Debris
import constants

class Small_Meteor(Debris):

    def __init__(self, pos):
        self.size = constants.sizes["SMALL"]
        super().__init__(pos, health=50)
        