# This program is a WIP and is just a demo. It is also a program written by another program :)
# Most of the time you would just want to use the program 'crunch' instead of this
# as that program is faster and better...

# iterblock
generate blocks of strings for password dictionaries (all possible english words and beyond, up to 12 characters)

# Set the executable bit
chmod +x iterblock-control

# Generate some strings
./iterblock-block 
Starting iterblock.
Running iterblock on Linux data blah UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
Checking for CPUs...
Found 16 cores.
Working in /home partition.
Details of partition: 
Percentage of partition used is 
Free space on home is .
Allocating up to  per child process...
spawnchild1
Type the block generation starting point then press enter.
Examples: gen4i67 gen10 gen4c1 ... you can read more of them in iterblock.py. The function determines the start position of the block and the number of characters.

# Type out the name of the function you want to run.
gen4c1

# Then follow the prompt to continue to spawn child processes.

# Read iterblock.py to review the function names. The functions vary in characters used, starting position, and length of string.
