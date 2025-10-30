arr=[35,68,99,76,85,25,78,100,67]
for i in range(1,len(arr)):
    k=arr[i]
    j=i-1
    while j>=0 and k<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=k
print ("Insertion Sort:", arr)