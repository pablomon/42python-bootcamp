import sys

def filterwords(text, length):    
    words = text.split(" ")
    filtered = [w for w in words if len(w) > length]
    print(filtered)

def error():
    print("ERROR")
    exit(1)

if not len(sys.argv) is 3:
    error()
s = sys.argv[1]
l = sys.argv[2]
if s.isnumeric() or not l.isnumeric() :
    error()
    
filterwords(s, int(l))