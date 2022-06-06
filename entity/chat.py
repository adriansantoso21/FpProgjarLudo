import pygame
pygame.init()
class Chat:
    def __init__(self, name, iconLogo, time, textChat):
        self.name = name
        self.iconLogo = iconLogo
        self.time = time
        self.textChat = textChat