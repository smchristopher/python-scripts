#Python2 Code to sequence DNA from txt file

#builds lists from DNA file
def buildList(lines):
    dataSet=[]
    names = []
    temp=[] 
    result = []
    
    names.append(lines.pop(0).strip())
    
    for line in lines:
        if line[0] == '>':
            line = line.strip()
            names.append(line)
            dataSet.append(temp)
            temp=[]
        else:
            strip_line = line.strip()
            cap_line = strip_line.upper()            
            temp.append(cap_line)
            
    dataSet.append(temp) 
    
    result = [''.join(items) for items in dataSet]
        
    return result, names

#calculates statistics for each sequence
def stats(fullList):
    lengths = [int(len(items)) for items in fullList]
    maximum = max(lengths)
    minimum = min(lengths)
    average = sum(lengths) / len(lengths)
    
    return maximum, minimum, average

#counts bases
def dna(fullList,names):
    for items in fullList:
        print('\n',names[fullList.index(items)],sep='')
        print('A:',items.count('A'))
        print('C:',items.count('C'))
        print('G:',items.count('G'))
        print('T:',items.count('T'))

#main driver
#reads in data and calculates statistics for DNA      
def main():
    filename = input('Enter a filename: ')
    input_file = open(filename, 'r')
    lines = input_file.readlines()

    fullList, names = buildList(lines)
    
    maximum, minimum, average = stats(fullList)
    
    print('\nReport for file', filename)
    print('Number of sequences', len(fullList))
    print('Maximum sequence length:', maximum)
    print('Minimum sequence length:', minimum)
    print('Average sequence length:', average)
       
    dna(fullList, names)
    input_file.close()
    
main()