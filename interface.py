import pygame

rect_w = 200
rect_h = 100


def draw_params(screen, hero, w, h):
    font = pygame.font.SysFont('None', 100)
    ammo = hero.weapon.ammo
    health = hero.health
    x = w - rect_w
    y = h - rect_h
    # print(ammo)
    pygame.draw.rect(screen, (0, 0, 100), (x, y, w, h))
    am = font.render(str(ammo), 5, (255, 255, 255))
    heal = font.render('F', 5, (255, 255, 255))
    screen.blit(am, (x + 10, y + 10))


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
