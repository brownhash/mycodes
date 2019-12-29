t=int(input())
nums=[]
def multi(n1,n2):
    N1=list(str(n1)[::-1])
    N2=list(str(n2)[::-1])
    result=""
    for i in N2:
        for j in range(0,len(N1)-1):
            res=int(N1[j])*int(i)
            if(res>9):
                a=int(str(res)[::-1])%10
                result+=str(a)
    return(result)

for i in range(0,t):
    n1,n2=list(map(int,input().split()))
    nums.append(n1)
    nums.append(n2)
result=[]
for i in range(0,len(nums),2):
    print("{} {}".format(len(multi(nums[i],nums[i+1])),multi(nums[i],nums[i+1]))) 
