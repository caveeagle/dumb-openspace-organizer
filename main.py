import sys
import os
import json
import random

#################################################

DEBUG = 1

DEFAULT_COLLEAGUES_FILENAME = 'new_colleagues.csv'

DEFAULT_OUTPUT_FILENAME = 'out.txt'

DEFAULT_NUM_OF_TABLES = 6

DEFAULT_NUM_OF_SEATS_PER_TABLE = 4

RANDOM_SEED = None

#################################################


class Seat:
    """
    Represents a single seat in a table.

    Attributes:
        is_free (bool): True if the seat is available, False otherwise.
        occupant (str or None): Name of the person occupying the seat, or None if free.
    """

    def __init__(self, is_free: bool = True, occupant: str = None):
        """
        Initialize a Seat instance.

        Args:
            is_free (bool): Optional, default True. Whether the seat is free.
            occupant (str or None): Optional, default None. Name of the occupant.
        """
        self.is_free = is_free
        self.occupant = occupant

    def set_occupant(self, name: str):
        """
        Assign a person to this seat.

        Args:
            name (str): Name of the person to assign.

        Raise exception if the seat is already occupied.
        """
        if self.is_free:
            self.occupant = name
            self.is_free = False
        else:
            raise Exception('The seat is busy!')

    def remove_occupant(self):
        """
        Free the seat by removing its occupant.
        """
        self.occupant = None
        self.is_free = True

    def __str__(self):
        """
        Return a string representation of the seat.

        Returns:
            str: "Seat occupied by <name>" if occupied, "Empty seat" if free.
        """
        out_str = f'Seat occupied by {self.occupant}' if not self.is_free else 'Empty seat'
        return out_str


class Table:
    """
    Represents a table containing multiple seats.

    Attributes:
        capacity (int): Number of seats at the table.
        seats (list of Seat): List of Seat objects.
    """

    def __init__(self, capacity: int = DEFAULT_NUM_OF_SEATS_PER_TABLE):
        """
        Initialize a Table with a given capacity.

        Args:
            capacity (int): Number of seats at the table. Default is 4.
        """
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    @property
    def has_free_spot(self) -> bool:
        """
        Check if there is at least one free seat at the table.

        Returns:
            bool: True if a seat is free, False otherwise.
        """
        for seat in self.seats:
            if seat.is_free:
                return True
        return False

    def assign_seat(self, name: str):
        """
        Assign a person to the first available seat.

        Args:
            name (str): Name of the person to assign.

        Returns:
            bool: True if assignment was successful.

        Raises:
            Exception: If no seats are available.
        """
        for seat in self.seats:
            if seat.is_free:
                seat.set_occupant(name)
                return True
        raise Exception("No free seats available!")

    @property
    def left_capacity(self) -> int:
        """
        Count the number of free seats at the table.

        Returns:
            int: Number of free seats.
        """
        count = 0
        for seat in self.seats:
            if seat.is_free:
                count += 1
        return count

    def __str__(self):
        """
        Return a string representation of the table.
        """
        out_str = []
        for seat in self.seats:
            if seat.is_free:
                out_str.append('--free')
            else:
                out_str.append(seat.occupant)
        return '\nTable:' + "\n".join(out_str)


class Openspace:
    """
    Represents an open space containing multiple tables.

    Attributes:
        number_of_tables (int): Number of tables in the open space.
        table_capacity (int): Number of seats per table.
        tables (list of Table): List of Table objects.
    """

    def __init__(self,
                 number_of_tables: int = DEFAULT_NUM_OF_TABLES,
                 table_capacity: int = DEFAULT_NUM_OF_SEATS_PER_TABLE):
        """
        Initialize an Openspace with tables and seats.

        Args:
            number_of_tables (int): Number of tables. Default is 6.
            table_capacity (int): Number of seats per table. Default is 4.
        """
        self.number_of_tables = number_of_tables
        self.table_capacity = table_capacity
        self.tables = []
        for _ in range(number_of_tables):
            table = Table(capacity=table_capacity)
            self.tables.append(table)

    @property
    def seats_in_openspace(self) -> int:
        """
        How many seats are in the room (int)
        """
        return self.number_of_tables * self.table_capacity

    @property
    def people_in_openspace(self) -> int:
        """
        How many people are in the room (int)
        """
        return sum(1 for table in self.tables for seat in table.seats
                   if not seat.is_free)

    @property
    def free_seats_in_openspace(self) -> int:
        """
        How many free seats are in the room (int)
        """
        return sum(1 for table in self.tables for seat in table.seats
                   if seat.is_free)

    def organize(self, names: list[str]) -> None:
        """
        Assign people to seats across all tables.

        Args:
            names (list of str): List of people to assign.
        """

        if (len(names) > self.seats_in_openspace):
            raise ValueError('Error: There are more people than seats!')

        for name in names:
            assigned = False
            for table in self.tables:
                if table.has_free_spot:
                    table.assign_seat(name)
                    assigned = True
                    break
            if not assigned:
                print(f"No free seats available for {name}!")

        ### Free seats in case of empty name
        for table in self.tables:
            for seat in table.seats:
                if (seat.occupant == ''):
                    seat.remove_occupant()

    def room_to_string_by_people(self) -> str:
        """
        String representation of object, group by people
        """
        people_list = []
        tables_list = []
        seats_list = []
        for table_index, table in enumerate(self.tables):
            for seat_index, seat in enumerate(table.seats):
                if (not seat.is_free):
                    person = seat.occupant
                    assert person not in people_list
                    people_list.append(person)
                    tables_list.append(table_index)
                    seats_list.append(seat_index)
        ### End of cycle
        result_list = list(zip(people_list, tables_list, seats_list))

        result_list.sort(key=lambda x: x[0])  # Sort by name

        out_str = ''
        for p, t, s in result_list:
            out_str += f'{p} seats at the table {t} on the seat {s}\n'
        return out_str

    def room_to_string_by_tables(self) -> str:
        """
        String representation of object, group by people
        """
        out_str = ''
        for table_index, table in enumerate(self.tables):

            if (table_index != 0):
                out_str += '\n\n'
            out_str += f"# Table N{table_index+1}:"

            for seat_index, seat in enumerate(table.seats):
                if seat.is_free:
                    out_str += f"\n  @ N{seat_index+1}: ------"
                else:
                    out_str += f"\n  @ N{seat_index+1}: {seat.occupant}"
        ### End of cycle

        if (self.free_seats_in_openspace != 0):
            out_str += f'\n\n{self.free_seats_in_openspace} seats are still available.'
        else:
            out_str += f'\n\nNo seats are available.'

        return out_str

    def room_to_string_in_json(self) -> str:
        """
        String representation of object in json format
        """
        return json.dumps(self, default=lambda obj: obj.__dict__, indent=2)

    def __str__(self):
        return self.room_to_string_by_tables(self)

    def output(self, filename: str = None, mode: int = 1) -> None:
        """
        Output the current seating arrangement
        
        Modes:
            1 - by people
            2 - by tables
            3 - in json
            
        Args:
            mode (int): Mode of input
            filename (str): Path to the output file. If None or empty, prints JSON to console.
        """
        if mode not in (1, 2, 3):
            raise ValueError(
                "Mode in function 'output must be 1, 2 or 3: see documentation!"
            )

        out_str = ''
        if (mode == 1):
            out_str = self.room_to_string_by_people()
        elif (mode == 2):
            out_str = self.room_to_string_by_tables()
        elif (mode == 3):
            out_str = self.room_to_string_in_json()

        if (not filename):  # Print to console
            print(out_str)
        else:  # Write to file
            try:
                with open(filename, "w") as f:
                    f.write(out_str)
            except PermissionError:
                print(f"Permission denied: {filename}")
            except OSError as e:
                print(f"OS error while writing file {filename}: {e}")

    # End of def output


#################################################


def read_names_from_file(filename: str) -> list:
    """
    Read names from a text file, one name per line.

    Args:
        filename (str): Path to the input file.

    Returns:
        list of str: List of names read from the file. Empty lines are ignored.

    Notes:
        - Strips leading/trailing whitespace from each line.
        - Handles common file errors:
            * FileNotFoundError: prints a message if the file does not exist.
            * PermissionError: prints a message if access is denied.
            * OSError: prints a message for other OS-related file errors.
    """

    lines = []

    try:

        with open(filename, 'r') as my_file:

            lines = [line.strip() for line in my_file
                     if line.strip()]  # Exclude empty strings

    except FileNotFoundError:
        print("File not found:", DATA_DIR + filename)
    except PermissionError:
        print("Permission error:", DATA_DIR + filename)
    except OSError as e:
        print("General OS file error:", e)
    return lines


def openspace_test():

    ### first, test previous classes:
    seat_cls_test()
    table_cls_test()

    ###

    office_1 = Openspace(number_of_tables=2, table_capacity=3)

    office_1.tables[0].assign_seat("Alice")
    office_1.tables[0].assign_seat("Bob")
    office_1.tables[1].assign_seat("Charlie")

    test_collegues = [
        "Aleksei", "Amine", "Anna", "Astha", "Brigitta", "Bryan", "Ena",
        "Esra", "Faranges", "Frederic", "Hamideh", "Heloise", "Imran",
        "Intan K.", "Jens", "Kristin", "Michiel", "Nancy", "Pierrick",
        "Sandrine", "Tim", "Viktor", "Welederufeal", "Zivile"
    ]

    office_2 = Openspace()
    office_2.organize(test_collegues)

    ### All tests passed
    print('\nAll tests passed')


def table_cls_test():

    t = Table(3)

    assert t.capacity == 3
    assert t.left_capacity == 3
    assert t.has_free_spot is True

    seat_num1 = t.assign_seat("Alice")

    assert t.left_capacity == 2

    seat_num2 = t.assign_seat("Bob")
    seat_num3 = t.assign_seat("Cat")

    assert t.left_capacity == 0
    assert t.has_free_spot == False

    try:
        t.assign_seat('Charlie')
        assert False, 'Must be exception'
    except Exception as e:
        assert str(e) == 'No free seats available!'


def seat_cls_test():

    s = Seat()
    s.set_occupant("Alice")
    assert s.occupant == 'Alice'

    s.remove_occupant()
    assert s.is_free is True
    assert s.occupant is None

    s2 = Seat(False, 'Bob')
    assert s2.occupant == 'Bob'


#################################################

if __name__ == "__main__":

    if (DEBUG):
        openspace_test()
    ''' 
    Check the command line. 
    If the first parameter is filename - read it
    '''
    filename = DEFAULT_COLLEAGUES_FILENAME

    if (DEBUG):
        filename = 'test_colleagues.csv'

    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            filename = sys.argv[1]

    names_list = read_names_from_file(filename)

    random.seed(RANDOM_SEED)

    if (not DEBUG):
        random.shuffle(names_list)  # Shuffle names

    my_office = Openspace()

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

    if (not DEBUG):
        my_office.output(None, 2)
        my_office.output(DEFAULT_OUTPUT_FILENAME, 1)

    print('\n\nScript finished')

#################################################
