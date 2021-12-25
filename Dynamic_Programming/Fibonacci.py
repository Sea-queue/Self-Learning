
# recursively calculating Fibonacci number
def fib_recure(n):
    if n <= 2:
        return 1
    return fib_recure(n - 1) + fib_recure(n - 2)


#Dynamic-programming using memoization:
def fibDP(n, fib_table):
    if n in fib_table:
        return fib_table[n];
    if n <= 2:
        return 1;
    fib_table[n] = fibDP(n - 1, fib_table) + fibDP(n - 2, fib_table);
    return fib_table[n];


# Iterative using tabulation:
def fibTabulation(n):
    table = [0] * (n + 3)
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        table[i + 2] += table[i]

    return table[n]



print(fib_recure(6))
print(fib_recure(7))
print(fib_recure(8))
print(fibDP(6, dict()))
print(fibDP(20, dict()))
print(fibDP(50, dict()))
print(fibTabulation(50))


# def main():
#     print(fib_recure(6))
#     print(fib_recure(7))
#     print(fib_recure(8))

# if __name__ == "__main__":
#     main();
