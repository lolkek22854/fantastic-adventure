import math as mmm
import pygame

COLOR = "#888888"
# proektor = pygame.image.load('proektor.png')


# proektor.set_colorkey(pygame.color.Color(COLOR))

# proektor.get_rect(bottomright=(61, 47))
# proektor_rect = proektor.get_rect(bottomright=(61, 47))


def bullet_speed(st_x, st_y, fin_x, fin_y):
    angle = mmm.atan2((fin_y - st_y), (fin_x - st_x))
    x_speed_k = mmm.cos(angle)
    y_speed_k = mmm.sin(angle)
    return x_speed_k, y_speed_k


class Shot(pygame.sprite.Sprite):
    def __init__(self, pos, npos, damage=1):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = npos
        self.damage = damage
        self.st_x, self.st_y = npos
        self.fin_x = pos[0]
        self.fin_y = pos[1]
        self.rad = 5
        self.vel = 15
        self.image = pygame.Surface((self.rad, self.rad))
        self.image = pygame.image.load('bullit_l.png').convert()
        # self.image.fill(pygame.color.Color(COLOR))
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.Rect(self.x, self.y, 5 * self.rad, 5 * self.rad)
        speed_ks = bullet_speed(self.st_x, self.st_y, self.fin_x, self.fin_y)
        self.x_speed = self.vel * speed_ks[0]
        self.y_speed = self.vel * speed_ks[1]

    def move_shot(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect = pygame.Rect(self.x, self.y, self.rad, self.rad)
        self.image.set_colorkey((0, 0, 0))

    def collide(self, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                return True

    def collide_en(self, enemies):
        for p in enemies:
            if pygame.sprite.collide_rect(self, p):
                return True, p
            else:
                return False, None
