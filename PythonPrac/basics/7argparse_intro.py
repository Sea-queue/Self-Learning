import argparse

"""
Using the argparse:
-------------------
first: creating an ArgumentParser object
the ArgumentParser object will hold all the information necessary to parse the
command line into Python data types.
"""
parser = argparse.ArgumentParser(description='Process some integers.')

"""
second: Adding arguments
Filling an ArgumentParser with information about program arguments is done by
making calls to the add_argument() method. These calls tell the ArgumentParser
how to take the strings on the command line and turn them into objects.

This infromation is stored and used when parse_args() is called.

Later, calling parse_args() will return an object with two attributes, integers
and accumulate. The integers attribute will be a list of one or more ints, and
the accumulate attribute will be either the sum(), if --sum was specified at
the command line, or the max() function if it was not.
"""

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max, help='sum the integers')

"""
third: Parsing arguments
ArgumentParser parses arguments through the parse_args() method. This will
inspect the command line, convert each argument to the appropriate type and then
invoke the appropriate action. In most cases, this means a simple Namespace object
will be built up from attributes parsed out of the command line.

in a script, parse_args() will typically be called with no arguments, and the
ArgumentParser will automatically determine the command-line arguments from sys.argv.

parser.parse_args(['--sum', '7', '-1', '42'])
"""
args = parser.parse_args()
print(args.accumulate(args.integers))
