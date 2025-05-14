import pymysql
import time

# 커넥션과 디비 연결하기 
conn = pymysql.connect(
    host='127.0.0.1', 
    port=3306, 
    user='root', 
    passwd='w123', 
    db='autoever',
    charset='utf8mb4')
print(f"connected successfully!: {conn}\n")


# DML
cursor = conn.cursor()

# # INSERT
# # statement 방식 (비권장)
# cursor.execute(
#     'insert into usertbl ' \
#     'values("aaa", "asdf", "1234", "asdf city", "01012341234", "2025-05-14");')
# # 와 이거 뭐지 string 여러줄에 걸쳐 쓰기 
# print("succesfully inserted the data \n")

# # prepared statement 방식 (권장) -> 쿼리문에는 포맷팅 해두고 값을 튜플로 줍니다. 
# cursor.execute(
#     'insert into usertbl values(%s, %s, %s, %s, %s, %s);', 
#     ("bbb", "asdf", "1234", "asdf city", "01012341234", "2025-05-14"))
# print("succesfully inserted the data \n")

# # UPDATE 
# cursor.execute(
#     'update usertbl set name = %s where name = %s;', 
#     ('qwer', 'asdf'))
# print("succesfully updated the data \n")

# # DELETE
# cursor.execute(
#     'delete from usertbl where name = %s;', 
#     ('asdf'))
# print("succesfully deleted the data \n")

# SELECT 
# cursor.execute("select * from usertbl") # 조회 구문 실행 (아무일도 안 일어남)
# data = cursor.fetchone() # 방금 실행 결과를 가져와? 
# print(data)
# # data[0] = 'kt' # errr : 조회결과는 이뮤터블인 튜플! 
# print()

# datas = cursor.fetchall() #아까 가져온건 비워지는듯. 그 담부터 출력되넹 
# for d in datas:
#     print(d)

# # 프로시저 활용 (myproc이라는 프로시저가 디비에 지정되어있다는 전제 하에...)
# cursor.callproc("myproc", args=('qqq', 'qqq', 1986, '남양주', '01012341234', '1986-11-05'))

# cursor.execute("select * from usertbl")
# datas = cursor.fetchall() 
# for d in datas:
#     print(d)

# conn.commit() 


# # BLOB 이미지를 디비에 저장을 해볼게요... 
# filename = 'image/ham.png'
# f = open(filename, 'rb') #파일 읽기전용으로 열기(통로 열어준거 ) 
# photo = f.read() #읽어오기 
# cursor.execute("insert into member values(%s, %s, %s)", ('햄', 'ham.png', photo))

# filename = 'image/ham_flower.png'
# f = open(filename, 'rb') #파일 읽기전용으로 열기(통로 열어준거 ) 
# photo = f.read() #읽어오기 
# cursor.execute("insert into member values(%s, %s, %s)", ('햄플라워', 'ham_flower.png', photo))
# conn.commit()

# # 읽어서 파일 저장하기 
# cursor.execute("select * from member")
# for data in cursor.fetchall():
#     f = open("result/"+data[1], 'wb')
#     f.write(data[2])
#     f.close()

conn.close()
print("connection closed... ")


