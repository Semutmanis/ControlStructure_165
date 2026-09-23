n = int(input("Masukkan n: "))

a = 0
b = 1

for i in range(n):
    if i % 3 != 0:
        print(a)

    a, b = b, a + b