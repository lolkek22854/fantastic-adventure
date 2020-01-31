from pygame import *
import pyganim
import os

WIDTH = 22
HEIGHT = 22
ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/mario/a1.png' % ICON_DIR),
                   ('%s/mario/a2.png' % ICON_DIR),
                   ('%s/mario/a3.png' % ICON_DIR)]


class Attack(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.frames_count = 0
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill((255, 255, 255))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image.set_colorkey((255, 255, 255))
        #        Анимация атаки вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

    def update(self, hero):
        if hero.direction:
            self.rect.x = hero.rect.x + 20
            self.rect.y = hero.rect.y
        else:
            self.rect.x = hero.rect.x - 12
            self.rect.y = hero.rect.y
        self.image = Surface((WIDTH, HEIGHT))
        self.boltAnimRight.blit(self.image, (0, 0))
        self.image.set_colorkey((255, 255, 255))
        self.frames_count += 1
