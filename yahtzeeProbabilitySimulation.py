#Python2 code to compute the probability of the various hands in Yahtzee.

import random

def roll_dice():
    #Returns 5 randomly rolled dice.#
    for i in range(5):
        dice += [random.randint(1,6)]
    return dice

 
def three_of_a_kind(dice):
    #Returns True or False if the dice are three of a kind.
    for i in range(0,5):
        if dice.count(i) == 3:
            return True
    return False
 
def four_of_a_kind(dice):
    # Returns True or False if the dice are four of a kind. 
    for i in range(0,5):
        if dice.count(i) == 4:
            return True
    return False


def full_house(dice):
    #Returns True of False if the dice are a full house.
    count = 0
    for i in range(0,5):
        if dice.count(i) == 3:
            count += 1
        elif dice.count(i) == 2:
            count += 2
            
        if count == 3:
            return True
    return False

     
def small_straight(dice):
    # Returns True or False if the dice represent a small straight. 
    straight1 = [1,2,3,4]
    straight2 = [2,3,4,5]
    sortRoll = sorted(dice)
    
    if sortRoll[0] == 1:
        if set(sortRoll) == set(straight1):
            return True
    elif sortRoll[0] == 2:
        if set(sortRoll) == set(straight2):
            return True
    else:
        return False
    
         
def large_straight(dice):
    # Returns True or False if the dice represent a large straight. 
    straight = [1,2,3,4,5]
    sortRoll = sorted(dice)

    if set(sortRoll) == set(straight):
        return True
    else:
        return False

 
def yahtzee(dice):
    # Returns True or False if the dice represent Yahtzee
    count = 0
    num = dice[0]
    
    for val in dice:
        if val == num:
            count += 1
        else:
            return False
    if count == 5:
        return True
        
def main():
    #The main driver
    rolls = ''
    
    while rolls != 'quit':
        rolls = input('>')
        yaht = 0
        four = 0
        large = 0
        full = 0
        small = 0
        three = 0
        misc = 0
        
        for i in range(int(rolls)):
            roll = roll_dice()
            if yahtzee(roll):
                yaht += 1
            elif four_of_a_kind(roll):
                four +=1
            elif large_straight(roll):
                large +=1
            elif full_house(roll):
                full +=1
            elif small_straight(roll):
                small +=1
            elif three_of_a_kind(roll):
                three +=1
            else:
                misc +=1
        print('yahtzee: ', yaht, ' (', round((yaht/int(rolls)*100),1), '%)',sep='')
        print('four of a kind: ', four, ' (', round((four/int(rolls)*100),1), '%)',sep='')
        print('large straight: ', large, ' (', round((large/int(rolls)*100),1), '%)',sep='')
        print('full house: ', full,' (', round((full/int(rolls)*100),1), '%)',sep='')
        print('small straight: ', small, ' (', round((small/int(rolls)*100),1), '%)',sep='')
        print('three of a kind: ', three, ' (', round((three/int(rolls)*100),1), '%)',sep='')
        print('misc: ', misc, ' (', round((misc/int(rolls)*100),1), '%)',sep='')

main()