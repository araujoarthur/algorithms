def insertion_sort(nums):
    i, j = 0, 0 # i is the index we are sorting+1, j is the comparable.
    for i in range(1, len(nums)):
        j = i
        print(f"I: {i} | {nums}")
        while j > 0 and nums[j-1] > nums[j]:
            #temp = nums[j]
            #nums[j] = nums[j-1]
            #nums[j-1] = temp
            # Above is the same as below:
			nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j-=1
    return nums
