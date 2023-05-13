import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILEZISE, TILEZISE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
<<<<<<< Updated upstream
        self.rect = self.image.get_rect(topleft=pos)
=======
        if sprite_type == "object":
            self.rect = self.image.get_rect(
                topleft=(pos[0], pos[1] - TILEZISE))
        else:
            self.rect = self.image.get_rect(topleft=pos)
>>>>>>> Stashed changes
        self.hitbox = self.rect.inflate(0, 10)
