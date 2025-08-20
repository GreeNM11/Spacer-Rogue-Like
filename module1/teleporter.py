from globalVar import *
from player import *

TELEPORTER_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'teleporter.png'))
OUTLINE_TELEPORTER_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'highlight_teleporter.png'))
ACTIVE_TELEPORTER_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'active_teleporter.png'))

class Teleporter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = TELEPORTER_IMAGE
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.teleporterPressed = False
        self.teleporterActive = False
        self.startTele = False
        self.endTele = True
        self.playerTouching = False

    def setTeleporterLocation(self):
        # Sets X and Y a Random Location Within Borders
        sizeX, sizeY = self.image.get_size()
        self.x = random.randint(borderX_left, borderX_right) + shiftX
        self.y = random.randint(borderY_top, borderY_bottom) + shiftY

    def teleporterInteract(self):
        if pygame.sprite.spritecollideany(self, player_group) and self.teleporterActive == False:
            keys_pressed = pygame.key.get_pressed()
            # Teleporter Glows If Player is Touching It
            Player.setTouchingTeleporter(playerList[0], True)
            self.image = OUTLINE_TELEPORTER_IMAGE
            # If 'e' Is Pressed Next to Teleporter, Event Starts
            if keys_pressed[pygame.K_e]:
                self.teleporterPressed = True
                print("Activated Teleporter")
        # If Boss is Alive Change Image
        elif self.teleporterActive == True:
            self.image = ACTIVE_TELEPORTER_IMAGE
        # Not Touching
        else:
            self.image = TELEPORTER_IMAGE

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getPressed(self):
        return self.teleporterPressed
    def setPressedFalse(self):
        self.teleporterPressed = False
    def setTeleporterActive(self, x):
        self.teleporterActive = x

    def displayPosition(self):
        self.displayX = self.x - playerX[0]
        self.displayY = self.y - playerY[0]

    def update(self):
        Teleporter.displayPosition(self)
        Teleporter.teleporterInteract(self)
        self.rect = self.image.get_rect(center=(self.displayX, self.displayY))
