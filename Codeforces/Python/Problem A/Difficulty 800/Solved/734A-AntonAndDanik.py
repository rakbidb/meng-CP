n = int(input())

list_menang = list(map(str, input().upper()))[:n]
if list_menang.count("A") > list_menang.count("D"):
    print("Anton")
elif list_menang.count("A") < list_menang.count("D"):
    print("Danik")
else:
    print("Friendship")