
def kata(a):
    s = "The {} numbers are:".format(len(a))
    for n in a:
        s += " " + str(n)
    print(s)
    
t = (19,42,21)
kata(t)