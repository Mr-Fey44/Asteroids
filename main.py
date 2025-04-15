# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    #set groups
    updatedable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #all players are in these groups
    Player.containers = (updatedable, drawable)
    Asteroid.containers = (updatedable, drawable, asteroids)
    AsteroidField.containers = (updatedable)
    Shot.containers = (updatedable, drawable, shots)


    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatedable.update(dt)

        for asteroid in asteroids:
            if player.colision(asteroid):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if bullet.colision(asteroid):
                    asteroid.split()
                    bullet.kill()

        screen.fill(color = "black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000





if __name__ == "__main__":
    main()
