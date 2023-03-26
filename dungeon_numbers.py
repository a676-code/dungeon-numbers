import numpy as np

def base(a, b):
    result = 0
    digits_backward = [int(d) for d in str(a)]
    digits = np.flip(digits_backward)
    for i, d in enumerate(digits):
        result += d * (int(b) ** i)
    return result

def dungeonNumber(*args, mode='b'):
    if isinstance(args[0], list):
        if mode == 'b': # bottom-up
            num = base(args[0][len(args[0]) - 2], args[0][len(args[0]) - 1])
            if (args[0]):
                args[0].pop(len(args[0]) - 1)
            if (len(args[0]) > 1):
                args[0].pop(len(args[0]) - 1)
                return dungeonNumber(*tuple(args[0]), num, mode='b')
            else:
                return num
        elif mode == 't': # top-down
            if len(args[0]) == 1:
                return args[0][0]
            else:
                num = base(args[0][0], args[0][1])
                if (args[0]):
                    args[0].pop(0)
                    if (len(args[0]) > 1):
                        args[0].pop(0)
                        return dungeonNumber(num, *tuple(args[0]), mode='t')
                    else:
                        return num
        else:
            print("ERROR: unknown mode specified")
    else:
        if mode == 'b': # bottom-up
            num = base(args[len(args) - 2], args[len(args) - 1])
            args = list(args)
            if (args):
                args.pop(len(args) - 1)
                if (len(args) > 1):
                    args.pop(len(args) - 1)
                    return dungeonNumber(*tuple(args), num, mode='b')
                else:
                    return num
        elif mode == 't': # top-down
            if len(args) == 1:
                return args[0]
            else:
                num = base(args[0], args[1])
                args = list(args)
                if (args):
                    args.pop(0)
                    if (len(args) > 1):
                        args.pop(0)
                        return dungeonNumber(num, *tuple(args), mode='t')
                    else:
                        return num
        else:
            print("ERROR: unknown mode specified")

print(dungeonNumber(10), end=', ') # 10
print(dungeonNumber(10, 11), end=', ') # 11
print(dungeonNumber(10, 11, 12), end=', ') # 13
print(dungeonNumber(10, 11, 12, 13), end=', ') # 16
print(dungeonNumber(10, 11, 12, 13, 14), end=', ') # 20
print(dungeonNumber(10, 11, 12, 13, 14, 15), end=', ') # 25
print(dungeonNumber(10, 11, 12, 13, 14, 15, 16), end=', ') # 31
print(dungeonNumber(10, 11, 12, 13, 14, 15, 16, 17), end=', ') # 38
print(dungeonNumber(10, 11, 12, 13, 14, 15, 16, 17, 18)) # 46

print(dungeonNumber(10), end=', ') # 10
print(dungeonNumber(11, 10), end=', ') # 11
print(dungeonNumber(12, 11, 10), end=', ') # 13
print(dungeonNumber(13, 12, 11, 10), end=', ') # 16
print(dungeonNumber(14, 13, 12, 11, 10), end=', ') # 20
print(dungeonNumber(15, 14, 13, 12, 11, 10), end=', ') # 25
print(dungeonNumber(16, 15, 14, 13, 12, 11, 10), end=', ') # 31
print(dungeonNumber(17, 16, 15, 14, 13, 12, 11, 10), end=', ') # 38
print(dungeonNumber(18, 17, 16, 15, 14, 13, 12, 11, 10)) # 46

print(dungeonNumber(10, mode='t'), end=', ') # 10
print(dungeonNumber(10, 11, mode='t'), end=', ') # 11
print(dungeonNumber(10, 11, 12, mode='t'), end=', ') # 13
print(dungeonNumber(10, 11, 12, 13, mode='t'), end=', ') # 16
print(dungeonNumber(10, 11, 12, 13, 14, mode='t'), end=', ') # 20 
print(dungeonNumber(10, 11, 12, 13, 14, 15, mode='t'), end=', ') # 30
print(dungeonNumber(10, 11, 12, 13, 14, 15, 16, mode='t'), end=', ') # 48
print(dungeonNumber(10, 11, 12, 13, 14, 15, 16, 17, mode='t'), end=', ') # 76
print(dungeonNumber(10, 11, 12, 13, 14, 15, 16, 17, 18, mode='t')) # 132

print(dungeonNumber(10, mode='t'), end=', ') # 10
print(dungeonNumber(11, 10, mode='t'), end=', ') # 11
print(dungeonNumber(12, 11, 10, mode='t'), end=', ') # 13
print(dungeonNumber(13, 12, 11, 10, mode='t'), end=', ') # 16
print(dungeonNumber(14, 13, 12, 11, 10, mode='t'), end=', ') # 20
print(dungeonNumber(15, 14, 13, 12, 11, 10, mode='t'), end=', ') # 28
print(dungeonNumber(16, 15, 14, 13, 12, 11, 10, mode='t'), end=', ') # 45
print(dungeonNumber(17, 16, 15, 14, 13, 12, 11, 10, mode='t'), end=', ') # 73
print(dungeonNumber(18, 17, 16, 15, 14, 13, 12, 11, 10, mode='t')) # 133