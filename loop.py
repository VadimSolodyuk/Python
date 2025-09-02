# s1 = "Панда"
# print(range(1, len(s1)))
# print(s1.find('о'))
# print(s1.isdigit())
# enumerate(s1,)

# n = '+7(123)456-78-99'
# it = iter(n)

# digits = [3, 4, 5, 7, 8, 9, 11, 12, 14, 15]
# t = [10, 13]
# if len(n) != 16 or n[:3] != '+7(' :
#     print('НЕТ')
# else:
#     for i, l in enumerate(n) :
#         if (i in digits) and l.isdigit() != True :
#             print('НЕТ')
#             break
#         elif i in t and l != '-' :
#             print('НЕТ')
#             break
#         elif i == 6 and l != ')' :
#             print('НЕТ')
#             break
#         else:
#             if i == len(n) - 1 :
#                 print('ДА')

# put your python code here
# e = list(input())

# while ' ' in e :
#     e.remove(' ')
    
# e = ''.join(e)

# operation = ['+', '-']
# ind = 0

# for i, sy in enumerate(e) :
#     if sy in operation:
#         ind = i
#         break
# res = int(e[:ind])

# for i, sy in enumerate(e) :
#     if i < ind :
#         continue
#     if sy.isdigit() != True :
#         for id, s in enumerate(e[i + 1:]) :
#             if s in operation :
#                 ind += id - 1
#                 break
#             ind += 1
#         if sy == '+':
#             res += int(e[i + 1:ind])
#         else:
#             res -= int(e[i + 1:ind])
            
# print(res)

# # является ли этот двумерный список симметричным относительно главной диагонали
# s = '''2 3 4 5 6
# 3 2 7 8 9
# 4 7 2 0 4
# 5 8 0 2 1
# 6 9 4 1 2''' #sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s.split(sep='\n')]

# # здесь продолжайте программу (используйте список lst_in)
# END = False

# for i, row in enumerate(lst_in[1:], start = 1) :
#     if END :
#         break
#     for j, x in enumerate(row[:i]) :
#         print(x, lst_in[j][i])
#         if x != lst_in[j][i] :
#             print('НЕТ')
#             END = True
#             break
#         if i == len(lst_in) - 1 and j == i - 1 :    
#             print('ДА')

# for i, row in enumerate(lst_in[0:-1]) :
#     if END :
#         break
#     else:
#         for j, x in enumerate(row[0:-1]) :
#             if END :
#                 break
#             else:
#                 if sum(lst_in[i][j:j + 2]) + sum(lst_in[i + 1][j:j + 2]) > 1 :
#                     print('НЕТ')
#                     END = True                                   
#                     break
# else:
#     print('ДА')
# for i, row in enumerate(lst_in) :
#     if END :
#         break
#     else:
#         if i == len(lst_in) - 1 :
#             continue
#         for j, x in enumerate(row) :
#             if END :
#                 break
#             else:
#                 if j == len(row) - 1 :
#                     continue
#                 sum = 0
#                 for ii, row in enumerate(lst_in[i:i + 2]) :
#                     if END :
#                         break
#                     else:
#                         for jj, x in enumerate(row[j:j + 2]) :
#                             sum += x
#                             if sum > 1 :
#                                 print('НЕТ')
#                                 END = True                                   
#                                 break
# else:
#     print('ДА')

# # сортировку выбором полученного списка по возрастанию (неубыванию)
# s = '6 3 7 9 3'
# num = list(map(int, s.split()))

# for i, x in enumerate(num) :
#     y = min(num[i:]) 
    
#     # print(num[i:])
#     # print(i, x, y)
#     if x > y :
        
#         ind_y = num[i:].index(y) + i
#         # print(ind_y)
#         num[i], num[ind_y] = num[ind_y], num[i]
#     else:
#         continue

# print(*num)

# # выполнить сортировку полученного списка по возрастанию (неубыванию) методом всплывающего пузырька
# s = '4 5 2 0 6 3 -56 3 -1'
# num = list(map(int, s.split()))

# for i in range(1, len(num)) :
#     for j in range(len(num) - i) : 
#         if num[j] > num[j + 1] :
#             num[j], num[j + 1] =  num[j + 1], num[j]
            
# print(*num)

# #определите, каким наименьшим количеством денежных купюр достоинством в 1, 2, 4, 8, 16, 32 и 64 можно выплатить сумму n?
# n = 221
# m = [1, 2, 4, 8, 16, 32,  64]

# pay = []
# dif = n

# for i, x in enumerate(m[::-1]) :
#     if dif == 0 :
#         break
#     while dif // x > 0 :
#         pay.append(x)
#         dif = n - sum(pay)
# print(*pay)
# r = range(0, len(m), 2)
# print(*r)

# put your python code here
t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]
lst = [[word for word in line.strip().split() if len(word) > 3]
       for line in t
      ]


print(lst)