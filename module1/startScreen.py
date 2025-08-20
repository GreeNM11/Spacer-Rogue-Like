from module1.globalVar import *

START_BUTTON_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'start_button.png'))
QUIT_BUTTON_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'quit_button.png'))

class StartScreenButtons(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        # Button Variables
        self.image = START_BUTTON_IMAGE
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.type = type
        self.isButton = False
        self.pressed = False
        StartScreenButtons.setButton(self)

    def startButton(self):
        # Sets the Start Button
        self.x = 500
        self.y = 480
        self.image = START_BUTTON_IMAGE
        self.isButton = True

    def quitButton(self):
        # Sets the Start Button
        self.x = 500
        self.y = 580
        self.image = QUIT_BUTTON_IMAGE
        self.isButton = True

    def setButton(self):
        if self.type == 1:
            StartScreenButtons.startButton(self)
        if self.type == 2:
            StartScreenButtons.quitButton(self)

    def pressed(self):
        self.pressed = True

    def returnPressed(self):
        return self.pressed

    def update(self):
        self.rect = self.image.get_rect(center=(self.x, self.y))


