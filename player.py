from typing import Any
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
#RUN STATE OF PLAYER
        self.sprites_run = [pygame.image.load(f"Ninja Images/Run__00{i}.png").convert_alpha() for i in range(10)]
        self.current_run = 0
        self.image = self.sprites_run[self.current_run]
        self.image = pygame.transform.scale(self.image, (75, 100))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
#IDLE STATE OF PLAYER
        self.sprites_idle = [pygame.image.load(f"Ninja Images/Idle__00{i}.png").convert_alpha() for i in range(10)]
        self.current_idle = 0
        self.image = self.sprites_idle[self.current_idle]
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
#JUMP STATE OF PLAYER
        self.sprites_jump = [pygame.image.load(f"Ninja Images/Jump__00{i}.png").convert_alpha() for i in range(10)]
        self.current_jump = 0
        self.image = self.sprites_jump[self.current_jump]
        self.image = pygame.transform.scale(self.image, (75,100))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
#ATTACK STATE OF PLAYER
        self.sprites_attack = [pygame.image.load(f"Ninja Images/Attack__00{i}.png").convert_alpha() for i in range(10)]
        self.current_attack = 0
        self.image = self.sprites_attack[self.current_attack]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))
#THROWING STATE OF PLAYER
        self.sprites_throwing = [pygame.image.load(f"Ninja Images/Throw__00{i}.png").convert_alpha() for i in range (10)]
        self.current_throwing = 0
        self.image = self.sprites_throwing[self.current_throwing]
        self.image = pygame.transform.scale(self.image, (80, 100))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))

#OTHER VARIABLES
        self.gravity_force = 0
        self.is_animating = False
        self.is_jumping = False
        self.is_attacking = False
        self.is_throwing = False
    
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

    def attack(self):
        self.is_attacking = True    
        
    def throw_kunai(self):
        self.is_throwing = True

    def update(self):
        if self.is_animating == True:
            self.rect.x = self.pos_x
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
        
        if self.is_attacking == True:
            self.current_attack += 0.3
            
            if self.current_attack >= len(self.sprites_attack):
                self.current_attack = 0
                self.is_attacking = False
            
            self.image = self.sprites_attack[int(self.current_attack)]
            self.image = pygame.transform.scale(self.image, (110, 110))

        if self.is_throwing == True:
            self.current_throwing += 0.3

            if self.current_throwing >= len(self.sprites_throwing):
                self.current_throwing = 0
                self.is_throwing = False

            self.image = self.sprites_throwing[int(self.current_throwing)]
            self.image = pygame.transform.scale(self.image, (80, 100))

    def init_update(self, width, height):
        self.rect.x = width // 2 - self.rect.width
        self.rect.y = height - self.rect.height * 2
        if self.is_animating == True:
            self.current_run += 0.3
                
            if self.current_run >= len(self.sprites_run):
                self.current_run = 0
                    
            self.image = self.sprites_run[int(self.current_run)]
            self.image = pygame.transform.scale(self.image, (175, 200))

            


class Kunai:
    def __init__(self, HEIGHT) -> None:
        self.h = HEIGHT
        self.angle = 0
        self.kunai_image_original = pygame.image.load("Ninja Images/Kunai.png").convert_alpha()
        self.kunai_image_original = pygame.transform.scale(self.kunai_image_original, (10, 50))
        self.kunai_image = self.kunai_image_original
        self.kunai_rect = self.kunai_image.get_rect()
        self.kunai_rect.x = 260
        self.kunai_rect.y = HEIGHT - 140
        self.is_flying = False

    def draw(self, screen):
        screen.blit(self.kunai_image, self.kunai_rect)

    def rotate(self):
        self.angle -= 10  # Adjust rotation speed as necessary
        self.kunai_image = pygame.transform.rotate(self.kunai_image_original, self.angle)
        self.kunai_rect = self.kunai_image.get_rect(center=self.kunai_rect.center)

    def fly(self):
        if self.is_flying:
            self.kunai_rect.x += 17
            self.rotate()

    def reset(self):
        self.kunai_rect.x = 260
        self.kunai_rect.y = self.h - 140
        self.is_flying = False
        self.angle = 0
        self.kunai_image = self.kunai_image_original
        self.kunai_rect = self.kunai_image.get_rect(topleft=(self.kunai_rect.x, self.kunai_rect.y))
