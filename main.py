import sys
import os
import random

from utils.table import Seat, Table
from utils.openspace import Openspace
from utils.file_utils import read_names_from_file
from utils.tests import openspace_test

#################################################

DEBUG = 1

DEFAULT_COLLEAGUES_FILENAME = 'new_colleagues.csv'

DEFAULT_OUTPUT_FILENAME = 'out.txt'

DEFAULT_NUM_OF_TABLES = 6

DEFAULT_NUM_OF_SEATS_PER_TABLE = 4

RANDOM_SEED = None

#################################################

if __name__ == "__main__":

    if (DEBUG):
        openspace_test()
    ''' 
    Check the command line. 
    If the first parameter is filename - read it
    '''
    filename = DEFAULT_COLLEAGUES_FILENAME

    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            filename = sys.argv[1]

    names_list = read_names_from_file(filename)

    random.seed(RANDOM_SEED)

    random.shuffle(names_list)  # Shuffle names

    my_office = Openspace(DEFAULT_NUM_OF_TABLES,DEFAULT_NUM_OF_SEATS_PER_TABLE)

    ######################################################
    
    # Check if there are more people than seats
    
    if (len(names_list) > my_office.seats_in_openspace):
        print('There are no free seats for ALL people!')
        try:
            print("Do you want to leave some random people behind?")
            type_input = input("Type Y/N: ")
            if (type_input in ('Y', 'y')):
                names_list = names_list[:my_office.seats_in_openspace]
            else:
                print("Sorry: in this case script can't do anything!")
                raise SystemExit(0)

        except EOFError:
            print("\nYou are not in the console.")
            print("Error: script can't do anything!")
            raise SystemExit(0)

    ######################################################
    
    # Check loneliness
    
    if (len(names_list) % DEFAULT_NUM_OF_SEATS_PER_TABLE == 1):
        '''
        I don't like doing something through objects 
        if it can be done with functions. 
        This code checks that a person is sitting at the table 
        alone and moves another person. 
        The code does this in the simplest way possible!
        '''
        names_list.append('')
        names_list[-3], names_list[-1] = names_list[-1], names_list[-3]

    ######################################################

    my_office.organize(names_list)

    my_office.output(None, 2)
    my_office.output(DEFAULT_OUTPUT_FILENAME, 1)

    print('\n\nScript finished')

#################################################
