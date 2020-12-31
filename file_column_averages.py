"""
This module contains a function which calculates the 
averages of each column in the csv files. These averages
are then used for plotting.
"""

def get_file_column_averages(filename):
    """
    This function

    Parameters: filename - name of the csv file to be opened
    Returns: averages - 2d list of column averages
    """

    myfile = open(filename, 'r')

    rows = myfile.readlines()
    # above line reads the file into separater lines
    row_list = []
    counter = 0 # set a counter variable for calculating averages

    for row in rows:
        strip = row.strip('\n')
        split = strip.split(',')
        split.pop(len(rows))
        #above line removes the useless characters 
        #at the end of the list
        row_list.append(split)
        counter += 1

    averages = []

    for i in range(len(row_list)):
        i_sum = 0
        for line in row_list:
            i_sum += float(line[i])
        i_average = i_sum / counter
        # above line calculates the average of the columns
        # by dividing the sum by the total number of elements (100).
        averages.append(i_average)

    return averages

if __name__ == "__main__":
    print(get_file_column_averages('optimizedBubbleSort'))
    # the above line returns a list of column averages as 
    # described in the assignment details.
