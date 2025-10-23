
new_collegues = ["Aleksei","Amine","Anna","Astha","Brigitta",
                 "Bryan","Ena","Esra","Faranges","Frederic",
                 "Hamideh","Heloise","Imran","Intan K.",
                 "Jens","Kristin","Michiel","Nancy","Pierrick",
                 "Sandrine","Tim","Viktor","Welederufeal","Zivile"]

#################################################

class Seat:
    def __init__(self, seat_number:int, is_free: bool = True, occupant: str = None):
        self.seat_number = seat_number
        self.is_free = is_free
        self.occupant = occupant

    def set_occupant(self,name):
        if self.is_free:
            self.occupant = name
            self.is_free = False
        else:
            raise Exception(f'The seat {self.seat_number} is busy!')    
    
    def remove_occupant(self):
        self.occupant = None
        self.is_free = True    
        
    
#################################################

if __name__ == "__main__":
    pass

                 
