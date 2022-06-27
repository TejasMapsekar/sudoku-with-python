import numpy as np
from colorama import Fore,Back
import sys
import os

class sudoku:
    def __init__(self):
        self.reset()
        self.print_utility(self.question)
        self.control_input()

    def reset(self):
        self.sudoku = np.zeros((9,9),dtype=int)
        self.row_random = np.random.randint(0,9,size=20)
        self.col_random = np.random.randint(0,9,size=20)
        self.make_sudoku()
        self.sudoku[self.row_random,self.col_random] = 0
        self.question = self.sudoku.copy()
        if(self.solve_sudoku(0,0) == False):
            self.reset()
            

    def make_sudoku(self):
        self.sudoku[0,:] = np.random.permutation(range(1,10))
        self.sudoku[1,:] = np.roll(self.sudoku[0,:],3)
        self.sudoku[2,:] = np.roll(self.sudoku[1,:],3)
        self.sudoku[3,:] = np.roll(self.sudoku[2,:],1)
        self.sudoku[4,:] = np.roll(self.sudoku[3,:],3)
        self.sudoku[5,:] = np.roll(self.sudoku[4,:],3)
        self.sudoku[6,:] = np.roll(self.sudoku[5,:],1)
        self.sudoku[7,:] = np.roll(self.sudoku[6,:],3)
        self.sudoku[8,:] = np.roll(self.sudoku[7,:],3)
    
    def check_sudoku(self,number,sudoku,i,j):
        if number in sudoku[:,j] or number in sudoku[i,:]:
            return False
        if number in sudoku[i-i%3:i-i%3+3,j-j%3:j-j%3+3]:
            return False
        
        return True
    
    def solve_sudoku(self,row,col):
        if row == 8 and col == 9:
            return True
        elif col == 9:
            return self.solve_sudoku(row+1,0)
        elif self.sudoku[row,col] != 0:
            return self.solve_sudoku(row,col+1)
        else:
            for number in range(1,10):
                if self.check_sudoku(number,self.sudoku,row,col):
                    self.sudoku[row,col] = number
                    return self.solve_sudoku(row,col+1)
        return False
    
    def print_utility(self,toprint):
        os.system('cls')
        string = ""
        for i in range(9):
            if(i%3 == 0):
                string +='-'*28+'\n'
            for j in range(9):
                if(j%3 == 0):
                    string+='|'
                if(j%3 != 0):
                    string+=" "
                if toprint[i,j] == 0:
                    string+=Back.GREEN+' '+Back.RESET+Fore.RESET
                else:
                    string+=Fore.RED+str(toprint[i,j])+Back.RESET+Fore.RESET
                string+=" "
            string+="|"+'\n'
        string+='-'*28                 
        print(string)
        
    def control_input(self):
        key = int(input("press 1 to solve 2 to get new sudoku 3 to exit: "))
        if key == 1:
            self.solve_sudoku(0,0)
            self.print_utility(self.sudoku)
            self.control_input()
        if key == 2:
            self.reset()
            self.print_utility(self.question)
            self.control_input()
        if key == 3:
            sys.exit()
sudoku()