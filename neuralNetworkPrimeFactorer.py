import numpy as np
import time
from math import log, floor
from random import random
upper = 200
hidden1 = 100
hidden2 = 100
#hidden3 = 50
#hidden4 = 50
def nonlin(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))
def get_factors(x):
    pos1 = 0
    pos2 = 0
    for j in range(len(x)):
        if(x[j] == " "):
            if(pos1 == 0):
                pos1 = j
            else:
                pos2 = j
    num1 = ""
    num2 = ""
    factorable = ""
    for j in range(pos1):
        num1 = num1+x[j]
    for j in range(pos2-pos1-1):
        num2 = num2+x[pos1+j+1]
    for j in range(len(x)-pos1-pos2):
        factorable = factorable+x[pos1+pos2+j]
    num1 = int(num1)
    num2 = int(num2)
    factorable = int(factorable)
    return [num1,num2,factorable]
def to_binary(x):
    if(log(x)/log(2)%1 == 0):
        places = floor(log(x)/log(2))+2
    else:
        places = floor(log(x)/log(2))+1
    bin_list = [0 for x in range(places)]
    for i in range(places):
        if(x/2**(places-i-1)>=1):
            bin_list[i] = 1
            x = x-2**(places-i-1)
    return bin_list
def from_binary(x):
    z = 0
    for y in range(len(x)):
        z += x[len(x)-y-1]*2**(y)
    return z
def combine_primes(prm1, prm2):
    combined = [0 for x in range(2*(floor(log(upper)/log(2))+1))]
    prma1 = [0 for x in range(floor(log(upper)/log(2))+1)]
    prma2 = [0 for x in range(floor(log(upper)/log(2))+1)]
    for x in range(len(prm1)):
        prma1[len(prma1)-1-x] = prm1[len(prm1)-1-x]
    for x in range(len(prm2)):
        prma2[len(prma2)-1-x] = prm2[len(prm2)-1-x]
    for x in range(len(prma1)):
        combined[x] = prma1[x]
    for x in range(len(prma2)):
        combined[x+len(prma1)] = prma2[x]
    return combined
def fix_factorable(factorable):
    fixed_factorable = [0 for x in range(floor(2*log(upper)/log(2))+1)]
    factorable = to_binary(factorable)
    for x in range(len(factorable)):
        fixed_factorable[len(fixed_factorable)-1-x] = factorable[len(factorable)-1-x]
    return fixed_factorable
np.random.seed(floor(time.time()))
syn0 = 2*np.random.random((floor(2*log(upper)/log(2))+1,hidden1)) - 1
syn1 = 2*np.random.random((hidden1, hidden2)) - 1
#syn2 = 2*np.random.random((hidden2, hidden3)) - 1
#syn3 = 2*np.random.random((hidden3, hidden4)) - 1
syn2 = 2*np.random.random((hidden2, 2*(floor(log(upper)/log(2))+1))) - 1
try:
    f = open('neuralshorsweights.txt', 'r')
    weights = f.readlines()
    holder = 0
    for weight in weights:
        if(holder < len(syn0)*len(syn0[0])):
            syn0[floor(holder/len(syn0[0]))][holder-floor(holder/len(syn0[0]))*len(syn0[0])] = float(weight.rstrip("\n"))
        elif(holder >= len(syn0)*len(syn0[0]) and holder < len(syn0)*len(syn0[0])+len(syn1)*len(syn1[0])):
            syn1[floor((holder-len(syn0)*len(syn0[0]))/len(syn1[0]))][(holder-len(syn0)*len(syn0[0]))-floor((holder-len(syn0)*len(syn0[0]))/len(syn1[0]))*len(syn1[0])] = float(weight.rstrip("\n"))
        elif(holder >= len(syn0)*len(syn0[0])+len(syn1)*len(syn1[0]) and holder < len(syn0)*len(syn0[0])+len(syn1)*len(syn1[0])+len(syn2)*len(syn2[0])):
            syn2[floor((holder-len(syn0)*len(syn0[0])-len(syn1)*len(syn1[0]))/len(syn2[0]))][(holder-len(syn0)*len(syn0[0])-len(syn1)*len(syn1[0]))-floor((holder-len(syn0)*len(syn0[0])-len(syn1)*len(syn1[0]))/len(syn2[0]))*len(syn2[0])] = float(weight.rstrip("\n"))
#        elif(holder >= len(syn0)*len(syn0[0])+len(syn1)*len(syn1[0])+len(syn2)*len(syn2[0]) and holder < len(syn0)*len(syn0[0])+len(syn1)*len(syn1[0])+len(syn2)*len(syn2[0])+len(syn3)*len(syn3[0])):
#            syn3[floor((holder-len(syn0)*len(syn0[0])-len(syn1)*len(syn1[0])-len(syn2)*len(syn2[0]))/len(syn3[0]))][(holder-len(syn0)*len(syn0[0])-len(syn1)*len(syn1[0])-len(syn2)*len(syn2[0]))-floor((holder-len(syn0)*len(syn0[0])-len(syn1)*len(syn1[0])-len(syn2)*len(syn2[0]))/len(syn3[0]))*len(syn3[0])] = float(weight.rstrip("\n"))
#        elif(holder >= len(syn0)*len(syn0[0])+len(syn1)*len(syn1[0])+len(syn2)*len(syn2[0])+len(syn3)*len(syn3[0]) and holder < len(syn0)*len(syn0[0])+len(syn1)*len(syn1[0])+len(syn2)*len(syn2[0])+len(syn3)*len(syn3[0])+len(syn4)*len(syn4[0])):
#            syn4[floor((holder-len(syn0)*len(syn0[0])-len(syn1)*len(syn1[0])-len(syn2)*len(syn2[0])-len(syn3)*len(syn3[0]))/len(syn4[0]))][(holder-len(syn0)*len(syn0[0])-len(syn1)*len(syn1[0])-len(syn2)*len(syn2[0])-len(syn3)*len(syn3[0]))-floor((holder-len(syn0)*len(syn0[0])-len(syn1)*len(syn1[0])-len(syn2)*len(syn2[0])-len(syn3)*len(syn3[0]))/len(syn4[0]))*len(syn4[0])] = float(weight.rstrip("\n"))
        holder += 1
except:
    holder = 0
f = open("primesfactored.txt","r")
primes = f.readlines()
f.close()
errorflag = 0
for x in range(3):
    errorflag = 0
    for i in primes:#range(int(input("how many rounds\n"))*1000):
        if(i != "\n"):
            processed = get_factors(list(i))#primes[floor(random()*len(primes))]))
            for x in range(floor(errorflag/10)+1):
                y = np.array([combine_primes(to_binary(processed[0]),to_binary(processed[1]))])
                X = np.array([fix_factorable(processed[2])])
                l0 = X
                l1 = nonlin(np.dot(l0,syn0))
                l2 = nonlin(np.dot(l1,syn1))
                l3 = nonlin(np.dot(l2,syn2))
                #l4 = nonlin(np.dot(l3,syn3))
                #l5 = nonlin(np.dot(l4,syn4))
                l3_error = y - l3
                if(errorflag == 0):
                    print("Error:" + str(np.mean(np.abs(l3_error))))
                    errorflag = 1
                #l5_delta = l5_error*nonlin(l5,deriv=True)
                #l4_error = l5_delta.dot(syn4.T)
                #l4_delta = l4_error * nonlin(l4,deriv=True)
                #l3_error = l4_delta.dot(syn3.T)
                l3_delta = l3_error * nonlin(l3,deriv=True)
                l2_error = l3_delta.dot(syn2.T)
                l2_delta = l2_error * nonlin(l2,deriv=True)
                l1_error = l2_delta.dot(syn1.T)
                l1_delta = l1_error * nonlin(l1,deriv=True)
                #syn4 += l4.T.dot(l5_delta)
                #syn3 += l3.T.dot(l4_delta)
                syn2 += l2.T.dot(l3_delta)
                syn1 += l1.T.dot(l2_delta)
                syn0 += l0.T.dot(l1_delta)
            errorflag += 1
f = open('neuralshorsweights.txt', "w+")
for x in range(len(syn0)):
    for y in range(len(syn0[0])):
        f.write(str(syn0[x][y])+"\n")
for x in range(len(syn1)):
    for y in range(len(syn1[0])):
        f.write(str(syn1[x][y])+"\n")
for x in range(len(syn2)):
    for y in range(len(syn2[0])):
        f.write(str(syn2[x][y])+"\n")
#for x in range(len(syn3)):
#    for y in range(len(syn3[0])):
#        f.write(str(syn3[x][y])+"\n")
#for x in range(len(syn4)):
#    for y in range(len(syn4[0])):
#        f.write(str(syn4[x][y])+"\n")
X = np.array([fix_factorable(int(input("test number: ")))])
l0 = X
l1 = nonlin(np.dot(l0,syn0))
l2 = nonlin(np.dot(l1,syn1))
l3 = nonlin(np.dot(l2,syn2))
#l4 = nonlin(np.dot(l3,syn3))
#l5 = nonlin(np.dot(l4,syn4))
x1 = np.array([0.000000000000 for x in range(int(len(l3[0])/2))])
x2 = np.array([0.000000000000 for x in range(int(len(l3[0])/2))])
print(l3)
for x in range(int(len(l3[0])/2)):
    x1[x] = round(l3[0][x])
print(x1)
x1 = int(from_binary(x1))
for x in range(int(len(l3[0])/2)):
    x2[x] = round(l3[0][x+int(len(l3[0])/2)])
print(x2)
x2 = int(from_binary(x2))
confidence = 0
for x in range(len(l3[0])):
    confidence += 1-abs(round(l3[0][x])-l3[0][x])
confidence = confidence/(len(l3[0]))
print("factored "+str(x1)+" "+str(x2))
print("traditional confidence "+str(confidence))
print("confidence "+str(confidence**10))
input("")