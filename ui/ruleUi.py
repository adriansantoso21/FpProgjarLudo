import pygame
from data.ruleWinConditionData import rules, winConditions
pygame.init()

def setWindow():
    pygame.display.set_caption("Ludo Board Game")
    iconLogo = pygame.image.load("../asset/img/gameIcon.jpg")
    pygame.display.set_icon(iconLogo)

def setBackground():
    background = pygame.image.load("../asset/img/gameBg.jpg")
    background = pygame.transform.scale(background, (1450, 700))
    screen.blit(background, (0,0))

def setTitle():
    font = pygame.font.Font('freesansbold.ttf', 36)
    titleFont = font.render('How to Play', True, (255, 255, 255))
    screen.blit(titleFont, (622, 40))

def setRule():
    for rule in rules:
        #draw the container
        containerColor = (62, 49, 40)
        pygame.draw.rect(screen, containerColor, rule.container, border_radius=15)
        #draw image
        ruleImage = pygame.image.load(rule.image)
        ruleImage = pygame.transform.scale(ruleImage, (150, 150))
        screen.blit(ruleImage, rule.imagePosition)
        #draw text
        words = rule.text.split()
        tempLength = 0
        tempWords = ""
        yIncrement = 165

        for word in words:
            font = pygame.font.Font('freesansbold.ttf', 16)
            word_width, word_height = font.size(word)
            tempLength += word_width
            tempWords = tempWords + word + " "
            if tempLength > 105:
                ruletext = font.render(tempWords, True, textColor)
                screen.blit(ruletext, (rule.imagePosition[0] - 5, rule.imagePosition[1] +yIncrement))
                yIncrement += 20
                tempWords = ""
                tempLength = 0

def main():
    global gameRunning, screen, textColor
    gameRunning = True
    screen = pygame.display.set_mode((1450, 700))
    textColor = (255, 179, 34)

    while gameRunning:
        setWindow()
        setBackground()
        setTitle()
        setRule()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False

        pygame.display.update()