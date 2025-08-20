
from globalVar import *

class PlayerHealth(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        # Location
        self.originalX = 150
        self.x = self.originalX
        self.y = 650
        # Size
        self.totalSize = 200
        self.sizeX = self.totalSize
        self.sizeY = 40
        self.percentHP = 100
        # Creating Object
        self.type = type
        self.color = None
        self.image = pygame.Surface([self.sizeX, self.sizeY])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        PlayerHealth.defineHealthbar(self)

    def defineHealthbar(self):
        # Green Healthbar
        if self.type == 1:
            self.color = GREEN
            self.image.fill(self.color)
        # Red Healthbar
        if self.type == 2:
            self.color = RED
            self.image.fill(self.color)

    def setHealthbar(self, playerHP, playerTotalHP):
        if self.type == 1:
            self.percentHP = (playerHP / playerTotalHP)
        if self.type == 2:
            self.percentHP = 1 - (playerHP / playerTotalHP)

    def manageHealthbar(self):
        self.sizeX = self.percentHP * self.totalSize
        if self.type == 1:
            self.x = self.originalX - ((self.totalSize - self.sizeX) / 2)
        if self.type == 2:
            self.x = self.originalX - ((self.sizeX - self.totalSize) / 2)

        if self.sizeX <= self.totalSize:
            self.image = pygame.Surface([self.sizeX, self.sizeY])
            self.image.fill(self.color)

    def update(self):
        PlayerHealth.manageHealthbar(self)
        self.rect = self.image.get_rect(center=(self.x, self.y))