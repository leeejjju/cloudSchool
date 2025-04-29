
#해당 자료형의 사용 가능한 메서드 출력
print(dir("안녕"))

#언더바 두개로 감싸인건 연산자 오버로딩 
print("안녕".__add__("하세요요"))
print("안녕" + "하세요요")

#메서드의 사용법이 궁금하다면... (man페이지같은거임)
help("안녕".__add__)


#키워드와 사용자정의이름 
import keyword
print(keyword.kwlist)

print(str.upper("hello"))
str = 10 #이제부터 str은 int형의 변수이빈다 
# print(str.upper("hello")) #error

int = "happy" #ㅇㅈㄹ이 된다니 충격 그 자체 
print(int) #not error 

#모듈을 찾는 순서대로 출력해줌 (깔았는데왜안댐?시 여기서 확인할 것.)
import sys
print(sys.path)

#실수의 부정확성
print(10-8 ==2)
print(1.0-0.8==0.2) 

aa = 0.1
sum = 0
for i in range(1000):
    sum += aa
print(sum)


print(dir("helloWorld"))
for i in "helloWorld":
    print(i)


#id란? 리터럴이 중복저장되지 않음을 증명. 
asdf = 10
zxcv = 11
qwer = 10
print(id(asdf))
print(id(zxcv))
print(id(qwer))
#우왕 
asdf = 15
print(id(asdf))
asdf = 11
print(id(asdf))

print(type(asdf))
asdf = "hello"
print(type(asdf)) #이게되네 막 휙휙 바뀌어버리네... 