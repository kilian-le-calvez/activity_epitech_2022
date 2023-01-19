import pygame

class Character:

    def __init__(self, imagePath, logoPath, position):
        self.sprite = pygame.image.load(imagePath)
        self.headSprite = pygame.image.load(logoPath)
        self.rect = self.sprite.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.logorect = self.headSprite.get_rect()

        self.logorect.x = position[0]
        self.logorect.y = position[1]

        self.textIndex = 0
        # self.setScale()

    def setScale(self, x = 300, y = 300):
        self.sprite = pygame.transform.scale(self.sprite, (x, y))

    def setLogoPos(self, x, y):
        self.logorect.x = x;
        self.logorect.y = y;

    def getRect(self):
        return self.sprite.get_bounding_rect()
    
    def setPosition(self, x, y):
        self.logorect.x = x
        self.logorect.y = y
        self.rect.x = x
        self.rect.y = y