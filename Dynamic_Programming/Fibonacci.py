
# recursively calculating Fibonacci number
def fib_recure(n):
    if n <= 2:
        return 1
    return fib_recure(n - 1) + fib_recure(n - 2)


print(fib_recure(6))
print(fib_recure(7))
print(fib_recure(8))


#Dynamic-programming using memoization:
def fibDP(n, fib_table):
    if n in fib_table:
        return fib_table[n];
    if n <= 2:
        return 1;
    fib_table[n] = fibDP(n - 1, fib_table) + fibDP(n - 2, fib_table);
    return fib_table[n];


print(fibDP(6, dict()));
print(fibDP(20, dict()));
print(fibDP(50, dict()));


# def main():
#     print(fib_recure(6))
#     print(fib_recure(7))
#     print(fib_recure(8))

# if __name__ == "__main__":
#     main();
