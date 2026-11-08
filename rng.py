
import random
from debris import Debris
import constants




from large_meteor import Large_Meteor
from medium_meteor import Medium_Meteor
from small_meteor import Small_Meteor

def meteors():
    meteors_list = []
    for i in range(random.randint(8, 10)):
        meteors_list.append(random.choice([Large_Meteor, Medium_Meteor, Small_Meteor])((random.randint(0, constants.RESOLUTION[0] * constants.SPACE_X["PANEL_NUM"]), random.randint(0, constants.RESOLUTION[1] * constants.SPACE_Y["PANEL_NUM"]))))
    return meteors_list
