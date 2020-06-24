"""
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each test case, in a new line, print the starting and ending positions(1 indexing) of first such occurring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Test case 1: sum of elements from 2nd position to 4th position is 12
Test case 2: sum of elements from 1st position to 5th position is 15
"""


def find_subarray(input_array, required_sum):
    for i in range(0, len(input_array)):
        for j in range(0, len(input_array)):
            arr = input_array[i:j+1]
            if sum(arr) == required_sum:
                return "{} {}".format(i+1, j+1)
    return "-1"


INPUT = """2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10"""

num_test_cases = int(INPUT.split("\n")[0])
input_data = INPUT.split("\n")[1:]

for i in range(0, len(input_data), 2):
    expected_sum = int(input_data[i].split(" ")[1])
    arr = input_data[i+1].split(" ")
    for j in range(0, len(arr)):
        arr[j] = int(arr[j])

    print(find_subarray(arr, expected_sum))
