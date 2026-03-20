#product of Array Except Self:

#Que : Given an array , return an array where each element is the product of all the elements of the array except itself.

def productExceptSelf(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    output = [1] * n

    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]

    for i in range(n):
        output[i] = left[i] * right[i]

    return output
nums = [1, 2, 3, 4]
result = productExceptSelf(nums)
print(result)