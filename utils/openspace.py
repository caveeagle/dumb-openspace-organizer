import json
from .table import Seat, Table

class Openspace:
    """
    Represents an open space containing multiple tables.

    Attributes:
        number_of_tables (int): Number of tables in the open space.
        table_capacity (int): Number of seats per table.
        tables (list of Table): List of Table objects.
    """

    def __init__(self,
                 number_of_tables: int,
                 table_capacity: int):
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
            table = Table(table_capacity)
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


