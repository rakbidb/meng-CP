n = int(input())

jawaban = list(map(int, input().split()))[:n]
if jawaban.count(1) >= 1:
    print("HARD")
else:
    print("EASY")