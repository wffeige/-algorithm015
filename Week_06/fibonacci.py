#!coding:utf-8


memory = dict()


def fib1(n):
    if n <= 1:
        return n

    if memory.setdefault(n, 0) == 0:
        memory[n] = fib1(n - 1) + fib1(n - 2)

    return memory[n]


def fib2(n):
    """
    自底向上得方法
    return
    """
    memory[0] = 0
    memory[1] = 1
    if n < 1:
        return memory[n]

    i = 0
    while i <= n:
        if memory.setdefault(n, 0) == 0:
            memory[i] = memory[i-1] + memory[i-2]
        i += 1

    return memory[n]


def main():
    n = 10
    print(fib1(n))
    print(fib2(n))


if __name__ == "__main__":
    main()


