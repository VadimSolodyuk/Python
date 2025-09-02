s1 = "Панда"
s2 = 'Панда'
print(s1, s2)

text = ''' asdcdda
asfffsadfdfssdfsd
sdfffsd''' 
print(text)

s1 = "Я люблю"
s2 = 'язык Python'
print(s1 + " " + s2)

s3 = str(5)
print(s1 + " " + s3)

print(s1 * 5)

print(len(s1))

print('я' in s1)

print(s1 == "Я люблю ")

print('кот' > 'кит')
print('Кот' < 'кот')
print('кот' > 'кот')

print(ord('k'), ord('K'))

print("Сергей\nБалакирев")

# s1, s2 = map(str, input().split())

# print(s1[:len(s2)][::2])


s = r'"спецсимволы"'
print(s)

# v = input().split() 

# lst = list(map(int, input().split()))


# a, b = map(float, input().split())
# a, b = map(int, input().split())

if True :
    print('ДА')
else:
    print('НЕТ')

# put your python code here
n, m = map(int, input().split())
seq = []
while n <= m :
    seq.append(n if n % 2 != 0 else '-')
    n += 1
c = seq.count('-')
i = 0
while i < c :
    seq.remove('-')   
    i += 1
print(*seq)

