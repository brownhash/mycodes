result={}
def set_sort(a):
    b=set(a)
    return(b)

def manual_sort(a):
    b=[]
    for i in a:
        if(i not in b):
            b.append(i)
    return(b)

import time

def test(num):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9] * num
    print("Length of array to be sorted - ",len(a))
    start = time.time()
    c = set_sort(a)
    print(c)
    end = time.time() - start
    print("time by sets = {} sec".format(end))

    start1 = time.time()
    c = manual_sort(a)
    print(c)
    end1 = time.time() - start1
    print("time by manual sort = {} sec".format(end1))

    if (end1 > end):
        #result[num]='set'
        print("\nmanual sort took more time: {} sec".format(end1-end))
    else:
        #result[num]='mannual'
        print("\nset sort took more time: {} sec".format(end-end1))

test(10000000)

"""
Execution results -
system config ( 
    Macbook Pro 2015 
    2.2 GHz i7
    16GB 1600 MHz 
)
 
Length of array to be sorted -  90000000
{1, 2, 3, 4, 5, 6, 7, 8, 9}
time by sets = 1.073444128036499 sec
[1, 2, 3, 4, 5, 6, 7, 8, 9]
time by manual sort = 8.20632791519165 sec

manual sort took more time: 7.132883787155151 sec
"""