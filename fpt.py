import math
import random

def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, math.floor(y/2), N)
    if y % 2 == 0:  # even
        return math.pow(z, 2) % N
    else:
        return (x * math.pow(z, 2)) % N

def fpt(N, k):
    countIfPrime = 0
    countIfNotPrime = 0

    for i in range(0, k):
        a = random.randint(1, N-1)
        if modexp(a, N-1, N) != 1:
            countIfNotPrime += 1
        else:
            countIfPrime += 1
    percentNo = (countIfNotPrime/k) * 100
    percentYes = (countIfPrime / k) * 100
    if countIfPrime == k:
        return print('{0:<10d}{1:<10d}{2:<10d}{3:20}{4:<.3f}\t{5:<.3f}'.format
                     (N, countIfPrime, countIfNotPrime, "N is prime", percentYes, percentNo))
    else:
        return print('{0:<10d}{1:<10d}{2:<10d}{3:20}{4:<.3f}\t{5:<.3f}'.format
                     (N, countIfPrime, countIfNotPrime, "N is not prime", percentYes, percentNo))


n = []
times = []
inputs = input("Enter N: ")
k = int(input("Enter k: "))
inputSplit = inputs.replace(',', ' ').split()  # separate numbers
    ## Table output
print("------------------------------------------------------------------")
print('{0:10}{1:10}{2:10}{3:20}{4:10}{5:10}'.format
      ('N', "Passed", "!Passed", "Prime?", "Yes %", "Not %"))

for i in range(0, len(inputSplit)):
    inputNumber = int(inputSplit[i])
    n.append(inputNumber)
    fpt(n[i], k)