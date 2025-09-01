'''
Aula 4 - 13/08/2025
'''

# DESCOBRINDO SE O ANO DIGITADO É BISEXTO

# função para verificar se o ano é bissexto
def anoBisexto():
    anoDigitado = int(input("Digite o ano...\n"))
    condicao400 = anoDigitado % 400 == 0
    condicao100 = anoDigitado % 100 == 0
    condicao4 = anoDigitado % 4 == 0

    if condicao400 or condicao100 or condicao4:
        print(f"\nO ano {anoDigitado} é bisexto\n")
    else:
        print(f"\nO ano não é bisexto\n")

anoBisexto()

def verficaSaldo(valorSaldo):
    if valorSaldo >= 2:
        produto = float(input("\nDigite o valor do produto: \n"))
        verficaProduto(produto, valorSaldo)
    else:
        print ("\nSaldo insuficiente.\nO saldo deverá ser maior ou igual a 2\n")
        saldo = float(input("\nDigite o saldo: \n"))
        verficaSaldo(saldo)
    
def verficaProduto(valorProduto, valorSaldo):
    
    if valorProduto < 5:
        print("\nVerifique o valor do produto. Deverá ser maior que ou igual a 5\n")
        produto = float(input("\nDigite o valor do produto: \n"))
        verficaProduto(produto,valorSaldo)
    elif valorProduto > valorSaldo:
        print ("\nVocê não tem saldo suficiente para está compra.\nO saldo deverá ser maior ou igual a 2\n")
        saldo = float(input("Digite o saldo: \n"))
        verficaSaldo(saldo)
    elif valorProduto >= 5 and valorSaldo >= valorProduto:
        print("\nAproxime o cartão")
    
def verficaCartao(temCard):
    if temCard == "S":
        saldo = float(input("\nDigite o saldo: \n"))
        verficaSaldo(saldo)
    else:
        print("\nSó aceitamos cartão de débito\n")
    

cartao = input("Tem cartão? Digite S ou N: \n")
verficaCartao(cartao)