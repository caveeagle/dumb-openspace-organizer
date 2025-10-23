
import json

#################################################

DEBUG = 1

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
    def __init__(self, capacity: int = 4):
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
    def __init__(self, number_of_tables: int = 6, table_capacity: int = 4):
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

    def organize(self, names: list[str]) -> None:
        """
        Assign people to seats across all tables.

        Args:
            names (list of str): List of people to assign.
        """
        for name in names:
            assigned = False
            for table in self.tables:
                if table.has_free_spot:
                    table.assign_seat(name)
                    assigned = True
                    break
            if not assigned:
                print(f"No free seats available for {name}!")  

    def __str__(self):
        """
        Return a string representation of the Openspace.

        Returns:
            str: Status of all tables and their seats.
        """
        out_str = ''
        for table_index, table in enumerate(self.tables):
            out_str += f"Table {table_index+1}:"
            for seat_index, seat in enumerate(table.seats):
                if seat.is_free:
                    out_str += f"\n  Seat {seat_index+1}: free"
                else:
                    out_str += f"\n  Seat {seat_index+1}: occupied by {seat.occupant}"
        return out_str

    def display(self):
        """
        Print the current seating arrangement to the console.
        """
        print(str(self))

    def store(self, filename: str) -> None:
        """
        Store the seating arrangement in a JSON file.

        Args:
            filename (str): Path to the output file. If None or empty, prints JSON to console.
        """
        json_str = json.dumps(self, default=lambda obj: obj.__dict__, indent=2)
        if not filename:
            print(json_str)
        else:
            with open(filename, "w") as f:
                f.write(json_str)
    
        
                    
#################################################

def class_openspace_test():
    
    office_1 = Openspace(number_of_tables=2, table_capacity=3)

    office_1.tables[0].assign_seat("Alice")
    office_1.tables[0].assign_seat("Bob")
    office_1.tables[1].assign_seat("Charlie")
    
    #office_1.display() # USE capsys from pytest !! 

    test_collegues = ["Aleksei","Amine","Anna","Astha","Brigitta",
                     "Bryan","Ena","Esra","Faranges","Frederic",
                     "Hamideh","Heloise","Imran","Intan K.",
                     "Jens","Kristin","Michiel","Nancy","Pierrick",
                     "Sandrine","Tim","Viktor","Welederufeal","Zivile"]

    
    office_2 = Openspace()
    office_2.organize(test_collegues)
    
    #office_2.display()
    
    #office_1.store(None)
    #office_2.store('out.txt')
 
 
def class_table_test():

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
    
def read_names_from_file(filename:str)->list:
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
        
            lines = [line.strip() for line in my_file if line.strip()]  # Exclude empty strings
            
        if(DEBUG):
            print(lines)    
    
    except FileNotFoundError:
        print("File not found:", DATA_DIR + filename)
    except PermissionError:
        print("Permission error:", DATA_DIR + filename)
    except OSError as e:
        print("General OS file error:", e)
    return lines

def class_seat_test():
    
    s = Seat()
    s.set_occupant("Alice")
    assert s.occupant == 'Alice'     

    s.remove_occupant()
    assert s.is_free is True
    assert s.occupant is None
    
    s2 = Seat(False,'Bob')
    assert s2.occupant == 'Bob'
    
          
#################################################

if __name__ == "__main__":
    
    if(DEBUG):
        class_seat_test()
        class_table_test()
        class_openspace_test()
        
        read_names_from_file('new_colleagues.csv')

    ### All tests passed
    print('\nAll tests passed')
    
#################################################


                 
