import pygame
import asteroidfield
from asteroid import Asteroid
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print( "Screen width:", SCREEN_WIDTH, 
          "\nScreen height:", SCREEN_HEIGHT)
    pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    clock = pygame.time.Clock()
    dt = 0
    asteroidfield.AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     
        updatable.update(dt)
        screen.fill("black")
        for items in drawable:
            items.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        
    

if __name__ == "__main__":
    main()
