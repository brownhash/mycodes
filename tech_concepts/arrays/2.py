"""
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. First line of each test case contains an Integer N denoting size of array and the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1

Explanation:
Test case 1: There are 2 triplets: 1 + 2 = 3 and 3 +2 = 5
"""


def find_triplet(arr):
    result = []
    for i in arr:
        for j in arr:
            for k in arr:
                if ((i+j == k) or (j+k == i) or (k+i == j)) and (i != j and i != k and j != k):
                    data = [i, j, k]
                    data.sort()
                    if data not in result:
                        result.append(data)

    if len(result) == 0:
        return -1
    else:
        return len(result)
