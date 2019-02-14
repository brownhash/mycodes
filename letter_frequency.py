class frequency:
    def freq(s):
        letters=[]
        freq=[]
        c=0
        for i in range(0,len(s)):
            if(s[i] not in letters):
                for j in range(i,len(s)):
                    if(s[i]==s[j]):
                        c+=1
                letters.append(s[i])
                freq.append(c)
            c=0
