'''in this file are grouped the functions relating to the parsing
 of args'''

import sys

def parse_args(arg):
    '''this function parse the arguments'''
    inp = "input.txt"
    out = "output.txt"
    ver = False
    if len(arg) > 1:
        if (arg.count("-h") >1 or arg.count("-o") >1 or arg.count("-i") >1):
            print("Wrong arguments")
            sys.exit()
        if arg.count("-f") >1:
            print("Wrong arguments")
            sys.exit()
        if "-h" in arg:
            print("-h print this help message")
            print("-i specify an input file ")
            print("-o specify an output file")
            print("-v verbose mode, print each step of the execution")
            sys.exit()
        if "-i" in arg:
            if len(arg) <= (arg.index("-i") + 1):
                print("Wrong arguments")
                sys.exit()
            inp = (arg[arg.index("-i") + 1])
        if "-o" in arg:
            if len(arg) <= (arg.index("-o") + 1):
                print("Wrong arguments")
                sys.exit()
            out = (arg[arg.index("-o") + 1])
        if "-v" in arg:
            ver = True
    return inp, out, ver
