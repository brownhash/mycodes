def insertionsort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

n=100000
arr=[]
import random, time
for i in range (0,n):
    index=random.randint(0,1000000)
    arr.append(index)

start=time.time()
insertionsort(arr)
print("Sorted List-")
print(arr)
print("Sorting time: {} sec".format(time.time()-start))
