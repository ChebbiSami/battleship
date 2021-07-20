'''Welcome to the main file of the battlefileda'''
import sys
from parsing.parsing_args import parse_args
from parsing.parsing_file import parse_file
from processing.process_instructions.process_instructions import process_instructions
from processing.output import create_output

input_path, output_path, verbose = parse_args(sys.argv)
if verbose:
    print("opening file : ",input_path)
try:
    input_file = open(input_path, "r")
except OSError:
    print("Could not open file")
    sys.exit()
if verbose:
    print("parsing input file ")
battle_filed, map_size, ships_list, order_list = parse_file(input_file, verbose)
if verbose:
    print("processing instructions")
process_instructions(ships_list, order_list, battle_filed, map_size)
if verbose:
    print("preparing the output")
output_list = create_output(ships_list)
if verbose:
    print("writing on output file")
try:
    with open(output_path, "w") as output_file:
        output_file.write(output_list)
except OSError:
    print("Could not open file")
    sys.exit()

input_file.close()
output_file.close()
