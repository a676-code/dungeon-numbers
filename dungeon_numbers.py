import sys

sys.path.append("C:\\Users\\\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages")

import numpy as np

def dungeonNumber(a, b):
    result = 0
    digits_backward = [int(d) for d in str(a)]
    digits = np.flip(digits_backward)
    for i, d in enumerate(digits):
        result += d * (int(b) ** i)
    return result

# Descending from the bottom up
# 11
print(dungeonNumber(10, 11))
# 13
print(dungeonNumber(10, dungeonNumber(11, 12)))
# 16
print(dungeonNumber(10, dungeonNumber(11, dungeonNumber(12, 13))))
# 20
print(dungeonNumber(10, dungeonNumber(11, dungeonNumber(12, dungeonNumber(13, 14)))))
# 25
print(dungeonNumber(10, dungeonNumber(11, dungeonNumber(12, dungeonNumber(13, dungeonNumber(14, 15))))))

print()

# Ascending from the bottom up
# 11
print(dungeonNumber(11, 10))
# 13
print(dungeonNumber(dungeonNumber(10, 11), 12))
# 16
print(dungeonNumber(dungeonNumber(dungeonNumber(10, 11), 12), 13))
# 20
print(dungeonNumber(dungeonNumber(dungeonNumber(dungeonNumber(10, 11), 12), 13), 14))
# 30
print(dungeonNumber(dungeonNumber(dungeonNumber(dungeonNumber(dungeonNumber(10, 11), 12), 13), 14), 15))

print()

# Descending from the bottom up
#11
print(dungeonNumber(11, 10))
# 13
print(dungeonNumber(12, dungeonNumber(11, 10)))
# 16
print(dungeonNumber(13, dungeonNumber(12, dungeonNumber(11, 10))))
# 20
print(dungeonNumber(14, dungeonNumber(13, dungeonNumber(12, dungeonNumber(11, 10)))))
# 25
print(dungeonNumber(15, dungeonNumber(14, dungeonNumber(13, dungeonNumber(12, dungeonNumber(11, 10))))))

print()

# Descending from the top down
# 11
print(dungeonNumber(11, 10))
# 13
print(dungeonNumber(dungeonNumber(12, 11), 10))
# 16
print(dungeonNumber(dungeonNumber(dungeonNumber(13, 12), 11), 10))
# 20
print(dungeonNumber(dungeonNumber(dungeonNumber(dungeonNumber(14, 13), 12), 11), 10))
# 28
print(dungeonNumber(dungeonNumber(dungeonNumber(dungeonNumber(dungeonNumber(15, 14), 13), 12), 11), 10))