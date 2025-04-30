
#클래스의 메서드 사용하기 
print(dir(str))
help(str.upper)
ss = "hello world" #string class의 인스턴스인 ss입니다. 

print(ss.upper().lower()) #bound 호출
print(str.upper(ss)) #unbound 호출 (첫 인자로 인스턴스 대입, self 자리임!)

def compare(self):
    #id끼리의 비교는 == 연산자 대신 is를 사용합니다. 
    if Student.schoolName is self.schoolName:
        print("두 속성은 같습니다. ")
    else:
        print("두 속성은 같지 않습니다.")
    print()

#클래스 만들어보기
class Student:
    schoolName = "meow elementary school" #이렇게 선언한거는 클래스 속성이 됩니다. 
    
    @staticmethod
    def sayHello()->None: 
        print("Hello! ")


    #일케 쓰는게 맞나?? 
    __doc__ = "this is Students class that contain name and age, and some acts"

    def __init__(self, name="NONAME", age=0): #초기값도 주는거 개추요 
        self.name = name
        self.age = age

    def __del__(self): #소멸자, 인스턴스 소멸될 때 호출, 보통 프로그램 종료시. 
        print(f"Student {self.name} is gone...")

    def setName(self, name:str)->None:
        self.name = name
    def setAge(self, age:int)->None:
        self.age = age

    def getName(self)->str:
        return self.name
    def getAge(self)->int:
        return self.age

    def introduce(self)->None:
        print(f"My name is {self.name} and I'm {self.age} years old.")
        



Student.sayHello() #이건 인스턴스 없이도 가넝 
# Student.introduce() #이건 곤란. 

JJLee = Student()
JJLee.setName("JJLee")
JJLee.setAge(24)

JJLee.sayHello() 
JJLee.introduce()
Student.introduce(JJLee)

HMPark = Student("HMPark", 23) #init 활용한 초기화 
HMPark.introduce()

#클래스로 접근해서 속성을 변경하면 바뀜 
Student.schoolName = "meow middle school"
print(f"클래스 속성\t: {Student.schoolName}")
print(f"인스턴스 속성\t: {JJLee.schoolName}")
compare(JJLee)

#인스턴스로 접근해서 속성을 변경하면 원본은 접근 못하고 자기만의 속성으로 만들어 바꿔버림 
JJLee.schoolName = "meow high school"
print(f"클래스 속성\t: {Student.schoolName}")
print(f"인스턴스 속성\t: {JJLee.schoolName}")
compare(JJLee)

#한번 인스턴스 속성이 된 아이는 더이상 원본 변경에 영향받지 x  
Student.schoolName = "meow university"
print(f"클래스 속성\t: {Student.schoolName}")
print(f"인스턴스 속성\t: {JJLee.schoolName}")
compare(JJLee)

import sys
#가비지컬렉션한테 정리당해버리는 거 구경하기 
tmpStd = Student(name="tmp1")
print(f"tmpStd의 참조 횟수: {sys.getrefcount(tmpStd)-1}")
ref = tmpStd
print(f"tmpStd의 참조 횟수: {sys.getrefcount(tmpStd)-1}")

tmpStd = Student(name="tmp2") #tmp1은 바꿔치기 해버리기 
# ref.introduce() #아직 tmp1를 가리키는 애가 있어서 생존.
tmpStd = None #이름 빼앗아버리기 -> 이 시점에서 tmp2 소멸 (신기햐요)
ref = None #-> 이 시점에서 tmp1 소멸
print(f"tmpStd의 참조 횟수: {sys.getrefcount(tmpStd)-1}") #0이면 오버플로우가 나버리나? 


class testClass:

    __slots__ = ["__num", "name"] #특정한 속성만 instance가 소유하도록 강제함 
    def __init__(self, name="NONAME", num=0):
        self.name = name
        self.__num = num #언더바를 붙여서 private으로 바꿔줌! 


    @staticmethod
    def smethod()->None: 
        print("this is static! ")

    @classmethod
    def cmethod(cls):
        print(f"class method: {cls}")

    def getNum(self):
        return self.__num
    
    def setNum(self, num:int):
        self.__num = num
    
    public_num = property(fget=getNum, fset=setNum)


testInstance = testClass()
print(testInstance.name)
# print(testInstance.num) #err ->private이기 떄문에 직접접근 안됨 
# testInstance.height = 180 #err -> slot으로 제한되어있기 때문  
print(testInstance.getNum()) #내부에선 다룰 수 있으므로 일케쓰면 ㅇㅋ 
print(testInstance.public_num) #

#상속받은 친구 
class csStudent(Student):
    def introduce(self): #overriding
        super().introduce()
        print("I am CS major student.")

YELee = csStudent("YELee", 24)
YELee.introduce()

#다중상속
class Base1:
    def method(self):
        print("Base1's method")

class Base2:
    def method(self):
        print("Base2's method")

class Derived(Base1, Base2):
    def method(self):
        super().method() #첫번째 상속인자로 연결됨
        super(Base1, self).method() #이러면 그 뒤에 애로 연결됨 
        #둘 다 같은 메서드가 있었어서 가능했던 듯?? 

derived = Derived()
derived.method() 


import abc

#추상 클래스: 인스턴스를 만들지 못하는 클래스. 상속 원툴. 
class Starcraft(metaclass=abc.ABCMeta):
    #추상 메서드: 반드시 하위 클래스에서 재정의 할 것 
    @abc.abstractmethod
    def attack(self):
        pass

#추상 클래스 구현
class Protoss(Starcraft):

    def attack(self):
        print("Protoss의 공격!")
    
alian = Protoss()
alian.attack()


print("[System is turned out]")