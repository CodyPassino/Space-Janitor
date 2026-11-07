from debris import Debris

class Small_Meteor(Debris):
    def __init__(self, pos):
        super().__init__(pos, health=50)
        