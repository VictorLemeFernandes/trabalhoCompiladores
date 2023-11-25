import state
import variaveisGlobais as funcoes

estadoAtual = funcoes.estadoInicial()

with open("code.txt", "r") as arquivo:
    caractere = arquivo.read(1) # Le 1 caractere do arquivo

    while funcoes.estadoFinal(estadoAtual) == False and estadoAtual != -1:

        if caractere == ' ' or caractere == '\n' or caractere == '\t':
            estadoAtual = funcoes.move(estadoAtual, caractere)
            if funcoes.estadoFinal(estadoAtual):
                estadoAtual = funcoes.estadoInicial() # Volta para o estado inicial quando le espaços, tabulações e quebras de linha
                caractere = arquivo.read(1)
            else:
                break
        estadoAtual = funcoes.move(estadoAtual, caractere)
        caractere = arquivo.read(1)
        if not caractere:
            estadoAtual = funcoes.move(estadoAtual, caractere)
            break
        

if funcoes.estadoFinal(estadoAtual):
    print('Cadeia aceita!')
else:
    print('Cadeia não aceita.')
