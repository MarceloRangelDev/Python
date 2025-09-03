"""
    ************* ATIVIDADE 3 *************
        
                - Marcelo Santos Rangel de Abreu
                - marcelo.rangel.abreu@gmail.com
                - 09 de Setembro de 2025

"""
print("\n ############### EXECÍCIO 1 ############### \n")
'''
Início da Questão 1 - Detector de Números Primos
- Crie uma função que recebe dois números inteiros, início e fim, e retorna uma lista de todos os números primos nesse intervalo, incluindo os limites.
'''
def getNumerosPrimos(inicio, fim):
    primos = []
    for num in range(inicio, fim + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primos.append(num)
    return primos
inputo_inicio = int(input("Digite o início do intervalo (Ex: 10): "))
inputo_fim = int(input("Digite o fim do intervalo (Ex: 50): "))
numeros_primos = getNumerosPrimos(inputo_inicio, inputo_fim)
print(f"Números primos encontrados: {numeros_primos}")
print(f"Total de números primos encontrados: {len(numeros_primos)}")
# Fim da Questão 1 - Detector de Números Primos

print("\n ############### EXECÍCIO 2 ############### \n")
'''
Início da Questão 2 - Verificador de Números Pares e Ímpares
- Crie uma função que recebe dois números inteiros, início e fim, e retorna uma lista de todos os números pares e ímpares nesse intervalo, incluindo os limites.
'''

# Programa para verificar se um número é par ou ímpar
while True:
    numero = int(input("Digite um número inteiro para verificar paridade: "))
    if numero % 2 == 0:
        print(f"{numero} é PAR.")
    else:
        print(f"{numero} é ÍMPAR.")

    # Aplicação 1: Colorir linhas alternadas de uma tabela
    print("\nTabela com linhas alternadas coloridas (simulação):")
    linhas = 10
    for i in range(1, linhas + 1):
        if i % 2 == 0:
            print(f"Linha {i}: [COR 1]")
        else:
            print(f"Linha {i}: [COR 2]")

    # Aplicação 2: Validador simplificado de cartão de crédito usando paridade
    cartao = input("\nDigite um número de cartão de crédito (apenas dígitos): ")
    soma_pares = 0
    soma_impares = 0
    for idx, digito in enumerate(cartao):
        if digito.isdigit():
            if int(digito) % 2 == 0:
                soma_pares += int(digito)
            else:
                soma_impares += int(digito)
    print(f"Soma dos dígitos pares: {soma_pares}")
    print(f"Soma dos dígitos ímpares: {soma_impares}")
    if soma_pares > soma_impares:
        print("Cartão válido (soma dos pares maior que ímpares).")
    else:
        print("Cartão inválido (soma dos pares não é maior que ímpares).")

    sair = input("\nDeseja repetir o programa? (s/n): ")
    if sair.lower() != 's':
        break

def getNumerosParesImpares(inicio, fim):
    pares = []
    impares = []
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares
inputo_inicio = int(input("Digite o início do intervalo (Ex: 10): "))
inputo_fim = int(input("Digite o fim do intervalo (Ex: 50): "))
numeros_pares, numeros_impares = getNumerosParesImpares(inputo_inicio, inputo_fim)
print(f"Números pares encontrados: {numeros_pares}")
print(f"Números ímpares encontrados: {numeros_impares}")
print(f"Total de números pares encontrados: {len(numeros_pares)}")
print(f"Total de números ímpares encontrados: {len(numeros_impares)}")
# Fim da Questão 2 - Verificador de Números Pares e Ímpares

print("\n ############### EXECÍCIO 3 ############### \n")
'''
Início da Questão 3 - Calculadora de Média de Notas
- Crie uma função que recebe uma lista de notas e retorna a média aritmética.
'''
def calcular_media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

while True:
    try:
        qtd_notas = int(input("Quantas notas deseja inserir? "))
        if qtd_notas <= 0:
            print("Digite um número maior que zero.")
            continue
    except ValueError:
        print("Digite um número inteiro válido.")
        continue

    notas = []
    for i in range(qtd_notas):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1} (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota fora do intervalo. Digite entre 0 e 10.")
            except ValueError:
                print("Nota inválida. Digite um número.")

    media = calcular_media(notas)
    print(f"A média das notas é: {media:.2f}")

    if media >= 7.0:
        print("Situação: Aprovado")
    elif media >= 5.0:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")

    repetir = input("Deseja calcular outra média? (s/n): ")
    if repetir.lower() != 's':
        break

notas = []
while True:
    nota = input("Digite uma nota (ou 'sair' para finalizar): ")
    if nota.lower() == 'sair':
        break
    try:
        notas.append(float(nota))
    except ValueError:
        print("Nota inválida. Digite um número.")

media = calcular_media(notas)
print(f"A média das notas é: {media}")
# Fim da Questão 3 - Calculadora de Média de Notas

print("\n ############### EXECÍCIO 4 ############### \n")
'''
Início da Questão 4 - Gerador de Tabuada
- Crie uma função que recebe um número e gera sua tabuada.
'''
def gerar_tabuada(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

while True:
    try:
        numero = int(input("Digite um número para ver sua tabuada (ou 0 para sair): "))
        if numero == 0:
            break
        print(f"\nTabuada do {numero}:")
        gerar_tabuada(numero)
        print()
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

def gerar_tabuada(numero):
    return [numero * i for i in range(1, 11)]

while True:
    try:
        numero = int(input("Digite um número para ver sua tabuada (ou 0 para sair): "))
        if numero == 0:
            break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        continue

    tabuada = gerar_tabuada(numero)
    print(f"Tabuada do {numero}:")
    for i, valor in enumerate(tabuada, start=1):
        print(f"{numero} x {i} = {valor}")
# Fim da Questão 4 - Gerador de Tabuada

print("\n ############### EXECÍCIO 5 ############### \n")
'''
Início da Questão 5 - Calculadora de Soma Sequencial
- Crie uma função que recebe uma lista de números e retorna a soma dos elementos.
'''

# Versão com loop for
def soma_sequencial_for(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

# Versão com loop while
def soma_sequencial_while(n):
    soma = 0
    i = 1
    while i <= n:
        soma += i
        i += 1
    return soma

# Versão usando fórmula matemática
def soma_sequencial_formula(n):
    return n * (n + 1) // 2

while True:
    try:
        n = int(input("Digite um número inteiro N para calcular a soma de 1 até N (ou 0 para sair): "))
        if n == 0:
            break
        print(f"Soma usando for: {soma_sequencial_for(n)}")
        print(f"Soma usando while: {soma_sequencial_while(n)}")
        print(f"Soma usando fórmula matemática: {soma_sequencial_formula(n)}")
        print("A fórmula matemática utilizada é: soma = n * (n + 1) / 2")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Fim da Questão 5 - Calculadora de Soma Sequencial

print("\n ############### EXECÍCIO 6 ############### \n")
'''
Início da Questão 6 - Gerenciador de Times de Futebol Brasileiro
- Crie um programa que trabalhe com uma lista de times brasileiros de futebol.
'''
# Gerenciador de Times de Futebol Brasileiro

times = [
    "Flamengo", "Palmeiras", "Corinthians", "São Paulo", "Vasco",
    "Grêmio", "Internacional", "Cruzeiro", "Atlético Mineiro", "Botafogo",
    "Santos", "Fluminense", "Bahia", "Athletico Paranaense", "Fortaleza"
]

def exibir_times(lista):
    print("\nLista de times:")
    for idx, time in enumerate(lista, start=1):
        print(f"{idx}. {time}")

def filtrar_por_letra(letra):
    filtrados = [time for time in times if time.lower().startswith(letra.lower())]
    return filtrados

def adicionar_time(novo_time):
    if novo_time and novo_time not in times:
        times.append(novo_time)
        print(f"Time '{novo_time}' adicionado com sucesso.")
    else:
        print("Time já existe ou nome inválido.")

def remover_time(remover_time):
    if remover_time in times:
        times.remove(remover_time)
        print(f"Time '{remover_time}' removido com sucesso.")
    else:
        print("Time não encontrado.")

def buscar_time(nome):
    encontrados = [time for time in times if nome.lower() in time.lower()]
    return encontrados

def mostrar_fatia(inicio, fim):
    fatia = times[inicio:fim]
    exibir_times(fatia)

while True:
    print("\n--- Menu Gerenciador de Times ---")
    print("1. Exibir todos os times")
    print("2. Filtrar times por letra inicial")
    print("3. Adicionar novo time")
    print("4. Remover time")
    print("5. Buscar time por nome")
    print("6. Exibir fatia da lista de times")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_times(times)
    elif opcao == "2":
        letra = input("Digite a letra inicial: ")
        filtrados = filtrar_por_letra(letra)
        if filtrados:
            exibir_times(filtrados)
        else:
            print("Nenhum time encontrado com essa letra.")
    elif opcao == "3":
        novo_time = input("Digite o nome do novo time: ").strip()
        adicionar_time(novo_time)
    elif opcao == "4":
        remover_time_nome = input("Digite o nome do time a remover: ").strip()
        remover_time(remover_time_nome)
    elif opcao == "5":
        busca = input("Digite parte do nome do time para buscar: ").strip()
        encontrados = buscar_time(busca)
        if encontrados:
            exibir_times(encontrados)
        else:
            print("Nenhum time encontrado.")
    elif opcao == "6":
        try:
            inicio = int(input("Índice inicial (começa em 0): "))
            fim = int(input("Índice final (não incluso): "))
            mostrar_fatia(inicio, fim)
        except ValueError:
            print("Índices inválidos.")
    elif opcao == "0":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
# Fim da Questão 6 - Gerenciador de Times de Futebol Brasileiro

print("\n ############### EXECÍCIO 7 ############### \n")
'''
Início da Questão 7 - Sistema de Audiência de Novelas Brasileiras
- Crie um programa que trabalhe com uma lista de novelas brasileiras.
'''

# Sistema de Audiência de Novelas Brasileiras

novelas = {
    "Avenida Brasil": 45,
    "O Clone": 38,
    "Senhora do Destino": 41,
    "Terra Nostra": 36,
    "Vale Tudo": 43
}

def exibir_novelas(novelas):
    print("\nNovelas e audiências:")
    for nome, audiencia in novelas.items():
        print(f"- {nome}: {audiencia} pontos")

def adicionar_novela(novelas):
    nome = input("Digite o nome da novela: ").strip()
    if nome in novelas:
        print("Novela já cadastrada.")
        return
    try:
        audiencia = float(input("Digite a audiência (em pontos): "))
        novelas[nome] = audiencia
        print("Novela adicionada com sucesso.")
    except ValueError:
        print("Audiência inválida.")

def consultar_audiencia(novelas):
    nome = input("Digite o nome da novela para consultar: ").strip()
    if nome in novelas:
        print(f"Audiência de '{nome}': {novelas[nome]} pontos")
    else:
        print("Novela não encontrada.")

def filtrar_sucessos(novelas):
    print("\nNovelas de sucesso (audiência > 40 pontos):")
    sucesso = False
    for nome, audiencia in novelas.items():
        if audiencia > 40:
            print(f"- {nome}: {audiencia} pontos")
            sucesso = True
    if not sucesso:
        print("Nenhuma novela de sucesso encontrada.")

def estatisticas(novelas):
    if not novelas:
        print("Nenhuma novela cadastrada.")
        return
    total = 0
    max_audiencia = None
    min_audiencia = None
    max_novela = ""
    min_novela = ""
    for nome, audiencia in novelas.items():
        total += audiencia
        if max_audiencia is None or audiencia > max_audiencia:
            max_audiencia = audiencia
            max_novela = nome
        if min_audiencia is None or audiencia < min_audiencia:
            min_audiencia = audiencia
            min_novela = nome
    media = total / len(novelas)
    print(f"\nEstatísticas:")
    print(f"- Média de audiência: {media:.2f} pontos")
    print(f"- Maior audiência: {max_novela} ({max_audiencia} pontos)")
    print(f"- Menor audiência: {min_novela} ({min_audiencia} pontos)")

def ranking(novelas):
    print("\nRanking das novelas (maior para menor audiência):")
    ordenadas = sorted(novelas.items(), key=lambda x: x[1], reverse=True)
    for idx, (nome, audiencia) in enumerate(ordenadas, start=1):
        print(f"{idx}. {nome}: {audiencia} pontos")

while True:
    print("\n--- Sistema de Audiência de Novelas ---")
    print("1. Exibir todas as novelas e audiências")
    print("2. Adicionar nova novela")
    print("3. Consultar audiência de uma novela")
    print("4. Filtrar novelas de sucesso (> 40 pontos)")
    print("5. Estatísticas (média, máximo, mínimo)")
    print("6. Ranking das novelas")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_novelas(novelas)
    elif opcao == "2":
        adicionar_novela(novelas)
    elif opcao == "3":
        consultar_audiencia(novelas)
    elif opcao == "4":
        filtrar_sucessos(novelas)
    elif opcao == "5":
        estatisticas(novelas)
    elif opcao == "6":
        ranking(novelas)
    elif opcao == "0":
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
# Fim da Questão 7 - Sistema de Audiência de Novelas Brasileiras

print("\n ############### EXECÍCIO 8 ############### \n")
'''
Início da Questão 8 - Catálogo de Comidas Brasileiras por Região
- Implemente um sistema que gerencie informações sobre comidas típicas
brasileiras usando tuplas
'''
# Catálogo de Comidas Brasileiras por Região

comidas = [
    ("Feijoada", "Sudeste", 35.0),
    ("Acarajé", "Nordeste", 18.0),
    ("Churrasco", "Sul", 40.0),
    ("Tacacá", "Norte", 22.0),
    ("Pamonha", "Centro-Oeste", 12.0),
    ("Moqueca", "Sudeste", 38.0),
    ("Baião de Dois", "Nordeste", 25.0),
    ("Arroz Carreteiro", "Sul", 28.0),
    ("Cuscuz", "Nordeste", 15.0),
    ("Peixada", "Norte", 30.0)
]

def exibir_comidas(lista):
    print("\nComidas cadastradas:")
    for nome, regiao, preco in lista:
        print(f"- {nome} | Região: {regiao} | Preço: R$ {preco:.2f}")

def filtrar_por_regiao(regiao):
    filtradas = []
    for comida in comidas:
        if comida[1].lower() == regiao.lower():
            filtradas.append(comida)
    return filtradas

def preco_medio():
    total = 0
    for comida in comidas:
        total += comida[2]
    return total / len(comidas) if comidas else 0

def estatisticas():
    if not comidas:
        print("Nenhuma comida cadastrada.")
        return
    maior = comidas[0]
    menor = comidas[0]
    total = 0
    for comida in comidas:
        total += comida[2]
        if comida[2] > maior[2]:
            maior = comida
        if comida[2] < menor[2]:
            menor = comida
    media = total / len(comidas)
    print(f"\nEstatísticas:")
    print(f"- Preço médio: R$ {media:.2f}")
    print(f"- Mais cara: {maior[0]} (R$ {maior[2]:.2f})")
    print(f"- Mais barata: {menor[0]} (R$ {menor[2]:.2f})")

while True:
    print("\n--- Menu Catálogo de Comidas ---")
    print("1. Exibir todas as comidas")
    print("2. Consultar comidas por região")
    print("3. Calcular preço médio das comidas")
    print("4. Estatísticas de preços")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_comidas(comidas)
    elif opcao == "2":
        regiao = input("Digite a região para consultar: ")
        filtradas = filtrar_por_regiao(regiao)
        if filtradas:
            exibir_comidas(filtradas)
        else:
            print("Nenhuma comida encontrada para essa região.")
    elif opcao == "3":
        media = preco_medio()
        print(f"Preço médio das comidas: R$ {media:.2f}")
    elif opcao == "4":
        estatisticas()
    elif opcao == "0":
        print("Saindo do sistema de comidas.")
        break
    else:
        print("Opção inválida. Tente novamente.")
# Fim da Questão 8 - Catálogo de Comidas Brasileiras por Região

print("\n ############### EXECÍCIO 9 ############### \n")
'''
Início da Questão 9 - Calculadora Interativa com Loop While
- Desenvolva uma calculadora interativa que permaneça em execução até que o
usuário escolha sair
'''
def calculadora():
    while True:
        print("\n--- Calculadora Interativa ---")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo da calculadora.")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            resultado = num1 + num2
            print(f"Resultado da adição: {resultado}")
        elif opcao == "2":
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado}")
        elif opcao == "3":
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {resultado}")
        elif opcao == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da divisão: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Tente novamente.")

calculadora()
# Fim da Questão 9 - Calculadora Interativa com Loop While

print("\n ############### EXECÍCIO 10 ############### \n")
'''
Início da Questão 10 - Sistema de Loja Virtual Brasileira
- Desenvolva um sistema completo de loja virtual que permita gerenciar produtos
brasileiros.
'''
produtos_loja = []
vendas = []

def adicionar_produto():
    print("\n--- Adicionar Produto ---")
    nome = input("Nome do produto: ").strip()
    categoria = input("Categoria: ").strip()
    origem = input("Origem: ").strip()
    while True:
        try:
            preco = float(input("Preço (R$): "))
            if preco < 0:
                print("Preço não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Digite um valor válido para o preço.")
    while True:
        try:
            estoque = int(input("Quantidade em estoque: "))
            if estoque < 0:
                print("Estoque não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Digite um valor inteiro para o estoque.")
    produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "estoque": estoque,
        "origem": origem
    }
    produtos_loja.append(produto)
    print("Produto adicionado com sucesso.")

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if not produtos_loja:
        print("Nenhum produto cadastrado.")
        return
    for idx, produto in enumerate(produtos_loja, start=1):
        print(f"{idx}. {produto['nome']} | Categoria: {produto['categoria']} | Preço: R$ {produto['preco']:.2f} | Estoque: {produto['estoque']} | Origem: {produto['origem']}")

def listar_por_categoria():
    categoria = input("Digite a categoria para filtrar: ").strip()
    encontrados = [p for p in produtos_loja if p['categoria'].lower() == categoria.lower()]
    if encontrados:
        print(f"\nProdutos na categoria '{categoria}':")
        for produto in encontrados:
            print(f"- {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Estoque: {produto['estoque']} | Origem: {produto['origem']}")
    else:
        print("Nenhum produto encontrado nessa categoria.")

def buscar_produto():
    termo = input("Digite o nome ou parte do nome do produto: ").strip().lower()
    encontrados = [p for p in produtos_loja if termo in p['nome'].lower()]
    if encontrados:
        print("\nProdutos encontrados:")
        for produto in encontrados:
            print(f"- {produto['nome']} | Categoria: {produto['categoria']} | Preço: R$ {produto['preco']:.2f} | Estoque: {produto['estoque']} | Origem: {produto['origem']}")
    else:
        print("Nenhum produto encontrado.")

def gerenciar_estoque():
    nome = input("Digite o nome do produto para atualizar estoque: ").strip().lower()
    for produto in produtos_loja:
        if produto['nome'].lower() == nome:
            print(f"Estoque atual de '{produto['nome']}': {produto['estoque']}")
            while True:
                try:
                    novo_estoque = int(input("Novo valor de estoque: "))
                    if novo_estoque < 0:
                        print("Estoque não pode ser negativo.")
                        continue
                    produto['estoque'] = novo_estoque
                    print("Estoque atualizado com sucesso.")
                    break
                except ValueError:
                    print("Digite um valor inteiro para o estoque.")
            return
    print("Produto não encontrado.")

def realizar_venda():
    print("\n--- Realizar Venda ---")
    if not produtos_loja:
        print("Nenhum produto disponível para venda.")
        return
    listar_produtos()
    nome = input("Digite o nome do produto para comprar: ").strip().lower()
    for produto in produtos_loja:
        if produto['nome'].lower() == nome:
            print(f"Produto encontrado: {produto['nome']} | Estoque: {produto['estoque']}")
            if produto['estoque'] == 0:
                print("Produto esgotado.")
                return
            while True:
                try:
                    quantidade = int(input("Quantidade para comprar: "))
                    if quantidade <= 0:
                        print("Quantidade deve ser maior que zero.")
                        continue
                    if quantidade > produto['estoque']:
                        print("Quantidade maior que o estoque disponível.")
                        continue
                    break
                except ValueError:
                    print("Digite um valor inteiro para a quantidade.")
            produto['estoque'] -= quantidade
            valor_total = produto['preco'] * quantidade
            vendas.append({
                "nome": produto['nome'],
                "quantidade": quantidade,
                "valor_total": valor_total
            })
            print(f"Venda realizada! Total: R$ {valor_total:.2f}")
            return
    print("Produto não encontrado.")

def calcular_total_vendas():
    total = 0
    for venda in vendas:
        total += venda['valor_total']
    print(f"\nValor total das vendas realizadas: R$ {total:.2f}")

def relatorio_vendas():
    print("\n--- Relatório de Vendas ---")
    if not vendas:
        print("Nenhuma venda realizada.")
        return
    for idx, venda in enumerate(vendas, start=1):
        print(f"{idx}. Produto: {venda['nome']} | Quantidade: {venda['quantidade']} | Total: R$ {venda['valor_total']:.2f}")
    calcular_total_vendas()

while True:
    print("\n--- Menu Loja Virtual Brasileira ---")
    print("1. Adicionar produto")
    print("2. Listar todos os produtos")
    print("3. Listar produtos por categoria")
    print("4. Buscar produto por nome")
    print("5. Gerenciar estoque")
    print("6. Realizar venda")
    print("7. Calcular valor total das vendas")
    print("8. Relatório de vendas")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        listar_por_categoria()
    elif opcao == "4":
        buscar_produto()
    elif opcao == "5":
        gerenciar_estoque()
    elif opcao == "6":
        realizar_venda()
    elif opcao == "7":
        calcular_total_vendas()
    elif opcao == "8":
        relatorio_vendas()
    elif opcao == "0":
        print("Saindo do sistema de loja virtual.")
        break
    else:
        print("Opção inválida. Tente novamente.")
# Fim da Questão 10 - Sistema de Loja Virtual Brasileira