
def fib_recure(n):
    if (n <= 2):
        return 1
    return fib_recure(n - 1) + fib_recure(n - 2)

print(fib_recure(6))
print(fib_recure(7))
print(fib_recure(8))


def main():
    print(fib_recure(6))
    print(fib_recure(7))
    print(fib_recure(8))

if __name__ == "__main__":
    main();
