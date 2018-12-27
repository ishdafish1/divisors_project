def div(num):
    divisors = []
    listOfIntegers = []
    sum = 0
    
    for i in range(1, num+1):
        listOfIntegers.append(i)
    
    for integer in listOfIntegers:
        if num % integer == 0:
            divisors.append(integer)
            sum += integer
            del integer
        else:
            for otherInteger in listOfIntegers:
                if otherInteger % integer == 0:
                    del otherInteger
# print('The divisors of your numbers are: ' + str(divisors))
#  print('Sum of its divisors: ' + str(sum))
    return sum

startPoint = 0 # number to begin testing from
maxAttempts = 100000 # maximum number of attempts before program stops
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
