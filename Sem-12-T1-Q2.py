carro = int(input(""))
poupanca = 10000
mes = 0
while True:
        carro = carro +(carro *(0.4/ 100))
        poupanca = poupanca +(poupanca *(0.7/ 100))
        mes = mes + 1
        if poupanca > carro:
            print(mes)
            break
