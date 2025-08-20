from startScreen import *
from globalVar import *

MOUSE_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'mouse.png'))

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Mouse Variables
        self.image = MOUSE_IMAGE
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def clickMouse(self):
        # Checks If the Mouse Clicked on a Button
        if pygame.sprite.spritecollideany(self, startButton_group):
            b = pygame.sprite.spritecollideany(self, startButton_group)
            StartScreenButtons.pressed(b)

    def update(self):
        # Gets and Sets Mouse Coordinates
        self.x, self.y = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        # Checks Events if Mouse Clicked
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Mouse.clickMouse(self)

