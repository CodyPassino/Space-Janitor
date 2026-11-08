import pygame
import constants
import math
import sprite_constants

def setpos(screen, sprite,x, y):
        x = x * constants.DELTA_TIME
        y = y * constants.DELTA_TIME

        # Checks if already loaded or incoming zoomed img
        if sprite != pygame.surface: # File path
                sprite_img = pygame.image.load(sprite).convert_alpha()
        else:
                sprite_img = sprite

        screen.blit(sprite_img, (x, y))

def render(clock):
        clock.tick(constants.FPS)
        pygame.display.flip()

def combine(screen, sprite_location_d):
        for path in sprite_location_d:
                img = pygame.image.load(path).convert_alpha()
                screen.blit(img, sprite_location_d[path])

def bg_loop(display, d_x, d_y):

        bg = pygame.image.load(sprite_constants.BG_1).convert()
        bg_width = bg.get_width()
        bg_height = bg.get_height()

        # plus one for smoothing loop
        panels_x = math.ceil(constants.RESOLUTION[0]/bg_width) + constants.SPACE_X["PANEL_NUM"] + 1
        panels_y = math.ceil(constants.RESOLUTION[1]/bg_height) + constants.SPACE_Y["PANEL_NUM"] + 1

        display.scroll_x += constants.SHIP_TURN_SPEED * d_x
        display.scroll_y += constants.SHIP_TURN_SPEED * d_y

        # Checks for location of player to loop back around to other side of "space"
                
        right_bound = -1 * bg_width * (constants.SPACE_X["PANEL_NUM"]) - 1
        left_bound = 0
        station_x = bg_width/2

        up_bound = -1 * bg_height * (constants.SPACE_Y["PANEL_NUM"]) - 1
        down_bound = 0
        station_y = bg_height/2

        if display.scroll_x < right_bound:
                # Right loop
                display.scroll_x = left_bound

        elif display.scroll_x > left_bound:
                # Left loop
                display.scroll_x = right_bound
                #station_x = right_bound
        
        if display.scroll_y < up_bound:
                # Up loop
                display.scroll_y = down_bound
        
        elif display.scroll_y > down_bound:
                 # Down loop
                 display.scroll_y = up_bound
                 #station_y = up_bound
        

        
        FONT = pygame.font.Font(None, 36)

        for x_panel in range(panels_x):
                new_x = x_panel * bg_width + display.scroll_x - bg_width
                for y_panel in (range(panels_y)):
                        new_y = y_panel * bg_height + display.scroll_y - bg_height
                        
                        display.screen.blit(bg,(new_x, new_y))

                        text = FONT.render(str(x_panel), True, (0, 255, 0))
                        display.screen.blit(text,(new_x + 600, new_y+ 600))

                        smooth_panel_x = constants.SPACE_X["STATION"]
                        smooth_panel_y = constants.SPACE_Y["STATION"]

                        if x_panel % constants.SPACE_X["PANEL_NUM"] == smooth_panel_x and y_panel % constants.SPACE_Y["PANEL_NUM"] == smooth_panel_y:
                                setpos(display.screen, sprite_constants.STATION, new_x/constants.DELTA_TIME, new_y/constants.DELTA_TIME )
                               

def zoom(screen, obj):
        path = "temp"

        match obj.size:
                case 1:
                        path = sprite_constants.SMALL_BL_METEOR

        img = pygame.image.load(path).convert()
        new_width = img.get_width() + (obj.pos[constants.POS["Z"]]* constants.SHIP_SPEED)
        new_height = img.get_height() + (obj.pos[constants.POS["Z"]]* constants.SHIP_SPEED)

        zoomed_img = pygame.transform.scale(img, (new_width, new_height))
        setpos(screen, zoomed_img, obj.pos[constants.POS["x"]], obj.pos[constants.POS["Y"]])