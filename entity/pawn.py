import pygame
pygame.init()
class Pawn:
    def __init__(self, xBasePos, yBasePos, type):
        self.xBasePos = xBasePos
        self.yBasePos = yBasePos
        self.xCurrentPos = xBasePos
        self.yCurrentPos = yBasePos
        self.baseRect = pygame.Rect(xBasePos, yBasePos, 20, 33)
        self.currentRect = pygame.Rect(xBasePos, yBasePos, 20, 33)
        self.currentSteps = -1
        if type == 1: self.image = "../asset/img/Pawn/bluePawn.png"
        elif type == 2: self.image = "../asset/img/Pawn/yellowPawn.png"
        elif type == 3: self.image = "../asset/img/Pawn/greenPawn.png"
        elif type == 4: self.image = "../asset/img/Pawn/redPawn.png"
        self.outFromBase = False
        self.finish = False