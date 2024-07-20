import math
def is_perfect_cube(n):
    if n < 0:
        return round(n ** (1/3)) ** 3 == n
    return round(n ** (1/3)) ** 3 == n

n = int(input("Enter a number: "))
print("Perfect Cube" if is_perfect_cube(n) else "Not Perfect Cube")
