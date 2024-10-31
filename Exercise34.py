#wap to print fibonacci series in 1 to 10 using for loop.
series = [0,1]
num = int (input("Enter a number here :"))

if num == 1:
    print(series[0])
elif num == 2:
    print(series)
else:
  
   for i in range(2,num):
       next_fib = series[-1] + series[-2]
       series.append(next_fib)

print(series)



