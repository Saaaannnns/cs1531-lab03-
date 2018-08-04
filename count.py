'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    pass
    # add your code here
    count = {}
    for char in text:
        count[char] = text.count(char)
    
    for char in count:
        print(char ,count[char])


def count_char_insensitive(text):
    pass
    # add your code here
    count = {}
    lower = text.lower()
    for char in lower: 
        count[char] = lower.count(char)
    
    for char in count:
        print(char,count[char])        


# bonus task:
def count_char_ordered(text):
    pass
    # add your code here
    count = {}
    lower = text.lower()
    start = lower[0]
    for char in lower:
        count[char] = lower.count(char)
    
    largest = count[start]
    while len(count) > 0:
        str = ''
        for char in count:
            if count[char] >= largest:
                largest = count[char]
                target = char
        print(target,largest)
        del count[target]
        
        for char in count:
            str += char
        
        if len(count) > 0:
            largest = count[str[0]]
    

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO,WorLd!'

# testing exercise 2
#count_char(text2)
#count_char_insensitive(text2)
count_char_ordered(text2)

