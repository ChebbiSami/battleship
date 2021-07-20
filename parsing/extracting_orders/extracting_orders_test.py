"""this is a file test to test order extraction"""
import sys
sys.path.append("...")
from extracting_orders import extracting_orders
from classes.ship import Ship
import pytest


def test_sunk_order(capsys):
    """this function test issuing of SUNK order """
    order_list = []
    ships = [Ship(0, 7, 1, "E")]
    order_list = extracting_orders("(7, 1)", 10, order_list, ships)
    assert order_list[0]["order_type"] == "SUNK"
    assert order_list[0]["target_coordinate_x"] == 7
    assert order_list[0]["target_coordinate_y"] == 1
    assert order_list[0]["target_serial_number"] == 0

def test_moving_order(capsys):
    """this function test issuing of moving orders """
    order_list = []
    ships = [Ship(8, 6, 2, "W")]
    order_list = extracting_orders("(6, 2)RRMLMLLMMR", 10, order_list, ships)
    assert order_list[0]["order_type"] == "TURN_RIGHT"
    assert order_list[0]["target_coordinate_x"] == 6
    assert order_list[0]["target_coordinate_y"] == 2
    assert order_list[0]["target_serial_number"] == 8
    assert order_list[1]["order_type"] == "TURN_RIGHT"
    assert order_list[2]["order_type"] == "MOVE_FORWARD"
    assert order_list[3]["order_type"] == "TURN_LEFT"
    assert order_list[4]["order_type"] == "MOVE_FORWARD"
    assert order_list[5]["order_type"] == "TURN_LEFT"
    assert order_list[6]["order_type"] == "TURN_LEFT"
    assert order_list[7]["order_type"] == "MOVE_FORWARD"
    assert order_list[8]["order_type"] == "MOVE_FORWARD"
    assert order_list[9]["order_type"] == "TURN_RIGHT"
    assert order_list[10]["order_type"] == "END_OF_INSTRUCTION"

def test_wrong_number_of_argument(capsys):
    """this test wherever the function will stop a program with
     an error message in case it get more than one parameter"""
    order_list = []
    ships = [Ship(0, 7, 1, "E")]
    with pytest.raises(SystemExit) as err:
        extracting_orders("(7, 1) (17, 71)", 100, order_list, ships)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong arguments\n"

def test_wrong_arguments(capsys):
    """this test wherever the function will stop a program with
     an error message in case it get wrong arguments"""
    order_list = []
    ships = [Ship(0, 7, 1, "E")]
    with pytest.raises(SystemExit) as err:
        extracting_orders("(7, 1, 1)", 100, order_list, ships)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong arguments\n"
    with pytest.raises(SystemExit) as err:
        extracting_orders("(7,)", 100, order_list, ships)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong arguments\n"
    with pytest.raises(SystemExit) as err:
        extracting_orders(",)", 100, order_list, ships)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong arguments\n"
    with pytest.raises(SystemExit) as err:
        extracting_orders(")", 100, order_list, ships)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong arguments\n"
    with pytest.raises(SystemExit) as err:
        extracting_orders("", 100, order_list, ships)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong arguments\n"
    with pytest.raises(SystemExit) as err:
        extracting_orders("(b, a)", 100, order_list, ships)
    assert err.type == SystemExit
    out,err = capsys.readouterr()
    assert err == "Wrong arguments\n"

def test_out_of_map_order(capsys):
    """this test behavior of the function in case out of
     map order coordinate were given"""
    order_list = []
    ships = [Ship(0, 7, 1, "E")]
    extracting_orders("(17, 71)", 10, order_list, ships)
    out,err = capsys.readouterr()
    assert err == "You can not send orders to other words\n"
