from datetime import datetime


'''
************* Atividade 2 - Lógica de Programação *************
        
        Marcelo Santos Rangel de Abreu
        marcelo.rangel.abreu@gmail.com
        25/08/2025
        
'''
# Calculadora de idade
def calcular_idade_auto(ano_nascimento):
    # Obtém o ano atual automaticamente usando a biblioteca datetime
    newDatetime = datetime.now()
    # Obtém o ano atual
    newYear = newDatetime.strftime("%Y")
    idade = int(newYear) - ano_nascimento
    return idade
# Solicita ao usuário o ano de nascimento e o ano atual
ano_nascimento2 = int(input("Digite o ano de nascimento: "))
# Calcula a idade
idade2 = calcular_idade_auto(ano_nascimento2)
# Exibe a idade calculada
print(f"Sua idade é: {idade2} anos\n")

# Área do retângulo
def calcular_area_retangulo(largura, altura):
    # Calcula a área do retângulo multiplicando largura por altura
    area = largura * altura
    return area
# Solicita ao usuário a largura e a altura do retângulo
largura = float(input("Digite a largura do retângulo: "))
# Solicita ao usuário a altura do retângulo
altura = float(input("Digite a altura do retângulo: "))
# Calcula a área do retângulo
area = calcular_area_retangulo(largura, altura)
# Exibe a área calculada
print(f"A área do retângulo é: {area}\n")

# Média Aritmética
def calcular_media(nota1, nota2, nota3):
    # Calcula a média aritmética somando as notas e dividindo por 3
    media = (nota1 + nota2 + nota3) / 3
    return media
# Solicita ao usuário as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
# Calcula a média das notas
media = calcular_media(nota1, nota2, nota3)
# Exibe a média calculada
print(f"A média é: {media:.2f}\n")

# Conversão de temperatura
def converter_celsius_para_fahrenheit(celsius):
    # Converte a temperatura de Celsius para Fahrenheit usando a fórmula
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
# Solicita ao usuário a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: "))
# Converte a temperatura para Fahrenheit
fahrenheit = converter_celsius_para_fahrenheit(celsius)
# Exibe a temperatura convertida
print(f"{celsius}°C equivale em Fahrenheit a: {fahrenheit}°F\n")

# Calculadora de desconto
def calcular_preco_com_desconto(preco, desconto):
    # Calcula o preço com desconto subtraindo o valor do desconto do preço original
    preco_com_desconto = preco - (preco * desconto / 100)
    return preco_com_desconto
# Solicita ao usuário o preço do produto e o percentual de desconto
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))
# Calcula o preço com desconto
preco_com_desconto = calcular_preco_com_desconto(preco, desconto)
print(f"O preço original é: R$ {preco}")
print(f"O desconto {desconto}%: R$ {preco-preco_com_desconto} ")
# Exibe o preço com desconto
print(f"O preço final é: R$ {preco_com_desconto}\n")

# Calculadora de troco
def calcular_troco(valor_pago, valor_compra):
    # Calcula o troco subtraindo o valor da compra do valor pago
    troco = valor_pago - valor_compra
    if troco < 0:
        print (f"Falta: R$ {abs(troco):.2f}\n")
    elif troco == 0:
        print ("R$ 0.00\n")
    else:
        print (f"Troco: R$ {troco:.2f}\n")
# Solicita ao usuário o valor pago e o valor da compra
valor_compra = float(input("Digite o valor da compra: R$ "))
valor_pago = float(input("Digite o valor pago: R$ "))
# Calcula o troco
calcular_troco(valor_pago, valor_compra)

#conversão de moedas
def converter_real_para_dolar(valor_real, cotacao_dolar):
    # Converte o valor de Real para Dólar dividindo pelo valor da cotação
    valor_dolar = valor_real / cotacao_dolar
    return valor_dolar
# Solicita ao usuário o valor em Real e a cotação do Dólar
valor_real = float(input("Digite o valor em Real (R$): "))
cotacao_dolar = float(input("Digite a cotação do Dólar (R$): "))
# Converte o valor para Dólar
valor_dolar = converter_real_para_dolar(valor_real, cotacao_dolar)
# Exibe o valor convertido
print(f"O valor em Dólar é: ${valor_dolar:.2f}\n")

# simulador de investimento com valor inicial, juros mensal, aporte mensal, meses do investimento - detalhado (1o período)
def calcular_primeiro_periodo(valor_inicial, taxa_juros, aporte_mensal):
    # Calcula o rendimento do primeiro período
    rend = (valor_inicial * taxa_juros) / 100
    # Calcula o total após o primeiro período
    semi_total = valor_inicial + rend
    # Adiciona o aporte mensal
    total = semi_total + aporte_mensal

    # Exibe os detalhes do cálculo
    print(f"Valor inicial: R$ {valor_inicial:.2f}") 
    print(f"Rendimento por período: {taxa_juros:.2f}%")
    print(f"Aporte por período: R$ {aporte_mensal:.2f}")
    print(f"Total de períodos: {meses}")
    print(f"Total após o 1o período: R$ {total:.2f}")

# Solicita ao usuário o valor inicial, a taxa de juros, o aporte mensal e o número de meses
valor_inicial = float(input("Digite o valor inicial (em R$): "))
taxa_juros = float(input("Digite o rendimento por período (em %): "))
aporte_mensal = float(input("Digite o aporte a cada período (em R$): "))
meses = int(input("Digite o total de períodos (número inteiro): "))

calcular_primeiro_periodo(valor_inicial, taxa_juros, aporte_mensal) # 1o período

