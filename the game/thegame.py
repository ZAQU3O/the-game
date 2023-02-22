from time import sleep
#Magic

#listas de números pré-posicionados.
lista1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
lista2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
lista3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
lista4 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
lista5 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

print(10*'#=', 'MAGIC', 10*'#=')
print()
sleep(2)
print('Olá, eu sou o Pudim! Vamos brincar!!!')
sleep(1)
nome = str(input('Qual o seu nome? '))
sleep(1)
print('Gostei do seu nome, ', nome)
print('Mas chega de enrolação e vamos ao que interessa!')
print('Agora a mágica vai rolar')
sleep(1)
print('Primeiro, {}, quero que você pense em um numero de 1 a 31.'.format(nome))
sleep(1)
print('ESPERANDO VOCÊ PENSAR...')
sleep(5)
print('Pensou?')
sleep(1)
print('Agora {}, me responda: '.format(nome))
print('CARREGANDO...')
sleep(3)
print("Observe essa lista: \n\n", lista1)
x = str(input("\nVocê consegue ver o numero que pensou? Se sim, digite 'S'. Se não, digite 'N'. \n"))

if x.upper() == "S":
    soma1 = 1
else:
    soma1 = 0

print("Agora olhe essa outra lista: \n\n", lista2)
y = str(input("\nEai? Consegue ver o numero que você pensou nessa lista? Se sim, digite 'S'. Se não, digite 'N'.\n"))

if y.upper() == "S":
    soma2 = 2
else:
    soma2 = 0

print("Olhe essa outra: \n\n", lista3)
z = str(input("\nE nessa? Conseguiu ver o numero que pensou? Se sim, digite 'S'. Se não, digite 'N'.\n"))

if z.upper() == "S":
    soma3 = 4
else:
    soma3 = 0

print("Calma que estamos chegando lá: \n\n", lista4)
t = str(input("\nVê seu numero nessa lista? Se sim, digite 'S'. Se não, digite 'N'.\n"))

if t.upper() == "S":
    soma4 = 8
else:
    soma4 = 0

print("A ultima para a magica acontecer: \n\n", lista5)
u = str(input("\nSeu numero está aqui? Se sim, digite 'S'. Se não, digite 'N'.\n"))

if u.upper() == "S":
    
    soma5 = 16
else:
    soma5 = 0

equacao = soma1 + soma2 + soma3 + soma4 + soma5

print()
print('Então {}, o número que você pensou foi: '.format(nome))
sleep(1)
print('CONTAGEM REGRESSIVA!')
print('TRÊS!')
sleep(1)
print('DOIS!')
sleep(1)
print('UM!')
sleep(1)
print('CARREGANDO...')
sleep(1)
print(20*'#=')
print("O NÚMERO QUE VOCÊ PENSOU FOI O: {}.".format(equacao))
print(20*'#=')