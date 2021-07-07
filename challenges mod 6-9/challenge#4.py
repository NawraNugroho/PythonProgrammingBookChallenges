# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:11:34 2021

@author: pc
"""

class Critter(object):
    def __init__(self, name, hunger, boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        
    def __pass_time(self, hunger_add, boredom_add):
        self.hunger += hunger_add
        self.boredom += boredom_add

    def __str__(self):
        return "Name: "+self.name+", Hunger: "+str(self.hunger)+", Boredom: "+str(self.boredom)+", Mood: "+self.mood+"\n"
        

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
    
    list = []
    
    list.append(Critter("Petsy", 1, 3))
    list.append(Critter("Chubby", 3, 1))
    list.append(Critter("Speedy", 2, 3))
    list.append(Critter("Chili", 3, 2))
    list.append(Critter("Biby", 1, 1))
    res = None

    while res != 0:
        print(
            """
                Critters Caretaker
    
            0 - exit
            1 - talk
            2 - eat
            3 - play
    
            """
        )
    
        res = int(input("Input: "))        
            
        if res == 1:
            for item in list:
                crit = item
                crit.talk()
        elif res == 2:
            food = int(input("How much food would you like to give?: "))
            for item in list:
                crit = item
                crit.eat(food)
        elif res == 3:
            minute = int(input("How many minute does it take for you to play?: "))
            for item in list:
                crit = item
                crit.play(minute)
        elif res == 4:
            for item in list:
                crit = item
                print(crit.__str__())

main()
        
    