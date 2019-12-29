a=[-2,1,-3,4,-1,2,1,-5,4]

sublist = []

temp = 0

def check(a,elem,i):
    if((i+1)<len(a)):
        if(a[i+1]>elem):
            return(a[i+1])
        else:
            return(False)
    else:
        return(False)

for i in range(0,len(a)):
    sub =[a[i]]
    elem = a[i]
    data = check(a,elem,i)
    while(data!=False):
        sub.append(data)
        sublist.append(sub)
        data = check(a,data,i+1)

print(sublist)

