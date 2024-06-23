# Fungsi untuk penjumlahan
def add(x, y):
    return x + y

# Fungsi untuk pengurangan
def subtract(x, y):
    return x - y

# Fungsi untuk perkalian
def multiply(x, y):
    return x * y

# Fungsi untuk pembagian
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

# Fungsi untuk kalkulator
def calculator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    choice = input("Masukkan pilihan (1/2/3/4): ")

    num1 = float(input("Masukkan bilangan pertama: "))
    num2 = float(input("Masukkan bilangan kedua: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Input yang Anda masukkan tidak valid.")

# Memanggil fungsi kalkulator
calculator()
