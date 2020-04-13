import sys

def operations(a, b):    
    adition     = a + b
    print('{:13} {}'.format('Sum', adition))
    difference  = a - b
    print('{:13} {}'.format('Difference', difference))
    product     = a * b
    print('{:13} {}'.format('Product', product))
    if (b is 0):
        quotient = "ERROR (div by zero)"
        remainder = "ERROR (modulo by zero)"
    else:
        quotient    = a / b
        remainder   = a % b

    print('{:13} {}'.format('Quotient', quotient))
    print('{:13} {}'.format('Remainder', remainder))

usage = 'Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3'
if len(sys.argv) is 0:
    print(usage)
    exit(0)
    
error = ''
if len(sys.argv) < 3:
    error = 'Input error: Too few arguments'
elif len(sys.argv) > 3:
    error = 'Input error: Too many arguments'
else:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    if (not arg1.isnumeric()) or (not arg2.isnumeric()):
        error = 'Input error: Only numbers'

if len(error) > 0:
    print(error)
    print(usage)
    exit(1)

operations(
    int(sys.argv[1]) ,
    int(sys.argv[2])
)