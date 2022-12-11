
def standardToMilitaryTime(time):
    hour = time[0:2]
    minutes = time[3:5]
    seconds = time[6:8]
    am_pm = time[8:10]
    
    if am_pm == "AM":
        if int(hour) == 12:
            hour = "0"
        else:
            diff = str(12 - int(hour))
            hour = str(12 - int(diff))
    else:
        if int(hour) != 12:
            hour = str(12 + int(hour))
    
    if int(hour) < 10:
        print(f"0{hour}:{minutes}:{seconds}")
    
    else:
        print(f"{hour}:{minutes}:{seconds}")