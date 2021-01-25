import pickle, shelve

print("1 - reset trivia games1 high score list\
\n2 - reset file and exception trivia high score list\
\n3 - see trivia games1 high score list\
\n4 - see file and exception trivia high score list\
\nexit - to exit")
ans = None


while ans != "exit":
    ans = input("\nNumber: ").lower()

    if ans == "1":
        #reseting the list
        player1 = ["None"]
        high_scores1 = [0]

        f = open("highscores triviagames1.dat", "wb")

        pickle.dump(player1, f)
        pickle.dump(high_scores1, f)
        f.close()

        print("-----Music trivia game-----")
        print("Success reseting the list!")

    if ans == "3":
        #look at the list
        f = open("highscores triviagames1.dat", "rb")

        player1 = pickle.load(f)
        high_scores1 = pickle.load(f)

        print("-----Music trivia game-----")
        print("Player:", player1)
        print("high scores:", high_scores1)
        f.close()

    if ans == "2":
        #reseting the list
        s = shelve.open("highscores.db")

        s["player2"] = ["None"]
        s["high_scores2"] = [0]

        s.sync()
        s.close()

        print("-----File and Exception trivia game-----")
        print("Success reseting the list!")

    if ans == "4":
        #look at the list
        s = shelve.open("highscores.db", "r")

        player2 = s["player2"]
        high_scores2 = s["high_scores2"]

        print("-----File and Exception trivia game-----")
        print("Player: ", player2)
        print("high scores: ", high_scores2)

        s.close()
