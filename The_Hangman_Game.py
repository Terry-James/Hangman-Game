#Terry James/ Section 01 / Program 4 / 5-2-16 at 4:30pm

# The Hangman Game

from graphics import *
from random import *
from time import *

def DisplayWindow(window):
    Header = Image (Point(500, 80), 'Directory.gif')
    Header.draw(window)

    hangmangame = Text (Point (430, 280), "1. Hangman.txt")
    hangmangame.draw(window)
 
    text1 = Text (Point (300, 200), "Enter a file name:")
    text1.draw(window)

    Game_List = Text (Point (430, 250), "Game List:")
    Game_List.draw(window)

    entry1 = Entry (Point (430, 200), 12)
    entry1.draw(window)
    window.getMouse()
    text1.undraw()
    entry1.undraw()
    Header.undraw()
    Game_List.undraw()
    hangmangame.undraw()
    

    while (entry1.getText() != 'Hangman.txt'):
        Header = Image (Point(500, 80), 'Directory.gif')
        Header.draw(window)

        hangmangame = Text (Point (430, 280), "1. Hangman.txt")
        hangmangame.draw(window)
        
        text1 = Text (Point (300, 200), "Enter a file name")
        text1.draw(window)

        Game_List = Text (Point (430, 250), "Game List:")
        Game_List.draw(window)

        entry1 = Entry (Point (430, 200), 12)
        entry1.draw(window)
        window.getMouse()
        text1.undraw()
        entry1.undraw()
        Header.undraw()
        Game_List.undraw()
        hangmangame.undraw()
        
        

    FileName = str (entry1.getText())
    
    if (entry1.getText() == 'Hangman.txt'):
        File = open ('Directions.txt', 'r')
        Directions = File.read()
        File.close()

        D = Text (Point (400,300), Directions )
        D.draw(window)
        window.getMouse()
        D.undraw()
        
        

    wrongCharacters = 0
    rightCharacters = 0
    wrongWords = 0
    rightWords = 0

    Back = Image (Point (750,250), 'Stage0.gif')
    Back.draw(window)

    words = ExtractData ( entry1.getText())
    
    count = 0
    for i in range ( len(words)):
        CurrentWord = words[count].lower()
        

        Question_mark = Text (Point (100, 130), "?")
        Question_mark.setOutline('black')
        Question_mark.draw(window)
        square = Rectangle (Point (80,110), Point (120,145))
        square.draw(window)

        box1 = Text (Point(150,300), "A")
        box1.setSize(14)
        box1.setStyle('bold')
        box1.draw(window)
        box2 = Text (Point(170,300), "B")
        box2.setSize(14)
        box2.setStyle('bold')
        box2.draw(window)
        box3 = Text (Point(190,300), "C")
        box3.setSize(14)
        box3.setStyle('bold')
        box3.draw(window)
        box4 = Text (Point(210,300), "D")
        box4.setSize(14)
        box4.setStyle('bold')
        box4.draw (window)
        box5 = Text (Point(230,300), "E")
        box5.setSize(14)
        box5.setStyle('bold')
        box5.draw(window)
        box6 = Text (Point(250,300), "F")
        box6.setSize(14)
        box6.setStyle('bold')
        box6.draw(window)
        box7 = Text (Point(270,300), "G")
        box7.setSize(14)
        box7.setStyle('bold')
        box7.draw(window)
        box8 = Text (Point(150,330), "H")
        box8.setSize(14)
        box8.setStyle('bold')
        box8.draw(window)
        box9 = Text (Point(170,330), "I")
        box9.setSize(14)
        box9.setStyle('bold')
        box9.draw(window)
        box10 = Text (Point(190,330), "J")
        box10.setSize(14)
        box10.setStyle('bold')
        box10.draw(window)
        box11 = Text (Point(210,330), "K")
        box11.setSize(14)
        box11.setStyle('bold')
        box11.draw(window)
        box12 = Text (Point(230,330), "L")
        box12.setSize(14)
        box12.setStyle('bold')
        box12.draw(window)
        box13 = Text (Point(250,330), "M")
        box13.setSize(14)
        box13.setStyle('bold')
        box13.draw(window)
        box14 = Text (Point(270,330), "N")
        box14.setSize(14)
        box14.setStyle('bold')
        box14.draw(window)
        box15 = Text (Point(150,360), "O")
        box15.setSize(14)
        box15.setStyle('bold')
        box15.draw(window)
        box16 = Text (Point(170,360), "P")
        box16.setSize(14)
        box16.setStyle('bold')
        box16.draw(window)
        box17 = Text (Point(190,360), "Q")
        box17.setSize(14)
        box17.setStyle('bold')
        box17.draw(window)
        box18 = Text (Point(210,360), "R")
        box18.setSize(14)
        box18.setStyle('bold')
        box18.draw(window)
        box19 = Text (Point(230,360), "S")
        box19.setSize(14)
        box19.setStyle('bold')
        box19.draw(window)
        box20 = Text (Point(250,360), "T")
        box20.setSize(14)
        box20.setStyle('bold')
        box20.draw(window)
        box21 = Text (Point(270,360), "U")
        box21.setSize(14)
        box21.setStyle('bold')
        box21.draw(window)
        box22 = Text (Point(150,390), "V")
        box22.setSize(14)
        box22.setStyle('bold')
        box22.draw(window)
        box23 = Text (Point(170,390), "W")
        box23.setSize(14)
        box23.setStyle('bold')
        box23.draw(window)
        box24 = Text (Point(190,390), "X")
        box24.setSize(14)
        box24.setStyle('bold')
        box24.draw(window)
        box25 = Text (Point(210,390), "Y")
        box25.setSize(14)
        box25.setStyle('bold')
        box25.draw(window)
        box26 = Text (Point(230,390), "Z")
        box26.setSize(14)
        box26.setStyle('bold')
        box26.draw(window)

        CurrentWrongWord = 0
        HangmanStage = 0

        CoveredWord=""
        for i in range (len (CurrentWord)-1):
            CoveredWord += "_"
        
        WordText = Text (Point(200,100), CoveredWord)
        WordText.draw(window)

        character = Text (Point (200, 160), "Enter a letter or word")
        character.draw(window)
        
        characterEntry = Entry (Point (200 , 130), 12)
        characterEntry.setText ('Click ? for hint')
        characterEntry.draw(window)

        for i in range (len (CurrentWord)-1):
            Length_Word = Text (Point (200,180), "The length of the word is")
            Length_Word.draw(window)
            
            L1 = Text(Point (300, 180), (len(CurrentWord)-1))
            L1.draw(window)

        CurrentWordTry = True

        while ((CurrentWordTry ==True) and (CurrentWrongWord < 3) and (HangmanStage < 6)):
            click_mouse = window.getMouse()
            xCoord = click_mouse.getX()
            yCoord = click_mouse.getY()

            
            if ((0 <= xCoord <= 120) and (0 <= yCoord <= 145)):
                hint = Text (Point (200,210), "Your word has something to do with computers")
                hint.draw(window)
                sleep(2)
                hint.undraw()
            
            UserInput = characterEntry.getText()
            UserInput.lower()
            
            EmptyWord = WordText.getText()

            if len(UserInput)> 1:
                empty = ""
                if (UserInput in CurrentWord):
                    empty = empty + UserInput
                    rightWords += 1
                    CurrentWordTry = False
                    WordText.undraw()
                    WordText.setText(empty)
                    WordText.draw(window)
                    sleep(2)
                    WordText.undraw()
                    characterEntry.setText("")
                    
                 
                else:
                    CurrentWrongWord += 1
                    characterEntry.setText("")
                           
            else:
                UserValue = Lookup (CurrentWord, UserInput)
                if (UserValue == False):
                    HangmanStage += 1
                    wrongCharacters += 1
                    DisplayHangManStage (window, HangmanStage)
                    characterEntry.setText("")
                    if (UserInput == 'a'):
                        box1.undraw()
                        box1.setTextColor('red')
                        box1.draw(window)
                    if (UserInput == 'b'):
                        box2.undraw()
                        box2.setTextColor('red')
                        box2.draw(window)
                    if (UserInput == 'c'):
                        box3.undraw()
                        box3.setTextColor('red')
                        box3.draw(window)
                    if (UserInput == 'd'):
                        box4.undraw()
                        box4.setTextColor('red')
                        box4.draw(window)
                    if (UserInput == 'e'):
                        box5.undraw()
                        box5.setTextColor('red')
                        box5.draw(window)
                    if (UserInput == 'f'):
                        box6.undraw()
                        box6.setTextColor('red')
                        box6.draw(window)
                    if (UserInput == 'g'):
                        box7.undraw()
                        box7.setTextColor('red')
                        box7.draw(window)
                    if (UserInput == 'h'):
                        box8.undraw()
                        box8.setTextColor('red')
                        box8.draw(window)
                    if (UserInput == 'i'):
                        box9.undraw()
                        box9.setTextColor('red')
                        box9.draw(window)
                    if (UserInput == 'j'):
                        box10.undraw()
                        box10.setTextColor('red')
                        box10.draw(window)
                    if (UserInput == 'k'):
                        box11.undraw()
                        box11.setTextColor('red')
                        box11.draw(window)
                    if (UserInput == 'l'):
                        box12.undraw()
                        box12.setTextColor('red')
                        box12.draw(window)
                    if (UserInput == 'm'):
                        box13.undraw()
                        box13.setTextColor('red')
                        box13.draw(window)
                    if (UserInput == 'n'):
                        box14.undraw()
                        box14.setTextColor('red')
                        box14.draw(window)
                    if (UserInput == 'o'):
                        box15.undraw()
                        box15.setTextColor('red')
                        box15.draw(window)
                    if (UserInput == 'p'):
                        box16.undraw()
                        box16.setTextColor('red')
                        box16.draw(window)
                    if (UserInput == 'q'):
                        box17.undraw()
                        box17.setTextColor('red')
                        box17.draw(window)
                    if (UserInput == 'r'):
                        box18.undraw()
                        box18.setTextColor('red')
                        box18.draw(window)
                    if (UserInput == 's'):
                        box19.undraw()
                        box19.setTextColor('red')
                        box19.draw(window)
                    if (UserInput == 't'):
                        box20.undraw()
                        box20.setTextColor('red')
                        box20.draw(window)
                    if (UserInput == 'u'):
                        box21.undraw()
                        box21.setTextColor('red')
                        box21.draw(window)
                    if (UserInput == 'v'):
                        box22.undraw()
                        box22.setTextColor('red')
                        box22.draw(window)
                    if (UserInput == 'w'):
                        box23.undraw()
                        box23.setTextColor('red')
                        box23.draw(window)
                    if (UserInput == 'x'):
                        box24.undraw()
                        box24.setTextColor('red')
                        box24.draw(window)
                    if (UserInput == 'y'):
                        box25.undraw()
                        box25.setTextColor('red')
                        box25.draw(window)
                    if (UserInput == 'z'):
                        box26.undraw()
                        box26.setTextColor('red')
                        box26.draw(window)

                else:
                    if (characterEntry.getText() == 'a'):
                        box1.undraw()
                        box1.setTextColor('green')
                        box1.draw(window)
                    if (characterEntry.getText() == 'b'):
                        box2.undraw()
                        box2.setTextColor('green')
                        box2.draw(window)
                    if (characterEntry.getText() == 'c'):
                        box3.undraw()
                        box3.setTextColor('green')
                        box3.draw(window)
                    if (characterEntry.getText() == 'd'):
                        box4.undraw()
                        box4.setTextColor('green')
                        box4.draw(window)
                    if (characterEntry.getText() == 'e'):
                        box5.undraw()
                        box5.setTextColor('green')
                        box5.draw(window)
                    if (characterEntry.getText() == 'f'):
                        box6.undraw()
                        box6.setTextColor('green')
                        box6.draw(window)
                    if (characterEntry.getText() == 'g'):
                        box7.undraw()
                        box7.setTextColor('green')
                        box7.draw(window)
                    if (characterEntry.getText() == 'h'):
                        box8.undraw()
                        box8.setTextColor('green')
                        box8.draw(window)
                    if (characterEntry.getText() == 'i'):
                        box9.undraw()
                        box9.setTextColor('green')
                        box9.draw(window)
                    if (characterEntry.getText() == 'j'):
                        box10.undraw()
                        box10.setTextColor('green')
                        box10.draw(window)
                    if (characterEntry.getText() == 'k'):
                        box11.undraw()
                        box11.setTextColor('green')
                        box11.draw(window)
                    if (characterEntry.getText() == 'l'):
                        box12.undraw()
                        box12.setTextColor('green')
                        box12.draw(window)
                    if (characterEntry.getText() == 'm'):
                        box13.undraw()
                        box13.setTextColor('green')
                        box13.draw(window)
                    if (characterEntry.getText() == 'n'):
                        box14.undraw()
                        box14.setTextColor('green')
                        box14.draw(window)
                    if (characterEntry.getText() == 'o'):
                        box15.undraw()
                        box15.setTextColor('green')
                        box15.draw(window)
                    if (characterEntry.getText() == 'p'):
                        box16.undraw()
                        box16.setTextColor('green')
                        box16.draw(window)
                    if (characterEntry.getText() == 'q'):
                        box17.undraw()
                        box17.setTextColor('green')
                        box17.draw(window)
                    if (characterEntry.getText() == 'r'):
                        box18.undraw()
                        box18.setTextColor('green')
                        box18.draw(window)
                    if (characterEntry.getText() == 's'):
                        box19.undraw()
                        box19.setTextColor('green')
                        box19.draw(window)
                    if (characterEntry.getText() == 't'):
                        box20.undraw()
                        box20.setTextColor('green')
                        box20.draw(window)
                    if (characterEntry.getText() == 'u'):
                        box21.undraw()
                        box21.setTextColor('red')
                        box21.draw(window)
                    if (characterEntry.getText() == 'v'):
                        box22.undraw()
                        box22.setTextColor('green')
                        box22.draw(window)
                    if (characterEntry.getText() == 'w'):
                        box23.undraw()
                        box23.setTextColor('green')
                        box23.draw(window)
                    if (characterEntry.getText() == 'x'):
                        box24.undraw()
                        box24.setTextColor('green')
                        box24.draw(window)
                    if (characterEntry.getText() == 'y'):
                        box25.undraw()
                        box25.setTextColor('green')
                        box25.draw(window)
                    if (characterEntry.getText() == 'z'):
                        box26.undraw()
                        box26.setTextColor('green')
                        box26.draw(window)
                        
                    empty = ""
                    for i in range (len (EmptyWord)):
                        if (i in UserValue):
                            empty = empty + UserInput
                            rightCharacters += 1
                        else:
                            empty = empty + EmptyWord[i]
                            
                    WordText.undraw()
                    WordText.setText(empty)
                    WordText.draw(window)
                    characterEntry.setText("")
                if (EmptyWord.count("_") == 0 ):
                    WordText.undraw()
                    CurrentWordTry = False   
                    ResetImageToNothing(window)
                    characterEntry.setText("")
                if (HangmanStage==6):
                    WordText.undraw()
                    CurrentWordTry = False
                    ResetImageToNothing(window)

                    
        wrong1 = Text (Point(200, 500), "Number of Characters you got wrong is:")
        wrong1.draw(window)            
        wrong = Text (Point(380,500), wrongCharacters)
        wrong.draw(window)
        
        right1 = Text (Point (200, 550), "Number of Characters you got right is:")
        right1.draw(window)
        right = Text (Point (380, 550), rightCharacters)
        right.draw(window)
        
        WrongWord_Text = Text (Point (200, 600), "Number of wrong words entered is:")
        WrongWord_Text.draw(window)
        WrongWord1 = Text (Point(380, 600), wrongWords)
        WrongWord1.draw(window)
         
        RightWord_Text = Text (Point (200, 650), "Number of right words entered is:")
        RightWord_Text.draw(window)
        RightWord1 = Text (Point (380, 650), rightWords)
        RightWord1.draw(window)
        sleep(2)
        wrong1.undraw()
        wrong.undraw()
        right1.undraw()
        right.undraw()
        WrongWord_Text.undraw()
        WrongWord1.undraw()
        RightWord_Text.undraw()
        RightWord1.undraw()
        count += 1

        if (count > 3):
            CloseWin (window)


    return CurrentWord, UserInput  

def ExtractData( filedata):
    Words = []
    List_of_Words = open (filedata, 'r')
    AllWords = List_of_Words.readlines()
    List_of_Words.close()

    for i in range (len (AllWords)):
        ChoosenWord = AllWords[i]
        Lowercase = ChoosenWord.lower()
        Words.append(Lowercase)

    return Words

    
def Lookup (CurrentWord, UserInput):
    if (UserInput not in CurrentWord):
        character = False
        return character
    
    else:
        number = []
        for i in range (len(CurrentWord)):
            if UserInput == CurrentWord[i]:
                number.append(i)

        return number

        
def ResetImageToNothing(win):
    Stage0 = Image (Point (750,250), 'Stage0.gif')
    Stage0.draw(win)    

def DisplayHangManStage (window, Stage):
    if (Stage == 0):
        Stage0 = Image (Point (750,250), 'Stage1.gif')
        Stage0.draw(window)
        
    elif (Stage == 1):
        Stage1 = Image (Point (750,250), 'Stage1.gif')
        Stage1.draw(window)
        
    elif (Stage == 2):
        Stage2 = Image (Point (750,250), 'Stage2.gif')
        Stage2.draw(window)
        
    elif (Stage == 3):
        Stage3 = Image (Point (750,250), 'Stage3.gif')
        Stage3.draw(window)
        
    elif (Stage == 4):
        Stage4 = Image (Point (750,250), 'Stage4.gif')
        Stage4.draw(window)
        
    elif (Stage == 5):
        Stage5 = Image (Point (750,250), 'Stage5.gif')
        Stage5.draw(window)
        
    elif (Stage == 6):
        Stage6 = Image (Point (750,250), 'Stage6.gif')
        Stage6.draw(window)

def CloseWin (window):
    window.getMouse()
    window.close()

def main():
    window = GraphWin("HangMan", 1000, 1000)
    window.setBackground('gray')
    
    DisplayWindow(window)

    
main()
