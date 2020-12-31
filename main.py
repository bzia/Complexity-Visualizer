"""
This module imports other modules and their functions
to build a user interface and drive the program.
"""

import menu
import plotter
import counting_quad_sorts
from collect_function_performance_data import *
from file_chooser import *
from file_column_averages import *

MAX_N = 100 # Maximum length of randomly generated lists
NUM_TESTS = 100 # Number of tests to run on each chosen sort.


def main():
    
    choices_1 = ['Generate Sort Times Files', 'Plot Average Sort Times']
    choices_2 = ['Bubble Sort', 'Optimized Bubble Sort', 'Selection Sort', 'Insertion Sort']
    # the 2 above lines are options for the menu prompted below

    while True:

        choice_1 = menu.do_menu('Main Menu', choices_1)
    
        if choice_1 is None:
            break
        
        while True:
            if choice_1 == 1:
                choice_2 = menu.do_menu('Select a Sort:', choices_2)
                if choice_2 == 1:
                    test_function(counting_quad_sorts.bubbleSort, MAX_N, NUM_TESTS)
                    break
                elif choice_2 == 2:
                    test_function(counting_quad_sorts.optimizedBubbleSort, MAX_N, NUM_TESTS)
                    break
                elif choice_2 == 3:
                    test_function(counting_quad_sorts.selectionSort, MAX_N, NUM_TESTS)
                    break
                elif choice_2 == 4:
                    test_function(counting_quad_sorts.insertionSort, MAX_N, NUM_TESTS)
                    break
                elif choice_2 is None:
                    break

            elif choice_1 == 2:
                path = get_file_path_and_name(pattern='*.csv') # filter for csv files only
                if path is None:
                    break # return to main loop if path resolves to none
                print("Calculating averages")
                averages = get_file_column_averages(path[1])

                plots = plotter.plot(title='plot of ' + path[1] + ' iterations', 
                                    origin_x = 5, origin_y = 5, scale_x = 6, 
                                    scale_y = 0.11, bg = 'yellow')

                plots['draw_axes'](tick_length = 1, tick_interval_y = 100)
                x = 0
                for i in averages:
                    plots['plot_point'](x, i, diam = 5, colour = 'black')
                    x+=1
                plots['block']()

main()


