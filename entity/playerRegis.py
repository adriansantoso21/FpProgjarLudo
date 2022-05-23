class PlayerRegis:
    def __init__(self, colorInactive, colorActive, nameRect, emailRect, title, titlePosition, iconLogo, iconPosition):
        self.colorInactive = colorInactive
        self.colorActive = colorActive
        self.nameColor = colorInactive
        self.emailColor = colorInactive
        self.nameActive = False
        self.emailActive = False
        self.name = ""
        self.email = ""
        self.nameRect = nameRect
        self.emailRect = emailRect
        self.title = title
        self.titlePosition = titlePosition
        self.iconLogo = iconLogo
        self.iconPosition = iconPosition