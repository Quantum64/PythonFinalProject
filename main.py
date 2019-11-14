import pygame
from pygame.locals import *


class Game:
    width = 640
    height = 400

    def __init__(self):
        self.running = True
        self.display = None
        self.size = (self.width, self.height)

    def load(self):
        pygame.init()
        pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True

    def start(self):
        self.load()
        while self.running:
            for event in pygame.event.get():
                self.event(event)
            self.tick()
            self.render()
        self.exit()

    def render(self):
        pass

    def tick(self):
        pass

    def event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            return

    def exit(self):
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.start()
