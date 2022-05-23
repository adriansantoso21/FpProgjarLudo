class Pawn:
    def __init__(self, xPos, yPos, type):
        self.xPos = xPos
        self.yPos = yPos
        if type == 1: self.image = "../asset/img/Pawn/bluePawn.png"
        elif type == 2: self.image = "../asset/img/Pawn/yellowPawn.png"
        elif type == 3: self.image = "../asset/img/Pawn/greenPawn.png"
        elif type == 4: self.image = "../asset/img/Pawn/redPawn.png"
        self.outFromBase = False
        self.finish = False