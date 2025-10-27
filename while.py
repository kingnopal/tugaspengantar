import random

while True:
    try:
        n_input = input("5")
        n = int(n_input)
        if n > 0:
            break
        else:
            print("Masukkan bilangan bulat positif.")
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")

print(f"\nMenampilkan {n} bilangan acak yang lebih kecil dari 0.5:")

for i in range(n):
    bilangan_acak = random.random()
    while bilangan_acak >= 0.5:
        bilangan_acak = random.random()
    print(f"Bilangan acak ke-{i + 1}: {bilangan_acak:.4f}")
