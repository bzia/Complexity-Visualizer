"""
This module contains four sorting algorithms which 
can be used in other models to generate empirical data.
"""

def bubbleSort(items):
    """
    Orders the items from lowest to highest value
    
    Parameters: items - list to be sorted
    Returns: count - number of times the loop has been iterated 
    """
    swapped = True
    count = 0 
    while swapped:
        swapped = False
        for i in range(1,len(items)):
            if items[i-1] > items[i]:
                items[i-1], items[i] = items[i], items[i-1] # Swap values
                swapped = True
            count += 1 
    
    return count

def optimizedBubbleSort(items):
    """
    Optimized version of classic bubble sort which 
    orders the items from lowest to highest value 
    
    Parameters: items - list to be sorted
    Returns: count - number of times the loop has been iterated 
    """
    count = 0
    n = len(items)
    swapped = True
   
    while swapped:
        count += 1
        swapped = False
        for i in range(1, n):
            count += 1
            if items[i-1] > items[i]:
                items[i-1], items[i] = items[i], items[i-1]
                swapped = True
        n -= 1
    
    return count

def selectionSort(items):
    """
    Orders the items from lowest to highest value
   
    Parameters: items - list to be sorted
    Returns: count - number of times the loop has been iterated 
    """
    
    count = 0 # for analysis only
    n = len(items)
    for i in range(n-1):
        count += 1
        min = i
        for j in range(i + 1,n):
            if (items[j] < items[min]):
                min = j
            count += 1 
        if (min != i):
            items[i], items[min] = items[min], items[i] # Swap Values

    return count

def insertionSort(items): 
    """
    Orders the items from lowest to highest value

    Parameters: items - list to be sorted
    Returns: count - number of times the loop has been iterated 
    """
    
    count = 0
    # Traverse from 1 to the length of the list. 
    for i in range(1, len(items)): 
        count += 1
        key = items[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < items[j]: 
                count += 1
                items[j + 1] = items[j] 
                j -= 1
        items[j + 1] = key 
    
    return count


if __name__ == '__main__':
    print(bubbleSort([9,8,7,6,5,4,3,2,1]))
    print(optimizedBubbleSort([9,8,7,6,5,4,3,2,1]))
    print(selectionSort([9,8,7,6,5,4,3,2,1]))
    print(insertionSort([9,8,7,6,5,4,3,2,1]))
    # The above code prints the loop iterations ('count')
    # for each of the 4 sorting algorithms.

