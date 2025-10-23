
import random

#################################################

new_collegues = ["Aleksei","Amine","Anna","Astha","Brigitta",
                 "Bryan","Ena","Esra","Faranges","Frederic",
                 "Hamideh","Heloise","Imran","Intan K.",
                 "Jens","Kristin","Michiel","Nancy","Pierrick",
                 "Sandrine","Tim","Viktor","Welederufeal","Zivile"]

#################################################

class Seat:
    def __init__(self, is_free: bool = True, occupant: str = None):
        self.is_free = is_free
        self.occupant = occupant

    def set_occupant(self,name):
        if self.is_free:
            self.occupant = name
            self.is_free = False
        else:
            raise Exception(f'The seat is busy!')    
    
    def remove_occupant(self):
        self.occupant = None
        self.is_free = True    

class Table:
    def __init__(self, capacity: int = 4):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]

    @property
    def has_free_spot(self) -> bool:
        for seat in self.seats:
            if seat.is_free:
                return True
        return False

    def assign_seat(self, name: str):
        for seat in self.seats:
            if seat.is_free:
                seat.set_occupant(name)
                return True  
        # Cycle has finished
        raise Exception("No free seats available!") 
    
    @property
    def left_capacity(self) -> int:
        count = 0
        for seat in self.seats:
            if seat.is_free:
                count += 1
        return count

class Openspace:
    def __init__(self, number_of_tables: int):
        self.number_of_tables = number_of_tables
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]

    def organize(self, names: list[str]):

        random.shuffle(names) 

        for name in names:
            assigned = False
 
            for table in self.tables:
                if table.has_free_spot:
                    table.assign_seat(name)
                    assigned = True
                    break
            if not assigned:
                print(f"No free seats available for {name}!")  

    def display(self):
        pass

    def store(self, filename: str):
        pass
                    
#################################################

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
    


def class_seat_test():
    
    s = Seat()
    s.set_occupant("Alice")
    assert s.occupant == 'Alice'     

    s.remove_occupant()
    assert s.is_free is True
    assert s.occupant is None
    
    s2 = Seat(False,'Bob')
    assert s2.occupant == 'Bob'
    
    ### All tests passed
    print('\nAll tests passed')
          
#################################################

if __name__ == "__main__":
    class_seat_test()
    class_table_test()

#################################################


                 
