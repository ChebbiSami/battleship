"""this file is dedicated to the verification and execution of orders  """
import sys
def process_instructions(ships_list, order_list, battle_filed, map_size):
    """this function simply send extracted order to all ships"""
    for order in order_list:
        for ship in ships_list:
            if ship.serial_number == order["target_serial_number"]:
                if order["order_type"] != "END_OF_INSTRUCTION":
                    if order["order_type"] == "SUNK" and not ship.out_of_the_map:
                        battle_filed[ship.y_coordinate][ship.x_coordinate] = 0
                    ship.process_order(order["order_type"])
                else:
                    x_coor = ship.x_coordinate
                    y_coor = ship.y_coordinate
                    fall_off_word = False
                    if (x_coor >= map_size) or (y_coor >= map_size):
                        fall_off_word = True
                    if (x_coor < 0) or (y_coor < 0):
                        fall_off_word = True
                    if fall_off_word:
                        print("the ship number ", ship.serial_number, " fell off the world :'-(")
                        ship.out_of_the_map = True
                        continue
                    if battle_filed[y_coor][x_coor] != 0:
                        print("ship cannot be placed in an occupied location", file=sys.stderr)
                        sys.exit()
