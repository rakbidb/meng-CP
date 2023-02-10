# n = int(input())
# count = 0
# while n:
#     if n >= 100:
#         n -= 100
#     elif n >= 20:
#         n -= 20
#     elif n >= 10:
#         n -= 10
#     elif n >= 5:
#         n -= 5
#     elif n >= 1:
#         n -= 1
#     count += 1

# print(count)

n=int(input());print(n//100+n%100//20+n%20//10+n%10//5+n%5)