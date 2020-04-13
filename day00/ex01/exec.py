import sys

separator = " "
args = separator.join(sys.argv[1:])
swapped = args.swapcase()
reversed = ''.join(reversed(swapped))
print(reversed)