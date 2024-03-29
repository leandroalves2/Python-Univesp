import random

def maior(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], maior(list[1:]))

list = []
rand = random.randint(1, 100)
l = int(input("Quantos números terão na lista: "))
for i in range(l):
    list.append(random.randint(1,100))

for i in range(l):
    print(list[i])

print("")
print(maior(list))

