


def ten_div(x:int) -> float:
    if x == 10:
        raise Exception("강제로 발생된 예외")
    return 10/x

# #문자를 집어넣기
# try:
#     print(ten_div("a"))
# except:
#     print("This value is not available: this is a char")

# #0를 집어넣기
# try:
#     print(ten_div(0))
# except:
#     print("This value is not available: this is a zero")

err = [5, 'a', 0, 10]

for er in err:
    try:
        print(f"result: {ten_div(er)}")
    except TypeError as e:
        print(f"type err: {e}")
    except ZeroDivisionError as e:
        print(f"zero err: {e}")
    except Exception as e: 
        print(f"unknown err: {e}")
    else: # 오류가 발생하지 않을 시 수행될 내용 
        print("오류 발생 안 함 ^^*")
    finally: #오류 여부와 관계 없이 반드시 수행될 내용 
        print(":D")

import platform
assert platform.system() == "Windows", "Windows 운영체제에서만 실행 가능합니다."
# assert platform.system() == "Darwin", "Mac 운영체제에서만 실행 가능합니다."
print('정상 종료됨')