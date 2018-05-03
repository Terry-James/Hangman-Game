from graphics import *
from random import *
from time import *

# Function to display created window where game is played
def DisplayWindow(window):
    mainWindow = Image (Point(500, 80), 'Directory.gif') # adds banner
    mainWindow.draw(window)

    displayGames = Text (Point (430,280), "1. Hangman.txt") # list game choices
    displayGames.draw(window)

    GameSelect(window, mainWindow, displayGames) # call input to select game

# Function for entering game to be played
def GameSelect(window, mainWin, display):
    selectGames = Text (Point (450, 250), "Enter a game to play") # Text Statement
    selectGames.draw(window)

    entryText = Entry (Point (430,200), 12) # Allow user to enter a game to play
    entryText.draw(window)
    window.getMouse()
    selectGames.undraw()
    entryText.undraw()
    mainWin.undraw()
    display.undraw()

    if (entryText.getText() != 'Hangman.txt'): # Cycle back to game selection if wrong game name is entered
        DisplayWindow(window)

    elif (entryText.getText() == 'Hangman.txt'): # Pulls the directions for the selected game entered
        File = open ('Directions.txt', 'r')
        Directions = File.read()
        File.close()

        Direct = Text (Point (400, 300), Directions)
        Direct.draw(window)
        window.getMouse()
        Direct.undraw()

        Game(window, entryText) # call game function to set up game

# Function for controlling all stats for game
def Game (window, userEnter):
    # List of Statistics for game
    wrongCharacters = 0
    rightCharacters = 0
    wrongWords = 0
    rightWords = 0
    currentWrongWord = 0
    hangmanStage = 0
    count = 0

    wordEntry = ExtractData (userEnter.getText()) # pulls words for game from file

    currentWord = ""
    coveredWord = ""

    backImage = Image (Point (750, 250), 'Stage0.gif') # set first image
    backImage.draw(window)

    # Allow player to get a clue on the current word
    Clue = Text (Point (100,130), "?")
    Clue.setOutline('black')
    Clue.draw(window)
    boxAround = Rectangle (Point (80, 110), Point (120, 145))
    boxAround.draw(window)

    wrongUsed = Text (Point (100, 475), "Wrong Letters Used")
    wrongUsed.draw(window)
    letterBox = Rectangle (Point (40, 485), Point (150, 550))
    letterBox.draw(window)

    correctUsed = Text (Point (350, 475), "Correct Letters Used")
    correctUsed.draw(window)
    letterBox = Rectangle (Point (300, 485), Point (410, 550))
    letterBox.draw(window)

    for i in range( len(wordEntry)):
        currentWord = wordEntry[count].lower() # set the words to lowercase

    DrawAlpaBoxes(window) # shows all possible letters

    for i in range (len (currentWord)-1): # covers the current word
        coveredWord += "_"

    wordText = Text (Point (200, 100), coveredWord)
    wordText.draw(window)

    enterLetter = Text (Point (200, 160), "Enter a letter or Word")
    enterLetter.draw(window)

    charEntry = Entry (Point (200, 130), 16)
    charEntry.setText('Click ? box for hint')
    charEntry.draw(window)
    sleep(2)
    charEntry.setText("")

    currentTry = True
    while ((currentTry == True) and (currentWrongWord < 3) and (hangmanStage < 6)):
        clickMouse = window.getMouse()
        xCoord = clickMouse.getX()
        yCoord = clickMouse.getY()

        if ((0 <= xCoord <= 120) and (0 <= yCoord <= 145)):
            Hint(window, currentWord) # call hint function to show hint

        userInput = charEntry.getText()
        userInput.lower()

        emptyWord = wordText.getText()

        if len(userInput) > 1:
            empty = ""
            if(userInput in currentWord):
                empty += userInput
                rightWords += 1
                currentTry = False
                wordText.undraw()
                wordText.setText(empty)
                wordText.draw(window)
                sleep(2)
                wordText.undraw()
                charEntry.setText("")

            else:
                currentWrongWord += 1
                charEntry.setText("")
        else:
            userValue = Lookup (currentWord, userInput)
            if(userValue == False):
                hangmanStage += 1
                wrongCharacters += 1
                ChangeImages(window, hangmanStage)
                charEntry.setText("")
                WrongPlayerChoice(window, userInput)
            else:
                RightPlayerChoice(window, userInput)
                empty = ""
                for j in range (len (emptyWord)):
                    if (j in userValue):
                        empty += userInput
                        rightCharacters += 1
                    else:
                        empty += emptyWord[j]
                wordText.undraw()
                wordText.setText(empty)
                wordText.draw(window)
                charEntry.setText("")
            if (emptyWord.count("_") == 0):
                wordText.undraw()
                currentWordTry = False
                ResetImage(window)
                charEntry.setText("")
                count += 1
            if (hangmanStage == 6):
                wordText.undraw()
                currentWordTry = False
                ResetImage(window)
                count += 1

        if (count > 3):
            CloseWin(window)

def Statistics(window, wrongCharacter, rightCharacter, wrongWord, rightWord):
    wrong = Text (Point(200, 500), "Number of Characters you got wrong is: " + str(wrongCharacter))
    wrong.draw(window)

    right = Text (Point (200, 550), "Number of Characters you got right is: " + str(rightCharacter))
    right.draw(window)

    WrongWord_Text = Text (Point (200, 600), "Number of wrong words entered is: " + str(wrongWord))
    WrongWord_Text.draw(window)

    RightWord_Text = Text (Point (200, 650), "Number of right words entered is: " + str(rightWord))
    RightWord_Text.draw(window)
    sleep(2)
    wrong.undraw()
    right.undraw()
    WrongWord_Text.undraw()
    RightWord_Text.undraw()


def RightPlayerChoice(window, playerInput):
    x = 320
    y = 500
    counter = 0
    Alpa = ['A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','','']
    choice = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
              'q','r','s','t','u','v','w','x','y','z','','']
    for i in range(len(choice)):
        if (playerInput == choice[i]):
            box = Text (Point (x, y), Alpa[i])
            box.setTextColor('green')
            box.draw(window)
            counter += 1
            x += 20
            if (counter % 7 == 0):
                x = 150
                y += 30

def WrongPlayerChoice(window, playerInput):
    x = 50
    y = 500
    counter = 0
    Alpa = ['A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','','']
    choice = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
              'q','r','s','t','u','v','w','x','y','z','','']
    for i in range(len(choice)):
        if (playerInput == choice[i]):
            box = Text (Point (x, y), Alpa[i])
            box.setTextColor('red')
            box.draw(window)
            counter += 1
            x += 20

            if (counter % 7 == 0):
                x = 150
                y += 30

# Function for showing hint message
def Hint (window, currentWord):
    current = len (currentWord)-1
    for i in range (current):
        lengthWord = Text (Point (200,180), "The length of the word is: " + str(current))
        lengthWord.draw(window)
        sleep(1)
        lengthWord.undraw()

# Function for drawing all letters on the window
def DrawAlpaBoxes(window):
    x = 150
    y = 300
    counter = 0
    Alpa = ['A','B','C','D','E','F','G','H','I','J','K',
            'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','','']
    for i in range (len(Alpa)):
        box = Text (Point (x, y), Alpa[counter])
        box.setSize(14)
        box.setStyle('bold')
        box.draw(window)
        counter += 1
        x += 20

        if (counter % 7 == 0):
            x = 150
            y += 30

# Function for extracting the words from a file and putting them in an array
def ExtractData(filedata):
    Words = []
    List_of_Words = open (filedata, 'r')
    allWords = List_of_Words.readlines()
    List_of_Words.close()

    for i in range (len (allWords)):
        choosenWord = allWords[i]
        lowerCase = choosenWord.lower()
        Words.append(lowerCase)

    return Words

# Function for checking if the letter or word matches a letter or word in the current word
def Lookup (currentWord, userInput):
    if(userInput not in currentWord):
        character = False
        return character
    else:
        number = []
        for i in range (len (currentWord)):
            if userInput == currentWord[i]:
                number.append(i)

        return number

# Function to reset image for a new game
def ResetImage (window):
    Stage0 = Image (Point (750,250), 'Stage0.gif')
    Stage0.draw(window)

# Function for changing the images as characters are entered wrong
def ChangeImages (window, stage):
    if (stage == 0):
        stage0 = Image (Point (750,250), 'Stage1.gif')
        stage0.draw(window)

    elif (stage == 1):
        stage1 = Image (Point (750,250), 'Stage1.gif')
        stage1.draw(window)

    elif (stage == 2):
        stage2 = Image (Point (750,250), 'Stage2.gif')
        stage2.draw(window)

    elif (stage == 3):
        stage3 = Image (Point (750,250), 'Stage3.gif')
        stage3.draw(window)

    elif (stage == 4):
        stage4 = Image (Point (750,250), 'Stage4.gif')
        stage4.draw(window)

    elif (stage == 5):
        stage5 = Image (Point (750,250), 'Stage5.gif')
        stage5.draw(window)

    elif (stage == 6):
        stage6 = Image (Point (750,250), 'Stage6.gif')
        stage6.draw(window)

# Function for closing the program
def CloseWindow(window):
    window.getMouse()
    window.close()

# Main function for program
def main():
    # Creates the window the game will be played in.
    gameWindow = GraphWin("Hangman", 1000, 1000)
    gameWindow.setBackground('gray')

    DisplayWindow(gameWindow) # calls opening game page

main()
