def kata(tuple):
    print("day_{:02d}, ex_{:02d} : {:.2f}, {:.2e}, {:.2e}"
    .format(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4]))


tuple = ( 0, 4, 132.42222, 10000, 12345.67)
kata(tuple)