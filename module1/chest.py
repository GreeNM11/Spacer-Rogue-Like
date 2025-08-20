from globalVar import *

SMALL_CHEST_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'chest.png'))
SMALL_CHEST_HIGHLIGHT_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'highlight_chest.png'))
SMALL_CHEST_OPEN_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'open_chest.png'))

class Chest(pygame.sprite.Sprite):
    def __init__(self, x, y, t, multiplier):
        super().__init__()
        self.image = SMALL_CHEST_IMAGE
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.type = t
        self.list_of_items = []
        self.multiplier = multiplier
        self.opened = False
        self.price = 20

        self.selected = False

    def manageChest(self):
        # Sets Image for Type 1 Chest
        if not pygame.sprite.spritecollideany(self, player_group):
            self.selected = False

        if self.type == 1 and self.opened == False:
            # Sets Normal Chest Image
            if not self.selected:
                self.image = SMALL_CHEST_IMAGE
            # Highlights image if player is near it and not opened
            elif self.selected:
                self.image = SMALL_CHEST_HIGHLIGHT_IMAGE

        elif self.type == 1:
            self.image = SMALL_CHEST_OPEN_IMAGE

    def setSelected(self, touching):
        self.selected = touching
    def setOpened(self):
        self.opened = True
    def getOpened(self):
        return self.opened
    def getCost(self):
        return self.price

    def displayPosition(self):
        self.displayX = self.x - playerX[0]
        self.displayY = self.y - playerY[0]
    
    def displayPrice(self):
        x = 1

    def update(self):
        Chest.displayPosition(self)
        Chest.manageChest(self)
        Chest.displayPrice(self)
        self.rect = self.image.get_rect(center=(self.displayX, self.displayY))

