def fat(n):
    if n == 0:
        return 1
    else:
        resp = n * fat(n-1)
        return resp

n = int(input("Digite um numero para ser fatorado: "))
print(fat(n))