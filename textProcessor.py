#Python2 script to count words, characters, and sentences for a text file

#counts characters in file
def countChar(file):
    lines = file.readlines()
    length = 0
    for line in lines:
        length += len(line)
    
    print('Characters:', length)

#counts sentences in file
def countSentences(file):
    lines = file.readlines()
    s = ''
    joined = s.join(lines)
    splitLine = joined.split('.')
    count = (len(splitLine) - 1)
    print('Sentences:', count)

#counts words in file
def countWords(file):
    lines = file.readlines()
    words = 0
    for line in lines:
        if line[0] == '\n':
            yum = 1
        else:
            splitLine = line.strip()
            splitLine = line.split(' ')
            if splitLine[-1] == '\n' or splitLine[-1] == '':
                splitLine.remove(splitLine[-1])
            words += len(splitLine)
    print('Words:', words)

#main driver    
def main():
    fileName = input('Enter a filename: ')
    input_file = open(fileName, 'r')
    file2 = open(fileName, 'r')
    file3 = open(fileName, 'r')
    
    countChar(file2)
    countSentences(input_file)
    countWords(file3)

main()
    