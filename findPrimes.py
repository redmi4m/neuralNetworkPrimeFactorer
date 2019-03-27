from math import sqrt, floor
x=2
flag = False
primes = []
upper = 200
while(x<upper):
    flag = False
    for y in range(floor(sqrt(x))-1):
        if(x%(y+2) == 0):
            flag = True
            break
    if(flag == False):
        primes.append(x)
    x += 1
f = open("primesfactored.txt", "w+")
for i in range(len(primes)):
    for j in range(len(primes)-i):
        f.write(str(primes[i])+" ")
        f.write(str(primes[j+i])+" ")
        f.write(str(primes[i]*primes[j+i])+"\n")
f.close()