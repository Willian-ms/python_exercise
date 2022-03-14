ladoA = int(input('Digite o lado A: '))
ladoB = int(input('Digite o lado B: '))
ladoC = int(input('Digite o lado C: '))

ladoAB = ladoA + ladoB
ladoBC = ladoB + ladoC
ladoAC = ladoA + ladoC

if ladoAB == ladoBC == ladoAC:
    print('True')
else:
    print('False')
