

#list와 deque의 속도 비교 

from time import time
from collections import deque
ranges = range(10 ** 7) #이게몰까 설마 10의 7승...?? 

li = []
start = time()
for i in ranges:
    li.append(i)
end = time()
print(f"list 소요시간\t: {end-start}")

deq = deque()
start = time()
for i in ranges:
    deq.append(i)
end = time()
print(f"deque 소요시간\t: {end-start}")
#deque가 좀 더 빠르네용


print(10**1)
print(10**2)
print(10**3) #헐 **n 하면 n제곱인가바

#deque의 사이즈 제한 기능(?)
limited = deque(maxlen=3)
limited.append(1)
limited.append(2)
print(limited)
limited.append(3)
limited.append(4) #꽉끼는데 넣으면 젤 옛날게 튕겨져 나가심 
print(limited)
limited.append(5)
print(limited)

#튜플플님
tup = (1, 2, 3, 4, 5)
# tup[3] = 5 #err!! 튜플은 이뮤터블입니당  
print(tup[3])



