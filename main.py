def div(num):
  divisors = []
  sum = 0
  for i in range(1, num+1):
    if num % i == 0:
      divisors.append(i)
      sum += i
  print('The divisors of your numbers are: ' + str(divisors))
  print('Sum of its divisors: ' + str(sum))
  
