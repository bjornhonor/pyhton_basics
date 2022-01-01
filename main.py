
#PRINT -> PADRAO, UTILIZADO AQUI COMO INTERFACE
print("Hello World!")

#VARIABLES -> VARIAVEIS E SEUS TIPOS
#strings
#name = "bruno"
#last_name = "carrara"
#full_name = name+" "+last_name
#print("opa "+name)
#print(name+" "+last_name)
#print(full_name)
#print(type(name))

#INT -> INTEIRO
#age = 21
#age += 1
#print(age)
#print(type(age))
#print("sua idade: "+str(age))

#FLOAT -> DECIMAL
#altura = 176.5
#print(altura)
#print(type(altura))
#print("sua altura: "+str(altura)+" cm")

#boolean
#situacao = False
#print(situacao)
#print(type(situacao))

#MULTASSINGMENT -> VARIVEIS QUE POSSUEM O MSM VALOR | OU DECLARACAO DE VARIAVEIS POR ORDEM RESPECTIVA
#name, age, is_hot = "bruno", 20, True
#print(name)
#print(age)
#print(is_hot)

#mui = mucho = much = muy = "muito"
#print(much)

#STRING FUNCTIONS -> MANIPULACAO DE STRINGS
#nome = "bjorn"
#print(len(nome))
#print(nome.find("b"))
#print(nome.capitalize())
#print(nome.upper())
#print(nome.lower())
#print(nome.isdigit())
#print(nome.isalpha())
#print(nome.count("b"))
#print(nome.replace("b", "j"))
#print(nome*2)

#TYPECASTING -> MUDAR O TIPO DE VARIAVEL
#x = 1
#y = 2.0
#z = "3"
#z = int(z)
#x = float(x)
#y = str(y)
#print(x)
#print(int(y))
#print(z*2)

#USER INPUT -> PEGAR VALOR INSERIDO PELO USUARIO E ATRIBUILO A UMA VARIAVEL
#nome = input("digite seu nome")
#age = int(input("digite sua idade"))
#altura = float(input("digite sua altura"))
#print("bem vindo(a) "+nome)
#print("voce tem ", age, "anos")
#print("vc tem "+str(altura)+"cm de altura")

#NUMBERS -> MANIPULACAO MATEMATICA DE NUMEROS
#import math
#x = 1
#y = 2
#z = 3
#pi = 3.14
#negativo = -1
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(negativo))
#print(pow(pi, 2))
#print(math.sqrt(pi))
#print(max(x, y, z))
#print(min(x, y, z))

#STRINGSLICE -> PEGAR PARTES DE UMA STRING
#name = "bjorn honor"
#first_caracter = name[0]
#first_name = name[0:5]
#last_name = name[6:11]
#eita = name[:10:2]
#reverse = name[::-1]
#link = "www.youtube.com"
#slice = slice(4, -4)

#print(first_caracter)
#print(first_name)
#print(last_name)
#print(eita)
#print(reverse)
#print(link[slice])

#IF ELSE -> COMPARACAO DE VALORES
#idade = int(input("digite sua idade:"))
#if idade >= 18:
#    print("vc e maior de idade")
#elif idade < 0:
#    print("pare de mentir")
#else:
#    print("vc e menor de idade")

#AND, OR, NOT -> APLICACOES NO IF
#temp = int(input("quantos graus esta fazendo la fora?:"))
#if temp>-5 and temp<15:
#    print("tempratura está otima!")
#elif temp<-5 or temp>15:
#    print("a temperatura está ruim!")
#
#if(not(temp>-5 and temp<15)):
#    print("temperatura esta ruim (reversed)")

#WHILE -> LOOP DEFINIDO OU INDEFINIDO
#nome = ""
#while len(nome) == 0:
#    nome = input("Digite seu nome")
#print("bem vindo(a) "+nome.capitalize()+"!")

#nome = None
#while not nome:
#    nome = input("Digite seu nome")
#print("opa "+nome.capitalize()+" tudo bem?")

#FOR -> LOOP DEFINIDO
#for i in range(10):
#    print(i+1)

#for i in range(50, 100+1, 2):
#    print(i)

#for i in "bjorn":
#    print(i)

#import time
#for seconds in range(10, 0, -1):
#    print(seconds)
#    time.sleep(1)
#print("Happy new year!")

#NESTED LOOPS -> MATRIZ CONSTRUIDA ATRAVES DE DOIS LOOPS FOR
#linhas = int(input("quantas linhas?"))
#colunas = int(input("quantas colunas?"))
#a = input("digite um simbolo:")
#for i in range(linhas):
#    for j in range(colunas):
#        print(a, end="")
#    print()

#BREAK -> SAI DO LOOP | CONTINUE -> IGNORA UM DETERMINADO VALOR NO LOOP | PASS -> PULA UM DETERMINADO VALOR NO LOOP
#while True:
#    name = input("digite seu nome: ")
#    if name != "":
#        break

#num = "0-0-00-00-0"
#for i in num:
#    if i == "-":
#        continue
#    print(i, end="")

#for i in range(1, 21):
#    if i == 17:
#        pass
#    else:
#        print(i, end="")

#LISTS -> ORDENADAS E INDEXADAS. PARECE VETOR
#comida = ["miojo", "hamburguer", "batata"]
#print(comida[2])
#comida.append("sorvete")
#comida.remove(3)
#comida.append("opa")
#comida.pop()
#comida.insert(0, "panetone")
#comida.sort()
#for i in comida:
#    print(i)
#comida.clear()

#2D LISTS -> MATRIZ DE LISTAS
#drinks = ["guarana", "coke", "water"]
#food = ["pizza", "panqueca", "sanduiche"]
#dessert = ["panetone", "sorvete", "fruta"]
#dinner = [drinks, food, dessert]
#for i in range(3):
#    print(dinner[i][0])

#TUPLE -> LISTA COM PROPRIEDADES ORDENADAS E INDEXADAS
#name = ("bruno", 20, "male")
#print(name.count("bruno"))
#print(name.index("male"))
#for i in name:
#    print(i)
#if "bruno" in name:
#    print("o brabo chegou!")

#SET -> LISTAS DESORDENADAS E NAO INDEXADAS. NAO ACEITAM MULTIPLOS VALORES IGUAIS. FASTER
#objects = {"tesoura", "lapis", "mouse"}
#dishes = {"prato", "pote", "panela"}
#objects.add("borracha")
#objects.remove("borracha")
#objects.remove("lapis")
#objects.add("pote")
#all = objects.union(dishes)
#for i in all:
#    print(i)
#print(objects.difference(dishes))
#print(objects.intersection(dishes))
#objects.clear()

#DICTIONARY -> MOLDAVEL, DESORNDENATO DE CHAVES UNICAS | RAPIDO | KEY + VALUE
#capitals = {'USA': 'Washignton', 'India': "New Dehli", 'Russia': "Moscow"}
#print(capitals['Russia'])
#print(capitals.get('Russia'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#capitals.update({'Germany': 'Berlin'})
#for key, value in capitals.items():
#   print(key, value)
#capitals.pop('India')
#capitals.clear()

#INDEX OPERATOR -> [] | ELEMENTOS EM SEQUENCIA, ARRAY
#name = 'bjorn honor!'
#if name[0].islower():
#    name = name.capitalize()
#print(name)

#first_name = name[:5].upper()
#last_name = name[6:].lower()
#last_char = name[-1]
#print(first_name)
#print(last_name)
#print(last_char)

#FUNCTIONS -> BLOCOS DE CODIGOS QUE SAO CHAMADOS


#def hello(name, age):
#    print("opa "+name+' bao?')
#    print("voce tem "+str(age)+' anos')
#    print()


#hello("bjorn", 20)
#hello("bruno", 20)

#RETURN STATEMENT -> RETORNA VALORES PARA ONDE ESSA FUNCAO FOI CHAMADA


#def multiply(n1, n2):
#    result = n1*n2
#    return result


#resultado = multiply(123, 423)
#print(multiply(123, 423))

#KEYWORDS ARGUMENTS -> ARGUMENTOS QUE POSSUEM IDENTIFICADORES | ORDEM NAO IMPORTA



#def hello(first, last):
#    print("fala "+first+" "+last)


#hello(last='honor', first='bjorn')

#NESTED FUNCTION CALLS -> FUNCOES DENTRO DE OUTRAS FUNCOES
#print(round(abs(float(input("digite um numero")))))










