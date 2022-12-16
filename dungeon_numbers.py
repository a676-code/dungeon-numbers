import sys

sys.path.append("C:\\Users\\\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages")

import numpy as np

def base(a, b):
    result = 0
    digits_backward = [int(d) for d in str(a)]
    digits = np.flip(digits_backward)
    for i, d in enumerate(digits):
        result += d * (int(b) ** i)
    return result

# Descending from the bottom up
# 11
print(base(10, 11))
# 13
print(base(10, base(11, 12)))
# 16
print(base(10, base(11, base(12, 13))))
# 20
print(base(10, base(11, base(12, base(13, 14)))))
# 25
print(base(10, base(11, base(12, base(13, base(14, 15))))))

print()

# Ascending from the bottom up
# 11
print(base(11, 10))
# 13
print(base(base(10, 11), 12))
# 16
print(base(base(base(10, 11), 12), 13))
# 20
print(base(base(base(base(10, 11), 12), 13), 14))
# 30
print(base(base(base(base(base(10, 11), 12), 13), 14), 15))

print()

# Descending from the bottom up
#11
print(base(11, 10))
# 13
print(base(12, base(11, 10)))
# 16
print(base(13, base(12, base(11, 10))))
# 20
print(base(14, base(13, base(12, base(11, 10)))))
# 25
print(base(15, base(14, base(13, base(12, base(11, 10))))))

print()

# Descending from the top down
# 11
print(base(11, 10))
# 13
print(base(base(12, 11), 10))
# 16
print(base(base(base(13, 12), 11), 10))
# 20
print(base(base(base(base(14, 13), 12), 11), 10))
# 28
print(base(base(base(base(base(15, 14), 13), 12), 11), 10))