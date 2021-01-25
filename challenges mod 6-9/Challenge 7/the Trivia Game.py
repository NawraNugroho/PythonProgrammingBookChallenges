import sys, pickle

def open_file(filename, mode):
    """open a file"""
    try:
        file = open(filename, mode)
    except IOError as a:
        print("Unable to open the file", filename, "\n", a)
        input("\nPress the enter key to exit")
        sys.exit()
    else:
        return file

def next_line(file):
    """Return next line from the trivia file, formatted."""
    line = file.readline()
    return line

def next_block(file):
    """Return the next block of data from the trivia file"""
    category = next_line(file)
    question = next_line(file)

    answers = []
    for i in range(4):
        answers.append(next_line(file))

    correct = next_line(file)
    explanation = next_line(file)
    point = next_line(file)
    
    return category, question, answers, correct, explanation, point

def welcome():
    """Welcome the player and announce the episode title"""
    print("---------- Welcome to Trivia Program ----------")
    print("\t\tMusic Theory")

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question).lower())
        except:
            print("Number only!")
            continue
        else:
            continue
    
    return response

def main():
    file = open_file("Trivia games1.txt", "r")
    welcome()

    score = 0

    #get first blcok
    category, question, answers, correct, explanation, point = next_block(file)
    
    
    while category:
        #convert answer from str to int
        correct_answer = int(correct)
        #convert str point to int point
        unique_point = int(point)
        
        #Ask a question
        print(category)
        print(question)

        for i in range(4):
            print(i+1, "-", answers[i])

        #get answers
        answer = ask_number("What's your answer?: ", 1, 5)

        #check answer
        if answer == correct_answer:
            print("\nRight!", end=" ")
            score += unique_point
        else:
            print("\nWrong!", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        #get next block
        category, question, answers, correct, explanation, point = next_block(file)

    file.close()
    print("\nYour final score is", score)

    f = open("highscores triviagames1.dat", "rb")

    player1 = pickle.load(f)
    high_scores1 = pickle.load(f)

    f.close()

    times = 0
    for item in high_scores1:
        if score > item:
            times += 1 # count how many times the score is higher than each high scores item
            continue
        else:
            continue


    f = open("highscores triviagames1.dat", "wb")
    
    if times == len(high_scores1):
        print("\nCongrats! You beat the high score!")
        name = input("What's your name?: ")
        player1.append(name)
        high_scores1.append(score)
        pickle.dump(player1, f)
        pickle.dump(high_scores1, f)

    f.close()

main()
