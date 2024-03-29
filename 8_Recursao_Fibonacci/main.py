import time

def rec_fibonacci(n):
    if n <= 1:
        return n
    else:
        return rec_fibonacci(n-1) + rec_fibonacci(n-2)

def int_fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a + b
        return b

n = 10

start = time.time()
print(rec_fibonacci(n))
print("Tempo de recursao: ", (time.time() - start))

start = time.time()
print(int_fibonacci(n))
print("Tempo de interação: ", time.time() - start)

