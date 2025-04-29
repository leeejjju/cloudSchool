#형변환

age = "55"
print(type(age))
n_age = int(age)
# age = int(age) #이 형식은 비추!! 원본을 보존하는 방향으로 습관을 들여주세요 
print(type(n_age))

# test = int("0.1") #형변환 불가한 경우 오류 뱉음 

#int 사용법
# help(int)

#콘솔출력
help(print)
print("hello", "world", sep=" ", end="^^\n", file=None, flush=True)
print(1, 2, 3, sep="\t")

import math
print("소수점 둘째자리까지의 pi값: %.2f" %3.1415)
print(f"나의 나이는 {age}입니다.")

