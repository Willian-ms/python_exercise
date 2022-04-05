lista = []
lista.append(int(input("Nota 1: ")))
lista.append(int(input("Nota 2: ")))
lista.append(int(input("Nota 3: ")))
lista.append(int(input("Nota 4: ")))

soma = sum(lista)
media = soma / 4

print(lista, media)
