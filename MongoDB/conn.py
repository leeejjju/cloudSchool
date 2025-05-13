#connection of server and DB
import pymongo
from pymongo import mongo_client



# 서버와 연결 
IP = "127.0.0.1"
PORT = 27017
conn = pymongo.MongoClient(IP, PORT)
print(conn, '\n')

# 데이터베이스와 연결 (없으면 만들어짐)
db= conn.adam
# print(db)

# 컬렉션과 연결 (없으면 만들어짐)
users = db.users
# print(users)

#인제 이거 가지고 요로코롬 조로코롬 ㅇㅋ? 
# myCursor = users.find()
# print(myCursor.next())
#아따마 즥이네예 

# 전반적으로 파이썬스럽게, 함수이름도 helloWorld에서 hello_world로 바뀌고... 좀 어레인지 된 듯. 

# doc1 = {'empno':10001, 'name':'JJLee'}
# doc2 = {'empno':10002, 'name':'HMPark'}
# doc3 = {'empno':10003, 'name':'YELee'}
# doc4 = {'empno':10004, 'name':'DBCho'}
# doc5 = {'empno':10005, 'name':'GRKim'}

# users.insert_one(doc1) #한개 넣기 
# users.insert_many([doc2, doc3, doc4, doc5]) #여러개 넣기: 배열 형태로 

print(f"users collection의 document 갯수: {users.count_documents({})}") #{}는 조건 드가는곳임 


print(users.find_one(), '\n') #맨위 하나만 조회 

cur = users.find() #결과를 cursor 형태로 반환. 
print(type(cur))
for c in cur: # 오... 이게 되면 to_list는 왜잇능겨 
    print(c)

    