# Critter Caretaker
# A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self, hunger_add, boredom_add):
        self.hunger += hunger_add
        self.boredom += boredom_add

    def __str__(self):
        return "Name: "+self.name+", Hunger: "+str(self.hunger)+", Boredom: "+str(self.boredom)+"\n"
        

    @property
    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "happy"
        elif 5 <= unhappines <= 10:
            m = "okay"
        elif 11 <= unhappines <= 15:
            m = "frustarated"
        else:
            m = "mad"

        return m

    def talk(self):
        print("\nHello! my name is", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time(1, 1)

    def eat(self, food):
        print("\nBruppp. Thank you!\n")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
            
        if food < 4:
            self.__pass_time(hunger_add = 2, boredom_add = 1)
        elif 4 <= food < 8:
            self.__pass_time(hunger_add = 1, boredom_add = 1)
        elif food >= 8:
            self.__pass_time(hunger_add = 0, boredom_add = 2)


    def play(self, fun):
        print("\nWheee. Thank you!\n")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        if fun < 4:
            self.__pass_time(hunger_add = 1, boredom_add = 2)
        elif 4 <= fun < 8:
            self.__pass_time(hunger_add = 1, boredom_add = 1)
        elif fun >= 8:
            self.__pass_time(hunger_add = 2, boredom_add = 0)


def main():
    name = input("What do you want to name your critter?: ")
    crit = Critter(name)

    print(
        """
            Critter Caretaker

        0 - exit
        1 - talk
        2 - eat
        3 - play

        """
    )

    res = int(input("Input: "))

    while res != 0:
        if res == 1:
            crit.talk()
        elif res == 2:
            food = int(input("How much food would you like to give?: "))
            crit.eat(food)
        elif res == 3:
            minute = int(input("How many minute does it take for you to play?: "))
            crit.play(minute)
        elif res == 4:
            print(crit.__str__())

        res = int(input("Input: "))

main()
            

    
