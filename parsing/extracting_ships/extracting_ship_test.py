"""this is a test file to test the parsing"""
from extracting_ships import extracting_ships
import numpy as np
import pytest

def test_normal_ships():
    """testing if function creates ships with good parameters"""
    matrix = np.zeros([100, 100])
    ships_list = extracting_ships("(12, 45, N)(56, 18, S)(19, 20, W)", 100, matrix)
    ship_one = ships_list[0]
    ship_two = ships_list[1]
    ship_three = ships_list[2]
    assert ship_one.x_coordinate == 12
    assert ship_one.y_coordinate == 45
    assert ship_one.orientation == "N"
    assert ship_two.x_coordinate == 56
    assert ship_two.y_coordinate == 18
    assert ship_two.orientation == "S"
    assert ship_three.x_coordinate == 19
    assert ship_three.y_coordinate == 20
    assert ship_three.orientation == "W"


def test_same_location_ships(capsys):
    """testing if function exit when two ships are in the same location"""
    matrix = np.zeros([100, 100])
    with pytest.raises(SystemExit) as err:
        extracting_ships("(12, 45, N)(56, 18, S)(12, 45, W)", 100, matrix)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong arguments\n"

def test_wrong_number_of_argument(capsys):
    """testing if function exit when wrong number of arguments is given"""
    matrix = np.zeros([100, 100])
    with pytest.raises(SystemExit) as err:
        extracting_ships("(12, 45, 13, N)(56, 18, S)(12, 45, W)", 100, matrix)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong number of parameters to create a ship\n"

def test_bad_arguments(capsys):
    """testing if function exit when bad arguments is given"""
    matrix = np.zeros([100, 100])
    with pytest.raises(SystemExit) as err:
        extracting_ships("(45, 13, N)(56, s, S)", 100, matrix)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong arguments\n"

def test_fell_off_edge(capsys):
    """tests if the function takes care of the case where the
    coordinates of the ship are out of the map"""
    matrix = np.zeros([100, 100])
    extracting_ships("(109, 13, N)", 100, matrix)
    out,err = capsys.readouterr()
    assert out == "the ship number  "+str(0)+"  fell off the world :'-(\n"
