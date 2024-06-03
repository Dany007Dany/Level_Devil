from typing import Any
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
#RUN STATE OF PLAYER
        self.sprites_run = [pygame.image.load(f"Ninja Images/Run__00{i}.png") for i in range(10)]
        self.current_run = 0
        self.image = self.sprites_run[self.current_run]
        self.image = pygame.transform.scale(self.image, (75, 100))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
#IDLE STATE OF PLAYER
        self.sprites_idle = [pygame.image.load(f"Ninja Images/Idle__00{i}.png") for i in range(10)]
        self.current_idle = 0
        self.image = self.sprites_idle[self.current_idle]
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
#JUMP STATE OF PLAYER
        self.sprites_jump = [pygame.image.load(f"Ninja Images/Jump__00{i}.png") for i in range(10)]
        self.current_jump = 0
        self.image = self.sprites_jump[self.current_jump]
        self.image = pygame.transform.scale(self.image, (75,100))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))



#OTHER VARIABLES
        self.gravity_force = 0
        self.is_animating = False
        self.is_jumping = False
        
    
    def animate(self):
         self.is_animating = True
    def not_animate(self):
        self.is_animating = False
        self.image = self.sprites_idle[self.current_idle]
        self.image = pygame.transform.scale(self.image, (50, 100))
        
    def jump(self):
        if self.rect.y == self.pos_y:
            self.is_jumping = True
            self.gravity_force = - 15
        
    
    def apply_gravity(self):
        self.gravity_force += 1
        if self.rect.y <= self.pos_y:    
            self.rect.y += self.gravity_force
        if self.rect.y >= self.pos_y:
            self.rect.y = self.pos_y
            self.gravity_force = 0
            self.is_jumping = False
   
            

        

    def update(self):
        if self.is_animating == True:
            self.current_run += 0.3
                
            if self.current_run >= len(self.sprites_run):
                self.current_run = 0
                    
            self.image = self.sprites_run[int(self.current_run)]
            self.image = pygame.transform.scale(self.image, (75, 100))
        
        if self.is_jumping == True:
            self.current_jump += 0.1

            if self.current_jump >= len(self.sprites_run):
                self.current_jump = 0
                self.is_jumping = False

            self.image = self.sprites_jump[int(self.current_jump)]
            self.image = pygame.transform.scale(self.image, (75,100))

        
                

        
        

