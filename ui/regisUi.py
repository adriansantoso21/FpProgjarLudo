import pygame
from ui import gameUi
from data.playerRegisData import playersRegis
from data.playerGameData import playersGame
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
    titleFont = font.render('Enter Your Name & Email', True, textColor)
    screen.blit(titleFont, (500, 40))

def setPlayerComponent():
    for player in playersRegis:
        # set playerTitle
        font = pygame.font.Font('freesansbold.ttf', 28)
        playerTitle = font.render(player.title, True, textColor)
        screen.blit(playerTitle, player.titlePosition)

        #set playerIcon
        playerIcon = pygame.image.load(player.iconLogo)
        playerIcon = pygame.transform.scale(playerIcon, (225, 225))
        screen.blit(playerIcon, player.iconPosition)

        # set text for nameEmail
        nameText = pygame.font.Font(None, 24)
        emailText = pygame.font.Font(None, 20)
        name = nameText.render(player.name, True, textColor)
        email = emailText.render(player.email, True, textColor)

        # draw nameEmail container
        pygame.draw.rect(screen, player.nameColor, player.nameRect)
        pygame.draw.rect(screen, player.emailColor, player.emailRect)

        # draw nameText and emailText
        screen.blit(name, (player.nameRect.x + 20, player.nameRect.y + 15))
        screen.blit(email, (player.emailRect.x + 15, player.emailRect.y + 15))

    pygame.display.update()

def setSubmitButton():
    buttonColor = (232, 55, 76)
    pygame.draw.rect(screen, buttonColor, submitButton, border_radius=25)

    text = pygame.font.Font('freesansbold.ttf', 28)
    buttonText = text.render('Submit', True, textColor)
    screen.blit(buttonText, (672.5, 607.5))

    pygame.display.update()

def setPlayerGameData():
    for index, playerRegis in enumerate(playersRegis):
        playersGame[index].name = playersRegis[index].name
        playersGame[index].email = playersRegis[index].email

def main():
    #declare global variable
    global gameRunning, screen, textColor, submitButton
    gameRunning = True
    screen = pygame.display.set_mode((1450, 700))
    textColor = (255, 255, 255)
    submitButton = pygame.Rect(625, 595, 200, 50)

    while gameRunning:
        setWindow()
        setBackground()
        setTitle()
        setPlayerComponent()
        setSubmitButton()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if hit submit button
                if submitButton.collidepoint(event.pos):
                    gameRunning = False
                    setPlayerGameData()
                    gameUi.main()
                for player in playersRegis:
                    #if hit nameContainer
                    if player.nameRect.collidepoint(event.pos):
                        player.nameActive = not player.nameActive
                        player.emailActive = False
                    #if hit emailContainer
                    elif player.emailRect.collidepoint(event.pos):
                        player.emailActive = not player.emailActive
                        player.nameActive = False
                    #if not hit both nameEmail container
                    if not player.nameRect.collidepoint(event.pos) and not player.emailRect.collidepoint(event.pos):
                        player.nameActive = False
                        player.emailActive = False
                    #set nameContainer color
                    if player.nameActive: player.nameColor = player.colorActive
                    else: player.nameColor = player.colorInactive
                    #set emailContainer color
                    if player.emailActive: player.emailColor = player.colorActive
                    else: player.emailColor = player.colorInactive
            if event.type == pygame.KEYDOWN:
                for player in playersRegis:
                    if player.nameActive:
                        #if player hit backspace
                        if event.key == pygame.K_BACKSPACE:
                            player.name = player.name[:-1]
                        #concat player name
                        else:
                            player.name += event.unicode
                    elif player.emailActive:
                        # if player hit backspace
                        if event.key == pygame.K_BACKSPACE:
                            player.email = player.email[:-1]
                        # concat player name
                        else:
                            player.email += event.unicode

        pygame.display.update()