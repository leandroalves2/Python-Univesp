#Lista
l = [1,2,3,"Lapis",'N']
def imprime_rec(l, i=0):
    if i < len(l):
        print(l[i])
        imprime_rec(l, i+1)
print("List:")
imprime_rec(l)

print()
#contagem
print("Countdown:")
def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)
countdown(3)