def print_even_odd(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i}: Even")
        else:
            print(f"{i}: Odd")

n = int(input("Enter a number n: "))
print_even_odd(n)
