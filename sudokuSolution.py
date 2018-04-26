#Python2 code to determine whether a Sudoku solution is valid

def valid_rows(soln):
    ''' Returns True if each row is valid 
        and False otherwise.
    ''' 
    test = [1,2,3,4,5,6,7,8,9]
    count = 0

    for value in soln:
        sortedRow = sorted(value)
        if test == sortedRow:
            count += 1
    if count == 9:
        return True
                
        

def valid_cols(soln):
    ''' Returns True if each column
        is valid and False otherwise.
    '''
    test = [1,2,3,4,5,6,7,8,9]
    count = 0
    for i in range(0,9):  
        column=[]
        for value in soln:
            column.append(value[i])
        if sorted(column) == test:
            count += 1
    if count == 9:
        return True
        
    

def valid_blocks(soln):
    ''' Checks each 3 x 3 block in the puzzle. 
        Returns True if each block is valid 
        and False otherwise.
    '''
    block = []
    count = 0
    test = [1,2,3,4,5,6,7,8,9]
    for i in range(0,9,3):
        for j in range(0,9,3):
            for value in soln[i:i+3]:
                block.append(value[j:j+3])
            blockList = [k for temp in block for k in temp]
            if sorted(blockList) == test:
                count +=1
            block.clear()
            
    if count == 9:
        return True 

def valid_soln(soln):
    ''' Returns True if a Sudoku solution is valid and False
        otherwise.
    '''
    
    # Check if rows are valid. 
    if not valid_rows(soln):
        return False

    # Check if columns are valid.
    if not valid_cols(soln):
        return False

    # Check if 3x3 submatrices (or blocks) are valid.
    if not valid_blocks(soln):
        return False        
    
    # If all checks pass, then the solution is valid.
    return True


def main():
   
    # Get file name.
    file_name = input('Enter filename: ')
    
    # Open file and read its data.
    input_file = open(file_name)
    file_data = input_file.readlines()
   
    # Close file since the information from the file is
    # stored in the list file_data. While not necessary,
    # it is a good habit to close a file once you are 
    # done with it.  
    input_file.close()
    
    # sudoku_soln is populated with the data
    # from the solution file. sudoku_soln is a
    # tuple of tuples, where each tuple is of size 9
   
    sudoku_soln = ()
    for line in file_data:
        row = ()
        for value in line.strip():
            row += (int(value),)     # Line A
        sudoku_soln += (row,)        # Line B
            
    # Check and print results. 
    print(sudoku_soln)
    if valid_soln(sudoku_soln):
        print('Valid solution')
    else:
        print('Invalid solution')


main()
