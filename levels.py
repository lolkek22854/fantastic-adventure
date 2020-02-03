import pygame


class Cell:
    def __init__(self, x, y, size, num, on_action):
        self.x_range = range(x, x + size)
        self.y_range = range(y, y + size)
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 55, 200)
        self.num = num
        self.image = pygame.font.SysFont('None', 50).render(str(self.num), 5, self.color)

    def in_cell(self, pos, change_flag=False):
        x, y = pos
        if x in self.x_range and y in self.y_range:
            if change_flag:
                color = (255, 255, 255)
                self.image = pygame.font.SysFont('None', 50).render(str(self.num), 5, color)
            return True
        else:
            if change_flag:
                color = (255, 55, 200)
                self.image = pygame.font.SysFont('None', 50).render(str(self.num), 5, color)
            return False

    def rect(self):
        return self.x, self.y, self.size, self.size


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.board = []
        i = 0
        for y in range(self.height):
            for x in range(self.width):
                i += 1
                self.board.append(Cell(x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, i, False))

    def render(self, screen):
        for c in self.board:
            screen.blit(c.image, (c.x, c.y))


def levels(screen):
    # running = True
    board = Board(2, 6)
    # pos_move = (0, 0)
    pos_push = (-1, -1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pos_move = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_push = event.pos

    for cell in board.board:
        cell.in_cell(pos_move)
        if cell.in_cell(pos_push):
            return cell.num

    screen.fill((0, 0, 0))
    board.render(screen)
