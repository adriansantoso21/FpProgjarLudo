import pygame
from ui import gameUi, homeUi
from logic.client import Client
from data.playerGameData import playersGame
pygame.init()

def setWindow():
    pygame.display.set_caption("Ludo Board Game")
    iconLogo = pygame.image.load("../asset/img/gameIcon.jpg")
    pygame.display.set_icon(iconLogo)

def setBackground():
    background = pygame.image.load("../asset/img/homeBg.jpg")
    background = pygame.transform.scale(background, (1450, 700))
    screen.blit(background, (0,0))

def setTitle():
    font = pygame.font.Font('freesansbold.ttf', 36)
    titleFont = font.render('Enter Your Name & Email', True, textColor)
    screen.blit(titleFont, (500, 40))

def setPlayerComponent():
    # set playerTitle
    font = pygame.font.Font('freesansbold.ttf', 28)
    playerTitle = font.render(player.title, True, textColor)
    screen.blit(playerTitle, (677.7, 135))

    # set playerIcon
    playerIcon = pygame.image.load(player.iconLogo)
    playerIcon = pygame.transform.scale(playerIcon, (225, 225))
    screen.blit(playerIcon, (612.5, 165))

    # set text for nameEmail
    nameText = pygame.font.Font(None, 24)
    emailText = pygame.font.Font(None, 24)

    name_width, name_height = font.size(nameTemp)
    email_width, email_height = font.size(emailTemp)

    if name_width > 278:
        boundary = 1
        while True:
            name_width, name_height = font.size(nameTemp[0:boundary])
            if name_width > 278:
                break
            else:
                boundary += 1

        name = nameText.render(nameTemp[0:boundary - 1], True, textColor)
        name2 = nameText.render(nameTemp[boundary - 1:len(nameTemp)], True, textColor)
        # draw name container
        pygame.draw.rect(screen, player.nameColor, nameRect)
        # draw name text
        screen.blit(name, (nameRect.x + 20, nameRect.y + 5))
        screen.blit(name2, (nameRect.x + 20, nameRect.y + 20))

    else:
        # set placeholder
        if len(nameTemp) == 0:
            name = nameText.render("Username", True, (51, 51, 51))
        else:
            name = nameText.render(nameTemp, True, textColor)
        # draw name container
        pygame.draw.rect(screen, player.nameColor, nameRect)
        # draw text text
        screen.blit(name, (nameRect.x + 20, nameRect.y + 15))

    if email_width > 278:
        boundary = 1
        while True:
            email_width, email_height = font.size(emailTemp[0:boundary])
            if email_width > 278:
                break
            else:
                boundary += 1
        email = emailText.render(emailTemp[0:boundary - 1], True, textColor)
        email2 = emailText.render(emailTemp[boundary - 1:len(emailTemp)], True, textColor)
        # draw email container
        pygame.draw.rect(screen, player.emailColor, emailRect)
        # draw email text
        screen.blit(email, (emailRect.x + 20, emailRect.y + 5))
        screen.blit(email2, (emailRect.x + 20, emailRect.y + 20))
    else:
        # set placeholder
        if len(emailTemp) == 0:
            email = emailText.render("Email Address", True, (51, 51, 51))
        else:
            email = emailText.render(emailTemp, True, textColor)
        # draw email container
        pygame.draw.rect(screen, player.emailColor, emailRect)
        # draw email text
        screen.blit(email, (emailRect.x + 20, emailRect.y + 15))

    pygame.display.update()

def setSubmitButton():
    buttonColor = (93, 73, 60)
    pygame.draw.rect(screen, buttonColor, submitButton, border_radius=25)

    text = pygame.font.Font('freesansbold.ttf', 28)
    buttonText = text.render('Submit', True, textColor)
    screen.blit(buttonText, (672.5, 607.5))

    pygame.display.update()

def setPlayerGameData():
    client = Client()
    client.setPlayerGameData("setPlayerGameData", order, nameTemp, emailTemp)

def main():
    #declare global variable
    global gameRunning, screen, textColor, submitButton, backButton, order, playersRegis
    global player, nameTemp, emailTemp, nameRect, emailRect
    gameRunning = True
    screen = pygame.display.set_mode((1450, 700))
    textColor = (255, 255, 255)
    submitButton = pygame.Rect(625, 595, 200, 50)
    backButton = pygame.Rect(75, 40, 120, 40)
    client = Client()
    order = int(client.getOrderRegis("getOrderRegis"))
    client = Client()
    playersRegis = client.getPlayersRegisData("getPlayersRegisData")
    player = playersRegis[order]
    nameTemp = ""
    emailTemp = ""
    nameRect = pygame.Rect(625, 420, 200, 40)
    emailRect = pygame.Rect(625, 480, 200, 40)

    setWindow()
    setBackground()
    setTitle()
    setPlayerComponent()
    setSubmitButton()

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if hit submit button
                if submitButton.collidepoint(event.pos):
                    gameRunning = False
                    setPlayerGameData()
                    # gameUi.main()
                #if hit back button
                if backButton.collidepoint(event.pos):
                    gameRunning = False
                    homeUi.main()
                # if hit nameContainer
                if nameRect.collidepoint(event.pos):
                    player.nameActive = not player.nameActive
                    player.emailActive = False
                # if hit emailContainer
                elif emailRect.collidepoint(event.pos):
                    player.emailActive = not player.emailActive
                    player.nameActive = False
                # if not hit both nameEmail container
                if not nameRect.collidepoint(event.pos) and not emailRect.collidepoint(event.pos):
                    player.nameActive = False
                    player.emailActive = False
                # set nameContainer color
                if player.nameActive: player.nameColor = player.colorActive
                else: player.nameColor = player.colorInactive
                # set emailContainer color
                if player.emailActive: player.emailColor = player.colorActive
                else: player.emailColor = player.colorInactive
                # update ui
                setPlayerComponent()

            if event.type == pygame.KEYDOWN:
                if player.nameActive:
                    # if player hit backspace
                    if event.key == pygame.K_BACKSPACE: nameTemp = nameTemp[:-1]
                    # concat player name
                    else: nameTemp += event.unicode
                    #update name
                    setPlayerComponent()
                elif player.emailActive:
                    # if player hit backspace
                    if event.key == pygame.K_BACKSPACE: emailTemp = emailTemp[:-1]
                    # concat player name
                    else: emailTemp += event.unicode
                    # update email
                    setPlayerComponent()