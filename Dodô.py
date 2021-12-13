entrada = int(input("Digite a quantidade da população de Dodô! "))
mortalidade, natalidade, ano = 0.06, 0.01, 1600

aux = entrada * 0.10

while entrada >= aux:
    entrada = entrada - (entrada * mortalidade)
    entrada = entrada + (entrada * natalidade)
    auxM = entrada - (entrada * mortalidade)
    auxM = entrada - auxM
    auxN = entrada + (entrada * natalidade)
    print("População: {:.0f}, Mortalidade: {:.0f}, Natalidade: {:.0f}, Ano: {}".format(entrada, auxM, auxN, ano))
    ano = ano + 1
