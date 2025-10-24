from .table import Seat, Table
from .openspace import Openspace
from .file_utils import read_names_from_file

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

    office_2 = Openspace(6,4)
    office_2.organize(test_collegues)

    ### All tests passed
    print('\nAll tests passed\n')


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


