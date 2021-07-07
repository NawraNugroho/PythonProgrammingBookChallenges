# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 19:58:16 2021

@author: pc
"""

import random

class Television(object):
    def __init__(self, number):
        self.number = number
        self.volume = 50

    def changevolume(self, change):
        og = self.volume
        self.volume += change
        
        if self.volume > 100:
            self.volume = og
            return None
        else:
            return self.volume

    def changenumber(self, change):
        self.number = change
        
    def __str__(self):
        return "Channel number: " + str(self.number) + "\nChannel volume: " + str(self.volume)

def main():
    number = random.randint(1, 20)
    channel = Television(number)
    res = None

    print("You're currently in channel", number)    
    while res != 0:

        print(
            """
                PRESS:
                0 - Turn off
                1 - Change channel
                2 - Change volume
                3 - Info

            """
              )
    
        res = int(input("input: "))

        if res == 1:
            number = None
            while number not in range(1, 21):
                number = int(input("What's the channel number?: "))
                
            channel.changenumber(number)

        elif res == 2:
            vol = None
            
            while vol not in range(0, 101):
                change = int(input("Change the volume by: "))
                vol = channel.changevolume(change)
            
        elif res == 3:
            print(channel.__str__())
            

main()
