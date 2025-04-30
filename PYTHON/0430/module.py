
#내가 만든 파일에 있는거 갖다쓰기 야옹이 
import newModule 
classs = newModule.NewClass()
classs.sayHello()


# import sys
# print(sys.path)
from sys import path #일케 속성을 지정해버리면 앞에 sys 안 붙이고 사용 가능 (붙이면 안됨)
print(path)

strings = "abcdefghijklmnopqrstuvwxyz"
print(strings[3]) #3번 인덱스 출력
print(strings[-2]) #뒤에서 두번째
print(strings[0] + strings[5])
print(strings*2)
print(len(strings))
print(strings[1:20:2]) #1번 인덱스부터 2씩 건너뛰며 출력, 20번 인덱스 직전까지.

msg = " Hello world "
print(msg)
print(msg.strip())
print(msg.upper())
print(msg.upper().strip()) #메서드의 연쇄적 호출 (메모리 절약! 사본을 안 만들어서.)

myList = [3, 4, 7, 8, 1, 2, 5]
# copyList = myList # 이 방식은 id의 복사. 그냥 참조를 하나 늘리는거. 
copyList = list(myList) # 이 방식은 새로운 리스트를 만드는 듯.
#  
myList.sort()
print(f"my list\t\t:{myList}")
print(f"copied list\t:{copyList}") #원본과 독립적이구나 
print(f"sorted list\t:{sorted(copyList)}") #sorted는 sorting된 복사본을 반환. 
print(f"copied list\t:{copyList}") #원본에 영향주지 x  

engList = ['a', 's', 'd', 'f', 'q', 'w', 'e', 'r']
engList.sort(key=str.upper, reverse=True)
print(engList)

