import pygame
from entity.playerRegis import PlayerRegis
pygame.init()

#blue
player1 = PlayerRegis(
    (1, 86, 213),                           #colorInactive
    (1, 61, 152),                           #colorActive
    "Player1",                              #title
    "./asset/img/playerIcon/icon1.png"     #iconLogo
)
#yellow
player2 = PlayerRegis(
    (255, 179, 34),
    (204, 133, 0),
    "Player2",
    "./asset/img/playerIcon/icon2.png"
)
#green
player3 = PlayerRegis(
    (2, 188, 111),
    (2, 100, 59),
    "Player3",
    "./asset/img/playerIcon/icon3.png"
)
#red
player4 = PlayerRegis(
    (232, 55, 76),
    (183, 21, 40),
    "Player4",
    "./asset/img/playerIcon/icon4.png"
)

playersRegis = [player1, player2, player3, player4]