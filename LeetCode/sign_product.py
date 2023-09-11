def arraySign(nums) -> int:
    total_product = 1
    for num in nums:
        total_product *= num
    
    return 1 if total_product > 0 else -1 if total_product< 0 else 0

print(arraySign([0]))