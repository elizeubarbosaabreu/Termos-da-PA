termo = 0
print('\033[7m {:^50} \033[m'.format('TERMOS DA PA'))
primeiro = int(input('Entre com o primeiro termo da PA: '))
razao = int(input('Entre com a razão: '))
quantidade = int(input('Quantos termos você quer exibir: '))
ultimo = primeiro + quantidade * razao
termoatual = primeiro
print('-_' * 30)
print(f'Os {quantidade} termos de uma P.A de Razão {razao}, onde o primeiro termo é {primeiro}, são: ')
for num in range(primeiro, ultimo, razao):
	termo += 1
	print(f'{termoatual}', end=' -> ')
	termoatual += razao
print('Fim')
print('-_' * 30)
