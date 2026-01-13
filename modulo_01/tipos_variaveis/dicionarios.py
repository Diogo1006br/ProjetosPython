# é uma colecao nao ordenada de pares , chave e valor

# Criando um dicionario de exemplo

pessoa = {"nome": "Diogo", "idade": 30, "cidade": "Joinville"}

print("Meu dicionario ", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Ramuski"
print("Sobrenome:", pessoa["sobrenome"])
print("Meu dicionario de exemplo", pessoa)

pessoa["idade"] = 31
print("Idade:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]

print("Meu dicionario de exemplo", pessoa)

# Métodos: keys(), values(), items()

chaves = list(pessoa.keys())
print("Chave do dicionarios:", chaves)
print("Primeira chave:", chaves[0])

# Métodos values 

valores = list(pessoa.values())
print("Valores de dicionarios:", valores)
print("Primeiro valor do dicionario:", valores[0])


# Método items , cada elemento é uma tupla com chave e valor.

itens = list(pessoa.items())
print("Pares chave-valor do dicionario", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))