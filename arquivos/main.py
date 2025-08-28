#COLEÇÕES: São variáveis que armazenam múltiplos valores.
#ORDENAÇÃO: É possível devido ao index, atribuido a cada item das coleções ordenadas, coisa que não acontece nas coleções não ordenadas.

#Coleção ordenada e mutável, permite membros dublicados
print("--------LISTA--------") 
#LISTA
palavras = ["Carro", True, "Avião", 3.14]
print(type(palavras))

for palavra in palavras:
    print(type(palavra))
    
#Coleção ordenda e imutável. Permite membros duplicados.
#Ou seja, após adicionar itens, não é possível editar ou remove-los   
print("--------TUPLA--------") 
#TUPLA
tupla = ("carro", True)
print(type(tupla))

#Coleção ordenada e mutável, não permite membros dublicados
#Aqui é trabalhado no sistema de CHAVE:VALOR. 
print("--------DICIONÁRIO--------") 
dicionario = {"carro": True, "nome": "Pedro"}
#Acessando um valor especifico, é preciso passar a chave desejada. 
print(dicionario["carro"])


#Set é uma coleção não ordenada e não indexada, não permite membros duplicados.
print("--------CONJUNTO--------")
conjunto = {"nome", 2, True, 2.5}