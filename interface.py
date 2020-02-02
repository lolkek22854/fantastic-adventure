import pygame
from shot import Shot

rect_w = 200
rect_h = 100


def draw_params(screen, hero, w, h):
    font = pygame.font.SysFont('None', 100)
    ammo = hero.weapon.ammo
    health = hero.hp
    x = w - rect_w
    y = h - rect_h
    # print(ammo)
    pygame.draw.rect(screen, (0, 0, 100), (x, y, w, h))
    am = font.render(str(ammo), 5, (255, 255, 255))
    heal = font.render(str(health), 5, (255, 0, 255))
    screen.blit(am, (x + 10, y + 10))
    screen.blit(heal, (x + 100, y + 10))


def check_and_draw(e, hero, ww, wh, levelw, levelh):
    x, y = e.rect.centerx, e.rect.centery
    x1, y1 = hero.rect.centerx, hero.rect.centery
    if x1 < ww / 2:
        ww = int(ww * 1.9)
    elif x1 > levelw - ww / 2:
        ww = int(ww * 1.9)
    else:
        ww = int(ww * 1.1)
    if y1 < wh / 2:
        wh = int(wh * 1.9)
    elif y1 > levelh - wh / 2:
        wh = int(wh * 1.9)
    else:
        wh = int(wh * 1.1)
    return x in range(x1 - ww // 2, x1 + ww // 2) and y in range(y1 - wh // 2, y1 + wh // 2)


def enemy_shoot(hero, shots):
    if hero.weapon.ammo > 0 and hero.shoot_count < 0:
        x, y, = hero.rect.center
        y1 = -6
        s = True
        shoots = []
        if hero.direction:
            s = Shot((x + 100, y + y1), (x + hero.wx_l, y + y1), hero.weapon.hit)
            if hero.weapon.bullet_num != 1:
                for i in range(hero.weapon.bullet_num):
                    shoot = Shot((x + 100, y - 20 + 10 * i), (x + hero.wx_l, y + y1), hero.weapon.hit)
                    shoot.image = pygame.image.load('bullit_r.png').convert()
                    shoots.append(shoot)
            s.image = pygame.image.load('bullit_r.png').convert()
        else:
            s = Shot((x - 100, y + y1), (x + hero.wx_r, y + y1), hero.weapon.hit)
            if hero.weapon.bullet_num != 1:
                for i in range(hero.weapon.bullet_num):
                    shoots.append(Shot((x - 100, y - 20 + 10 * i), (x + hero.wx_r, y + y1), hero.weapon.hit))

        if type(s) == Shot:
            hero.weapon.shoot()
            hero.shoot_count = 50
            shots.append(s)
            if shoots != []:
                shots += shoots
            return True
        else:
            return False


def udied(WIN_HEIGHT, WIN_WIDTH, screen):
    font = pygame.font.SysFont('None', 100)
    font1 = pygame.font.SysFont('None', 40)
    udied = font.render('YOU DIED', 5, (255, 0, 0))
    text = font1.render('press any key to exit', 2, (255, 40, 30))
    cy = WIN_HEIGHT // 2
    cx = WIN_WIDTH // 2
    screen.blit(udied, (cx - 100, cy - 30))
    screen.blit(text, (cx - 10, cy + 40))
