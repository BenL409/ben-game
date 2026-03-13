import sys
import pygame
import asteroidfield
from asteroid import Asteroid
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from logger import log_event
from shot import Shot
from ui import draw_game_over
def main():
    pygame.init()
    game_over = False
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ben's Asteroids")
    print("Starting Ben's Asteroids with pygame version: ", pygame.version.ver)
    print( "Screen width:", SCREEN_WIDTH, 
          "\nScreen height:", SCREEN_HEIGHT)
    pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    clock = pygame.time.Clock()
    dt = 0
    asteroidfield.AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = asteroidfield.AsteroidField()
    background_image = pygame.image.load("assets/background.jpg").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if game_over and event.type == pygame.KEYDOWN:
                game_over = False
                asteroid_field.kill()
                for group in (updatable, drawable, asteroids, shots):
                    group.empty()
                player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                asteroid_field = asteroidfield.AsteroidField()
        if not game_over:         
            updatable.update(dt)
            for asteroid in asteroids:
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()
                        break
                if player.collides_with(asteroid):
                    log_event("player_hit")
                    game_over = True
            
        screen.blit(background_image, (0, 0))
        
        for items in drawable:
            items.draw(screen)
            
        if game_over:
            draw_game_over(screen)  
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        
    

if __name__ == "__main__":
    main()
