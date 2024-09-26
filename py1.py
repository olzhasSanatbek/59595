nums = [1, 1, 1, 3, 5, 5, 7, 8, 8, 8]

def remove_duplicates(nums):
    k = 0 

    while k < len(nums) - 1:
        if nums[k] != nums[k + 1]:
            k += 1  
        else:
            del nums[k + 1]  
    
    return len(nums)

nums = [1, 1, 1, 3, 5, 5, 7, 8, 8, 8]
k = remove_duplicates(nums)
print(k)  
print(nums) 