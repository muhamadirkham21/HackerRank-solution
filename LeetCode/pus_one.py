def plusOne(digits):
    digit = int(''.join(map(str, digits))) + 1
    return [int(i) for i in str(digit)]

a = (plusOne([1, 9]))
print(a)