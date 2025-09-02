# print()  
print(1, 3, 5 )
print(abs(1 * 3 - 5))

a = 7.6
b = 7
c = 25.6
print(a, b, c, sep=" | ")
print("hello")

print(a, b, c, sep=" | ", end=" ")
print("hello")

# "Координаты точки: x = 5.76; y = -8"
x = 5.76
y = -8
print("Координаты точки: x = ", x, "; y = ", y, sep="")

# Python 3.6 F-строки
print(f"Координаты точки: x = {x}; y = {y}")

# input()
# a = input()
# print(a, type(a))

# a = abs(int(input()))
# print(a, type(a))

# a = abs(float(input()))
# print(a, type(a))


a = float(input("Введите длинну: "))
b = float(input("Введите шируну: "))
print("Периметр: ", 2 * (a + b))

