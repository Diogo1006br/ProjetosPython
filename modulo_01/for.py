""" loop é uma estrutura que permite repetir um bloco de codigo enquanto uma condicao for verdadeira."""

print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"Nome": "Diogo", "idade": 20, "cidade": "Joinville"}
print("For utilizando dicionario = chaves")
for chave in pessoa.keys():
    print(chave)
    
print("\nFor utilizando dicionario = valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utilizando dicionario = itens")
for chave, valor in pessoa.items():
    print(f"{chave} = {valor}")

# range(): intervalo numerico 
# [0,1,2,3,4,5,6,7,8,9]
print("\n Utilizando a funcao range()")
for numero in range(5):
    print("Numero:", numero)

print("\n Utilizando a funcao range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

# enumerate() permite que use uma lista 
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")