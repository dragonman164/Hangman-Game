import random
import string
import time

def select_random_word(level):
    f = open("Wordlist.txt","r")  # Sample wordlist taken for Testing
    Words = f.readlines()
    words_by_level = []
    min_length,max_length = 0,0
    if level == 1:
        min_length,max_length = 1,4
    elif level == 2:
        min_length,max_length = 4,8
    else:
        min_length,max_length = 8,10
    
    for word in Words:
        if len(word) >= min_length and len(word)<=max_length:
            words_by_level.append(word)
        
    chosen_index =  random.randint(0,len(words_by_level)-1)
    return words_by_level[chosen_index][0:-1].upper()

def fill_dashes(word,key,guessed_word):
    key = key.upper()
    guessed_word = [char for char in guessed_word]
    if key not in word:
        return False
 
    
    for i in range(len(word)):
        if word[i] == key:
            guessed_word[i] = key
    return ''.join(guessed_word)
    

def main():
    choice = True
    while choice:
        print("Welcome to Hangman Game........")

        print("--------------------------------------------------------------------------------")

        level = int(input("Enter Difficulty Level: 1,2,3: "))
        if level not in (1,2,3):
            print("Exiting...")
            exit(1)

        print("Creating Environment for you... Pls Wait")

        i = 0 
        while i<=5:
            print('.',end = ' ')
            time.sleep(1)
            i+=1

        selected_word = select_random_word(level)
        chances = 26  # Specify the number of chances to be given to the user
        guessed_word = "_"*len(selected_word)
        alphabets = string.ascii_lowercase
        chosen = dict()
        for alpha in alphabets:
            chosen[alpha] = False
        while True:
            
            print("You are Currently Here...")
            for elem in guessed_word:
                print(elem,end=' ')
        
            print(' ')


            if chances == 0 :
                print("Sorry you Loose!!!")
                break

            if '_' not in guessed_word:
                print("Congo... you Won!!!")
                break
            
            print('Available Characters are: ')
            for values in chosen.keys():
                if chosen[values] == False:
                    print(values,end=' ')
            
            print(' ')

            key = input("Enter a Character: ")
            
            if not fill_dashes(selected_word,key,guessed_word) or chosen[key]:
                    chances-=1
                    
                    print("Wrong Choice....")
            else:
                print("Wohoo... You are at the right Path")
                guessed_word = fill_dashes(selected_word,key,guessed_word)
            
            chosen[key] = True

        ch = input("Wanna Play Again? (Y/N)?")

        if ch == "Y":
            choice = True
        else:
            choice = False       

main()

