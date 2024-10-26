import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from shot import Shot
def main():

    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    Player.containers = (drawable, updatable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        for drawables in drawable:
            drawables.draw(screen)
        dt = clock.tick(60)/1000
        for updatables in updatable:
            updatables.update(dt)
        for shot in shots:
            shot.draw(screen)
            shot.update(dt)
            for asteroid in asteroids:
                if asteroid.isColliding(shot):
                    shot.kill()
                    asteroid.split()
        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
if __name__ == "__main__":
    main()
