from src import Character

class Player(Character):

    def __init__(self, imagePath, position, texts, font):
        Character.__init__(self, imagePath, position, texts, font)
        self.streetCread = 10
        self.lvl = 0

    def changeStreetCread(self, value):
        self.streetCread += value