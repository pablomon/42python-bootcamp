
def kata(time):
    if len(time) != 5:
        print("ERROR.")
    day     = time[4] 
    month   = time[3] % 12
    year    = time[2]
    hour    = time[0] % 24
    minute  = time[1] % 60
    sTime = "{}/{}/{} {}:{}".format(month,day,year,hour,minute)
    print(sTime)

time = (3,30,2019,9,25)
kata(time)