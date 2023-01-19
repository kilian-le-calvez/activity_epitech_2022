import json

LEVELS = [
    "assets/conversations/conv_clodo.json",
    "assets/conversations/conv_titi.json",
    "assets/conversations/conv_gaston.json",
    "assets/conversations/conv_ronald.json",
    "assets/conversations/conv_maman.json",
    "assets/conversations/conv_noel.json"
]

class InfosEnemy:
    def __init__(self, name: str, description: str, winShout: str, middleShout: str, looseShout: str):
        self.name = name
        self.description = description
        self.winShout = winShout
        self.middleShout = middleShout
        self.looseShout = looseShout

    def dump(self):
        print("Battle with: " + self.name)
        print("Description: " + self.description)
        print("His shouts:")
        print("- When you win: " + self.winShout)
        print("- When you middle: " + self.middleShout)
        print("- When you loose: " + self.looseShout)

class InfosResponse:
    def __init__(self, response: object):
        self.sentence = response["Sentence"]
        self.value = response["Value"]
    
    def dump(self):
        print("You say: " + self.sentence + ", you ", end="")
        if self.value > 0:
            print("win ", self.value, " points !")
        elif self.value < 0:
            print("loose ", self.value, " points...")
        else:
            print("stagnates with ", self.value, " points.")
        
class InfosTurn:
    def __init__(self, punch: str):
        self.punch = punch
        self.responses = []
    
    def setResponses(self, responses: list):
        for response in responses:
            newResponse = InfosResponse(response)
            self.responses.append(newResponse)
    
    def dump(self):
        for response in self.responses:
            response.dump()
            print("---")

class InfosBattle:
    def __init__(self):
        self.status = False
        self.turns = []

    def setEnemyInfos(self, infos):
        name = infos["Name"]
        description = infos["Description"]
        looseShout = infos["LooseShout"]
        middleShout = infos["MiddleShout"]
        winShout = infos["WinShout"]
        self.enemy = InfosEnemy(name, description, looseShout, middleShout, winShout)

    def setTurnsInfos(self, turns):
        for turn in turns:
            punch = turn["Punch"]
            oneTurn = InfosTurn(punch)
            listResponses = []
            responses = turn["Responses"]
            for response in responses:
                listResponses.append(response)
            oneTurn.setResponses(listResponses)
            self.turns.append(oneTurn)

    def loadJson(self, levelNumber: int):
        file = LEVELS[levelNumber]
        f = open(file)
        data = json.load(f)

        enemyInfos = data["Enemy"]
        turnsInfos = data["Turns"]
        self.setEnemyInfos(enemyInfos)
        self.setTurnsInfos(turnsInfos)

    def dump(self):
        self.enemy.dump()
        print()
        i = 1
        for turn in self.turns:
            print("[Turn ", i, " !]")
            print("He says: " + turn.punch)
            print()
            turn.dump()
            print()
            i += 1


# sample test

# infosBt = InfosBattle()
# infosBt.loadJson(0)
# infosBt.dump()