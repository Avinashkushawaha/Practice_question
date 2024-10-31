# print("triangle")
# for i in range (5):
#     for j in range (i +1):
#         print('*', end='')
#     print()


# for row in range (1,6):
#     for col in range (row):
#         print(row+col, end=' ')
#     print()


# num = 1
# for row in range (1,4):
#     for col in range (row):
#        print(num, end=' ')
#        num += 2    
# print()  


n = 5
num = 9

for row in range (1, n+1):
    for col in range (row):
     if num <1: num=9
    print(num, end=' ')
    num -= 1
print()