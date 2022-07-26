# Problem:
# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# To calculate the sum of a contiguous subarray, utilize the sum of the previous subarray.

# Steps:
# 1. Subtract element going out of sliding window (first element of the window)
# 2. Add next element to sliding window (the element right after the end of the window)

def max_sub_array_of_size_k(k, arr):
    if k>len(arr):
        return -1
    maxSum=0
    currSum=0
    for i in range(k):
        currSum+=arr[i]
    maxSum = currSum
    for i in range(k,len(arr)):
        currSum +=arr[i]-arr[i-k]
        maxSum = max(maxSum,currSum)
    return maxSum
    
def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()