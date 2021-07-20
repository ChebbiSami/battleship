'''in this file are grouped the functions relating to the parsing
 of files'''
import sys
import numpy as np
from parsing.extracting_orders.extracting_orders import extracting_orders
from parsing.extracting_ships.extracting_ships import extracting_ships


def extracting_map_size(line):
    '''extracting map size ,filtering unavailable map size lines
        and creating empy map
    '''
    line_component = line.split("//")
    no_comment = line_component[0]
    splited_no_comment = no_comment.split(" ")
    size = splited_no_comment[0]
    size = size.replace('\n', '')
    if not size.isdigit():
        print("only non-negative integer followed (or not) by comment")
        print("are accepted in the map size line")
        sys.exit()
    int_size = int(size)
    matrix = np.zeros([int_size, int_size], dtype=int)
    return int_size, matrix


def parse_file(input_file, verbose):
    '''this function parse the input file'''
    map_size = 0
    ships_list =[]
    order_list =[]
    contents = input_file.readlines()
    if len(contents) < 3:
        print("Wrong file format")
        sys.exit()

    for ind,content in enumerate(contents):
        if ind == 0:
            if verbose:
                print("++ creating map")
            map_size, battle_filed = extracting_map_size(content)
        if ind == 1:
            if verbose:
                print("++ creating ships")
            ships_list = extracting_ships(content, map_size, battle_filed)
        if ind >= 2:
            if verbose:
                print("++ extracting instructions of line ", ind + 1)
            order_list = extracting_orders(content, map_size, order_list, ships_list)
    return battle_filed, map_size, ships_list, order_list
