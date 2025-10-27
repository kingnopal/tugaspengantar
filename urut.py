print("Program Mengurutkan Data")

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

data = [a, b, c]

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

print("\nUrutan bilangan dari yang terkecil ke terbesar:")
for nilai in data:
    print(nilai, end=" ")

print() 
