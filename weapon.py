from pygame import *


class Weapon(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.rect = Rect(0, 0, 10, 10)
        self.image = image.load('blocks/platform.png')
        self.sound = mixer.Sound('sounds/03038.ogg')
        self.hit = 0
        self.max_ammo = 0
        self.ammo = self.max_ammo
        self.weight = 0
        self.bullet_num = 1
        self.direction = True
        self.flip_flag = False

    def shoot(self):
        self.ammo -= 1

    def reload(self):
        self.ammo = self.max_ammo


class Pistol(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.image = image.load('sprites/pistol.png')
        self.image.set_colorkey((255, 255, 255))
        self.hit = 5
        self.max_ammo = 7
        self.weight = 1
        self.reload()


class Shotgun(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.image = image.load('sprites/sg.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.hit = 3
        self.max_ammo = 5
        self.weight = 5
        self.bullet_num = 12
        self.reload()


class Ak47(Weapon):
    def __init__(self):
        Weapon.__init__(self)
        self.image = image.load('sprites/mp1.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.hit = 7
        self.max_ammo = 30
        self.weight = 5
        self.ammo = self.max_ammo
        self.reload()
