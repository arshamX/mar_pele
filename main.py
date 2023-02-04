from random import randint as rand
from os import system

class Player:
    def __init__(self,name):
        self.Name = name
        self.Ispalying = False
        self.Block = "Out"
    def Dice_rool(self) -> int:
        return rand(1,6)
    
    def Move(self,dice:int,board:dict):
        self.Block += dice
        if self.Block > 100:
            self.Block = 200 - self.Block 
        positaion = board[self.Block]
        while positaion != "R":
            if positaion == "S":
                self.Block //=2
                positaion = board[self.Block]
            elif positaion == "L":
                self.Block += 6
                positaion = board[self.Block]
            


        


class Board:
    Blocks = dict()
    Snakes = list()
    Ladders = list()
    def FillBorad(self):
        for i in range(1,101):
            if i in self.Snakes:
                self.Blocks[i] = "S"
            elif i in self.Ladders:
                self.Blocks[i] = "L"
            else :
                self.Blocks[i] = "R"
    def PrintBoard(self):
        x = 0
        for i in self.Blocks.keys():
            print(f"{i}:{self.Blocks[i]}",end="\t")
            x+=1
            if x%10 == 0:
                print("\n")

            
    def __init__(self):
        while len(self.Snakes) < 8:
            temp = rand(11,99)
            if temp not in self.Snakes:
                self.Snakes.append(temp)                
        while len(self.Ladders) < 8 :
            temp = rand(2,94)
            if (temp not in self.Snakes)and(temp not in self.Ladders):
                self.Ladders.append(temp)
        self.FillBorad()


if __name__ == "__main__":
    p1 = Player(input("Enter Player1 name :"))
    p2 = Player(input("Enter Player2 name :"))
    board =Board()
    while p1.Block != 100 and p2.Block != 100:
        roll1 = 0
        roll2 = 0
        board.PrintBoard()
        print(f"{p1.Name} Location: {p1.Block}\n")
        print(f"{p2.Name} Location: {p2.Block}\n")
        input(f"{p1.Name} is rolling press any key")
        roll1 = p1.Dice_rool()
        if p1.Ispalying == False:
            if roll1 == 6:
                p1.Ispalying =True
                p1.Block = 1
                temp = p1.Dice_rool()
                while temp == 6:
                    p1.Move(temp,board.Blocks)
                    temp = p1.Dice_rool()
                p1.Move(temp,board.Blocks)
            else:
                print(f"{p1.Name} did not get 6 maybe in net turn\n")
        else:
            while roll1 == 6:
                p1.Move(roll1,board.Blocks)
                roll1 = p1.Dice_rool()
            p1.Move(roll1,board.Blocks)
        if p1.Block == p2.Block:
            print(f"{p1.Name} attacked {p2.Name} so {p2.Name} is now out of the game.")
            p2.Ispalying = False
        

        input(f"{p2.Name} is rolling press any key")
        roll2 = p2.Dice_rool()
        if p2.Ispalying == False:
            if roll2 == 6:
                p2.Ispalying =True
                p2.Block = 1
                temp = p2.Dice_rool()
                while temp == 6:
                    p2.Move(temp,board.Blocks)
                    temp = p2.Dice_rool()
                p2.Move(temp,board.Blocks)
            else:
                print(f"{p2.Name} did not get 6 maybe in net turn\n")
        else:
            while roll2 == 6:
                p2.Move(roll1,board.Blocks)
                roll2 = p2.Dice_rool()
            p2.Move(roll2,board.Blocks)
        if p2.Block == p2.Block:
            print(f"{p2.Name} attacked {p1.Name} so {p1.Name} is now out of the game.")
            p1.Ispalying = False
    if p1.Block == 100:
        print(f"{p1.Name} is winner and {p2.Name} is in location {p2.Block}")
    else:
        print(f"{p2.Name} is winner and {p1.Name} is in location {p1.Block}")