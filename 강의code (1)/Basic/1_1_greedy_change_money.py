# 선언할 변수 종류를 결정, 선언
n = 1260    # n : 거스름돈
count = 0   # count : 거스름돈 전체 갯수
# temp 변수도 선언하여 사용 가능 (코딩양이 많을 경우에는 임시 변수를 사용할 필요) a, b, c

# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)