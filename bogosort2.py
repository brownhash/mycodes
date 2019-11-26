def bogoSort(a):
    n = len(a)
    while (is_sorted(a) == False):
        shuffle(a)

def is_sorted(a):
    n = len(a)
    for i in range(0, n - 1):
        if (a[i] > a[i + 1]):
            return False
    return True

def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]

n=10000
arr=[]
import random, time
for i in range (0,n):
    index=random.randint(0,100000)
    arr.append(index)
start=time.time()
bogoSort(arr)
print("Sorted array - ")
print(arr)
print("Sorting time: {} sec".format(time.time()-start))

