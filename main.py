# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame as pg
import constants as con

def main():
    pg.init()
    screen = pg.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0
    H = 0
    while H == 0:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.Surface.fill(screen, color = "black", rect = None)
        pg.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000





if __name__ == "__main__":
    main()
