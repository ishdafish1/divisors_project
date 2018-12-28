def div(num):
    divisors = []
    sum = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
            sum += i
# print('The divisors of your numbers are: ' + str(divisors))
#  print('Sum of its divisors: ' + str(sum))
    return sum

startPoint = 0 # number to begin testing from
maxAttempts = 100000 # maximum number of attempts before program stops
divisorSum = 2021 # the divisor sum you are searching for
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

def div2(num):
    divisors2 = []
    x = 0
    while x < num:
        x += 1
        divisors2.append(x)
    
    for x in divisors2:
        if num % x == 0:
            if num % i != 0:
            divisors2 = divisors2[:i-1] + divisors2[i:] 
            # ^^ not right yet, divisors2 being updated each time and with each iteration the new updated divisors2 is being updated rather than the original one.
        
           
