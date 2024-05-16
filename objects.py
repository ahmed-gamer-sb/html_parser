import pygame as pg

pg.init()

font = pg.font.Font(None, 30)


class ImgNode:
    def __init__(self):
        self.pos = [0, 0]
        self.name = "Begin"
        self.img = None
        self.rect = None
        self.padding = 10
        self.margin = 30
        self.width = None
        self.height = None
        self.parent = None
        self.childreen = []
        self.parent_point = [600, 0]
        self.childreen_point = [0, 0]

    def display(self, tabs=0):
        if self.name != "Start":
            print(
                tabs * "\t" + f"{self.name}: {self.pos}: {self.width, self.height};",
                end="\n",
            )
            tabs += 1
        for child in self.childreen:
            child.display(tabs)

    def space_out(self):
        pass

    def create(self, pos=(150, 150), head=False):
        self.img = font.render(self.name, True, (0, 0, 0), (255, 255, 255))
        self.rect = self.img.get_rect()
        self.width = self.img.get_width()
        self.height = self.img.get_height()

        if head:
            self.pos = [150, 150]
        else:
            self.pos[1] += (
                self.parent.pos[1] + self.parent.height + self.padding + self.margin
            )

        self.childreen_point = [
            self.pos[0] + self.width // 2,
            self.pos[1] + self.height,
        ]

        if not head:
            self.parent_point = self.pos

        self.rect.topleft = self.pos

        for x in range(int(len(self.childreen) // 2), len(self.childreen)):
            child = self.childreen[x]
            child.pos[0] = self.pos[0] + x * (self.width + self.margin + self.padding)

        for x in range(int(len(self.childreen) // 2)):
            child = self.childreen[x]
            child.pos[0] = self.pos[0] - (x + 1) * (self.width + self.padding)

        for child in self.childreen:
            child.create()

    def render(self, screen, head=False):
        if head:
            pg.draw.rect(
                screen, (255, 255, 255), self.rect.inflate(20, 20), border_radius=4
            )
            screen.blit(self.img, self.rect)
        else:
            pg.draw.rect(
                screen, (255, 255, 255), self.rect.inflate(20, 20), border_radius=4
            )
            screen.blit(self.img, self.rect)
            pg.draw.line(
                screen, (255, 0, 0), self.parent_point, self.parent.childreen_point, 3
            )

        for child in self.childreen:
            child.render(screen)

    def make_rel(self, parent, hnode):
        self.parent.childreen.append(self)
        self.parent = parent
        self.pos = list(parent.pos)
        self.pos[1] += self.margin + self.height + self.padding


class ImgTree:
    def __init__(self, head=None, pos=(150, 150)):
        self.head = head
        self.pos = list(pos)

    def create(self):
        self.head.create(pos=self.pos, head=True)

    def display(self):
        self.head.display()

    def render(self, screen):
        self.head.render(screen, head=True)
