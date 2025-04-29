import time

sec = 0
min = 0
hour = 0

while 1:
    sec = sec + 1
    if sec == 60:
        min = min+1
        sec = sec%60
    if min == 60:
        hour = hour+1
        min = min%60
    if hour == 24:
        hour = hour%24
    
    # print(hour,":",min,":",sec)
    print("%02d:%02d:%02d\n"% (hour, min, sec)) #포맷팅 
    time.sleep(1)#sleep 10 second

# i = 0
# names= ["KIA", "HYUNDAI", "DAEWOO"]
# while i < 50:
#     print(names[i%3])
#     i = i + 1
#     time.sleep(0.5)