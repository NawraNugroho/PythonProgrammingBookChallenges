import pickle, shelve

print("\n1 - reset file and exception trivia high score list\
\n2 - see file and exception trivia high score list\
\n0 - to exit")
ans = None


while ans != "0":
    ans = input("\nNumber: ").lower()

    if ans == "1":
        #reseting the list
        s = shelve.open("highscores.db")

        s["player2"] = ["None"]
        s["high_scores2"] = [0]

        s.sync()
        s.close()

        print("-----File and Exception trivia game-----")
        print("Success reseting the list!")

    if ans == "2":
        #look at the list
        s = shelve.open("highscores.db", "r")

        player2 = s["player2"]
        high_scores2 = s["high_scores2"]

        print("-----File and Exception trivia game-----")
        print("Player: ", player2)
        print("high scores: ", high_scores2)

        s.close()
