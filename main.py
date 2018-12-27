def div(num):
    divisors = []
    sum = 0
    for i in range(1, int(num/2)+1): # there will be no divisors beyond half the value of num
        if num % i == 0:
            divisors.append(i)
            sum += i
# print('The divisors of your numbers are: ' + str(divisors))
#  print('Sum of its divisors: ' + str(sum))
    return sum

startPoint = 0 # number to begin testing from
maxAttempts = 100 # maximum number of attempts before program stops
divisorSum = 2018 # the divisor sum you are searching for
success = False # shows whether a number with a satisfactory divisor sum has been found

attempts = 0

while attempts < maxAttempts:
    if div(startPoint + attempts) == divisorSum:
        success = True
        break
    else:
        attempts += 1

if success:
    print('The number ' + str(startPoint + attempts) + ' has a divisor sum of ' + str(divisorSum) + '.')
else:
    print('Program exceeded maximum number of attempts, without success.')
