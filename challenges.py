# Exercise 1
def reduceFraction(num, den):
    '''(int,int) --> tup 

    Reduces the fraction to its lowest terms and returns both the numerator and the denominator of the reduced fraction as integers within a tuple

    >>> reduceFraction(12, 15)
        (4, 5)
    >>> reduceFraction(3, 7)
        (3, 7)
    >>> reduceFraction(8, 16)
        (1, 2)
    '''
    from math import gcd

    highestCommonDenominator = gcd(num,den)
    numerator = num / highestCommonDenominator
    denmoinator = den / highestCommonDenominator

    return int(numerator), int(denmoinator)


# Exercise 2
def isMagicDate(day, month, year):
    ''' (int,int,int) --> bool

    A magic date is a date where the day mulitplied by the month is equal to the last two digits of the year.

    Take three ints (day,month,year) and return True if the date is a magic date, return False if it is not

    >>> isMagicDate(6, 10, 1960)
        True
    >>> isMagicDate(3, 4, 2012)
        True
    >>> isMagicDate(4, 12, 2020)
        False
    ''' 
    day_month = str(day * month)
    year_digits = str(year)[2:]

    if day_month == year_digits:
        return True
    else:
        return False


# Exercise 3
def sublist(l):
    ''' (list) --> list

    Take a list and return all sub-lists within the input list

    >>> sublist([1, 2, 3, 4]),
        [
            [],
            [1],
            [2],
            [3],
            [4],
            [1, 2],
            [2, 3],
            [3, 4],
            [1, 2, 3],
            [2, 3, 4],
            [1, 2, 3, 4],
        ]

    >>> sublist(["a", 2, (0, "zero")]),
        [
            [],
            ["a"],
            [2],
            [(0, "zero")],
            ["a", 2],
            [2, (0, "zero")],
            ["a", 2, (0, "zero")],
        ]
    '''
    lst = []

    for i in range(len(l)+1):
        for j in range(i,len(l)+1):
            items = l[i:j]
            lst.append(items)
        lst.remove([])
    lst.insert(0,[])
    lst.sort(key=len)

    return lst


# Exercise 4
def pigLatin(word):
    ''' (str) --> str

    If the word begins with a consonant (including y), then all letters at the beginging of the word, up to the first vowel (excluding y) are removed then added to the end of the word.

    If the word begins with a vowel (not inclucing y) then 'way' is added to the end of the word.

    Upper case letters and punctuation should be handled correctly ie transfer to the result

    >>> pigLatin("computer") 
        "omputercay"
    >>> pigLatin("think")
        "inkthay"
    >>> pigLatin("algorithm")
        "algorithmway"
    >>> pigLatin("office")
        "officeway"
    >>> pigLatin("Computer")
        "Omputercay"
    >>> pigLatin("Science!")
        "Iencescay!"
    '''

    vowels = 'aeiouAEIOU'
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    consonants = 0
  
    if word[-1] in punctuation:
        punct = word[-1]
        word2Punct = word[:(len(word)-1)]
            
        for char in word:
            if char in vowels:
                toVowel = word2Punct [:word2Punct.index(char)]
                constructWord = word2Punct [word2Punct.index(char):] + toVowel + 'ay'
                if word[0] in capitals:
                    convert = constructWord.capitalize()
                    return convert + punct
                convert = constructWord.lower()
                return convert + punct

    elif word [0] not in vowels:
        for char in word:
            if char not in vowels:
                consonants +=1
                if consonants == len(word):
                    return word + 'ay'
            if char in vowels:
                toVowel = word [:word.index(char)]
                constructWord = word [word.index(char):] + toVowel + 'ay'
                if word[0] in capitals:
                    convert = constructWord.capitalize()
                    return convert
                convert = constructWord.lower()
                return convert
    else:
        for char in word:
            if char in punctuation:
                punct2 = char
                word3 = word[:(len(word)-1)]
                return word3 + 'way' + punct2  
            else:
                return word + 'way'

# Exercise 5
def morseCode(message):
    ''' (str) --> str

    Take a str of numbers and letters and return a str in the form of morse code  (.,-)

    >>> morseCode("Hello, World!")
        ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
    >>> morseCode("Testing, 1, 2, 3, Testing!")
        "- . ... - .. -. --. .---- ..--- ...-- - . ... - .. -. --."
    >>> morseCode("1 is one! 2 is two?")
        ".---- .. ... --- -. . ..--- .. ... - .-- ---"
    '''
    codeMessage = ''

    morse = {

        '1': '.---- ',
        '2': '..--- ',
        '3': '...-- ',
        '4': '....- ',
        '5': '..... ',
        '6': '-.... ',
        '7': '--... ',
        '8': '---.. ',
        '9': '----. ',
        '0': '----- ',

        'A': '.- ',
        'B': '-... ',
        'C': '-.-. ',
        'D': '-.. ',
        'E': '. ',
        'F': '..-. ',
        'G': '--. ',
        'H': '.... ',
        'I': '.. ',
        'J': '.--- ',
        'K': '-.- ',
        'L': '.-.. ',
        'M': '-- ',
        'N': '-. ',
        'O': '--- ',
        'P': '.--. ',
        'Q': '--.- ',
        'R': '.-. ',
        'S': '... ',
        'T': '- ',
        'U': '..- ',
        'V': '...- ',
        'W': '.-- ',
        'X': '-..- ',
        'Y': '-.-- ',
        'Z': '--.. ',
    }

    for char in message.upper():
        if char in morse:
                codeMessage += morse[char]
    codeMessage = codeMessage.strip()
    return codeMessage

    


# Exercise 6
def int2Text(num):
    '''(int) --> str

    Take an int and return a str of the int in words

    precondition - int is between 0-999
    
    >>> int2Text(142)
        "one hundred fourty two"
    >>> int2Text(300)
        "three hundred"
    >>> int2Text(16)
        "sixteen"
    >>> int2Text(912)
        "nine hundred twelve"
    ''' 
   
    numbers = {
        '1' : 'one ',
        '2' : 'two ',
        '3' : 'three ',
        '4' : 'four ',
        '5' : 'five ',
        '6' : 'six ',
        '7' : 'seven ',
        '8' : 'eight ',
        '9' : 'nine ',
        
        '10' : 'ten ',
        '11' : 'eleven ',
        '12' : 'twelve ',
        '13' : 'thirteen ',
        '14' : 'fourteen ',
        '15' : 'fifteen ',
        '16' : 'sixteen ',
        '17' : 'seventeen ',
        '18' : 'eighteen ',
        '19' : 'nineteen ',
        
        '20' : 'twenty ',
        '30' : 'thirty ',
        '40' : 'forty ',
        '50' : 'fifty ',
        '60' : 'sixty ',
        '70' : 'seventy ',
        '80' : 'eighty ',
        '90' : 'ninety ',

        '100' : 'one hundred ',
        '200' : 'two hundred ',
        '300' : 'three hundred ',
        '400' : 'four hundred ',
        '500' : 'five hundred ',
        '600' : 'six hundred ',
        '700' : 'seven hundred ',
        '800' : 'eight hundred ',
        '900' : 'nine hundred '
    }
    

    strnum = str(num)
    unit = ""
    tens = ""
    hundreds = ""

    if num == 0:
        return 'zero'
    elif int(strnum[-2:]) == 0:
        hundreds = numbers[strnum]

    elif len(strnum)== 3:
            strhun = str((int(strnum[0]) * 100))
            hundreds = numbers[strhun]
            if int(strnum[-2:])< 20 and int(strnum[-2:]) >= 10:
                tens = numbers[strnum[-2:]]
            elif int(strnum[-2:]) < 10:
                unit = numbers[strnum[-1]]

            else:            
                strtens = str((int(strnum[-2])*10))
                tens = numbers[strtens]
                if int(strnum[-1])<1:
                    tens = numbers[strtens]
                else:
                    strunit = numbers [strnum[-1]]
                    unit = strunit

    elif len(strnum) == 2:
        if int(strnum[-2:])< 20:
            tens = numbers[strnum[-2:]]
        else:            
            strtens = str((int(strnum[-2])*10))
            tens = numbers[strtens]
            if int(strnum[-1])<1:
                tens = numbers[strtens]
            else:
                strunit = numbers [strnum[-1]]
                unit = strunit
                
    elif len(strnum) == 1:
                strunit = numbers [strnum[-1]]
                unit = strunit
                
    text = hundreds + tens + unit     
    return text.strip()    



# Exercise 7
def missingComment(filename):
    '''(file) --> list

    Takes a filename, reads the file, idenitifies functions that are not immediately followed by a comment and returns a list of their names 

    >>> missingComment(input_file1)
        ["__init__", "overdrawn"]
    >>> missingComment(input_file2)
        []
    ''' 
    f = open(filename)

    funct_list = []
    prev_line = ''
    current_line = ''

    for line in f:
        if line.startswith('#') == True:
            prev_line = line
        elif line.startswith('def ') == True:
            current_line = line
            if prev_line == '':
                split_line = current_line[4:].split('(')
                funct_list.append(split_line[0])
        else:
            prev_line = ''
    
    return funct_list




# Exercise 8
def consistentLineLength(filename, length):
    ''' (file, int) --> list

    Take a filename and maximum length (int), open the file and read everyline, return a list of strings where everys string represents a line that is filled as much as possible without exceeding the given maximum length
    
    Precondition - int is positive
    
    >>> consistentLineLength(input_file, 50)
       ["Alice was beginning to get very tired of sitting",
        "by her sister on the bank, and of having nothing",
        "to do: once or twice she had peeped into the book",
        "her sister was reading, but it had no pictures or",
        'conversations in it,"and what is the use of a',
        'book," thought Alice, "without pictures or',
        'conversations?"]
    '''
    words = ''
    count = 0 
    line_list = []
    split_words = []


    f = open(filename)

    for line in f:
        split_words += line.split()

    for word in split_words:
        words += word + ' '
        count += 1
        try:
            next_word = split_words[count]
            if len(words + next_word) > length:
                line_list.append(words.strip())
                words = ''
        except:break
    line_list.append(words.rstrip())

    return line_list

# Exercise 9
def knight(start, end, moves):
    '''(str,str,str) --> bool

    Take three parameters initial position, final position and number of moves. Return True if a knight on an empty chessboard can get to the final position from the starting position in the max moves given else return False

    pre conditions - board is 8x8
        - Each cell is identified by its coordinates, a letter from a-h that identifies columns and a numbre from 1-8 that identifies rows.  The parameters are given in this format
        - Piece being used is the knight
        - Knight movement - two squares vertically and one square horizontally 

    >>> knight("a1", "c5", 2)
        True
    >>> knight("c2", "e3", 3)
        True
    >>> knight("c6", "h1", 3)
        False
    '''

    
    # |   |   | 0 |   |   |
    # | 0 |   |   | C | 0 |
    # |   |   | X |   |   |
    # |  0|   |   |   |  0|
    # |   | 0 |   | 0 |   |

    # frederico mentioned recursive so may need that here
    # x = knight
    # The knight cannot reach target cell c if it does not have moves left and it is not on cell c
    # the knight can reach target cell if cell c if its on a cell c
    # the kniwght can reach target cell c if it can reach it in one less move from one of the cells  
    

    return None


# Exercise 10
def warOfSpecies(environment):
    '''(list) --> list

    Takes an input of a list of strings of the same length, representing a rectangle grid, the char in the list represent the cells fo the grid (e.g ['X.......', '........', '.......O'] is a 3x8 grid, three substrings each 8 char in length). 
    
        Cells take three possible values:
                    - 'X' representing an individual of the species X
                    - 'O' representing an individual of the species O
                    - '.' representing an empty cell

    Return a list of str representing the next state of the environment according to the following rules:
            - An empty cell becomes non-empty if it is surronded by at least 2 individuals of the same species.  In the case of a draw between species the cell remains empty
            - A non-empty cell becomes empty if it is surrounded by more than six non-empty cells, regardless of its species
            - A non-empty cell becomes empty if it is surrounded by less than three members of its species
            - A non-empty cell become empty if it is surrounded by more members of the opposite species than members of its species
            - In an other circumstance, a cell does not change its value
    
    Pre condition - list of strings is in the correct format
    '''
    return None
