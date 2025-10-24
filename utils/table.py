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

    def __init__(self, capacity: int):
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

