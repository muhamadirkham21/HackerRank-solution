def calPoints(operations) -> int:
    stack = []
    for i in operations:
        if i == '+':
            stack.append(stack[-1]+stack[-2])
        elif i == 'C':
            stack.pop()
        elif i == 'D':
            stack.append(2 * stack[-1])
        else:
            stack.append(int(i))
    
    return sum(stack)

print(calPoints(["1","C"]))