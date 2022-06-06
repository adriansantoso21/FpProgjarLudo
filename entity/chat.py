import pygame
pygame.init()
class Chat:
    def __init__(self, order, iconLogo, time, textChat):
        self.order = order
        self.iconLogo = iconLogo
        self.time = time
        self.textChat = textChat