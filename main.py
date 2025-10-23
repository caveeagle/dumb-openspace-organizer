
import json

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
    def __init__(self, number_of_tables: int = 6, table_capacity: int = 4):
        self.number_of_tables = number_of_tables
        self.table_capacity = table_capacity

        self.tables = []
        for _ in range(number_of_tables):
            table = Table(capacity=table_capacity)
            self.tables.append(table)
    
    
    def organize(self, names: list[str]):

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
        for table_index, table in enumerate(self.tables):
            print(f"Table {table_index+1}:")
            for seat_index, seat in enumerate(table.seats):
                if seat.is_free:
                    print(f"  Seat {seat_index+1}: free")
                else:
                    print(f"  Seat {seat_index+1}: occupied by {seat.occupant}")

    def store(self, filename: str):
        json_str = json.dumps(self, default=lambda obj: obj.__dict__, indent=2)
        if( not filename):
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
    
    #office_1.display()
    
    office_2 = Openspace()
    office_2.organize(new_collegues)
    
    #office_2.display()
    
    office_1.store(None)
    office_2.store('out.txt')
 
 
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
    class_openspace_test()
    
#################################################


                 
