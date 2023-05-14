import random

#picking word from a pool of words
words=["turquoise", "lavender", "vermilion", "maroon", "sapphire", "chocolate", "magenta", "violet", "turmeric"]
random_word=random.choice(words)

#Hiding characters from the randomly choosen words

num_to_hide = len(random_word) // 2
indices_to_hide = random.sample(range(len(random_word)), num_to_hide)
# Create a new string with the hidden characters replaced by dashes
hidden_word = ""
for i in range(len(random_word)):
    if i in indices_to_hide:
        hidden_word += "_"
    else:
        hidden_word += random_word[i]


#snippet whether the contest had directly choosen the word
def find_by_word():
    print("Find your word: \n \t \033[1m", hidden_word,"\033[0m")
    word_count=3
    while(word_count):
        choosed_word=str(input())
        if choosed_word==random_word:
            print("Congragulations, You won the game \U0001F600")
            break
        else:
            word_count-=1
        
            if word_count==0:
                print("You lost the game \U0001F622, The word is ",random_word)
            else:
                print("Sorry! Incorrect Guess, You have",word_count,"more chances")


#snippet whether we are finding the word by entering characters
def find_by_characters():

    print("Guess the characters, your hint( ",hidden_word," )")
    guesses = ''
    turns = len(random_word)+1
    while turns > 0:
        failed = 0
        for char in random_word:
            if char in guesses:
                print(char, end=" ")
 
            else:
                print("_",end=" ")
                failed += 1
 
        if failed == 0:
            print("\nCongragulations, You Won")
            print("The word is: ", random_word)
            break
        print()
        try:
            guess = chr(input("Guess a character: "))
            guesses += guess
        except:
            print("Invalid character!")
            return 
 
        # check input with the character in word
        if guess not in random_word:
            turns -= 1
            print("Wrong")
            print("You have", + turns, 'more guesses')
 
            if turns == 0:
                print("You Lost \U0001F622 ,The word is",random_word)


name_of_Player=str(input("Kindly enter your name: "))

if name_of_Player=="":
    print("Improper entry!")
else:
    print("Welcome ",name_of_Player," to the game \U0001F600")
    print("!------Welcome To Hangman Game------!")
    try:
        choice_of_playing=int(input("Please select the mode of playing (1 OR 2) \n 1. Guess the Word \n 2. Guess the Character\n"))
        if choice_of_playing==1:
            find_by_word()
        else:
            find_by_characters()
    except:
        print("Not a valid choice!")