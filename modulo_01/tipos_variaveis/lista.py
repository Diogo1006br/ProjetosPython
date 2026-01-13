# Declaracao
minha_lista = [1, 2, 3, 4, 5, "Rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo a lista
minha_lista[0] = "python"
print("Minha lista de exemplo", minha_lista)

print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5]) 
print("minha_lista[1:7]:", minha_lista[1:7])  #minha_lista[1], minha_lista[2],...minha_lista[6]
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])

# Métodos de lista

# Método append(): Adicion a um elemento no final da lista

minha_lista.append(6)
print("Apos append(6):", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Indece do elemento 6:", indice)

# Método insert: Insere um elemento em um  indice especifico
minha_lista.insert(2, 10)
print("Apos o insert(2, 10):", minha_lista)

# Método pop : Remove e retorna o elemento de indice especifico

elemento_removido = minha_lista.pop(3)
print("Elemento Removido:", elemento_removido)
print("Apos pop(3):", minha_lista)

# Método remove : Ele remove o primeiro elemento com valor especificado

minha_lista.remove(True)
print("Apos o remove(True):", minha_lista)

# Metodo sort
minha_lista.sort()
print("Minha lista()", minha_lista)