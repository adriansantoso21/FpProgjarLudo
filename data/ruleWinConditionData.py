import pygame
pygame.init()
from entity.ruleWinCondition import RuleWinCondition

rule1 = RuleWinCondition(
    "Players take turns clockwise and the order of play is determined by the highest roll of the dice",     #text
    "../asset/img/rule/rule1.jpg",                                                                          #image
    (100, 157.5),                                                                                           #imagePosition
    pygame.Rect(75, 122.5, 200, 360)                                                                        #containerPosition
)

rule2 = RuleWinCondition(
    "To move a pawn from base, 6 dice result is needed",
    "../asset/img/rule/rule2.jpg",
    (375, 157.5),
    pygame.Rect(350, 122.5, 200, 360)
)

rule3 = RuleWinCondition(
    "If player get 6 dice result three times in a row, the move will be thrown to the next player",
    "../asset/img/rule/rule3.jpg",
    (650, 157.5),
    pygame.Rect(625, 122.5, 200, 360)
)

rule4 = RuleWinCondition(
    "Players must move the pawn according to the value of the dice obtained",
    "../asset/img/rule/rule4.jpg",
    (925, 157.5),
    pygame.Rect(900, 122.5, 200, 360)
)

rule5 = RuleWinCondition(
    "If the position of our pawn is occupied by the opponent's pawn, then our pawn is moved to the initial position",
    "../asset/img/rule/rule5.jpg",
    (1200, 157.5),
    pygame.Rect(1175, 122.5, 200, 360)
)

rules = [rule1, rule2, rule3, rule4, rule5]