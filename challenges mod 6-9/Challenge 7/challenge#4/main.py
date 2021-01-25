import sys, shelve

def welcome():
    """Welcoming player and give a description of this game"""
    print("\t\tWelcome to Python Trivia Game!")
    print("\nThis game is about Python files and exception knwoledge. So be ready!")


def ask_number(question):
    """Ask number in range 5 (1, 2, 3, 4)"""
    response = None
    while response not in range(1, 5):
        try:
            response = int(input(question))
        except:
            print("Number only!")
            continue
        else:
            continue

    return response


def open_file(filename, mode):
    """Opening a file"""
    try:
        the_file = open(filename, mode, encoding="UTF8")
    except IOError as a:
        print("Unable to open file", filename, "Ending program.\n", a)
        sys.exit()
    else:
        return the_file

def next_line(file):
    """Return next line from the trivia file, formatted."""
    line = file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(file):
    """returning the next block"""
    episode = next_line(file)
    question = next_line(file)
    answer = []
    for i in range(4):
        answer.append(next_line(file))

    correct = next_line(file)
    explanation = next_line(file)
    point = next_line(file)

    return episode, question, answer, correct, explanation, point


def main():
    trivia_file = open_file("FileAndExceptionTrivia.txt", "r")
    welcome()
    score = 0
    input("Press enter to start playing!")

    episode, question, answer, correct, explanation, point = next_block(trivia_file)
    
    while episode:
        correct_answer = int(correct)
        unique_point = int(point)
        print("\n" + episode)
        #ask a question
        print(question)
        #display all 4 answers
        for i in range(4):
            print(i + 1, "-", answer[i])
        #ask the player
        player = ask_number("What's your answer?: ")
        #check answer
        if player == correct_answer:
            print("\nRight!", end=" ")
            score += unique_point
        else:
            print("\nWrong!", end=" ")
        print(explanation)

        episode, question, answer, correct, explanation, point = next_block(trivia_file)

    trivia_file.close()

    print("\nYour final score is", score)

    s = shelve.open("highscores.db", "r")

    player = s["player2"]
    high_scores = s["high_scores2"]

    s.close()

    s = shelve.open("highscores.db", "w")

    times = 0
    for item in high_scores:
        if score > item:
            times += 1 #how many times the score is higher than each high scores item
            continue
        else:
            continue

    if times == len(high_scores):
        print("\nCongrats! You beat the high score!")
        name = input("What's your name? ")
        player.append(name)
        high_scores.append(score)
        s["player2"] = player
        s["high_scores2"] = high_scores
        s.sync()
    
    s.close()

main()
