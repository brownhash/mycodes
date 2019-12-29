"""
Calculate the longest substring containing a sequence of continuous numbers.

Example:
    input: 1231234
    output: 1234
    Explanation: 
        it has 2 substrings containing a sequence of continuous numbers - 123 and 1234
        As 1234 is greater in length hence 1234 is the answer
    
    input: 1231232345
    output: 2345
            
    input: 123123123
    output: 123
"""

def substring(a):
    try:
        a = str(a)
        substring = ""
        temp = ""

        for i in a:
            if (len(temp) > 0):
                check = temp[len(temp) - 1]
                elem = i
                if (int(elem) == int(check) + 1):
                    temp += elem
                else:
                    temp = ""
                    temp += elem
            else:
                temp += i
            if (len(temp) > len(substring)):
                substring = temp

        return (substring)
    except:
        return("Invalid literals")

print(substring("abcab"))
