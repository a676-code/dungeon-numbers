import numpy as np

def base(a, b):
    result = 0
    digits_backward = [int(d) for d in str(a)]
    digits = np.flip(digits_backward)
    for i, d in enumerate(digits):
        result += d * (int(b) ** i)
    return result

def bottomUp(*args):
    num = base(args[len(args) - 2], args[len(args) - 1])
    args = list(args)
    if (args):
        args.pop(len(args) - 1)
        if (len(args) > 1):
            args.pop(len(args) - 1)
            return bottomUp(*tuple(args), num)
        else:
            return num
        
def topDown(*args):
    num = base(args[0], args[1])
    args = list(args)
    if (args):
        args.pop(0)
        if (len(args) > 1):
            args.pop(0)
            return topDown(num, *tuple(args))
        else:
            return num
    

print("HERE: ")
print(topDown(10, 11, 12, 13, 14, 15))
print()

print(bottomUp(10)) # 10
print(bottomUp(10, 11)) # 11
print(bottomUp(10, 11, 12)) # 13
print(bottomUp(10, 11, 12, 13)) # 16
print(bottomUp(10, 11, 12, 13, 14)) # 20
print(bottomUp(10, 11, 12, 13, 14, 15)) # 25

# print()

# print(bottomUp(11, 10)) # 11
# print(bottomUp(12, 11, 10)) # 13
# print(bottomUp(13, 12, 11, 10)) # 16
# print(bottomUp(14, 13, 12, 11, 10)) # 20
# print(bottomUp(15, 14, 13, 12, 11, 10)) # 25

print()
# Ascending from the bottom up
# 11
print(base(10, 11))
# 13
print(base(base(10, 11), 12))
# 16
print(base(base(base(10, 11), 12), 13))
# 20
print(base(base(base(base(10, 11), 12), 13), 14))
# 30
print(base(base(base(base(base(10, 11), 12), 13), 14), 15))

print()


# print()
# print(topDown(10, 11)) # 11
# print(topDown(10, 11, 12)) # 13
# print(topDown(10, 11, 12, 13)) # 16
# print(topDown(10, 11, 12, 13, 14)) # 20 
# print(topDown(10, 11, 12, 13, 14, 15)) # 30

# print()
# print(topDown(11, 10)) # 11
# print(topDown(12, 11, 10)) # 13
# print(topDown(13, 12, 11, 10)) # 16
# print(topDown(14, 13, 12, 11, 10)) # 20
# print(topDown(15, 14, 13, 12, 11, 10)) # 28