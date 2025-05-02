import os.path
#파일 다루기 모듈

print(os.path.abspath(".")) #절대경로

import time #숫자에서 인간용으로 바꿔주는 친구 
print(f"이건머지: {time.gmtime(os.path.getatime("dataType2.py"))}")
print(f"생성시간: {time.gmtime(os.path.getctime("dataType2.py"))}")
print(f"수정시간: {time.gmtime(os.path.getmtime("dataType2.py"))}")

import glob #디렉터리 속 파일 순회하는... 
print(glob.glob("*.py")) #조건에 맞는 파일명/폴더명 리스트로 반환 
print(glob.glob("../*"))

import os

dir_name = "testDir"
os.makedirs(dir_name) #이미 있으면 오류 남!!
# time.sleep(5)
os.removedirs(dir_name)

# os.system("notepad") #프로그램을 열수도 있음! 
os.system("dir") #명령어 사용 가능! (ls가 안되네... 윈도우라 그런듯 )

import sys
print(f"기본 인코딩: {sys.getdefaultencoding()}")
print(f"로딩된 모듈: {sys.modules}")

a = "HELL WORLD" #'a' 등 캐릭터 하나거나 int형태 등 정수 하나...?인 친구일 때 참조횟수가 헤까닥 하는데 웨지감자 
b = a
c = a
print(f"{a}가 참조된 횟수: {sys.getrefcount(a)}")