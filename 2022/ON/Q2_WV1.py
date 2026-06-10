class Card:
    def __init__(self,pnum,pcol):
        self.Number=pnum
        self.Colour=pcol
    def GetNumber(self):
        return self.Number
    def GetColour(self):
        return self.Colour
class Hand:
    def __init__(self,card1,card2,card3,card4,card5):
        self.Firstcard=0
        self.Numbercard=5
        self.Cards=[]
        self.Cards.append(card1)
        self.Cards.append(card2)
        self.Cards.append(card3)
        self.Cards.append(card4)
        self.Cards.append(card5)
    def GetCard(self,cardNum):
        return self.Cards[cardNum]


#Main
FirstRed = Card(1, "red")
SecondRed = Card(2, "red")
ThirdRed = Card(3, "red")
FourthRed = Card(4, "red")

FirstBlue = Card(1, "blue")
SecondBlue = Card(2, "blue")
ThirdBlue = Card(3, "blue")
FourthBlue = Card(4, "blue")

FirstYellow = Card(1, "yellow")
SecondYellow = Card(2, "yellow")
ThirdYellow = Card(3, "yellow")
FourthYellow = Card(4, "yellow")
FifthYellow = Card(5, "yellow")

Player1=Hand(FirstRed, SecondRed, ThirdRed, FourthRed, FirstYellow)
Player2=Hand(SecondYellow, ThirdYellow, FourthYellow, FifthYellow, FirstBlue)
def CalculateValue(Player):
    score=0
    for i in range(0,4):
        playercard=Player.GetCard(i)
        score+=playercard.GetNumber()
        Colour=playercard.GetColour()
        if Colour== "red":
            score+=5
        elif Colour== "blue":
            score+=10
        else:
            score+=15
    return score

Player1Score=CalculateValue(Player1)
Player2Score=CalculateValue(Player2)
if Player1Score > Player2Score:
    print("Player 1 wins.")
elif Player1Score < Player2Score:
    print("Player 2 wins.")
else:
    print("It is a draw.")