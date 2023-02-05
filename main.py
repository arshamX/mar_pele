from random import randint as rand
from os import system
import time

class Player:
    def __init__(self,name):
        self.Name = name
        self.Ispalying = False
        self.Block = "Out"  
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

class Activity:
    @staticmethod
    def Dicer_roll() -> int:
        return rand(1,6)
    @staticmethod
    def Attack(player1:Player,player2:Player) -> None:
        if player1.Block == player2.Block:
            print(f"{player1.Name} attacked {player2.Name} so {player2.Name} is now out of the game.")
            player2.Ispalying = False
            player2.Block = "Out"




        


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
            f = True
            if temp not in self.Snakes:
                for i in self.Snakes:
                    if i-1 == temp or i+1 == temp:
                        f = False
                if f :
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
        roll1 = Activity.Dicer_roll()
        print(f"rolled {roll1}")
        if p1.Ispalying == False:
            if roll1 == 6:
                p1.Ispalying =True
                p1.Block = 1
                temp = Activity.Dicer_roll()
                print(f"rolled {temp}")
                while temp == 6:
                    p1.Move(temp,board.Blocks)
                    Activity.Attack(player1=p1,player2=p2)
                    temp = Activity.Dicer_roll()
                    print(f"rolled {temp}")
                p1.Move(temp,board.Blocks)
                Activity.Attack(player1=p1,player2=p2)
            else:
                print(f"{p1.Name} did not get 6 maybe in net turn\n")
        else:
            while roll1 == 6:
                p1.Move(roll1,board.Blocks)
                Activity.Attack(player1=p1,player2=p2)
                roll1 = Activity.Dicer_roll()
                print(f"rolled {roll1}")
            p1.Move(roll1,board.Blocks)
            Activity.Attack(player1=p1,player2=p2)
        

        input(f"{p2.Name} is rolling press any key")
        roll2 = Activity.Dicer_roll()
        print(f"rolled {roll2}")
        if p2.Ispalying == False:
            if roll2 == 6:
                p2.Ispalying =True
                p2.Block = 1
                temp = Activity.Dicer_roll()
                print(f"rolled {temp}")
                while temp == 6:
                    p2.Move(temp,board.Blocks)
                    Activity.Attack(player1=p2,player2=p1)
                    temp = Activity.Dicer_roll()
                    print(f"rolled {temp}")
                p2.Move(temp,board.Blocks)
                Activity.Attack(player1=p2,player2=p1)
            else:
                print(f"{p2.Name} did not get 6 maybe in net turn\n")
        else:
            while roll2 == 6:
                p2.Move(roll1,board.Blocks)
                Activity.Attack(player1=p2,player2=p1)
                roll2 = Activity.Dicer_roll()
                print(f"rolled {roll2}")
            p2.Move(roll2,board.Blocks)
            Activity.Attack(player1=p2,player2=p1)
        time.sleep(2)
        try:
            system("cls")
        except:
            system("clear")


    if p1.Block == 100:
        print(f"{p1.Name} is winner and {p2.Name} is in location {p2.Block}")
    elif p2.Block == 100:
        print(f"{p2.Name} is winner and {p1.Name} is in location {p1.Block}")