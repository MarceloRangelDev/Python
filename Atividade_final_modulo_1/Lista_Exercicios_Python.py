"""
    ************* Lista de Exercícios Python - Módulo 1 *************
        
                - Marcelo Santos Rangel de Abreu
                - marcelo.rangel.abreu@gmail.com
                - 09 de Setembro de 2025

"""

'''
1. Verificar Elementos em uma Lista
    Verifica se o valor 2 está presente na lista e imprime uma mensagem indicando o resultado.
'''
print("\n ############### EXECÍCIO 1 ############### \n")
lista = [1, 3, 4, 5, 6]
if 2 not in lista:
    print(f"O valor 2 não está presente na lista {lista}.\n")

'''
2. Converter Lista para Dicionário
    Converte uma lista de inteiros em um dicionário, onde as chaves são os elementos da lista e os valores são o dobro das chaves.
'''
print(" ############### EXECÍCIO 2 ############### \n")
dicionario = {chave: chave * 2 for chave in lista}
print(f"{dicionario}\n")


'''
3. Ajustar um Endereço IP
    Função que ajusta um endereço IP para o formato especificado, substituindo '.' por '[.]'.
    - Implementação com for e if.
    - Implementação utilizando o método replace().
    - Explicação do funcionamento do método replace().
'''
print(" ############### EXECÍCIO 3 ############### \n")
# a) Descreva textualmente o passo a passo da sua solução.
str_ip_title = " ************* Passo a Passo da Solução Ajustar um Endereço IP *************"
str_ip_a = "Passo 1: Dividir o endereço IP em partes usando o ponto como separador."
str_ip_b = "Passo 2: Substituir cada parte do endereço IP pelo formato desejado."
str_ip_c = "Passo 3: Juntar as partes novamente em uma única string."
str_ip_d = "Passo 4: Retornar o endereço IP ajustado."
print(f"{str_ip_title}\n{str_ip_a}\n{str_ip_b}\n{str_ip_c}\n{str_ip_d}\n")

# b) Desenvolva a função usando if e for .
def ajustar_ip(ip):
    partes = ip.split(".")
    for i in range(len(partes)):
        if i < len(partes) - 1:
            partes[i] += "[.]"
    return "".join(partes)

print(f"{ajustar_ip("1.1.1.1")}\n")

# c) Pesquise e explique o funcionamento da função built-in replace() e como ela poderia ser aplicada nesta solução.
str_replace_title = " ************* Funcionamento da Função replace() *************"
str_replace_a = "A função replace() é um método de string que substitui ocorrências de uma substring por outra."
str_replace_b = "Ela recebe dois argumentos principais: a substring a ser substituída e a substring que irá substituí-la."
print(f"{str_replace_title}\n{str_replace_a}\n{str_replace_b}\n")

# d) Demonstre a solução usando o replace() .

def ajustar_ip(ip):
    return ip.replace(".", "[.]")

print(f"{ajustar_ip("1.1.1.1")}\n")


'''
4. Contar Números com Dígito Par
    Função que conta quantos números em uma lista possuem um número par de dígitos.
    - Explicação do funcionamento da função len().
'''
print(" ############### EXECÍCIO 4 ############### \n")
numeros = [12, 342, 345, 2, 8, 7896]
# a) Descreva textualmente o passo a passo da sua solução.
str_passo_numero_par_title = " ************* Passo a Passo da Solução Contar Números com Dígito Par *************"
str_passo_numero_par_a = "Passo 1: Inicializar um contador em zero."
str_passo_numero_par_b = "Passo 2: Iterar sobre cada número na lista."
str_passo_numero_par_c = "Passo 3: Para cada número, verificar se a quantidade de dígitos é par."
str_passo_numero_par_d = "Passo 4: Se for par, incrementar o contador."
str_passo_numero_par_e = "Passo 5: Retornar o contador ao final.\n"
print(f"{str_passo_numero_par_title}\n{str_passo_numero_par_a}\n{str_passo_numero_par_b}\n{str_passo_numero_par_c}\n{str_passo_numero_par_d}\n{str_passo_numero_par_e}")

# b) Crie a função que conta quantos números têm um número par de dígitos.
def contar_numeros_par(numeros):
    # Criando o dicionário de contagem
    frequencias = {}
    for elemento in numeros:
        if elemento % 2 == 0:
            frequencias[elemento] = len(str(elemento))
    # Retornando a soma dos elementos que aparecem uma única vez
    return frequencias
print(f"Quantidade de números com dígitos pares: {contar_numeros_par(numeros)}\n") 

# c) Explique o funcionamento da função built-in len() .
str_len_title = " ************* Funcionamento da Função len() *************"
str_len_a = "A função len() é uma função embutida em Python que retorna o número de itens em um objeto."
str_len_b = "No caso de strings, ela retorna o número de caracteres na string."
str_len_c = "No contexto desta solução, usamos len() para contar o número de dígitos em cada número, \nconvertendo o número em uma string e verificando o comprimento dessa string."
print(f"{str_len_title}\n{str_len_a}\n{str_len_b}\n{str_len_c}\n")

'''
5. Somar Elementos Únicos de um Array
    Função que retorna a soma dos elementos únicos de um array.
    - Criação de um dicionário para contar a quantidade de cada elemento.
    - Explicação do passo a passo da solução.
'''
print(" ############### EXECÍCIO 5 ############### \n")
# a) Descreva textualmente o passo a passo da sua solução.
str_somar_elementos_title = " ************* Passo a Passo da Solução Somar Elementos Únicos de um Array *************"
str_somar_elementos_a = "Passo 1: Criar um conjunto a partir do array para obter elementos únicos."
str_somar_elementos_b = "Passo 2: Iterar sobre os elementos únicos e somá-los."
str_somar_elementos_c = "Passo 3: Retornar a soma total."
print(f"{str_somar_elementos_title}\n{str_somar_elementos_a}\n{str_somar_elementos_b}\n{str_somar_elementos_c}\n")

meu_array = [1, 2, 3, 2, 1, 4, 10]
# b) Crie um dicionário que armazene as chaves e valores com a quantidade de cada elemento do array.
def contar_elementos(array):
    contagem = {}
    for elemento in array:
        contagem[elemento] = contagem.get(elemento, 0) + 1
    return contagem
print(f"{contar_elementos(meu_array)}")  # Saída: {1: 2, 2: 2, 3: 1, 4: 1, 10: 1}

# c) Crie a função que retorna a soma dos elementos únicos.
def soma_elementos_unicos(arr: list[int]) -> int:
    soma = 0
    for elemento in arr:
        if arr.count(elemento) == 1:
            soma += elemento
    return soma

print(f"A soma dos elementos é: {soma_elementos_unicos(meu_array)}\n")  # Saída: 17

'''
6. Retornar o Elemento Que Aparece Uma Vez
    Função que retorna o único elemento que aparece uma vez em um array.
    - Explicação do passo a passo da solução.
'''
print(" ############### EXECÍCIO 6 ############### \n")
# a) Descreva textualmente o passo a passo da sua solução.
str_passo_title = " ************* Passo a Passo da Solução Retornar o Elemento Que Aparece Uma Vez *************"
str_passo_a = "Passo 1: Criar um dicionário para contar a ocorrência de cada elemento."
str_passo_b = "Passo 2: Iterar sobre o array e atualizar a contagem no dicionário."
str_passo_c = "Passo 3: Encontrar e retornar o elemento que aparece uma vez."
print(f"{str_passo_title}\n{str_passo_a}\n{str_passo_b}\n{str_passo_c}")

# b) Crie a função que retorna o único elemento que aparece uma vez.
array = [1, 2, 2, 1, 3, 3, 4, 5, 5, 6, 6]
def encontrar_unico(array):
    contagem = {}
    for elemento in array:
        contagem[elemento] = contagem.get(elemento, 0) + 1
    for elemento, qtd in contagem.items():
        if qtd == 1:
            return elemento
    return None
print(f"Esse é o único elemento que não se repete: {encontrar_unico(array)}\n")  # Saída: 4

'''
7. Funções de Análise de um Array de Números Inteiros
    Funções para:
        a) Retornar o menor número.
        b) Retornar o maior número.
        c) Retornar a soma do menor com o maior número usando sort().
        d) Retornar a soma de todos os números.
        e) Retornar a média dos valores do array.
'''
print(" ############### EXECÍCIO 7 ############### \n")
lista = [1, 5, 33, 8, 77, 43, 124, 6, 8, 99]
# a) Crie uma função que retorne o menor número.
def encontrar_menor(lista):
    return min(lista)
print(f"O menor número é: {encontrar_menor(lista)}")

# b) Crie uma função que retorne o maior número.
def encontrar_maior(lista):
    return max(lista)
print(f"O maior número é: {encontrar_maior(lista)}")

# c) Crie uma função que retorne a soma do menor número com o maior número, utilizando sort() .
def somar_extremos(lista):
    lista.sort()
    return lista[0] + lista[-1]
print(f"A soma do menor com o maior número é: {somar_extremos(lista)}")

# d) Crie uma função que retorne a soma de todos os números.
def somar_todos(lista):
    return sum(lista)
print(f"A soma de todos os números é: {somar_todos(lista)}")

# e) Crie uma função que retorne a média dos valores do array.
def calcular_media(lista):
    if not lista:
        return 0
    return somar_todos(lista) / len(lista)
print(f"A média dos valores é: {calcular_media(lista)}\n")

'''
8. Manipulação de uma Lista
    Operações em uma lista vazia:
        a) Adicionar valores.
        b) Remover valores.
        f) Explicação dos métodos append(), pop(), insert(), sort(), count(), sum().
'''
print(" ############### EXECÍCIO 8 ############### \n")
lista = []
# a) Adicione o valor de 10 nela.
lista.append(10)
print(f"Lista após adicionar 10: {lista}")

# b) Adicione o valor 20 .
lista.append(20)
print(f"Lista após adicionar 20: {lista}")

# c) Adicione o valor 30 .
lista.append(30)
print(f"Lista após adicionar 30: {lista}")

# d) Remova o valor 20 .
lista.remove(20)
print(f"Lista após remover 20: {lista}")

# e) Remova o valor 10 .
lista.remove(10)
print(f"Lista após remover 10: {lista}\n")

# f) Explique o funcionamento do método append() .
str_append_title = " ************* Explicação do Método append() ************* "
str_append_a = "O método append() adiciona um elemento ao final da lista. Ele modifica a lista original e \nnão retorna um novo objeto.\n"
print(f"{str_append_title}\n{str_append_a}")

# g) Explique o funcionamento do método pop() .
str_pop_title = " ************* Explicação do Método pop() ************* "
str_pop = "O método pop() remove e retorna o último elemento da lista. Se um índice for fornecido, ele \nremove e retorna o elemento nesse índice.\n"
print(f"{str_pop_title}\n{str_pop}")

# h) Explique o funcionamento do método insert() .
str_insert_title = " ************* Explicação do Método insert() ************* "
str_insert = "O método insert() adiciona um elemento em uma posição específica da lista. Ele recebe dois \nargumentos: o índice onde o elemento deve ser inserido e o elemento a ser inserido.\n"
print(f"{str_insert_title}\n{str_insert}")

# i) Explique o funcionamento do método sort() .
str_sort_title = " ************* Explicação do Método sort() ************* "
str_sort = "O método sort() ordena os elementos da lista em ordem crescente. Ele modifica a lista original \ne não retorna um novo objeto.v"
print(f"{str_sort_title}\n{str_sort}")

# j) Explique o funcionamento do método count() .
str_count_title = " ************* Explicação do Método count() ************* "
str_count = "O método count() retorna o número de vezes que um elemento específico aparece na lista.\n"
print(f"{str_count_title}\n{str_count}")

# k) Explique o funcionamento do método sum() em uma lista de inteiros.
str_sum_title = " ************* Explicação do Método sum() ************* "
str_sum = "O método sum() retorna a soma de todos os elementos da lista.\n"
print(f"{str_sum_title}\n{str_sum}")

'''
9. Manipulação de um Dicionário
    Operações em um dicionário vazio:
        a) Adicionar e remover entradas.
        g) Explicação dos métodos update(), pop(), get(), keys(), values(), items().
'''
print(" ############### EXECÍCIO 9 ############### \n")
dicionario = {}
# a) Adicione uma entrada com a chave a e o valor 410 .
dicionario['a'] = 410
print(f"Dicionário após adicionar a: {dicionario}")

# b) Adicione uma entrada com a chave b e o valor 3 .
dicionario['b'] = 3
print(f"Dicionário após adicionar b: {dicionario}")

# c) Adicione uma entrada com a chave b e o valor 4 .
dicionario['b'] = 4
print(f"Dicionário após adicionar b: {dicionario}")

# d) Adicione uma entrada com a chave c e o valor 56 .
dicionario['c'] = 56
print(f"Dicionário após adicionar c: {dicionario}")

# e) Remova a entrada com a chave b que possui o valor 3 .
dicionario.pop('b', None)
print(f"Dicionário após remover b: {dicionario}")

# f) Remova a entrada com a chave b que possui o valor 4 .
dicionario.pop('b', None)
print(f"Dicionário após remover b: {dicionario}\n")

# g) Explique o funcionamento do método update() .
str_update_title = " ************* Explicação do Método update() ************* "
str_update_a = "O método update() é utilizado para atualizar um dicionário com os pares chave-valor de \noutro dicionário ou de um iterável de pares. Se a chave já existir, seu valor é atualizado; \ncaso contrário, a nova chave-valor é adicionada.\n"
print(f"{str_update_title}\n{str_update_a}")

# h) Explique o funcionamento do método pop() .
str_pop_title = " ************* Explicação do Método pop() ************* "
str_pop_a = "O método pop() é utilizado para remover uma entrada de um dicionário com base em sua chave. \nEle retorna o valor associado à chave removida, ou um valor padrão se a chave não existir.\n"
print(f"{str_pop_title}\n{str_pop_a}")

# i) Explique o funcionamento do método get() .
str_get_title = " ************* Explicação do Método get() ************* "
str_get_a = "O método get() é utilizado para acessar o valor associado a uma chave em um dicionário. \nSe a chave não existir, ele retorna um valor padrão, que é None se não for especificado.\n"
print(f"{str_get_title}\n{str_get_a}")

# j) Explique o funcionamento do método keys() .
str_keys_title = " ************* Explicação do Método keys() ************* "
str_keys_a = "O método keys() é utilizado para obter uma visão (view) das chaves do dicionário.\n"
print(f"{str_keys_title}\n{str_keys_a}")

# k) Explique o funcionamento do método values() .
str_values_title = " ************* Explicação do Método values() ************* "
str_values_a = "O método values() é utilizado para obter uma visão (view) dos valores do dicionário.\n"
print(f"{str_values_title}\n{str_values_a}")

# l) Explique o funcionamento do método items() .
str_items_title = " ************* Explicação do Método items() ************* "
str_items_a = "O método items() é utilizado para obter uma visão (view) dos pares chave-valor do dicionário.\n"
print(f"{str_items_title}\n{str_items_a}")

'''
10. Verificação de Sequência em uma String
    Função que retorna True se cada 'a' aparece antes de cada 'b' na string, caso contrário retorna False.
'''
print(" ############### EXECÍCIO 10 ############### \n")
def verificar_sequencia(s):
    encontrou_b = False
    for char in s:
        if char == 'b':
            encontrou_b = True
        elif char == 'a' and encontrou_b:
            return False
    return True

# Testando a função
print(f"O retorno de ab é: {verificar_sequencia("ab")}")  # True
print(f"O retorno de abababab é: {verificar_sequencia("abababab")}")  # False
print(f"O retorno de babababa é: {verificar_sequencia("babababa")}")  # False
print(f"O retorno de aaaaabbbbbba é: {verificar_sequencia("aaaaabbbbbba")}")  # False

'''
11. Encontrar o Único Número que Faltou em um Array
    - Função que retorna o único número faltante no intervalo [0, n] de um array.
'''
print(" ############### EXECÍCIO 11 ############### \n")
def encontrar_faltando(array):
    n = len(array)
    soma_total = n * (n + 1) // 2
    soma_atual = sum(array)
    return soma_total - soma_atual

# Testando a função
print(f"O retorno de [0, 2, 3, 4, 5, 6, 7, 8] é: {encontrar_faltando([0, 2, 3, 4, 5, 6, 7, 8])}")  # 1

'''
12. Encontrar o Elemento com Mais Frequência em um Array
    - Função que encontra o elemento que aparece com mais frequência em uma lista.
'''
print(" ############### EXECÍCIO 12 ############### \n")
def encontrar_mais_frequente(array):
    contagem = {}
    for num in array:
        contagem[num] = contagem.get(num, 0) + 1
    return max(contagem, key=contagem.get)

# Testando a função
print(f"O retorno de [1, 2, 3, 3, 3, 4, 5] é: {encontrar_mais_frequente([1, 2, 3, 3, 3, 4, 5])}\n")  # 3

'''
13. Converter Uma Lista em Dicionário
    - Função que converte uma lista em um dicionário e retorna o valor do elemento cuja chave é igual ao seu valor.
'''
print(" ############### EXECÍCIO 13 ############### \n")
# a) Explique o passo a passo da solução com suas palavras.
str_converter_title = " ************* Passo a Passo da Solução Converter Uma Lista em Dicionário ************* "
str_converter_a = "A função irá percorrer cada elemento da lista e adicioná-lo a um dicionário, \nonde a chave e o valor serão o próprio elemento. No final, a função irá retornar \no valor do elemento cuja chave é igual ao seu valor.\n"
print(f"{str_converter_title}\n{str_converter_a}")

# b) Desenvolva a solução que converte a lista em um dicionário e retorne o valor do elemento cuja chave é igual ao seu valor.

def converter_lista_para_dicionario(lista):
    dicionario = {}
    for item in lista:
        dicionario[item] = item
    return dicionario

# Testando a função
meu_array_2 = [1, 2, 2, 3, 3, 4, 4, 4, 5, 7, 1]
dicionario_resultante = converter_lista_para_dicionario(meu_array_2)
print(f"Convertendo a lista em um dicionário chave => valor: {dicionario_resultante}")