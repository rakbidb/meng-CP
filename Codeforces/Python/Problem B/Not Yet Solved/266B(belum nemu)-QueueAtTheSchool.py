n, t = map(int, input().split())
s = list(map(str, input().upper()))[:n]

for i in range(n):
    if s[i] == "G" and s[i + 1]  == "B":
        