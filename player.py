from pygame import *
from weapon import *
import pyganim
import os

MOVE_SPEED = 7
WIDTH = 20
HEIGHT = 32
COLOR = (255, 255, 255)
JUMP_POWER = 10
GRAVITY = 0.35  # Сила, которая будет тянуть нас вниз
ANIMATION_DELAY = 0.1  # скорость смены кадров
ICON_DIR = os.path.dirname(__file__)  # Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/mario/r1.png' % ICON_DIR),
                   ('%s/mario/r2.png' % ICON_DIR),
                   ('%s/mario/r3.png' % ICON_DIR),
                   ('%s/mario/r4.png' % ICON_DIR),
                   ('%s/mario/r5.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/mario/l1.png' % ICON_DIR),
                  ('%s/mario/l2.png' % ICON_DIR),
                  ('%s/mario/l3.png' % ICON_DIR),
                  ('%s/mario/l4.png' % ICON_DIR),
                  ('%s/mario/l5.png' % ICON_DIR)]
ANIMATION_JUMP_LEFT = [('%s/mario/jl.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/mario/jr.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/mario/j.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/mario/0.png' % ICON_DIR, 0.1)]
ANIMATION_CSTAY = [('%s/mario/c0.png' % ICON_DIR, 0.1)]
ANIMATION_CRIGHT = [(ICON_DIR + '/mario/cr1.png'),
                    (ICON_DIR + '/mario/cr2.png'),
                    (ICON_DIR + '/mario/cr3.png'),
                    (ICON_DIR + '/mario/cr4.png'),
                    (ICON_DIR + '/mario/cr5.png')]
ANIMATION_CLEFT = [(ICON_DIR + '/mario/cl1.png'),
                    (ICON_DIR + '/mario/cl2.png'),
                    (ICON_DIR + '/mario/cl3.png'),
                    (ICON_DIR + '/mario/cl4.png'),
                    (ICON_DIR + '/mario/cl5.png')]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость перемещения. 0 - стоять на месте
        self.startX = x  # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.wx = 7
        self.wy = 8
        self.health = 100
        self.weapon = Pistol()
        self.hide = False
        self.img_flag = True
        self.direction = True
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # На земле ли я?
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill((255, 255, 255))
        self.rect = Rect(x, y, WIDTH, HEIGHT)  # прямоугольный объект
        self.image.set_colorkey((255, 255, 255))  # делаем фон прозрачным
        #        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
        #        Анимация движения влево
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        boltAnim = []
        for anim in ANIMATION_CLEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimCLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimCLeft.play()

        boltAnim = []
        for anim in ANIMATION_CRIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimCRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimCRight.play()

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0))  # По-умолчанию, стоим

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimCStay = pyganim.PygAnimation(ANIMATION_CSTAY)
        self.boltAnimCStay.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

    def update(self, left, right, up, platforms, ctrl=False, stairs='', down=False):
        # self.weapon.image.set_colorkey((255, 255, 255))
        self.hide = ctrl
        last = self.direction
        if right:
            self.direction = True
        elif left:
            self.direction = False

        if self.direction != last:
            self.weapon.image = transform.flip(self.weapon.image, True, False)
            self.wx = 7 if self.direction else -4

        if not ctrl:
            if self.img_flag:
                self.image = Surface((WIDTH, HEIGHT))
                self.img_flag = False
            x, y = self.rect.x, self.rect.y
            self.rect = Rect(x, y, WIDTH, HEIGHT)
            if up:
                if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                    self.yvel = -JUMP_POWER
                self.image.fill(COLOR)
                self.boltAnimJump.blit(self.image, (0, 0))

            if left:
                self.xvel = -MOVE_SPEED  # Лево = x- n
                self.image.fill(COLOR)
                if up:  # для прыжка влево есть отдельная анимация
                    self.boltAnimJumpLeft.blit(self.image, (0, 0))
                else:
                    self.boltAnimLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED  # Право = x + n
                self.image.fill(COLOR)
                if up:
                    self.boltAnimJumpRight.blit(self.image, (0, 0))
                else:
                    self.boltAnimRight.blit(self.image, (0, 0))

            if not (left or right):  # стоим, когда нет указаний идти
                self.xvel = 0
                # if not up:
                #     self.image.fill(COLOR)
                #     self.boltAnimRight.blit(self.image, (0, 0))

        else:
            self.img_flag = True
            self.image = Surface((WIDTH, HEIGHT - 10))
            x, y = self.rect.x, self.rect.y
            self.rect = Rect(x, y, WIDTH, HEIGHT - 10)
            if left:
                self.xvel = -MOVE_SPEED / 2  # Лево = x- n
                self.image.fill(COLOR)
                if up:  # для прыжка влево есть отдельная анимация
                    self.boltAnimJumpLeft.blit(self.image, (0, 0))
                else:
                    self.boltAnimCLeft.blit(self.image, (0, 0))

            if right:
                self.xvel = MOVE_SPEED / 2  # Право = x + n
                self.image.fill(COLOR)
                if up:
                    self.boltAnimJumpRight.blit(self.image, (0, 0))
                else:
                    self.boltAnimCRight.blit(self.image, (0, 0))

            if not (left or right):  # стоим, когда нет указаний идти
                self.xvel = 0
                # if not up:
                #     self.image.fill(COLOR)
                #     self.boltAnimCStay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, stairs, up, down)

        self.rect.x += self.xvel  # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms, stairs, up, down)
        self.image.set_colorkey((255, 255, 255))

    def collide(self, xvel, yvel, platforms, stairs, up, down):
        for p in platforms:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.yvel = 0  # и энергия падения пропадает

                if yvel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0  # и энергия прыжка пропадает

            for s in stairs:
                if sprite.collide_rect(self, s):
                    if up:
                        # print('u')
                        self.yvel = -3
                    elif not down:
                        # print('d')
                        self.yvel = 3
                    else:
                        self.yvel = 0

    # def collide_ladder(self, stairs, up, down):
    #     for s in stairs:
    #         if sprite.collide_rect(self, s):
    #             if up:
    #                 print('u')
    #                 self.yvel = -3
    #             elif not down:
    #                 print('d')
    #                 self.yvel = 3
    #             else:
    #                 self.yvel = 0
