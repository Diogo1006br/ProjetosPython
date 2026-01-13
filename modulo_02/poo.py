# POO



# Pessoa exemplo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Objetos
pessoa1 = Pessoa("Diogo", 20)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="DIOGO", idade=25)
mensagem = pessoa2.saudacao()
print(mensagem)

