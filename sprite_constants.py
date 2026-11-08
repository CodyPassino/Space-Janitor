# Sprite paths
PATH_SPRITE = "sprites/"

    # Background
PATH_BACKGROUND = PATH_SPRITE + "backgrounds/"

BG_1 = PATH_BACKGROUND + "background_1.png"

#Debris 
PATH_DEBRIS = PATH_SPRITE + "debris/"
    # Meteor
PATH_METEOR = PATH_DEBRIS + "meteor/"
        # Small
PATH_SMALL_METEOR = PATH_METEOR + "small/"
            # Pieces
SMALL_BL_METEOR = PATH_SMALL_METEOR + 'small_bl.png'
SMALL_BR_METEOR = PATH_SMALL_METEOR + 'small_br.png'
SMALL_UL_METEOR = PATH_SMALL_METEOR + 'small_ul.png'
SMALL_UR_METEOR = PATH_SMALL_METEOR + 'small_ur.png'



# HUD
PATH_HUD = PATH_SPRITE + "HUD_elements/"

HUD_CROSSHAIR = PATH_HUD + "crosshair.png"
HUD_BOTTOM = PATH_HUD + "HUD_bottom.png"
HUD_TOP = PATH_HUD + "HUD_top.png"

MYHUD = {
    HUD_CROSSHAIR: (0,0),
    HUD_BOTTOM: (0,0),
    HUD_TOP: (0,0)
}


SIZES = {
    "LARGE": 3,
    "MEDIUM": 2,
    "SMALL": 1
}