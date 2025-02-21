def bubble_sort(nums):
    nums_copy = nums.copy()
    swapped = True
    end = len(nums_copy)
    while swapped:
        swapped = False
        print(nums_copy)
        for i in range(1, end):
            if nums_copy[i] < nums_copy[i-1]:
                swapped = True
                tmp = nums_copy[i]
                nums_copy[i] = nums_copy[i-1]
                nums_copy[i-1] = tmp
                print(f"Swapped nums_copy[{i}] = {nums_copy[i]} with nums_copy[{i-1}] = {nums_copy[i-1]}")
        end -= 1 
                
    return nums_copy
