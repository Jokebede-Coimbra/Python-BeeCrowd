
print('====================')
print('======CARDÁPIO======')
print('1 HAMBURGUER R$ 4.00')
print('2 HOT DOG    R$ 3.00')
print('3 COXINHA    R$ 5.00')
print('====================')

entrada = 0

while entrada not in [1,2,3]:
    entrada = int(input('Entre com a opção do cardápio: '))
qtd = int(input('Entre com a quantidade: '))

if entrada == 1:
    h = qtd * 4
    print(f'Total do hamburguer: R$ {h:.2f}')
elif entrada == 2:
    hd = qtd * 3
    print(f'Total do hot dog: R$ {hd:.2f}')
elif entrada == 3:
    cx = qtd * 5
    print(f'Total da coxinha: R$ {cx:.2f}')

print('Volte sempre!')

