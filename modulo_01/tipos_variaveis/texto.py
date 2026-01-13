# Declarcao
nome_completo = "Dioogo Raamuski"

nome_completo_aspas = """ Diogo
Ramuski"""

nome_completo_quebra = "Diogo \
Ramuski"

nome = "Diogo"
sobrenome = "Ramuski"

# Formatacao
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Diogo" + "Sobrenome")
print("Nome completo (4a forma):" + "Diogo", "Ramuski")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (10a forma): {} {}".format(nome, sobrenome))


# .upper() maiusculo
# .lower() minusculo

"""

>>> nome = "Diogo"
>>> sobrenome = "Ramuski"
>>> nome_completo = "Diogo Ramuski"

>>> nome_completo.count("a")
1
>>> nome_completo.find("a")
7
>>> nome.find("a")
-1
>>> sobrenome.find("a")
1
>>> sobrenome.find("R")
0
>>> nome.encode()
b'Diogo'
>>> nome.encode().decode()
'Diogo'
>>> nome_completo.replace("R" , "a")
'Diogo aamuski'
>>> "-".join("Diogo")
'D-i-o-g-o'
>>> nome_completo.split(" ")
['Diogo', 'Ramuski']
>>> nome_completo.split()
['Diogo', 'Ramuski']

"""


"""

>>> nome = "xDiogo Ramuskix"
>>> nome.strip("X")
'xDiogo Ramuskix'
>>> nome.strip("x")
'Diogo Ramuski'
>>> nome.strip("a")
'xDiogo Ramuskix'
>>> nome.rstrip("x")
'xDiogo Ramuski'
>>> nome_completo
'Diogo Ramuski'
True
>>> nome_completo.startswith("Be")
False
>>> "go" in nome_completo
True
>>> "abc" in nome_completo
False
>>> "abc" not in nome_completo
True
>>>

"""