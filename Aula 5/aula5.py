'''
Aula 5 - 18/08/2025
'''

# fator = 1.0
# contador = 0
# juros = 0.08

# while fator < 1.5:
#     fator = fator * (juros * fator)
#     contador += 1

# print(f"levará {contador} anos")


while True:
    opt = input("1-Ver, 2-Editar, 3-Sair\n")

    if opt == '1':
        print("Ver")
    elif opt == "2":
        print("Editar")
    elif opt == "3":
        break
    else:
        continue

