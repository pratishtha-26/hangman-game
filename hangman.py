import random
def hangman():
    words =  random.choice(["plane","happy","apple","rain","food","netflix","water","coffee","books","music","stars","movies"])
    validinput = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guesses = ""
    while len(words) >0:
        main = ""

        for letter in words:
            if letter in guesses:
                main = main + letter
            else:
                main = main +"_"+""
        if main == words:
            print(main)
            print("YOU GUESSED THE WORD! YIPPIE!!")
            break
        print("Guess the word :", main)
        guess = input()
        if guess in validinput:
            guesses = guesses + guess
        else:
            print("Enter a valid input")
            guess = input("Valid input please :")
        if guess not in words:
            turns = turns-1
            if turns == 9:
                print("9 turns lefts!")
                print("  ------------  ")
            elif turns == 8:
                print("8 turns left!")
                print("  -------------  ")
                print("        O        ")
            elif turns == 7:
                print("7 turns left!")
                print("  -------------  ")
                print("        O        ")
                print("        |        ")
            elif turns == 6:
                print("6 turns left!")
                print("  -------------  ")
                print("        O        ")
                print("        |        ")
                print("       /         ")
            elif turns == 5:
                print("5 turns left!")
                print("  -------------  ")
                print("        O        ")
                print("        |        ")
                print("       / \       ")
            elif turns == 4:
                print("4 turns left!")
                print("  -------------  ")
                print("       \O        ")
                print("        |        ")
                print("       / \       ")

            elif turns == 3:
                print("3 turns left!")
                print("  -------------  ")
                print("       \O/       ")
                print("        |        ")
                print("       / \       ")

            elif turns == 2:
                print("2 turns left!")
                print("  -------------  ")
                print("       \O/|      ")
                print("        |        ")
                print("       / \       ")
            elif turns ==1:
                print("1 turn left!")
                print("Last chance to save him!")
                print("  -------------  ")
                print("       \O_|/     ")
                print("        |        ")
                print("       / \       ")
            else:
                print("YOU LOSE! THE MAN IS HANGED!!!")
                print("  -------------  ")
                print("        O_|      ")
                print("       /|\       ")
                print("       / \       ")
                break




name = input("Enter your name :")
print("Welcome" , name)
print("--------------")
print("Try to guess the word in less than 10 attempts!")
hangman()
print()
