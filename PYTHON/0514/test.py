# # Q5
# scores = list(map(int, input().split()))

# if min(scores) < 0 or max(scores) > 100:
#     print("잘못된 점수")
# else:
#     if sum(scores)/len(scores) >= 80:
#         print("합격")
#     else:
#         print("불합격")

# Q6
H = int(input())
for h in range(1, H+1):
    print(" "*(H-h) + "*"*h + "*"*(h-1))

# # Q7
# # 51900 ; 83000 ; 158000 ; 367500 ; 250000 ; 52900 ; 128500 ; 1304000
# def modified(n):
#     nn = list(str(n))
#     for i in range(len(nn)-3, 0, -3):
#         nn.insert(i, ',')
#     rst = ("%-9s"%("".join(nn)))
#     return rst

# prices = sorted(list(map(int, input().split(';'))), reverse=True)
# result = list(map(modified, prices))
# for r in result:
#     print(r)

# # Q8
f = open("words.txt", "r")
while True:
    word = (f.readline()).strip()
    if word == '':
        break
    if word == word[::-1]:
        print(word)
f.close()
