
a = 10
b = a
print(f"a: {id(a)}\nb: {id(b)}")
a = 12
print(b) #스칼라라 영향을 안 받은 듯?? -> 12라는 새로운 저장메모리의 주소를 a가 갖고 원래거는 니 하셈ㅇㅇ 해서 그런듯 
print(f"a: {id(a)}\nb: {id(b)}")

aa = "HELLO"
bb = aa
print(f"aa: {id(aa)}\nbb: {id(bb)}")
aa = "HELL"
print(bb) #이것도 영향을 안 받네?? -> 문자열은 이뮤터블이라 복사본이 새로 생성되고 대입된거라 그런듯 ㅇㅇ
print(f"aa: {id(aa)}\nbb: {id(bb)}")

#--------------- 여기부턴 vector 데이터들 

aaa = [1, 2, 3]
bbb = aaa
print(f"aaa: {id(aaa)}\nbbb: {id(bbb)}")
aaa.append(4)
print(bbb) #이건 영향을 받으셨어. 이건 확실히 안되셔. 
print(f"aaa: {id(aaa)}\nbbb: {id(bbb)}")

#copy 메서드 써보기
import copy

# 해보니까 기본 list.copy()도 카피카피랑 똑같더라. 1차원까진 되고 2차원부턴 안되고... 
ccc = copy.copy(aaa)
print(f"aaa: {id(aaa)}\nccc: {id(ccc)}")
aaa.append(5)
print(ccc) #일차원이라 일단 분리가 되셨는데유 

asdf = [aaa, bbb, ccc] #이차원배열
qwer = copy.copy(asdf)
print(f"asdf: {id(asdf)}\nqwer: {id(qwer)}")
print(f"asdf[0]: {id(asdf[0])}\nqwer[0]: {id(qwer[0])}")
asdf[0].append(6)
print(qwer) #아~ 영향을 받아버렸네요~~~ 이차원 이상 인자들이~~ 

#그럼 뭐다? 딥카피다~
zxcv = copy.deepcopy(asdf)
print(f"asdf: {id(asdf)}\nzxcv: {id(zxcv)}")
print(f"asdf[0]: {id(asdf[0])}\nzxcv[0]: {id(zxcv[0])}")
zxcv[0].append(10000)
print(zxcv)
print(asdf) #와! 영향을 안 받으심!!! 

