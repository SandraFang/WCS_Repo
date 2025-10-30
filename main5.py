PrimeRange=int(input("Enter the number:"))
PrimeList=[]

i=2
while (i<PrimeRange):
    j=2
    isPrime=False
    #decide if i is prime
    while (j<i):
        if i%j==0:
            isPrime=False
            break
        else:
            j+=1
            if j==i: isPrime=True
    if isPrime==True:
        PrimeList.append(i)
    i+=1
print (PrimeList)