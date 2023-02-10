n = int(input())

jam = n // 3600
menit = (n % 3600) // 60
detik = (n % 3600) % 60

print(jam)
print(menit)
print(detik)