for i in range(1,25):
    if(i<12):
        print(i,"AM")
    elif(i==12):
        print(i,"NOON")
    elif(i>12 and i!=24):
        print(i-12,"PM")
    elif(i==24):
        print("midnight")
