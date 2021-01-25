#                         Challenges modules 4

# Challenges number 1...
print("Challenges number 1")
print("----------------------------------------------------------------")
start = int(input("Enter a starting number: "))
end = int(input("Enter the ending number: "))
amount = int(input("Enter the amount by which to count: "))

for i in range(start, end, amount):
    print(i, end=" ")

#Challenges number 2..
print("\n\n\n\nChallenges number 2")
print("----------------------------------------------------------------")
word = input("Enter a message: ")
starting = len(word) - 1
print(word[starting], end="")
for i in range(len(word) - 1):
    starting -= 1
    print(word[starting], end="")

#Challenges number 3...
print("\n\n\n\nChallenges number 3")
print("----------------------------------------------------------------")
print(
"""     Welcome to Word Jumble!

Unscramble the letters to make a word.
(press the enter key at prompt to quit.
Enter 'hint' at prompt to see a hint.)
Enjoy!!!

"""
)

score_hint = 0
score_correct = 0
score = 0
end_score = 0
guess = "      "

while guess.lower() != "":
    score_hint = 0
    
    WORDS = ["python", "jumble", "easy", "difficult", "answer",
             "xylophone", "symphony", "affect", "thought", "firework",
             "alias", "ventriloquist", "exotic", "properly", "suddenly",
             "magnificent", "congratulations", "psychology", "sensitive", "exhausted"]
    
    import random
    
    word = random.choice(WORDS)
    
    correct = word
    
    jumble = ""
    
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]
        
    print("\nThe jumble is:", jumble)
    
    guess = input("\nYour guess: ")
    while guess.lower() != correct or guess.lower() == "hint" or guess.lower() == "":
        while guess.lower() == "hint":
            print("Hint:", correct[0 : score_hint + 1])
            score_hint += 1
            guess = input("Your guess: ")
            if guess.lower() == "":
                break
        if guess.lower() == "":
            break
        if guess.lower() != correct:
            print("Sorry, that's not it.")
            guess = input("Your guess: ")
            if guess.lower() == "":
                break
        
    if guess.lower() == correct:
        print("That's it! You guessed it!\n")
        score_correct += 2
        score += score_hint
        
end_score = score_correct - score
print("\n\nYour score is", end_score)


#Challenges number 4...
print("\n\n\nChallenges number 4")
print("----------------------------------------------------------------")
print(

"""         Guess the word!
          
Enter 1 letter of a word. You will get
5 chances to guess a letter, then you're
going to guess the word. Enjoy!!

"""
)

import random

WORD = ["pencil", "coming", "trans", "beaver", "always",
        "because", "amazing", "super", "things", "water",
        "story", "board", "violin", "braid", "know"]

word = random.choice(WORD)

the_word = word

print("\nThere are", len(the_word), "letter in the word")

for i in range(5):
    letter = input("\nEnter one letter of the word: ")
    if letter.lower() in the_word:
        print("yes")
    else:
        print("no")

answer = input("\nNow guess the word: ")

if answer.lower() == the_word:
    print("\nCorrect!! The word is", the_word)
else:
    print("\nWrong!! The word is", the_word)

print("Thanks for playing :)")


