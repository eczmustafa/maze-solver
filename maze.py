import math
from functools import reduce
import numpy as np
import pandas as pd
import sys


class clsPoint:
    index, x, y, prevIndex, cost, distanceToTarget = None, None, None, None, 0, 0


class maze:
    nodesOriginal = []
    nodesPuzzle = []
    waitingPoints = []
    calculatedPoints = []
    target = clsPoint()
    limitMove = 5_000

    def calculateDistanceToTarget(self, x1, y1, x2, y2):
        a = abs(x1 - x2)
        b = abs(y1 - y2)
        return math.sqrt(a**2 + b**2)

    def addToWaitingPoints(self, **d):
        point = clsPoint()
        point.y = d.get("y")
        point.x = d.get("x")
        point.index = len(self.waitingPoints) + len(self.calculatedPoints)
        point.cost = d.get("cost")
        point.prevIndex = d.get("prevIndex")
        point.distanceToTarget = self.calculateDistanceToTarget(
            point.x, point.y, self.target.x, self.target.y
        )
        self.waitingPoints.append(point)

    def readStartAndTarget(self):
        nodes = self.nodesOriginal
        # önce hedefi bul sonra, başlangıcı
        # başlangıç eklenirken hedefe uzaklık hesaplaması için önceden hedefin bilinmesi gerekli
        startX, startY = None, None
        for i in range(len(nodes)):
            for k in range(len(nodes[i])):
                if nodes[i][k] == "T":
                    self.target.y = i
                    self.target.x = k
                    # son durak
                    self.target.index = -1
                    self.target.prevIndex = -1
                    self.target.cost = -1
                if nodes[i][k] == "S":
                    startX, startY = k, i

        # başlangıcı ilk durak olarak ekle
        self.addToWaitingPoints(x=startX, y=startY, cost=0, prevIndex=None)

    def read(self, dosya):
        f = open(dosya)
        m = f.readlines()
        f.close()
        self.nodesOriginal = list(map(lambda x: list(x.replace("\n", "")), m))
        self.nodesPuzzle = self.nodesOriginal
        self.readStartAndTarget()

    def print(self, **kwd):
        st = list(map("".join, self.nodesPuzzle))
        mt = reduce(lambda x, y: x + "\n" + y, st)
        print(mt)
        if "fileName" in kwd:
            with open(kwd.get("fileName"), "w") as f:
                f.write(mt)

    def findDirections(self, point):
        x = point.x
        y = point.y

        # 4 yönü belirle
        prepending = []
        prepending.append({"y": y, "x": x - 1})  # yukarı
        prepending.append({"y": y + 1, "x": x})  # sağ
        prepending.append({"y": y - 1, "x": x})  # sol
        prepending.append({"y": y, "x": x + 1})  # aşağı

        for d in prepending:
            if self.nodesPuzzle[d["y"]][d["x"]] == " ":  # durak hesaplanmamış
                self.addToWaitingPoints(
                    x=d["x"], y=d["y"], cost=point.cost + 1, prevIndex=point.index
                )
                self.nodesPuzzle[d["y"]][d["x"]] = "O"
            elif self.target.x == d["x"] and self.target.y == d["y"]:
                self.target.prevIndex = point.index
                break
        if not point.index == 0:
            self.nodesPuzzle[point.y][point.x] = "X"

    def calculateSolutionPath(self, point: clsPoint):
        if (
            not point.index == -1 and not point.index == 0
        ):  # hedef veya başlangıç nodun kendisi değilse
            self.nodesPuzzle[point.y][point.x] = str((point.cost - 1) % 10)  # "."
        if point.prevIndex == 0:  # başlangıç noda geldi
            # labirentteki X ve O'ları temizle
            for i in range(len(self.nodesPuzzle)):
                for k in range(len(self.nodesPuzzle[i])):
                    if self.nodesPuzzle[i][k] == "X" or self.nodesPuzzle[i][k] == "O":
                        self.nodesPuzzle[i][k] = "."
        else:
            prev = next(
                filter(lambda x: x.index == point.prevIndex, self.calculatedPoints),
                None,
            )
            self.calculateSolutionPath(prev)

    def solve(self):
        move = 0

        while len(self.waitingPoints) > 0:
            point = min(self.waitingPoints, key=lambda x: x.distanceToTarget)
            self.findDirections(point)
            self.waitingPoints.remove(point)
            self.calculatedPoints.append(point)
            move += 1
            if move >= self.limitMove:
                break
            if not self.target.prevIndex == -1:  # target reached
                self.calculateSolutionPath(self.target)
                break


def main():
    m = maze()
    inputFile, outputFile = "maze.txt", "maze-solved.txt"

    if len(sys.argv) == 1:
        pass  # leave defaults
    elif len(sys.argv) == 3:
        inputFile, outputFile = (*sys.argv[1:],)
    elif len(sys.argv) == 4:
        inputFile, outputFile, m.limitMove = (*sys.argv[1:],)
        m.limitMove = int(m.limitMove)
    else:
        print("Valid usages:")
        print("maze.py")
        print("maze.py [input.txt] [output.txt]")
        print("maze.py [input.txt] [output.txt] [limit_move_count]")
        exit()

    m.read(inputFile)  # read the maze data from file
    m.print()  # print the unsolved maze to the screen
    m.solve()  # solve the maze
    m.print(fileName=outputFile)  # print the solved maze to file and screen


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print("Error: " + str(ex))
