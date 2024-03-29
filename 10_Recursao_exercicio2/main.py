import random

def soma(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + soma(list[1:])

list = []
rand = random.randint(1, 100)
l = int(input("Quantos números terão na lista: "))
for i in range(l):
    list.append(random.randint(1,100))

for i in range(l):
    print(list[i])

print("")
print(soma(list))
