
# age = input("나이를 입력하세요") #string으로 입력 받아짐 
# print(f"당신의 나이는 {age}세.") 
# n_age = int(age) #산술계산을 위해서는 형변환 필수 
# print(f"10년 후 당신의 나이는 {n_age+10}세.")

#제어문 
# score = int(input("점수를 입력하세요: "))
# grade = ''
# if score <= 100 and score >= 90:
#     grade = 'A'
# elif score < 90 and score >= 80:
#     grade = 'B'
# elif score < 80 and score >= 70:
#     grade = 'C'
# elif score < 70 and score >= 0:
#     grade = 'D'
# else:
#     grade = "not available"
# print(f"당신의 성적은 {grade}. ")


x = 10
if x == 10:
    result = True
else:
    result = False 
result = True if x == 10 else False


#딕셔너리를 이용한 스위치문 
myDict = {0:"Mon", 1:"Tue", 2:"Wed", 3:"Thu", 4:"Fri", 5:"Sat", 6:"Sun"}
print(myDict.get(0, "없는날짜"))
print(myDict.get(10, "없는날짜"))

#match를 이용한 스위치문 (최신기술)
day = 0
match day:
    case 0:
        print("Mon")
    case 1:
        print("Tue")
    #...
    case _:
        print("없는날짜")

count = 0
while count < 5:
    print(count)
    count += 1
    # if count > 3:
    #     break
else:
    print("while문이 break없이 정상종료됨 ")

for i in range(5):
    i += 1
    # if(count > 3):
    #     break
else:
    print("for문이 break 없이 정상종료 됨")

for _ in range(5):
    #걍 다섯번 반복하겟단거 임시변수 안쓰고 
    None

for num in [5, 10, 15, 20]:
    print(num)

for char in "STRING":
    print(char)
else:
    print("^-^")

#튜플 순회 
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

#딕셔너리 순회
info = {"name": "Alice", "age": 25}
for key, value in info.items():
    print(key, value)

#인덱스와 같이 순회
fruits = ['apple', 'banana', 'cherry']
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

#여러개 동시 순회
names = ['Tom', 'Jerry', 'Spike']
ages = [5, 3, 7]
for name, age in zip(names, ages):
    print(name, age)



for xxx in range(10, 100, 20):
    print(xxx)

arr = range(100, 0, -1)
print(type(arr))
print(arr)
print(arr[5])
myList = list(arr)
print(type(myList))
print(myList)
print(myList[5])

#예제: 완전수 찾기  
cnt = 0
for i in range(2, 1001):
    sum = 0
    for ii in range(1, i):
        if i%ii == 0:
            sum += ii
    if sum == i:
        cnt += 1
print(f"2-1000까지의 범위에서 완전수의 갯수는 {cnt}개.")


#n번째 피보나치 수열의 값 출력하기
N = int(input("숫자를 입력하세요: "))
n1 = 1
n2 = 1
result = 1
if(N > 2):
    for _ in range(2, N):
        result = n1+n2
        n1 = n2
        n2 = result

print(f"{N}번째 피보나치 수열의 숫자는 {result}입니다. ")

print(3/2) # 이샛기가 그냥 값이고 
print(3//2) #헐랭 임마가 몫이었구나 
print(3%2)