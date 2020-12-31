"""
This module is responsible for generating csv files and 
writing iteration counts in rows to the file.
"""

import random

def test_function(fn, max_n, num_tests):
    """
    Parameters: fn - function taken from counting_quad_sorts module
                max_n - Max length of randomly generated list
                num_tests - Max number of tests (rows in the csv files)
    Returns: None
    """
    file_name = fn.__name__
    file = open(file_name + '.csv', 'w+')
    

    for i in range(num_tests):
       
        rand_list = [random.random() for x in range(max_n)] #Generate list of 100 random floats
        row = [] # Create a row for every test
        
        for n in range(max_n):
            row.append(fn(rand_list[:n]))
            # add each count for randomly sorted lists to the row
        for x in row:
            file.write(str(x) + ',')
        
        file.write('\n')
        # above line adds a new line character to move the 
        # pointer to the next line
    
    file.close()

if __name__ == '__main__':
    import counting_quad_sorts
    test_function(counting_quad_sorts.insertionSort, 100, 100)
    # the above line builds the CSV file and fills it with integer counts


