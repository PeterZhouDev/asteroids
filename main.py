import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()
    updatable.add(asteroid_field)


    Player.containers = (updatable, drawable)
    timer = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        log_state()
        screen.fill("black")
        dt = timer.tick(60) / 1000.0

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for sprite in drawable:
            sprite.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        # print(dt)



if __name__ == "__main__":
    main()
