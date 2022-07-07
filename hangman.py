import random
def hangman():
    list_of_words=['india','notebook','pen','laptop','hangman','random','phone','signup','python']
    word=random.choice(list_of_words)
    turns=10
    guessmade=''
    valid_entery=set('abcdefghijklmnopqrstuvwxyz')


    while len(word)>0:
        main_word=""
        missed=0
        for letter in word:
            if letter in guessmade:
                main_word=main_word+letter
            else:
                main_word=main_word+"_ "
        if main_word==word:
            print(main_word)
            print("YOU WON !!!!")
            break

        print("guess the words ", main_word)
        guess=input()
        if guess in valid_entery:
            guessmade=guessmade+guess
        else:
            print(" enter valid chracter")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left!!!!!!")
                print("__________________")
            if turns==8:
                print("8 turns left!!!!!!")
                print("__________________")
                print("       O          ")
            if turns==7:
                print("7 turns left!!!!!!")
                print("__________________")
                print("       O          ")
                print("       |          ")
            if turns==6:
                print("6 turns left!!!!!!")
                print("__________________")
                print("       O          ")
                print("       |          ")
                print("      /           ")
            if turns==5:
                print("5 turns left!!!!!!")
                print("__________________")
                print("       O          ")
                print("       |          ")
                print("      / \         ")
            if turns==4:
                print("4 turns left!!!!!!")
                print("__________________")
                print("      \O          ")
                print("       |          ")
                print("      / \         ")
            if turns==3:
                print("3 turns left!!!!!!")
                print("__________________")
                print("      \O/         ")
                print("       |          ")
                print("      / \         ")
            if turns==2:
                print("2 turns left!!!!!!")
                print("__________________")
                print("      \O/  |      ")
                print("       |          ")
                print("      / \         ")
            if turns==1:
                print(" only 1 turns left!!! hangman in on his last breath ")
                print("__________________")
                print("      \O/_|      ")
                print("       |          ")
                print("      / \         ")
            if turns==0:
                print("YOU LOOSE")
                print("you let a ood man die")
                print("__________________")
                print("       O_|      ")
                print("      /|\          ")
                print("      / \         ")
                break
name=input("ENTER THE NAME:   ")
print("WELCOME" ,name,"!")
print("--------------------")
print(" try to guess the words in less than 10 attempts ")
hangman()

            
                



            
