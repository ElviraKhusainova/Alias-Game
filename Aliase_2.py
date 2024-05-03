import pandas as pn
import random
data = pn.read_excel('/home/elvira/Python/Aliase.xlsx', header = None)

class Player:

    def __init__(self, name, score = 0):  #you might want to handle cases where the player enters an empty name or a name with leading/trailing spaces.
        self.name = name
        self.score = score

class GreatingsAndReports():

    def GreatThePlayers(Player_1, Player_2):
        print("I'm very happy to see you today", Player_1, " and ", Player_2, "!!!")  

    def PrintGetStarted():
        print("-------------------------------------------------")
        print("           LET'S GET STARTED!!!")
        print("  PRESS 'y' TO START THE GAME OR 'n' FOR EXIT")
        print("-------------------------------------------------")

    def PrintSeeYouGreating():
        print("-----------------------")
        print("SEE YOU NEXT TIME! BYE!")
        print("-----------------------")
        

class Button:

    def StartTheGame(yesorno):    #method currently doesn't do much except returning the input. You might want to consider adding more functionality to this method. You might want to modify this method to perform some validation or additional actions before returning the input.
        return yesorno
    
    def PressToStart(press):
        return press

class Picture: 

    def PaintSleepCat():
        print("       |\      _,,,---,,_ ")
        print(" ZZzz /,`.-'`'    -.  ;-;;,_ ")
        print("     |,4-  ) )-,_. ,\ (  `'-' ")
        print("     '---''(_/--'  `-'\_)   ")

    def PaintHappyCat():
        print("  /\_/\  (")
        print(" ( ^.^ ) _)")
        print("   \"/  (")
        print(" ( | | )")
        print("(__d b__)")


class FileReader:

    def ReadTheLineAndSaveInTheListOfLines(data):
        ListOfLines = []
        for index, row in data.iterrows():
            ListOfLines.append(row.tolist())
        return ListOfLines
        
class RandomWord:

    def GiveMeTheRandomWord(Words):              #you might want to handle the case where the list is empty.
        random_word = random.choice(Words[1:])
        return random_word

Player_1 = Player(input("Hello Player_1. Enter your name please: "))
Player_2 = Player(input("Hello Player_2. Enter your name please: "))
print()
print()
FirstGreating = GreatingsAndReports.GreatThePlayers(Player_1.name, Player_2.name)
print()
print()

print()
print()
print("Would you like to play Alias? Enter y or n")

Words = FileReader.ReadTheLineAndSaveInTheListOfLines(data)
Start = Button.StartTheGame(input())
if Start == "y":          

    GetStarted = GreatingsAndReports.PrintGetStarted()
    HappyCat = Picture.PaintHappyCat()
    
       
    Press = Button.PressToStart(input("PRESS 'y' FOR A FIRST WORD OR 'n' FOR EXIT"))             #Press for a first word
    while Press == "y":
        print("-------------------------------------------------")
        print(Words[0])
        print()
        Random_Word = RandomWord.GiveMeTheRandomWord(Words)
        print(Random_Word)
        print("-------------------------------------------------")
        print("NEXT ONE? PRESS 'y' FOR THE NEXT WORD or 'n' FOR EXIT")
        Press = Button.PressToStart(input()) 
        if Press not in ["y", "n"]:
            print("Enter only 'y' or 'n'")
            Press = Button.PressToStart(input())
            break
        if Press == "n":
            break


SeeYou = GreatingsAndReports.PrintSeeYouGreating()
SleepingCat = Picture.PaintSleepCat() 








    

