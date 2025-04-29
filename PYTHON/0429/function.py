
print(dir(__builtins__))

help(sum)
arr = [1, 2, 3, 4, 5]
print(sum(arr))
print(sum(arr, 3)) #초기값

help(max)
print(max(arr)) #쩐다... 
print(max(1, 3, 5, 7, 10))

def func(param, param2):
    aa = param + param2
    bb = param - param2
    cc = max(param, param2)
    return aa, bb, cc #여러개 동시리턴이 된다구요?

rst = func(1, 2)
print(type(rst)) #여러개를 리턴하면 튜플로 나옴 

a = 10
b = 20
def swap(aaaa:int, bbbb:int)->int:
    return bbbb, aaaa

print(f"a: {a}, b: {b}")
a, b = swap(a, b) #ㅇㅏ니 이게 문법이 말이 되냐 파이썬 혼자 사기치네 
print(f"a: {a}, b: {b}")
print(swap(bbbb=10, aaaa=5)) #파라미터에 이름을 지정해서 넣으면 순서 노상관해도 됨 

def callByValue(num:int)->None:
    num += 10
    return None

def callByReference(nums:list)->None:
    nums.append(100)
    return None

value = 10
values = [10, 20, 30, 40, 50]
print(f"value: {value}, ref: {values}")
callByValue(value)
callByReference(values)
print(f"value: {value}, ref: {values}") #scalar는 변경되지 않고, vector는 변경됨!!

def sayHello(): #매개변수 없어도 ㄱㅊ 
    print("Hello ^u^")
sayHello()

#파라미터에 기본값 설정. 단, 한번 설정하면 그 이후의 모든 파라미터는 기본값을 설정해야... (순서땜시 그런듯)
def paramTest(test, param1 = 0, param2 = 0):
    return test + param1 + param2
print(paramTest(5)) #초기값 활용 
print(paramTest(5, 5, 5)) #전부 지정해서 넘김 

ll = [1, 2, 3]
print(paramTest(*ll)) #리스트 등을 압축해제시켜 대입한 경우. (앞에 *붙이기)
ll.append(4) #일케 원소숫자가 파라미터 갯수랑 안 맞는 상태에서 하면
# print(paramTest(*ll)) #오류가 나옵니다 

myDict = {'test': 10, 'param1': 10, 'param2': 10} #약간 쁘띠 구조체 느낌 있네요.. json같기도 하구 
print(paramTest(**myDict))

def flexableParam1(first, *second):
    return first + max(second)
print(flexableParam1(10, 5, 10, 15, 20)) # 5~20까지가 second에 튜플로 들어감 

#딕셔너리 가변 매개변수는 어케 쓰는거람? 
def flexableParam2(**second):
    print(second)
flexableParam2(**myDict) #이미 있는 딕셔너리를 넣는건 알겟는디 
#아예 값만 대충 때려넣는건 안되남... 내가 너무 날먹을 바라는걸까?? 
flexableParam2(name="park", age=15, gender="Male") #아~~~역시 가능하다고 하네요~~~ 

#재귀 예시 - 피보나치
def fibo(n:int)->int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(10))

#pass함수: 추상적으로.. 이름만 대충 야옹이 할 때 에러나지 않게 내용 부분에 넣는거래요
def passFunc():
    pass #지나가욥~

passFunc() #그럼 호출하면 어케되는거?
#아무 일도... 없었다...! 

variable = passFunc #함수를 다른 변수에 대입해버리기 
variable() #오우 
#약간 c에 함수포인터 느낌이네요 
print(type(passFunc))
print(type(variable))

#람다함수 사용처이기도 한 친구들
datas = [10, 20, 30]
#기존 배열에 전부 2를 더한 새로운 배열을 만들고싶어용
def f(a):
    return a+2
print(list(map(f, datas))) #기존함수 쓰기
print(list(map(lambda a: a+2, datas))) #람다(일회용)함수 쓰기 

#진짜 맵이 반복문보다 빠른가?
import datetime

li = [i for i in range(100000)] # 큰 데이터

start = datetime.datetime.now()
for tmp in li:
    f(tmp)
end = datetime.datetime.now()
print(f"반복문 소요시간\t: {end-start}")

start = datetime.datetime.now()
map(lambda a:a+2, li)
end = datetime.datetime.now()
print(f"맵 소요시간\t: {end-start}")
