import random

class robot:
    name = "machine"
    game = ["pedra","paper","tisora"]

    def playing(self):
        choice = random.choice(self.game)
        return choice

class cara_creu_robot:
    name = "machine"
    game = ["cara","creu"]

    def playing(self):
        choice = random.choice(self.game)
        return choice

class tres_en_ratlla_robot:
    name = "machine"
    game1 = [["1a", "2a ", "3a"],] 
    def playing(self):
        while True:
                break
        choice = random.choice([0,1,2])
        return choice