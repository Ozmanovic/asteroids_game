import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = "#000000"
    white = "#FFFFFF"
    ONOFF = True
    toim = pygame.time.Clock()
    dt = 0
    
    shot_group = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    
    
    AsteroidField.containers = (updatable_group,)
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    
    


    while ONOFF:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black) 
        delt = toim.tick(60)
        dt = delt / 1000
        
        updatable_group.update(dt)
        for asteroid in asteroid_group:
            for shot in shot_group:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    asteroid.split()

            if player.check_collisions(asteroid):
                print("Game Over!")
                sys.exit()
        for draw in drawable_group:
            draw.draw(screen)
        
        

        pygame.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")






if __name__ == "__main__":
    main()