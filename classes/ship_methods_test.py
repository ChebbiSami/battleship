"""this is a test file to test the execution of the order"""
from ship import Ship

def test_move_forward():
    """testing MOVE_FORWARD instruction"""
    ship = Ship(0, 0, 0, "N")
    ship.process_order("MOVE_FORWARD")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 1
    assert ship.orientation == "N"
    ship = Ship(0, 1, 1, "S")
    ship.process_order("MOVE_FORWARD")
    assert ship.x_coordinate == 1
    assert ship.y_coordinate == 0
    assert ship.orientation == "S"
    ship = Ship(0, 0, 0, "E")
    ship.process_order("MOVE_FORWARD")
    assert ship.x_coordinate == 1
    assert ship.y_coordinate == 0
    assert ship.orientation == "E"
    ship = Ship(0, 1, 1, "W")
    ship.process_order("MOVE_FORWARD")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 1
    assert ship.orientation == "W"

def test_move_left():
    """testing TURN_LEFT instruction"""
    ship = Ship(0, 0, 0, "N")
    ship.process_order("TURN_LEFT")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 0
    assert ship.orientation == "W"
    ship = Ship(0, 0, 0, "E")
    ship.process_order("TURN_LEFT")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 0
    assert ship.orientation == "N"
    ship = Ship(0, 0, 0, "S")
    ship.process_order("TURN_LEFT")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 0
    assert ship.orientation == "E"
    ship = Ship(0, 0, 0, "W")
    ship.process_order("TURN_LEFT")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 0
    assert ship.orientation == "S"

def test_move_right():
    """testing TURN_RIGHT instruction"""
    ship = Ship(0, 0, 0, "N")
    ship.process_order("TURN_RIGHT")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 0
    assert ship.orientation == "E"
    ship = Ship(0, 0, 0, "E")
    ship.process_order("TURN_RIGHT")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 0
    assert ship.orientation == "S"
    ship = Ship(0, 0, 0, "S")
    ship.process_order("TURN_RIGHT")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 0
    assert ship.orientation == "W"
    ship = Ship(0, 0, 0, "W")
    ship.process_order("TURN_RIGHT")
    assert ship.x_coordinate == 0
    assert ship.y_coordinate == 0
    assert ship.orientation == "N"

def test_sunc():
    """testing TURN_RIGHT instruction"""
    ship = Ship(0, 0, 0, "W")
    assert ship.still_floating is True
    ship.process_order("SUNK")
    assert ship.still_floating is False
