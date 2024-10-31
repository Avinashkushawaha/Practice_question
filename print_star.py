# n = 6
# for row in range(n):
#     for col in range(n):
#         if row==0 or (row==col and row<=n//2) or (row<col and row+col <=n-1):
#             print('*', end='' )

#     else:   
#         print('', end='')
#         print()


# n = 7
# for row in range(n):
#     for col in range(n):
#         if row ==0 or row==7  or col==0 or (row+col <=n-1 or  row >=col) :


#             print('*' , end='')
#     else:
#         print('', end='')
#         print()


 
# n = 5

# for row in range(n):
#     for col in range(n):
#         if col ==0 or row==4  or col==4 and row >= n//2 or col==n//2 and row <= n//2 or col==n//2 or col <= n//2 or row==n//2 or row ==0 and col<= n//2 or col==1:


#             print('*' , end='')
#     else:
#         print('', end='')
#         print()


fruits = "Avinash"
print(fruits[-4::-2])  