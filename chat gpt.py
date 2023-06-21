import pygame
import random

pygame.init()

# set up game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# set up game variables
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 48)

# load game images
background_img = pygame.image.load("background.png").convert()
bird_img = pygame.image.load("bird.png").convert()
pipe_img = pygame.image.load("pipe.png").convert()  

# set up game classes
class Bird(pygame.sprite.Sprite):   
    def __init__(self):
        super().__init__()
        self.image = bird_img
        self.rect = self.image.get_rect()
        self.rect.center = (100, 300)
        self.velocity = 0
        self.gravity = 0.5 
        self.jump_force = -10
    
    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.velocity = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
    
    def jump(self):
        self.velocity = self.jump_force

class Pipe(pygame.sprite.Sprite):
    def __init__(self, direction, position):
        super().__init__()
        self.image = pygame.transform.flip(pipe_img, False, not direction)
        self.rect = self.image.get_rect()
        if direction:
            self.rect.bottomleft = position
        else:
            self.rect.topleft = position
        self.direction = direction
    
    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()

# set up game objects
all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()
bird = Bird()
all_sprites.add(bird)

# set up game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()
    
    # update game objects
    all_sprites.update()
    
    # spawn pipes
    if random.randint(0, 100) == 0:
        pipe_direction = random.choice([True, False])
        pipe_pos = (WINDOW_WIDTH, random.randint(50, WINDOW_HEIGHT - 200))
        pipe = Pipe(pipe_direction, pipe_pos)
        all_sprites.add(pipe)
        pipes.add(pipe)
    
    # check for collisions
    if pygame.sprite.spritecollide(bird, pipes, False):
        running = False
    
    # draw game objects
    window.blit(background_img, (0, 0))
    all_sprites.draw(window)
    
    # draw score
    score += 1
    score_text = font.render(str(score // 10), True, (255, 255, 255))
    window.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10, 10))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
