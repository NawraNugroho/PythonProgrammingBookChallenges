#Challenges 1
print("Challenges 1")
print("------------------------------------------------------------------------------")

import random

#set up the list
WORD = ["Love", "Hobby", "Matter", "Subject", "School", "Instrument", "Inteligence", "Magnificent", "Homophone", "Likely"]

#while all the word isn't display yet
for i in range(len(WORD)):
    number = random.randrange(0, len(WORD))
    print(WORD[number])
    del WORD[number] #delete the word that already shown
input("\n\nPress the enter key to continue.")


#Challenges 2
print("\n\nChallenges 2")
print("------------------------------------------------------------------------------")

#set up the variable
pool = 30
strength = 0
health = 0
wisdom = 0
dexerity = 0
choice = ""

print(
    """
                    Welcome to Character Creator Program

        Press:

        0 - exit
        1 - spend points
        2 - take points back
        3 - look each attribute
    """)

while choice != "0":
    print("\nYou have", pool, "points left on pool.")
    
    choice = input("\nChoice: ")

    if choice == "0":
        input("Press the enter key to continue.")

    #spend points from pool
    elif choice == "1" and pool != 0:
        attribute = input("Would you rather choose strength, health, wisdom or dexerity?: ")
        
        if attribute.lower() == "strength":
            points = int(input("How many points do you want to spend?: "))
            
            #if in pool has enough points
            if pool >= points:
                pool -= points #take points from pool
                strength += points #spend points to strength
            else:
                print("You don't have enough points on pool.")
                
        elif attribute.lower() == "health":
            points = int(input("How many points do you want to spend?: "))

            #if in pool has enough points
            if pool >= points:
                pool -= points #take points from pool
                health += points #spend points to health
            else:
                print("You don't have enough points on pool.")
                
        elif attribute.lower() == "wisdom":
            points = int(input("How many points do you want to spend?: "))

            #if in pool has enough points
            if pool >= points:
                pool -= points #take points from pool
                wisdom += points #spend points to wisdom
            else:
                print("You don't have enough points on pool.")
                
        elif attribute.lower() == "dexerity":
            points = int(input("How many points do you want to spend?: "))

            #if in pool has enough points
            if pool >= points:
                pool -= points #take points from pool
                dexerity += points #spend points to dexerity
            else:
                print("You don't have enough points on pool.")

        #if the choice doesn't exist
        else:
            print("Sorry, that choice didn't exist.")

    #take points to pool
    elif choice == "2" and pool != 30:
        attribute = input("Would you rather choose strength, health, wisdom or dexerity?: ")
        
        if attribute.lower() == "strength":
            points = int(input("How many points do you want to take back?: "))

            #if strength has enouugh points
            if strength >= points:
                strength -= points #take points from strength
                pool += points #spend points to pool
            else:
                print("You don't have enough points on strength.")
                
        elif attribute.lower() == "health":
            points = int(input("How many points do you want to take back?: "))

            #if health has enough points
            if health >= points:
                health -= points #take points from health
                pool += points #spend points to pool
            else:
                print("You don't have enough points on health.")
                
        elif attribute.lower() == "wisdom":
            points = int(input("How many points do you want to take back?: "))

            #if wisdom has enough points
            if wisdom >= points:
                wisdom -= points #take points from wisdom
                pool += points #spend points to pool
            else:
                print("You don't have enough points on wisdom.")
                
        elif attribute.lower() == "dexerity":
            points = int(input("How many points do you want to take back?: "))

            #if dexerity has enough points
            if dexerity >= points:
                dexerity -= points #take points from dexerity
                pool += points #spend points to pool
            else:
                print("You don't have enough points on dexerity.")

        #if the choice doesn't exist
        else:
            print("Sorry, that choice didn't exist.")

    #display each attribute points
    elif choice == "3":
        print("\nstrength:", strength)
        print("health:", health)
        print("wisdom:", wisdom)
        print("dexerity:", dexerity)
        print("pool:", pool)
        
    else:
        if choice == "1":
            print("You don't have any points left on the pool.")
        elif choice == "2":
            print("You don't have any points on attribute.")
        else:
            print("Oops, wrong input!")



#Challenges 3
print("\n\nChallenges 3")
print("------------------------------------------------------------------------------")

choice = ""
Son_father = {"Harry Potter" : "James Potter",
              "Ron Weasley" : "Arthur Weasley",
              "Tom Marvolo Riddle" : "Tom Riddle sr",
              "Neville Longbottom" : "Frank Longbottom",
              "Draco Malfoy" : "Lucius Malfoy"
              }

print(
    """

                    Who's Your Daddy? Program

        0 - Exit
        1 - Look up for daddy
        2 - Add son-daddy pair
        3 - Replace Daddy
        4 - Delete son-daddy pair
   """
    )

while choice != "0":
    choice = input("\nChoice: ")

    #exit
    if choice == "0":
        input("Press the enter key to continue.")
        
    #look up for daddy
    elif choice == "1":
        #print each son
        for item in Son_father:
            print("\n", item, end="")
        son = input("\n\nWhat's his name? ").title()
        if son in Son_father:
            father = Son_father[son]
            print(son, "daddy name is", father)
        else:
            print("Sorry, I don't know who is", son)


    #add son-daddy pair
    elif choice == "2":
        son = input("\nWhat's the name of a guy you want to add? ").title()
        if son not in Son_father:
            father = input("What's his daddy's name? ").title()
            Son_father[son] = father
            print(son + "-" + father, "has been added.")
        else:
            print(son, "daddy's name is", Son_father[son])
        
    #replace daddy
    elif choice == "3":
        for item in Son_father:
            print("\n", item, end="")
        son = input("\n\nWhich guy do you want to replace his daddy? ").title()
        if son in Son_father:
            father = input("Who's his new daddy? ")
            Son_father[son] = father
            print(son, "daddy has been replaced!")
        else:
            print("Sorry, I don't know who is", son)
        

    #delete son-father pair
    elif choice == "4":
        print("\n", Son_father)
        son = input("\nWhich pair that you want to delete? ").title()
        if son in Son_father:
            del Son_father[son]
            print(son, "and his daddy pair has been deleted!")
        else:
            print("Sorry, I don't know who is", son)



#Challeges 4
print("\n\nChallenges 4")
print("------------------------------------------------------------------------------")

choice = ""
pairs = {"Harry Potter" : {"daddy" : "James Potter", "grandpa" : "Fleamont Potter"},
         "Ron Weasley" : {"daddy" : "Arthur Weasley", "grandpa" : "Septimus Weasley"},
         "Tom Marvolo Riddle" : {"daddy" : "Tom Riddle sr", "grandpa" : "Thomas Riddle"},
         "Neville Longbottom" : {"daddy" : "Frank Longbottom", "grandpa" : "Eugene Longbottom"},
         "Draco Malfoy" : {"daddy" : "Lucius Malfoy", "grandpa" : "Abraxas Malfoy"}
         }

print(
    """

                    Who's Your Daddy? Program

        0 - Exit
        1 - Look up for daddy
        2 - Add son-daddy pair
        3 - Replace Daddy
        4 - Delete a pair
        5 - Look up for grandpa
   """
    )

while choice != "0":
    choice = input("\nChoice: ")

    #exit
    if choice == "0":
        input("Press the enter key to continue.")
        
    #look up for daddy
    elif choice == "1":
        #print each son
        for item in pairs:
            print("\n", item, end="")
        son = input("\n\nWhat's his name? ").title()
        if son in pairs:
            daddy = pairs[son]["daddy"]
            print(son, "daddy name is", daddy)
        else:
            print("Sorry, I don't know who is", son)


    #add son-daddy pair
    elif choice == "2":
        son = input("\nWhat's the name of a guy you want to add? ").title()
        if son not in pairs:
            pairs[son] = {}
            daddy = input("What's his daddy's name? ").title()
            pairs[son]["daddy"] = daddy
            print(son + "-" + daddy, "has been added.")
        else:
            print(son, "daddy's name is", pairs[son]["daddy"])
        
    #replace daddy
    elif choice == "3":
        for item in pairs:
            print("\n", item, end="")
        son = input("\n\nWhich guy do you want to replace his daddy? ").title()
        if son in pairs:
            daddy = input("Who's his new daddy? ")
            pairs[son]["daddy"] = daddy
            print(son, "daddy has been replaced!")
        else:
            print("Sorry, I don't know who is", son)
        

    #delete son-daddy pair
    elif choice == "4":
        for name in pairs:
            print("\n" + name)
            for key in pairs[name]:
                print(key + ":", pairs[name][key])
                
        son = input("\nWhich pair that you want to delete? ").title()
        if son in pairs:
            response = input("Daddy or grandpa? ").lower()
            del pairs[son][response]
            print(son, "and his daddy pair has been deleted!")
        else:
            print("Sorry, I don't know who is", son)


    #look up for grandpa
    elif choice == "5":
        #print each son
        for item in pairs:
            print("\n", item, end="")
        guy = input("\n\nWhat's his name? ").title()
        if guy in pairs:
            grandpa = pairs[guy]["grandpa"]
            print(guy, "daddy name is", grandpa)
        else:
            print("Sorry, I don't know who is", guy)






