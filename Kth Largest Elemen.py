def find_kth_largest(nums, k):
    nums.sort(reverse=True)#sorts the list nums in descending order
    return nums[k-1]

#test case
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))
