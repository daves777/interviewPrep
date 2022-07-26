# Problem:
# Given an array of positive numbers and a positive number S find the length of the smallest contiguous subarray
# whose sum is greater than or equal to S. Return 0 if no such subarray exists.

def smallest_subarray_sum(s, arr):
    start,end = 0,1
    out = 0
    currSum = arr[0]
    while(end<len(arr)):
        while(currSum<s):
            currSum+=arr[end]
            end+=1
            if(end> len(arr)):
                return out
        length = end-start+1
        if(out==0):
            out = length
        out = min(out,length)
        while(currSum>=s and start < end):
            currSum-=arr[start]
            start+=1
        out= min(out,end-start+1)
    return out
            

    
def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))

main()