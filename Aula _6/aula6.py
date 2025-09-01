'''
Aula 6 - 25/08/2025
'''

# mostra olá mundo
def showOlaMundo():
    print ("Olá mundo!")

showOlaMundo()


# mostra varios textos
def showMultipleTexts():
    # a = {"texto 1","Texto 2", "Texto 3", "Texto 4"}
    b = "Texto 1\nTexto 2\nTexto 3\nTexto 4"
    # print(a)
    print(b)

showMultipleTexts()

# função saudação personalizada
def showPersonalidada(nome):
    print(f"Olá, {nome}")

# função para solicitar nome
inputNome = input("Digite seu nome\n")
showPersonalidada(inputNome)
# função motico para aprender
def motivoParaAprender():
    a = ("Crescimento","Conhercimento","liberdade","Autocritica")
    print(a)
motivoParaAprender()

from datetime import datetime 
# função boas vindas com hora
def showBoasVindasHora(nome):
    agora = datetime.now()
    agoraFomat = agora.strftime("%H:%M:%S")
    print(f"Seja bem-vindo {nome}. Hora atual é {agoraFomat}")

inputNomeBemVindo = input("Digite seu nome\n")
showBoasVindasHora(inputNomeBemVindo)