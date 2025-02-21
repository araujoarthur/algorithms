def merge_sort(nums):
    if len(nums) < 2:
        return nums #already sorted
    else:
        middle = len(nums)//2
        left = nums[:middle]
        right = nums[middle:]
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
        return merge(sorted_left, sorted_right)


def merge(first, second):
    final = []
    i, j = 0, 0
    while  i < len(first) and  j < len(second):
        if first[i] < second[j]:
            final.append(first[i])
            i+=1
        else:
            final.append(second[j])
            j+=1
 
    final = final + first[i:] + second[j:]
    return final
