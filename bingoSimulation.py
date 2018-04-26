#Python2 code to simulate a bingo game and calculate statistics for each round

import random


def check_bingo(card):
    ''' Checks whether card has Bingo. 
        
        Keyword argument:
        
            card: a dictionary where the keys are the 
                  strings 'B', 'I', 'N', 'G', and 'O'.
                  The values for each key is a list of
                  five integers, where the values for
                  the key 'B' are in the range 1 to 15,
                  the values for key 'I' are in the range
                  16 to 30, etc.
                    
                  The integer 0 is used to represent a value 
                  that has been called.
                
        Returns:
            True if the dictionary structure card contains Bingo.
            Otherwise, returns False.
    '''
    

    test = [0,0,0,0,0]
    bingo = 0
    check = []
    diagonal = []
    
    for i in 'BINGO':
        if card[i] == test:
            bingo = 1
    for j in range(5):
        if check == test:
            bingo = 1
        check = []
        for k in 'BINGO':
            check.append(card[k][j])       
    for l, m in zip(range(5), 'BINGO'):
        diagonal.append(card[m][l])
    if diagonal == test:
        bingo = 1
        
    diagonal = []
    for n, o in zip(reversed(range(5)), 'BINGO'):
        diagonal.append(card[o][n])
    if diagonal == test:
        bingo = 1
    
    if bingo == 1:
        return True
    else:
        return False
            
        
        


def generate_random_card():
    ''' Generates a random Bingo card.  
    
        Keyword arguments: None
        
        Returns:
            a dictionary that represents a valid Bingo card.
            
            Remember, a valid Bingo card is a dictionary where 
            the keys are the strings 'B', 'I', 'N', 'G', and 'O'.
            The values for each key is a list of five integers, where 
            the values for the key 'B' are in the range 1 to 15,
            the values for key 'I' are in the range 16 to 30, etc.
    '''   
    
    card = {}
    
    tempList = []
    count = 1
    
    for i in 'BINGO':
        tempList = set()
        while len(tempList) < 5:
            tempList.add(random.randint(count, count + 14))
        card.update({i: list(tempList)})
        count += 15
    
    card['N'][2] = 0
    return card


def simulate_bingo(n, k):
    ''' Simulates k trials of Bingo, where n cards are 
        in play during the simulation.
    
        Keyword arguments:
        
           n: the number of cards in play during a game of Bingo
           
           k: the total number of games (trials) to play
           
        Returns:
            3 floating point values (minn, maxx, avg) returned.
            
            minn: the minimum number of calls
                required to get Bingo among the k games of
                Bingo played with n cards.
            
            maxx: maximum number of Bingo calls.
            
            avg: average number of Bingo calls.
            
    '''  

    minn = 0
    maxx = 0
    avg = 0
    draw = 0
    wins = []
    
    
    for i in range(k):
        cards = []
        for j in range(n):
                cards.append(generate_random_card())        
        checkCards = 0
        bingo = list(range(1,61))
        count = 0
        while checkCards != 1:
            random.shuffle(bingo)
            draw = bingo.pop()
            count += 1
            for card in cards:
                for keys, values in card.items():
                    if draw in values:
                        loc = values.index(draw)
                        card[keys][loc] = 0
                if check_bingo(card):
                    checkCards = 1
        wins.append(count)
    minn = min(wins)
    maxx = max(wins)
    avg = sum(wins) / len(wins)

    return minn, maxx, avg    


def print_card(card):
    ''' Prints a Bingo card.
    
        Keyword arguments:
        
            card: a dictionary where the keys are the 
                  strings 'B', 'I', 'N', 'G', and 'O'.
                  The values for each key is a list of
                  five integers, where the values for
                  the key 'B' are in the range 1 to 15,
                  the values for key 'I' are in the range
                  16 to 30, etc.
                  
        Returns: None
    '''
    
    # Quick checks to see if card dictionary is in
    # correct format.
    if len(card) == 0:
        return
    
    for key in 'BINGO':
        if key not in card.keys():
            print('Error: problem with keys in card dictionary.')
            print('card:', card)
            return
            
        if len(card[key]) != 5:
            print('Error: problem with values in card dictionary.')
            print('card:', card)
            return
            
    
    # Get the values (list of integers) for each key.
    b = card['B']
    i = card['I']
    n = card['N']
    g = card['G']
    o = card['O']
   
    # Print header of Bingo card. 
    print('%2s  %2s  %2s  %2s  %2s' \
          %('B', 'I', 'N', 'G', 'O'))
    
    # Print values of Bingo card.
    for j in range(5): 
        print('%2d  %2d  %2d  %2d  %2d' \
              %(b[j], i[j], n[j], g[j], o[j]))


def open_file_command(file_name):
    ''' Returns a Bingo card read from a file.
    
        Keyword arguments:
        
            file_name: the name of a Bingo CSV file to open
            
        Returns:
            a dictionary representation of a Bingo card (as described 
            in check_bingo() and generate_random_card() functions).
    '''
    
    card = {}
    file_data = open(file_name).readlines()
    for line in file_data[1:]:
        nums = [int(i) for i in line.split(',')]
        for index, key in enumerate('BINGO'):
            if key in card:
                card[key] += [nums[index]]    
            else:
                card[key] = [nums[index]]
    return card

     
def main():
    
    done = False
    
    while not done:
        user_input = input('> ')
        if user_input == 'random':
            card = generate_random_card()
            print_card(card)
            
        elif 'open' in user_input:
            file_name = user_input.split()[-1]
            card = open_file_command(file_name) 
            print_card(card)
            print('\nBingo:', check_bingo(card))
                
        elif 'sim' in user_input:
            command, n_cards, trials = user_input.split()
            minn, maxx, avg = simulate_bingo(int(n_cards), int(trials))
            print('Minimum: %.1f' %(minn))
            print('Maximum: %.1f' %(maxx))
            print('Average: %.1f' %(avg))
            
        elif user_input == 'quit':
            done = True
            
 
main()