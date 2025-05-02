#튜플플님
tup = (1, 2, 3, 4, 5)
# tup[3] = 5 #err!! 튜플은 이뮤터블입니당  
print(tup[3])
a, b, *c = tup #unpacking하여 저장하기. *c는 나머지 전부를 리스트 형태로 저장하는 것. 
print(f"a = {a}, b = {b}, c = {c}, tup = {tup}")


score = 59
grade = ('FAIL', 'PASS')[score >= 60] #삼항연산자. 근데 TF순서가 반대인
print(f"your grade: {grade}")


#이름, 나이, id를 하나로 저장하고 싶을 때. DTO(Data Transfer Object)
#1. class
class DTO_c:
    def __init__(self, num=0, name="noname", age=1):
        self.num = num
        self.name = name
        self.age = age 
    def status(self):
        print(f"[{self.num}] {self.name}, {self.age}")
dto1 = DTO_c(1, "JJLee", 24)
dto1.status()

#2. namedTuple
from collections import namedtuple
DTO_t = namedtuple("DTO_t", "num name age") #초기화할 때 필드명 써주기
dto2 = DTO_t(2, "HMPark", 23)
print(dto2)

# set: 데이터를 순서 상관 없이, 중복 제거된 형태로 만들어짐. 
myset1 = set()
myset2 = set("Hello world")
myset3 = {1, 2, 2, 3, 4, 5, 5, 6, 7}
print(myset2)
print(myset3)

# dict: 
dto3 = {"num":3, "name":"DBCho", "age":25}
print(dto3)
dto3["newKey"] = "newValue"
print(dto3)
print(dto3.get("name"))
print(dto3.get("nullKey", "The keuy doesn't exist!"))

for i in dto3:
    print(f"{i} : {dto3.get(i)}") #기본적으로 key값이 순회된다! 


# 대량의 데이터 처리시?
fruit = ["apple", "banana", "kiwi", "mango"]
vegetable = ["onion", "carrot", "garic"]
food = [fruit, vegetable] #이차원 배열이죠? (비권장) 
#-> 나중에 카테고리 추가되면 사용하는걸 다 일일히 수정해야 하는...

meat = ["chicken", "beef", "pork"]
food.append(meat)

print(food)

# for category in food: #고기 추가 전 코드... 고기 추가되면 수정해야댐...
#     print(f"{('과일:', '채소:')[category == food[1]]}", end=" ")
#     for one in category:
#         print(one, end="\t")
#     print()

category = ["과일", "채소", "고기"]
for idx in range(len(food)):
    print(f"{category[idx]}:", end=" ")
    for one in food[idx]:
        print(one, end="\t")
    print()


#대안: 딕셔너리 이용
food = [{"category":"과일", "data":fruit}, {"category":"채소", "data":vegetable}, {"category":"고기", "data":meat},]
for cate in food:
    print(cate["category"], ":", end=" ")
    for one in cate.get("data"):
        print(one, end="\t")
    print()
#이후에 데이터가 추가되어도 출력단을 수정할 필요가 없음! (와!!!!)

li1 = ["야옹이", "애옹이", "애옭이", "앵록이"]
li2 = [cat for cat in li1]
li3 = list(li1) #이것도 딥카피 가능이네요 

li1[3] = "꼬앵이" #원본변경 
print(li1)
print(li2) #노영향
print(li3) #노영향 

lili = [li1, li2, li3] #2차원
lili2 = [i for i in lili] #고대로 복사도 가능하고 
lili3 = [j for i in lili for j in i] #이차원가지고 일차원 생성! 다 하나에 때려박기! 
print(lili)
print(lili2)
print(lili3)

li4 = [i+'~' for i in li1] #모든 원소에 변경 적용(map보다 빠름 세계관 최강자임 )
li5 = [i for i in li2 if i[0] == '애'] #필터링깔쥐;;

print(li4)
print(li5)


#카운터 모듈 
from collections import Counter

#직접구현시 
counting = {}
for i in lili3:
    cnt = counting.get(i, 0) #i가 있으면 값 가져오고, 없으면 0
    cnt += 1
    counting[i] = cnt
print(counting.get("야옹이")) #3번 나옴

#카운터 모듈 사용시 
counter = Counter(lili3)
print(counter["야옹이"])
print(counter) #나중에 dict로 변환해서 사용하면 조음 

total = Counter()
ppl = [('a', 20, 160), ('b', 30, 186), ('c', 25, 258), ('a', 30, 155)]
for name, val1, val2 in ppl:
    total[name] += val1
    total[name] += val2
print(dict(total))
print(dict(total.most_common(2)))

#딕셔너리인데 값이 데이터 뭉탱이인. 
from collections import defaultdict
ddict = defaultdict(list) #list 형태로 야옹하겟다~

for name, val1, val2 in ppl:
    ddict[name].append((val1, val2)) #여러 데이터 한번에 야옹 이거는 튜플로 하면 되는구낭... 

for x in ddict:
    print(x, ":", ddict[x])

#기본 딕셔너리는 key순서 미보장, OrderdDict는 보장!
from collections import OrderedDict
keys = ["asdf", "qwer", "zxcv", "ghjk", "tyui"]
values = (1, 2, 3, 4, 5)

odict = OrderedDict(zip(keys, values))
ndict = dict(zip(keys, values))
for key in odict:
    print(key, ":", odict.get(key))

#근데 일반 딕셔너리도 대충 보면 순서 맞긴 하는데...ㅎ 
for key in ndict:
    print(key, ":", ndict.get(key))

import itertools