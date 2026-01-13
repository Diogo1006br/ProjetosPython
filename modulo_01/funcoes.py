# Exemplo 
def saudacao(nome):
    print(f"olá, {nome}!")

print("\n Chamando a funcao saudacao:")
saudacao("Alice")
saudacao("Bob")

# Funcao com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n Chamando funcao quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado da funcao quadrado", resultado_quadrado)

# Funcao com multiplos parametros 
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\n Chamando a funcao soma:")
numero1 = 25
numero2 = 30
resultado_soma = soma(numero1, numero2)
print("A soma  do numero %s e numero %s é %s" % (numero1, numero2, resultado_soma))