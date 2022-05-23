from entity.playerGame import PlayerGame
from data.pawnData import player1Pawns, player2Pawns, player3Pawns, player4Pawns

player1 = PlayerGame(
    "player1",
    (65, 650),
    "player1@gmail.com",
    "../asset/img/playerIcon/icon1.png",
    (25, 480),
    (85, 430),
    player1Pawns
)
player2 = PlayerGame(
    "player2",
    (65, 25),
    "player2@gmail.com",
    "../asset/img/playerIcon/icon2.png",
    (25, 40),
    (85, 205),
    player2Pawns
)
player3 = PlayerGame(
    "player3",
    (860, 25),
    "player3@gmail.com",
    "../asset/img/playerIcon/icon3.png",
    (820, 40),
    (880, 205),
    player3Pawns
)
player4 = PlayerGame(
    "player4",
    (860, 650),
    "player4@gmail.com",
    "../asset/img/playerIcon/icon4.png",
    (820, 480),
    (880, 430),
    player4Pawns
)
playersGame = [player1, player2, player3, player4]