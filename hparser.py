import sys

import pygame as pg

from settings import *
from objects import ImgTree, ImgNode
from util import Parser
from tree import Tree


class Render:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()

        self.html_tree = self.get_htree()
        self.img_tree = ImgTree(self.html_tree.copy_structure(ImgNode))
        self.img_tree.create()
        self.img_tree.display()

    def get_htree(self):
        my_parser = Parser()
        my_parser.parse(my_parser.get_html(sys.argv[1]))
        return my_parser.html_tree

    def handle_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

    def update(self):
        pass

    def render(self):
        self.screen.fill(color="orange")
        self.img_tree.render(self.screen)
        pg.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.dt = self.clock.tick(FPS)


if __name__ == "__main__":
    Render().run()
