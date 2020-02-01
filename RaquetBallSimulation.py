'''Raquetball Simulation.  Chapter 12 - Python Programming: Intro to Computer Science by John Zelle
Created by: Daniel Berrones
Email: daniel.a.berrones@gmail.com
Website: http://www.danielberrones.com
'''


from random import random


class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def winsServe(self):
        return random() <= self.prob

    def increaseScore(self):
        self.score += 1

    def getScore(self):
        return self.score


class GameInProgress:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA

    def play(self):
        while not self.endOfGame():
            if self.server.winsServe():
                self.server.increaseScore()
            else:
                self.changeServer()

    def endOfGame(self):
        a,b = self.getScores()
        return a == 15 or b == 15

    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA

    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()


class GameStats:
    def __init__(self):
        self.winsA = 0
        self.winsB = 0
        self.shutsA = 0
        self.shutsB = 0

    def update(self, aGame):
        pass

    def printReport(self):
        pass

    def printLine(self, label, wins, shuts, nGames):
        pass


def printIntro():
    print("\n***************************************************************")
    print("This program simulates racquetball between two players")
    print("Each player's skill (probability) is indicated between 0 and 1")
    print("that the player will win the point when serving")
    print("***************************************************************\n")
    input("\nPress enter to continue ")


def getInputs():
    'gets probA/probA (winning percentage) from user'
    probA = int(input("ProbA: "))
    probB = int(input("ProbB: "))
    nGames = int(input("Number games: "))
    return probA, probB, nGames


def main():
    printIntro()
    probA, probB, nGames = getInputs()

    stats = GameStats()
    for i in range(nGames):
        theGame = GameInProgress(probA,probB)
        theGame.play()
        stats.update(theGame)

    stats.printReport()

if __name__ == '__main__':
    main()
