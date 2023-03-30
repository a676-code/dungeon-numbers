# dungeon_numbers.py
# Andrew Lounsbury
# 26/3/23
# Purpose: compute dungeon numbers; https://www.youtube.com/watch?v=xNx3JxRhnZE; https://www.youtube.com/watch?v=HFeKdMf01rQ

import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# computes a base b
# input: two numbers, integer or decimal
def base(a, b):
    result = 0
    ls = []
    counter = 0
    countPlaces = False
    for char in str(a):
        if char != '.':
            ls.append(char)
        else:
            countPlaces = True
        if countPlaces:
            counter -= 1
    counter += 1
    digits_backward = [int(d) for d in ls]
    digits = np.flip(digits_backward)
    if countPlaces:
        i = counter
        for d in digits:
            result += d * (b ** i)
            i += 1
    else:
        for i, d in enumerate(digits):
            result += d * (b ** i)
    return result

# Computes a dungeon number
# input: either a sequence of individual numbers or a list of numbers, integer or decimal
def dungeonNumber(*args, mode='b'):
    if isinstance(args[0], list): # input is a list
        numbers = args[0].copy()
        if numbers:
            if mode == 'b': # bottom-up
                num = base(numbers[len(numbers) - 2], numbers[len(numbers) - 1])
                if (numbers):
                    numbers.pop(len(numbers) - 1)
                if (len(numbers) > 1):
                    numbers.pop(len(numbers) - 1)
                    return dungeonNumber(*tuple(numbers), num, mode='b')
                else:
                    return num
            elif mode == 't': # top-down
                if len(numbers) == 1:
                    return numbers[0]
                else:
                    num = base(numbers[0], numbers[1])
                    if (numbers):
                        numbers.pop(0)
                        if (len(numbers) > 1):
                            numbers.pop(0)
                            return dungeonNumber(num, *tuple(numbers), mode='t')
                        else:
                            return num
            else:
                print("ERROR: unknown mode specified")
        else:
            print("Error: list must be nonempty")
    else: # input is a sequence of individual integers
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

# 10, 11, 13, 16, 20, 25, 31, 38, 46
numbers = [10]
for i in range(9):
    print(dungeonNumber(numbers.copy()), end="")
    numbers.append(numbers[len(numbers) - 1] + 1)
    if i < 8:
        print(", ", end="")
print()

# 10, 11, 13, 16, 20, 25, 31, 38, 46
numbers = [10]
for i in range(9):
    print(dungeonNumber(numbers.copy()), end="")
    numbers.insert(0, numbers[0] + 1)
    if i < 8:
        print(", ", end="")
print()

# 10, 11, 13, 16, 20, 30, 48, 76, 132
numbers = [10]
for i in range(9):
    print(dungeonNumber(numbers.copy(), mode='t'), end="")
    numbers.append(numbers[len(numbers) - 1] + 1)
    if i < 8:
        print(", ", end="")
print()

# 10, 11, 13, 16, 20, 28, 45, 73, 133
numbers = [10]
for i in range(9):
    print(dungeonNumber(numbers.copy(), mode="t"), end="")
    numbers.insert(0, numbers[0] + 1)
    if i < 8:
        print(", ", end="")
print()

# Scatterplots of the Golden Ratio
onepointone = []
sequence = []
n = 10
for i in range(n):
    onepointone.append(1.1)
    sequence.append(dungeonNumber(onepointone))
    
df = pd.DataFrame(sequence, columns=["Number"])
indices = [i for i in range(n)]
df['index'] = indices
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/10.png")
plt.show()

onepointone = []
sequence = []
n = 50
for i in range(n):
    onepointone.append(1.1)
    sequence.append(dungeonNumber(onepointone))
    
print(sequence[len(sequence) - 1])
    
df = pd.DataFrame(sequence, columns=["Number"])
indices = [i for i in range(n)]
df['index'] = indices
sns.scatterplot(x="index", y="Number", data=df)
plt.savefig("images/50.png")
plt.show()