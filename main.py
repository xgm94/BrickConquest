
import pygame
import random


class Piece:
    piece_type = 0
    piece_distribution = []
    rotation = 0
    chess_position = []

    def locate(self,position):
        self.chess_position = position
        
    def rotate(self, direction = 0):
        if direction == 1: #clockwise
            if self.rotation < 3:
                self.rotation = self.rotation +1
            else:
                self.rotation = 0
            print("rotating clockwise")
            self.transpose()
            self.invert()
            
        elif direction == 0: #counter-clockwise
            print("rotating counter clockwise")
            if self.rotation > 0:
                self.rotation = self.rotation -1
            else:
                self.rotation = 3
            self.invert()
            self.transpose()
       
    def transpose(self):
        buffer = self.listToMatrix()
        buffer_transpossed =[*map(list, zip(*buffer))]
        self.matrixToList(buffer_transpossed)
        
    def invert(self):
        buffer = self.listToMatrix()
        for row in range(3):
            buffer_value = buffer[row][0]
            buffer[row][0] = buffer[row][2]
            buffer[row][2] = buffer_value
        self.matrixToList(buffer)
    
    def listToMatrix(self):
        buffer = []
        for row in range(3):
            buffer_row = []
            for col in range(3):
                buffer_row.append(self.piece_distribution[col + (3*row)])
            buffer.append(buffer_row)
        return buffer
    def matrixToList(self,buffer):
        for row in range(3):
            for col in range(3):
                self.piece_distribution[col + (3*row)] = buffer[row][col]
                
    def __init__(self, piece_type):
        self.piece_type = piece_type
        self.piece_distribution = self.selectType(self.piece_type)
        self.rotation = 0

    def printPiece(self):
        for row in range(3):
            buffer = []
            for col in range(3):
                buffer.append(self.piece_distribution[col +(3*row)])
            print(buffer)

    def selectType(self,piece_type):
        print("selecting") 
        if 0 == piece_type: #tavern
            return [0,0,0,
                    0,1,0,
                    0,0,0]
        elif 1 == piece_type: #stable
            return[0,1,0,
                   0,1,0,
                   0,0,0]
        elif 2 == piece_type: #inn
            return [0,1,0,
                    0,1,1,
                    0,0,0]

        elif 3 == piece_type: #bridge
            return [0,1,0,
                    0,1,0,
                    0,1,0]

        elif 4 == piece_type: #square
            return [1,1,0,
                    1,1,0,
                    0,0,0]

        elif 5 == piece_type: #abbey
            return [0,1,0,
                    0,1,1,
                    0,0,1]

        elif 6 == piece_type: #manon
            return [0,1,0,
                    1,1,1,
                    0,0,0]

        elif 7 == piece_type: #tower
            return [0,0,1,
                    0,1,1,
                    1,1,0]

        elif 8 == piece_type: #infirmary
            return [0,1,0,
                    1,1,1,
                    0,1,0]

        elif 9 == piece_type: #castle
            return [1,0,1,
                    1,1,1,
                    0,0,0]
        elif 10 == piece_type: #academy
            return [0,1,0,
                    1,1,0,
                    0,1,1]
        elif 11 == piece_type: #cathedral
            return [0,1,0,
                    1,1,1,
                    0,1,1]
class Game:
    chess = []
    player_white = None
    player_red = None
    def __init__(self,player_w, player_r):
        self.chess = self.initializeChess()
        self.player_red = player_r
        self.player_white = player_w
    def initializeChess(self):
        buffer = [] 
        for row in range(10):
            buffer_row = []
            for col in range(10):
                buffer_row.append(0)
            buffer.append(buffer_row)
        return buffer

    def printChess(self):
        for row in range(len(self.chess)):
            print(self.chess[row])

                
class Player:
    player_role = 0 #0-> white / 1-> red
    initial_pieces = [0,0,1,1,2,2,3,4,5,6,7,8,9,10]
    available_pieces = []
    used_pieces = []
    def __init__(self, player_role):
        self.player_role = player_role
        self.initializePieces

    def initializePieces (self):
        for i in range(len(initial_pieces)):
            self.available_pieces.append({"piece":Piece(initial_pieces[i]),
                                          "pice_id":i,
                                          "avaiable":True,
                                          "position":[]})

    def move(piece,position):
        pass
def main():
    print("initializing")
    tower = Piece(10)
    tower.printPiece()
    tower.rotate(1)
    tower.printPiece()
    tower.rotate(1)
    tower.printPiece()
    tower.rotate(1)
    tower.printPiece()
    
    player_white = Player(0)    
    player_red = Player(1)
    game = Game(player_white, player_red)
    game.printChess()
if __name__ == "__main__":
    main()
    
