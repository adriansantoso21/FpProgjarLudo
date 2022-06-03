import pygame
from data.ruleWinConditionData import rules, winConditions
from ui import homeUi
pygame.init()

def setWindow():
    pygame.display.set_caption("Ludo Board Game")
    iconLogo = pygame.image.load("./asset/img/gameIcon.jpg")
    pygame.display.set_icon(iconLogo)

def setBackground():
    background = pygame.image.load("./asset/img/gameBg.jpg")
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

def setBackButton():
    #set the container
    buttonColor = (62, 49, 40)
    pygame.draw.rect(screen, buttonColor, backButton, border_radius=25)

    #set backButton icon
    backButtonIcon = pygame.image.load("./asset/img/backButton.png")
    backButtonIcon = pygame.transform.scale(backButtonIcon, (20, 20))
    screen.blit(backButtonIcon, (90, 50))

    #set text
    text = pygame.font.Font('freesansbold.ttf', 20)
    buttonText = text.render('Back', True, (255, 255, 255))
    screen.blit(buttonText, (120, 52.5))

    pygame.display.update()

def main():
    #declare global variable
    global gameRunning, screen, textColor, backButton
    gameRunning = True
    screen = pygame.display.set_mode((1450, 700))
    textColor = (255, 179, 34)
    backButton = pygame.Rect(75, 40, 120, 40)

    setWindow()
    setBackground()
    setTitle()
    setRule()
    setBackButton()

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.collidepoint(event.pos):
                    gameRunning = False
                    homeUi.main()

        pygame.display.update()