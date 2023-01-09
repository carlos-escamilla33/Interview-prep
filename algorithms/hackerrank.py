
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

# ------------------------

def solution(s1, s2):
    charCount = 128 * [0]
    for char in s1:
        aIdx = ord(char)
        charCount[aIdx]+=1
        
    count = 0
    for char in s2:
        aIdx = ord(char)
        val = charCount[aIdx]
        if val > 0:
            charCount[aIdx]-=1
            count+=1
    return count

s1 = "aabcc"
s2 = "adcaa"
# print(solution(s1, s2))