#                         Challenges Chapter 3

# Challenges 1:
# This program display one of five unique fortunes, at random, each time it's run.
print("\t\t\tWelcome to 'Fortune Cookies' simulator...")
print("\n\nThis simulator will show you what message you got from fortune cookies!")
input("\nPress the enter key to find out!.")

import random

Fortunecookies = random.randint(1, 5)

if Fortunecookies == 1:
    print("\n\nYou got: ")
    print("You will meet your favorite character soon\n")
elif Fortunecookies == 2:
    print("\n\nYou got: ")
    print("You will have $1,000 soon\n")
elif Fortunecookies == 3:
    print("\n\nYou got: ")
    print("You are smarter than Albert Einstein\n")
elif Fortunecookies == 4:
    print("\n\nYou got: ")
    print("You will became a dentist in the future\n")
else:
    print("\n\nYou got: ")
    print("Your best friends will come to you in a minute\n")

input("Press the enter key to go to challenges 2.")

# Chalenges 2:
# This program display coin that flips 100 times and tells us the number
# of heads and tails we got.
print("--------------------------------------------------------------------------------")
print("\t\t\tWelcome to coin simulator games!")
print("This game will simulate a coin that " \
      + "flips 100 times and it tell you how many heads and tails you got")
      
input("\nPress the enter key to find out.")
print("\n\nYou got: ")
times = 0
head = 0
tail = 0

while times != 100:
    headortails = random.randint(1, 2)
    if headortails == 1:
        print("Head")
        head += 1
        times += 1
        if times == 10 or times == 20 or times == 30 or times == 40 or \
           times == 50 or times == 60 or times == 70 or times == 80 or \
           times == 90:
            if headortails == 1:
                print("\nHead")
                head +=1
                times += 1
            else:
                print("\nTail")
                tail += 1
                times += 1
    else:
        print("Tail")
        tail += 1
        times += 1
        if times == 10 or times == 20 or times == 30 or times == 40 or \
           times == 50 or times == 60 or times == 70 or times == 80 or \
           times == 90:
            if headortails == 1:
                print("\nHead")
                head += 1
                times += 1
            else:
                print("\nTail")
                tail += 1
                times += 1
print("\nYou got", tail, "tails and", head, "heads\n")
input("Press the enter key to go to challenges 3.")

# Challenges 3:
# In this game we have to guess the number that computer thinking of. We have
# a limited number of guesses. If we fails to guess in time, we loose. 
print("--------------------------------------------------------------------------------")
print("\t\t\tWelcome to 'Guess my number' games!")
print("\nGuess my number between 1 and 100")
print("You can only took 7 guesses")

number = random.randint(1, 100)
guess = 0
print("\n\nGuess my number: ")
number_input = ""

while number_input != number and guess != 7:
    number_input = int(input(""))
    guess += 1
    if number_input > number and number_input <= 100:
        print("Lower\n")
    elif number_input < number and number_input > 0:
        print("Higher\n")
    elif number_input == number and guess < 7:
        print("Correct, and it only take you", guess, "guess")
    elif number_input == number and guess == 7:
        print("Correct, and you guess in time!")
    else:
        print("Wrong input\n")
        guess -= 1

while number_input != number and guess == 7:
    print("\nThe number was", number)
    print("you can only take 7 guesses tries")
    break
input("\nPress the enter key to go to challenges 4.")

# Challenges 4
# In this game we have to think of a number between 1 and 100. Then the computer
# is gonna guess our number... (Is it lower, higher or correct)
print("--------------------------------------------------------------------------------")
print("\t\t\tWelcome to 'Guess Your Number' game!")
print("In this game I will guess your number between 1 to 100")
print("Now think of a number between 1 and 100")

input("\nPress the enter key to continue")


Computer_number = 100
Computer_guess = Computer_number // 2
minimum = 1
maximum = 100
guess = 0
Answer = ""

print("\n\nI’m guessing that your number is", Computer_guess)

while Answer.lower() != "correct" or Answer.lower() != "higher" or Answer.lower() != "lower":
    Answer = input("(input correct or higher or lower only) \n")
    if Answer == "correct":
        guess += 1
        print("\nI take", guess, "guesses")
        print("yes…:)")
        break
    elif Answer == "lower":
        maximum = Computer_guess - 1
        Computer_guess = minimum + (maximum - minimum) // 2
        if minimum > maximum:
            print("You are cheating!")
            break
        else:
            print(Computer_guess)
        guess += 1
    elif Answer == "higher":
        minimum = Computer_guess + 1
        Computer_guess = minimum + (maximum - minimum) // 2
        if minimum > maximum:
            print("You are cheating!")
            break
        else:
            print(Computer_guess)
        guess += 1
    else:
      continue




                   
            
    
