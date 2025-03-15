import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y, PLAYER_RADIUS)

    Shot.containers = (updatable, drawable, shots)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    field = AsteroidField()

    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        dt = clock.tick(60) 
        dt /= 1000
        
        updatable.update(dt)

        for thing in asteroids:
            if thing.colliding(player):
                print(f"Game over!")
                return
            for shot in shots:
                if shot.colliding(thing):
                    shot.kill()
                    thing.kill()
                    
        for thing in drawable:
            thing.draw(screen)

if __name__ == "__main__":
    main()

