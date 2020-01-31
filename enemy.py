import random
from pygame import *
from player import Player
from shot import Shot
import pyganim
import os


WIDTH = 20
HEIGHT = 32
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/mmario/r1.png' % ICON_DIR),
                   ('%s/mmario/r2.png' % ICON_DIR),
                   ('%s/mmario/r3.png' % ICON_DIR),
                   ('%s/mmario/r4.png' % ICON_DIR),
                   ('%s/mmario/r5.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/mmario/l1.png' % ICON_DIR),
                  ('%s/mmario/l2.png' % ICON_DIR),
                  ('%s/mmario/l3.png' % ICON_DIR),
                  ('%s/mmario/l4.png' % ICON_DIR),
                  ('%s/mmario/l5.png' % ICON_DIR)]
ANIMATION_JUMP_LEFT = [('%s/mmario/jl.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/mmario/jr.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/mmario/j.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/mmario/0.png' % ICON_DIR, 0.1)]


class Enemy(Player):
    def __init__(self, x, y, xp=None, hp=None):
        sprite.Sprite.__init__(self)
        Player.__init__(self, x, y)
        self.speed = random.randint(1, 3)
        self.alarm = False
        self.right = True
        self.left = False
        self.hp = 10
        self.xp = xp
        self.dead_count = 10
        self.shoot_count = 30
        self.is_alive = True
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

    def collide(self, xvel, yvel, platforms, stairs, up, down):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0

    def rule_enemy(self, hero):
        right, left, up = False, False, False
        hx, hy = hero.rect.center
        ex, ey = self.rect.center
        if hx > ex:
            right = True
        elif hx < ex:
            left = True
        else:
            left = False
            right = False
        if hy < ey:
            up = True
        return left, right, up

    def patrol(self):
        x1, x2, *_ = self.xp
        if self.rect.centerx < x1:
            self.right = True
            self.left = False
        if self.rect.centerx > x2:
            self.left = True
            self.right = False
        return self.left, self.right

    def can_see(self, hero):
        if not self.alarm:
            if abs(self.rect.centerx - hero.rect.centerx) < 600 and abs(self.rect.centery - hero.rect.centery) < 5:
                self.alarm = True
        else:
            if abs(self.rect.centerx - hero.rect.centerx) > 400:
                self.alarm = False
