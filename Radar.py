v = float(input('Digite a velocidade do veiculo: '))
if v > 80:
    print('Você foi multado em R$ {} por ultrapassar {} km acima de 80 km!'.format((v - 80)*7, v-80))
else:
    print('Parabéns por não ultrapassar a velecidade de 80 km'.format(v))