import pygame
import constants
import math
import sprite_constants
import small_meteor

def setpos(display, sprite,x, y):
        x = x * constants.DELTA_TIME
        y = y * constants.DELTA_TIME

        # Checks if already loaded or incoming zoomed img
        if type(sprite) == str: # File path
                sprite_img = pygame.image.load(sprite).convert_alpha()
        else:
                
                sprite_img = sprite

        display.screen.blit(sprite_img, (x, y))

def render(clock):
        clock.tick(constants.FPS)
        pygame.display.flip()

def combine(screen, sprite_location_d):
        for path in sprite_location_d:
                img = pygame.image.load(path).convert_alpha()
                screen.blit(img, sprite_location_d[path])

def bg_loop(display):

        bg = pygame.image.load(sprite_constants.BG_1).convert()
        bg_width = bg.get_width()
        bg_height = bg.get_height()

        # plus one for smoothing loop
        panels_x = math.ceil(constants.RESOLUTION[0]/bg_width) + constants.SPACE_X["PANEL_NUM"] + 1
        panels_y = math.ceil(constants.RESOLUTION[1]/bg_height) + constants.SPACE_Y["PANEL_NUM"] + 1

        display.scroll_x += constants.SHIP_TURN_SPEED * display.ship.dx
        display.scroll_y += constants.SHIP_TURN_SPEED * display.ship.dy

        # Checks for location of player to loop back around to other side of "space"
                
        right_bound = -1 * bg_width * (constants.SPACE_X["PANEL_NUM"]) - 1
        left_bound = 0

        up_bound = -1 * bg_height * (constants.SPACE_Y["PANEL_NUM"]) - 1
        down_bound = 0

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
        

        

        for x_panel in range(panels_x):
                new_x = x_panel * bg_width + display.scroll_x - bg_width
                for y_panel in (range(panels_y)):
                        new_y = y_panel * bg_height + display.scroll_y - bg_height
                        
                        display.screen.blit(bg,(new_x, new_y))

                        smooth_panel_x = constants.SPACE_X["STATION"]
                        smooth_panel_y = constants.SPACE_Y["STATION"]

                        if x_panel % constants.SPACE_X["PANEL_NUM"] == smooth_panel_x and y_panel % constants.SPACE_Y["PANEL_NUM"] == smooth_panel_y:
                                display.view.append(display.station)
                                display.station.pos = [new_x/constants.DELTA_TIME, new_y/constants.DELTA_TIME, 0]

                                zoom(display, display.station, space_down= False)

                        elif display.station in display.view:
                                # Not great but time rushed
                                display.view.remove(display.station)
                    
                               

def zoom(display, obj, pos = tuple(), space_down = True):
        if len(pos) == 0:
                pos = obj.pos
        path = "temp"

        match obj.size:
                case 0:
                        path = sprite_constants.STATION
                case 1:
                        path = sprite_constants.SMALL_BL_METEOR

        img = pygame.image.load(path).convert_alpha()
        if space_down:
                pos[constants.POS["Z"]] += constants.SHIP_SPEED
                new_width = img.get_width() + pos[constants.POS["Z"]]
                new_height = img.get_height() + pos[constants.POS["Z"]]
        else:
                new_width = img.get_width()
                new_height = img.get_height()

        zoomed_img = pygame.transform.scale(img, (new_width, new_height))
        
        setpos(display, zoomed_img, pos[constants.POS["X"]], pos[constants.POS["Y"]])