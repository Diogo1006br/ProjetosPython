# if , elif e else

# exemplo de if 
idade = 18
print("Exemplo de comando if:")
if idade >= 18:
    print("Voce é maior de idade.")

if idade == 19:
    print("Voce tem 19 anos")

if idade < 18:
    print("Voce é menor de idade")

if idade != 10:
    print("Voce nao tem 10 anos")


idade = int(input("Quantos anos voce tem? "))
print("Exemplo de comando else:")
if idade >= 18:
    print("Voce é maior de idade.")
elif idade >= 12:
    print("Voce é um adolescente.")
else:
    print("Voce é menor de idade.")

mensagem = "Pode tirar a carteira de habilitacao." if idade >= 18 else "Nao pode tirar a carteira de habilitacao"
print(mensagem)