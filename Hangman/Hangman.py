def hangman(word):
    
        missed = 0
        wrong = 0
        stages = [""
                  "______________       ",
                  "|            |       ",
                  "|            |       ",
                  "|            O       ",
                  "|           /|\      ",
                  "|           / \      ",
                  "|                    ",
                  "|                    ",
                  "|                    ",
                  "|                    ",
                  "|                    ",
                  "|                    ",]
        try:
            remainingLetters = list(word)
            board = ["_"] * len(word)
            wrongGuesses = [""] * 27
            win = False
            print("Welcome to hangman")
            while wrong < len(stages) - 1:
                print("\n")
                guess = input("Guess a letter: ")
                if " " in remainingLetters:
                    while " " in remainingLetters:
                        cind = remainingLetters.index(" ")
                        board[cind] = " "
                        remainingLetters[cind] = "$"
                if guess in remainingLetters:
                    while guess in remainingLetters:
                        cind = remainingLetters.index(guess)
                        board[cind] = guess
                        remainingLetters[cind] = "$"
                else :
                    wrong += 1
                    wrongGuesses[missed] = guess
                    missed = missed + 1
                print((" ".join(board)))
                print((" ".join(wrongGuesses[0: missed])))
                currentStage = wrong + 1
                print("\n".join(stages[0: currentStage]))
                if "_" not in board:
                    print("You win! It was: ")
                    print(" ".join(board))
                    win = True
                    break
            if not win:
                print("\n".join(stages[0 : wrong]))
                print("You lose! it was {}".format(word))
        except :
            print("\nPlease select a valid category")
            return


def getWord():
    list = ["Dog breeds" ,
            "Countries"]
    try :
        category = int(input("Please select a category: Dog breeds(0), Countries(1): "))
        with open(list[category] + ".txt" , "r") as word:
            for row in word:
                list.append(row)
            len(list)
            #print(len(list))
            import random
            rndSelection = random.randint(1,len(list))
            selection = rndSelection
            #print(selection)
            chosenSelection = str(list[selection]).lower()
            chosenSelection = chosenSelection.strip()
            return chosenSelection
    except (ValueError, IndexError):
        return

def main() :
    while 1 < 10:
        answer = input("\nWould you like to play hangman? (Yes/No): ").capitalize()
        if answer == "Yes" or answer == "Y":
            #word = getWord()
            #hangman(word)
            hangman(getWord())
        else :
            break
    return

main()

