from circleshape import *
from constants import *
from main import *
import random




class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)
        

    def draw(self, screen):

        pygame.draw.circle(screen, "#FFFFFF", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(angle)
            vec2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            mini_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            mini_asteroid1.velocity = vec1 * 1.2
            mini_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            mini_asteroid2.velocity = vec2 * 1.2




       
            
                   