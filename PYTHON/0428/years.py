year = 2025

if year%100 and not year%4 or not year%400 :
    print(year, "는 윤년")
else:
    print(year, "는 윤년 아님")

