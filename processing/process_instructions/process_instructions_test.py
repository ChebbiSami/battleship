"""this file is dedicated to the verification
of the process_instructions function  """
import sys
sys.path.append("...")
import numpy as np
import pytest
from process_instructions import process_instructions
from classes.ship import Ship

#(ships_list, order_list, battle_filed, map_size)
#MOVE_FORWARD
#TURN_RIGHT
#TURN_LEFT
#END_OF_INSTRUCTION
def test_ship_same_location(capsys):
    """this test behavior of the function in cases
    orders lids ship on the location of other one"""
    order_list = [{"target_serial_number":1,
                    "target_coordinate_x":6,
                    "target_coordinate_y":1,
                    "order_type":"MOVE_FORWARD"
                    },
                    {"target_serial_number":1,
                    "target_coordinate_x":6,
                    "target_coordinate_y":1,
                    "order_type":"END_OF_INSTRUCTION"}]
    ships = [Ship(0, 7, 1, "E"),Ship(1, 6, 1, "E")]
    matrix = np.zeros([100, 100])
    matrix[1][7] = 1
    matrix[1][6] = 1
    with pytest.raises(SystemExit) as err:
        process_instructions(ships, order_list, matrix, 100)
        assert err.type == SystemExit
    out,err_ = capsys.readouterr()
    assert err_ == "ship cannot be placed in an occupied location\n"

def test_ship_out_of_map(capsys):
    """this test behavior of the function in cases
    orders lids ship out of the map"""
    order_list = [{"target_serial_number":0,
                        "target_coordinate_x":7,
                        "target_coordinate_y":1,
                        "order_type":"MOVE_FORWARD"
                        },{"target_serial_number":0,
                        "target_coordinate_x":7,
                        "target_coordinate_y":1,
                        "order_type":"MOVE_FORWARD"
                        },{"target_serial_number":0,
                        "target_coordinate_x":7,
                        "target_coordinate_y":1,
                        "order_type":"MOVE_FORWARD"},
                        {"target_serial_number":0,
                        "target_coordinate_x":7,
                        "target_coordinate_y":1,
                        "order_type":"MOVE_FORWARD"
                        },{"target_serial_number":0,
                        "target_coordinate_x":7,
                        "target_coordinate_y":1,
                        "order_type":"END_OF_INSTRUCTION"},]
    matrix = np.zeros([10, 10])
    ships = [Ship(0, 7, 1, "E")]
    process_instructions(ships, order_list, matrix, 10)
    out,err = capsys.readouterr()
    assert out == "the ship number  0  fell off the world :'-(\n"
