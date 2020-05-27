'''Raquetball Simulation.  Chapter 12 - Python Programming: Intro to Computer Science by John Zelle
Created by: Daniel Berrones
Email: daniel.a.berrones@gmail.com
Website: http://www.danielberrones.com
'''

from random import random
#from websocket._http import proxy_info


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
        # print(a == 15 or b == 15) or (a == 7 and b == 0) or (b==7 and a==0)

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
        self.shutOutsA = 0
        self.shutOutsB = 0

    def update(self, aGame):
        a, b = aGame.getScores()
        if a > b:
            self.winsA += 1
            if b == 0:
                self.shutOutsA += 1
        else:
            self.winsB += 1
            if a == 0:
                self.shutOutsB += 1

    def printReport(self):
        n = self.winsA + self.winsB
        print("Player A won",self.winsA,"time(s).")
        print("Player B won",self.winsB,"time(s).")


def printIntro():
    print("\n***************************************************************")
    print("This program simulates racquetball between two players")
    print("Each player's skill (probability) is indicated between 0 and 1")
    print("that the player will win the point when serving")
    print("***************************************************************\n")
    input("\nPress enter to continue ")


def getInputs():
    'gets probA/probA (winning percentage) from user'
    a = float(input("ProbA: "))
    b = float(input("ProbB: "))
    n = int(input("Number games: "))
    return a, b, n


def main():
    printIntro()
    probA, probB, nGames = getInputs()

    stats = GameStats()
    print(stats.shutOutsA)
    #for i in range(nGames):
    #    theGame = GameInProgress(probA,probB)
    #    theGame.play()
    #    stats.update(theGame)

    stats.printReport()


if __name__ == '__main__':
    main()
