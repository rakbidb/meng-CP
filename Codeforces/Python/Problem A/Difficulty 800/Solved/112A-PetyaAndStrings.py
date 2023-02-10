# string1 = input().lower()
# string2 = input().lower()

# # Karena len(string1) sama seperti len(string1) berarti:
# for i in range(0, len(string1)):
#     if ord(string1[i]) < ord(string2[i]):
#         kesimpulan = -1
#     elif ord(string1[i]) == ord(string2[i]):
#         kesimpulan = 0
#     elif ord(string1[i]) > ord(string2[i]):
#         kesimpulan = 1

# print(kesimpulan)

string1 = input().lower()
string2 = input().lower()

for i in range(0, len(string1)):
    if ord(string1[i]) == ord(string2[i]):
        kesimpulan = 0
    elif ord(string1[i]) < ord(string2[i]):
        kesimpulan = -1
        break
    elif ord(string1[i]) > ord(string2[i]):
        kesimpulan = 1
        break
print(kesimpulan)