import pygame
from entity.playerRegis import PlayerRegis
pygame.init()

#blue
player1 = PlayerRegis(
    (1, 86, 213),                           #colorInactive
    (1, 61, 152),                           #colorActive
    pygame.Rect(152.5, 420, 200, 40),       #nameRect
    pygame.Rect(152.5, 480, 200, 40),       #emailRect
    "Player1",                              #title
    (205.2, 135),                           #titlePosition
    "../asset/img/playerIcon/icon1.png",    #iconLogo
    (140, 165)                              #iconPosition
)
#yellow
player2 = PlayerRegis(
    (255, 179, 34),
    (204, 133, 0),
    pygame.Rect(460, 420, 200, 40),
    pygame.Rect(460, 480, 200, 40),
    "Player2",
    (516.4, 135),
    "../asset/img/playerIcon/icon2.png",
    (450, 165)
)
#green
player3 = PlayerRegis(
    (2, 188, 111),
    (2, 100, 59),
    pygame.Rect(780, 420, 200, 40),
    pygame.Rect(780, 480, 200, 40),
    "Player3",
    (827.6, 135),
    "../asset/img/playerIcon/icon3.png",
    (765, 165)
)
#red
player4 = PlayerRegis(
    (232, 55, 76),
    (183, 21, 40),
    pygame.Rect(1090, 420, 200, 40),
    pygame.Rect(1090, 480, 200, 40),
    "Player4",
    (1138.8, 135),
    "../asset/img/playerIcon/icon4.png",
    (1080, 165)
)

playersRegis = [player1, player2, player3, player4]