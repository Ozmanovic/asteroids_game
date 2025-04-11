
from circleshape import *
from constants import *
from main import *






class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        
        

    def draw(self, screen):

        pygame.draw.circle(screen, "#FFFFFF", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt