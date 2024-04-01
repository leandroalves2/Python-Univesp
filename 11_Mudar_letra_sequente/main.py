# programa para mudar a letra para proxima letra

def mudar_palavra():
    palavra = input("Digite uma palavra: ");
    lista = list(palavra);
    temp = "";
    for x in lista:
        if (x == 'z'):
            temp += 'a';
        else:
            temp += chr(ord(x) + 1)
    return temp;


mudar_palavra();