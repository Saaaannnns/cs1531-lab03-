def find_reverse(numbers):
    #TODO: find the reverse of the list
    numbers.reverse()
    #reversed()
    return numbers
    pass

def find_max(numbers):
    #TODO: find the maximum of the list
    numbers.sort(key = lambda x : -x)
    return numbers[0]
    pass

def find_min(numbers):
    #return min(numbers)
    #TODO: find the minimum of the list
    numbers.sort()
    return numbers[0]
    pass

def find_sum(numbers):
    #return sum(numbers)
    #TODO: find the sum of all the numbers in the list
    sum = 0
    for i in numbers:
        sum += i
    
    return sum
    pass

def find_average(numbers):
    #return sum(numbers)/len(numbers)
    #TODO: find the average of all the numbers in the list
    sum = 0
    count = 0
    for i in numbers:
        sum += i
        count = count + 1
        
    return sum/count
    pass

def find_descending(numbers):
    #TODO: numbers sorted in descending order
    numbers.sort(key = lambda x : -x)
    return numbers
    pass

def second_smallest(numbers):
    #TODO: find the second smallest
    numbers.sort()
    for i in range(0,len(numbers)):
        if numbers[i] == numbers[i+1]:
            i = i + 1
        else:
            return numbers[i+1]
    pass


'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    #return sorted(set(numbers),key=int)[k-1]
    #TODO: find the kth smallest number in the list
    numbers.sort()
    count = 2
    if k == 1:
        return numbers[0]
    else:
        for i in range(0,len(numbers)):
            if numbers[i] == numbers[i+1]:
                i = i + 1
            elif count < k:
                i = i + 1
                count = count + 1
            else:
                return numbers[i+1]
            
    pass
