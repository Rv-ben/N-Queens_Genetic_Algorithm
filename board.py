import random
import numpy as np
import math

class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = 0
        self.encodedBoard = []
    
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1
            self.encodedBoard.append(j)
        
        self.fitness() #Compute inital fitness

    def fitness(self):        
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit += 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit += 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit += 1
                            
    ##Compute the board fitness and reposition the queens on board
    def updateBoard(self):
        n = len(self.encodedBoard)
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = 0
        for i in range(self.n_queen):
            self.map[i][self.encodedBoard[i]] = 1
        
        self.fitness()
        
        
     #formats board to show    
    def show_board(self):
        b = self.get_map()
        l = len(b)
        print_b = ''
        for i in b:
            for j in i:
                if j == 0:
                    print_b = print_b + '- '
                else:
                    print_b = print_b + str(1)+ " "
            print_b = print_b + '\n'
        print(print_b)
        
        
    def show(self):
        self.show_board()
        print("Fitness: ",  self.get_fit())

        
    def show_hill(self):
        self.show_board()
        print("Fitness: ",  self.get_fitness())        
        
        
    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0
    
   #Sets the ecodedboard strin
    def set_encodedBoard(self,encodedBoard):
        self.encodedBoard = encodedBoard

    def get_map(self):
        return self.map
    
    # resets fitness score to 0 
    def reset_fit(self):
        self.fit = 0
              
        
    # returns fitness of board    
    def get_fitness(self):
        return self.fit 
    
    
    def get_fit(self):
        return math.comb(self.n_queen,2) - self.fit #fitness = (8 choose 2) - attacking pairs
    
    def get_encodedBoard(self):
        return self.encodedBoard
            
if __name__ == '__main__':
    test = Board(8)
    test.fitness()
    test.show()
    print(test.get_encodedBoard())
    test.set_encodedBoard([3,2,4,2,4,2,3,6])
    test.updateBoard()
    test.fitness()
    test.show()
    print(test.get_encodedBoard())