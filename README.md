# Battleship
the idea is to create a program that reads from a given input file the initial state of a map and a series of operations, 
then it output to a given output file the position of all ships and whether it has sunk or not

## Deploying environment
for lunshing the program the environement stored in bio-env.txt should be deployed 
<pre>
 conda env create --file bio-env.txt -name warship
 conda activate warship
</pre>
or you can just install in your environment numpy and pytest
<pre>
  pip3 install numpy
  pip3 install pytest
</pre>
## Usage
you can display options that can be used to launch the program by taping
<pre>
  python3 main.py -h
</pre>
witch gives
<pre>
  -h print this help message
  -i specify an input file 
  -o specify an output file
  -v verbose mode, print each step of the execution
</pre>
for lunching the programe type
<pre>
python3 main.py -i the_input_file -o output_4.txt -v
</pre>
Don't forget to replace "the_input_file" by a file that fit the requirement
The first line contains the size of the board. The second line contains a list of
coordinate-and-orientation tuples (initial position of the ships). Any subsequent lines are
operations: shoot operations (simply coordinates) and move operations (coordinates to specify
the ship to be considered and a sequence of 'L' (rotate left), 'R' (rotate right) and 'M' (move)).
Assume the bottom-left cell to be the origin (0, 0).

** EXAMPLE **

Input:

  10                      // Size of the board is 10x10

  (0, 0, N) (9, 2, E)     // 2 ships in different locations

  (0, 0) MRMLMM           // move/rotate the ship located at (0, 0)

  (9, 2)                  // shoot at (9, 2) and sink the ship if there is one
## testing 
To test the program simply type:
<pre>
pytest
</pre>
