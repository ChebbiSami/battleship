"""In this file are grouped the functions relating to the extraction of ships"""
import sys
sys.path.append("...")
from classes.ship import Ship

def make_ship(cells, ind, battle_filed, map_size):
    '''this function is called to create a single instance of a ship
    and reject invalid ship lines'''
    error = False
    raw_cells = cells.replace(' ', '')
    raw_cells = raw_cells.replace('\n', '')
    raw_cells = raw_cells.split(sep = ",")
    if len(raw_cells)!=3:
        print("Wrong number of parameters to create a ship",file=sys.stderr)
        sys.exit()
    if raw_cells[0][0] != '(':
        error = True
    raw_cells[0] = raw_cells[0].replace('(', '')
    if not raw_cells[0].isdigit() or not raw_cells[1].isdigit():
        error = True
    if raw_cells[2] != "N" and raw_cells[2] != "S":
        if raw_cells[2] != "E" and raw_cells[2] != "W":
            error = True
    orient = raw_cells[2]
    if error:
        print("Wrong arguments", file=sys.stderr)
        sys.exit()
    if (map_size > int(raw_cells[1])) and (map_size > int(raw_cells[0])):
        if battle_filed[int(raw_cells[1])][int(raw_cells[0])] != 0:
            print("Wrong arguments", file=sys.stderr)
            sys.exit()
    x_coor = int(raw_cells[0])
    y_coor = int(raw_cells[1])
    if (map_size > y_coor) and (map_size > x_coor):
        battle_filed[y_coor][x_coor] = 1
    return Ship(int(ind), x_coor, y_coor, orient)

def extracting_ships(line, map_size, battle_filed):
    '''this function takes the ships coordinate line
     and return list of instance of ships'''
    ships_list = []
    line_component = line.split("//")
    raw_ships_params = line_component[0]
    cells_list = raw_ships_params.split(")")
    cells_list.pop()
    cells_list_len = len(cells_list)
    for ind in range(cells_list_len):
        single_ship = make_ship(cells_list[ind], ind, battle_filed, map_size)
        if single_ship.x_coordinate > map_size or single_ship.y_coordinate > map_size:
            print("the ship number ", str(ind), " fell off the world :'-(")
            continue
        ships_list.append(single_ship)
    return ships_list
