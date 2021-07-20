"""this file is dedicated to the creation of the output content """
def create_output(ships):
    """this function prepare the test for the output"""
    output_text = ""
    for ship in ships:
        if ship.out_of_the_map:
            continue
        x_coor = ship.x_coordinate
        y_coor = ship.y_coordinate
        orient = ship.orientation
        sunc = ""
        if not ship.still_floating:
            sunc = "SUNK"
        output_text = output_text + "("+str(x_coor)+", "+str(y_coor)+", "+orient+") "+sunc+"\n"
    return output_text
