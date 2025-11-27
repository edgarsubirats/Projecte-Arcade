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