def shellsort(arr):
    n=len(arr)
    gap=int(n/2)

    while(gap>0):
        for i in range(gap, n):
            temp=arr[i]
            j=i
            while j>=gap and arr[j-gap]>temp:
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=temp
        gap=int(gap/2)

n=1000000
arr=[]
import random, time
for i in range (0,n):
    index=random.randint(0,1000000)
    arr.append(index)
start=time.time()
shellsort(arr)
print("Sorted array - ")
print(arr)
print("Sorting time: {} sec".format(time.time()-start))
