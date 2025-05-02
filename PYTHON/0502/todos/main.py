from fastapi import FastAPI
aapp = FastAPI()

#기본 요청이 오면 아래 함수를 수행해서 결과를 리턴
@aapp.get("/")
async def welcome() -> dict:
    return {
    "message": "손으로 코딩하고 뇌로 컴파일하면 눈으로 디버깅한다."
    }