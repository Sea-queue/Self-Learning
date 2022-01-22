import argparse

parser = argparse.ArgumentParser()

# Positional Arguments:
# parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="display a square of a given number", type=int)

# Optional Arguments:
# v1:
# parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                     action="store_true")

# v2:
# parser.add_argument("-v", "--verbosity", type=int, choices=[0,1,2],
#                     help="increse output verbosity")

# v3:
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")

args = parser.parse_args()
answer = args.square**2

# print(args.echo)
# print(args.square**2)

# v1:
# if args.verbose:
#     print(f"the square of {args.square} equals {answer}")
# else:
#     print(answer)


# v2:
# if args.verbosity == 2:
#     print(f"the square of {args.square} equals {answer}")
# elif args.verbosity == 1:
#     print(f"{args.square})^2 == {answer}")
# else:
#     print(answer)

if args.verbosity >= 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity >= 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)
