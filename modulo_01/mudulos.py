print("Exemplo de impotacao de um modulo padrao:")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raizq quadrade de 25 é: {raiz_quadrada}")


print("\n Exemplo de criacao e utilizacao de um modulo personalizado")
from meu_modulo import saudacao, dobro

mensagem = saudacao("Diogo")
resultado_dobro = dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")