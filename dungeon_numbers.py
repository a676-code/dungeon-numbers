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
    if len(args) == 1:
        return args[0]
    else:
        num = base(args[0], args[1])
        args = list(args)
        if (args):
            args.pop(0)
            if (len(args) > 1):
                args.pop(0)
                return topDown(num, *tuple(args))
            else:
                return num

print(bottomUp(10), end=', ') # 10
print(bottomUp(10, 11), end=', ') # 11
print(bottomUp(10, 11, 12), end=', ') # 13
print(bottomUp(10, 11, 12, 13), end=', ') # 16
print(bottomUp(10, 11, 12, 13, 14), end=', ') # 20
print(bottomUp(10, 11, 12, 13, 14, 15), end=', ') # 25
print(bottomUp(10, 11, 12, 13, 14, 15, 16), end=', ') # 31
print(bottomUp(10, 11, 12, 13, 14, 15, 16, 17), end=', ') # 38
print(bottomUp(10, 11, 12, 13, 14, 15, 16, 17, 18)) # 46

print(bottomUp(10), end=', ') # 10
print(bottomUp(11, 10), end=', ') # 11
print(bottomUp(12, 11, 10), end=', ') # 13
print(bottomUp(13, 12, 11, 10), end=', ') # 16
print(bottomUp(14, 13, 12, 11, 10), end=', ') # 20
print(bottomUp(15, 14, 13, 12, 11, 10), end=', ') # 25
print(bottomUp(16, 15, 14, 13, 12, 11, 10), end=', ') # 31
print(bottomUp(17, 16, 15, 14, 13, 12, 11, 10), end=', ') # 38
print(bottomUp(18, 17, 16, 15, 14, 13, 12, 11, 10)) # 46

print(topDown(10), end=', ') # 10
print(topDown(10, 11), end=', ') # 11
print(topDown(10, 11, 12), end=', ') # 13
print(topDown(10, 11, 12, 13), end=', ') # 16
print(topDown(10, 11, 12, 13, 14), end=', ') # 20 
print(topDown(10, 11, 12, 13, 14, 15), end=', ') # 30
print(topDown(10, 11, 12, 13, 14, 15, 16), end=', ') # 48
print(topDown(10, 11, 12, 13, 14, 15, 16, 17), end=', ') # 76
print(topDown(10, 11, 12, 13, 14, 15, 16, 17, 18)) # 132

print(topDown(10), end=', ') # 10
print(topDown(11, 10), end=', ') # 11
print(topDown(12, 11, 10), end=', ') # 13
print(topDown(13, 12, 11, 10), end=', ') # 16
print(topDown(14, 13, 12, 11, 10), end=', ') # 20
print(topDown(15, 14, 13, 12, 11, 10), end=', ') # 28
print(topDown(16, 15, 14, 13, 12, 11, 10), end=', ') # 45
print(topDown(17, 16, 15, 14, 13, 12, 11, 10), end=', ') # 73
print(topDown(18, 17, 16, 15, 14, 13, 12, 11, 10)) # 73