def canMakeArithmeticProgression(arr) -> bool:
    arr = sorted(arr)
    res_arr = [arr[i]-arr[i-1] for i in range(1, len(arr))]
    return max(res_arr) == min(res_arr)
