import statistics
t = int(input())
for i in range(t):
    n = map(int, input().split())
    print(statistics.median(n))