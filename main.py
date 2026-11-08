from handlers.display_handler  import Display_Handler
import sprite_constants

def main():
    dh = Display_Handler()
    dh.display(sprite_constants.BG_1)

if __name__ == '__main__':
    main()