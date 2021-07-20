'''In this file are grouped the functions relating to the parsing
 of the instructions'''
import sys

def get_ship_id(coordinate_x, coordinate_y, ships):
    """this function take coordinate and retun the assosiated ship's id"""
    for ship in ships:
        if ship.x_coordinate == coordinate_x:
            if ship.y_coordinate == coordinate_y:
                return ship.serial_number
    return -42

def extracting_orders_types(cells):
    '''this function extract types of orders'''
    orders_types = []
    raw_cells = cells.replace(' ', '')
    raw_cells = raw_cells.replace('\n', '')
    raw_cells_len = len(raw_cells)
    if raw_cells_len == 0:
        return ["SUNK"]
    for sym in raw_cells:
        if sym not in ("M", "R", "L"):
            print("Wrong parameters", file=sys.stderr)
            sys.exit()
        if sym =="M":
            orders_types.append("MOVE_FORWARD")
        if sym =="R":
            orders_types.append("TURN_RIGHT")
        if sym =="L":
            orders_types.append("TURN_LEFT")
    orders_types.append("END_OF_INSTRUCTION")
    return orders_types

def extracting_target(cells):
    '''this function extract the target of the order'''
    error = False
    raw_cells = cells.replace(' ', '')
    raw_cells = raw_cells.replace('\n', '')
    raw_cells = raw_cells.split(sep = ",")
    if len(raw_cells)!=2:
        print("Wrong arguments", file=sys.stderr)
        sys.exit()
    if not raw_cells[0] or raw_cells[0][0] != '(':
        error = True
    raw_cells[0] = raw_cells[0].replace('(', '')
    if not raw_cells[0].isdigit() or not raw_cells[1].isdigit():
        error = True
    if error:
        print("Wrong arguments", file=sys.stderr)
        sys.exit()
    return int(raw_cells[0]), int(raw_cells[1])

def extracting_orders(line, map_size, order_list, ships):
    '''this function takes order line
    and return list of orders in dictionnarry format'''
    target_coordinate_x = 0
    target_coordinate_y = 0
    orders_types = ""
    line_component = line.split("//")
    raw_ships_params = line_component[0]
    cells_list = raw_ships_params.split(")")
    if len(cells_list) > 2:
        print("Wrong arguments", file=sys.stderr)
        sys.exit()
    target_coordinate_x , target_coordinate_y = extracting_target(cells_list[0])
    orders_types = extracting_orders_types(cells_list[1])
    for order_type in orders_types:
        if target_coordinate_x > map_size or target_coordinate_y > map_size:
            print("You can not send orders to other words", file=sys.stderr)
            continue
        order_list.append({
            "target_serial_number":get_ship_id(target_coordinate_x, target_coordinate_y, ships),
            "target_coordinate_x":target_coordinate_x,
            "target_coordinate_y":target_coordinate_y,
            "order_type":order_type
        })
    return order_list
