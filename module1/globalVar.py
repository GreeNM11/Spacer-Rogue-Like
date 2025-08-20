
import pygame
import os
import math
import random
sprites_folder = "Sprite Models"
#  Map Background
MAP_GAME_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'Map_Closed.png'))
MAP_START_IMAGE = pygame.image.load(os.path.join(sprites_folder, 'map_start.png'))
space_background = pygame.image.load(os.path.join(sprites_folder, 'space_background.jpg'))

# Global Variables

global playerX, playerY

GREEN = (0, 240, 0)
RED = (240, 0, 0)
BLACK = (0, 0, 0)

FPS = 60

difficulty = 1

# Import Number Images
number_image = "numbers"
ZERO_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'zero.png'))
ONE_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'one.png'))
TWO_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'two.png'))
THREE_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'three.png'))
FOUR_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'four.png'))
FIVE_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'five.png'))
SIX_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'six.png'))
SEVEN_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'seven.png'))
EIGHT_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'eight.png'))
NINE_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'nine.png'))

COLON_IMAGE = pygame.image.load(os.path.join(sprites_folder, number_image, 'colon.png'))

# Dimensions of Screen
WIDTH, HEIGHT = 1000, 700

# Dimensions of Map
mapX, mapY = 2000, 1400

size_one = 10
borderSize = 50
borderX_left = -450
borderX_right = 1450
borderY_top = -300
borderY_bottom = 1000

shiftX = 500
shiftY = 350

pygame.init()

# Groups
    # Non Player
nonPlayer_group = pygame.sprite.Group()
    # Player
player_group = pygame.sprite.Group()
playerList = []
playerX = [1]
playerY = [1]
    # Level
level_group = pygame.sprite.Group()
    # Enemy
enemy_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
    # Healthbars
healthbar_group = pygame.sprite.Group()
playerHealthBar_group = pygame.sprite.Group()
    # Game Objects
teleporter_group = pygame.sprite.Group()
chest_group = pygame.sprite.Group()
    # Bullets
bullet_group = pygame.sprite.Group()
enemyBullet_group = pygame.sprite.Group()
    # Numbers
timer_group = pygame.sprite.Group()
money_group = pygame.sprite.Group()
    # Buttons
startButton_group = pygame.sprite.Group()
    # Mouse
mouse_group = pygame.sprite.Group()
