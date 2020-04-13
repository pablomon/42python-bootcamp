import sys

if not sys.argv[1].isnumeric():
    print("ERROR")
    exit(0)
integer = int(sys.argv[1])
if integer == 0:
    print("I'm Zero.")
    exit(1)
reminder = integer % 2
if reminder == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")