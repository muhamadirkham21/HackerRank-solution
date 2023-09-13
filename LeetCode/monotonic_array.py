x = [1, 2, 2, 3, 4]
y = [7, 6, 6, 5, 1]
z = [1, 2, 1, 3, 5]


def isMonotonic(nums) -> bool:
    is_monoton_ = False

    diff_ = [nums[i-1]-nums[i] for i in range(1, len(nums))]
    if all(list(map(lambda i : i>=0, diff_ ))):
        is_monoton_ = True
    elif all(list(map(lambda i : i<=0, diff_ ))):
        is_monoton_ = True
        
    return is_monoton_