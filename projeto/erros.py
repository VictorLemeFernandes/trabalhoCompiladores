import state
import variaveisGlobais as funcoes

def verificaCadeia():
    estadoAtual = funcoes.estadoInicial()

    contLinha = 1
    contColuna = 1

    with open("code.txt", "r") as arquivo:
        caractere = arquivo.read(1) # Le 1 caractere do arquivo
        contColuna += 1

        while estadoAtual != -1:
            if (caractere == ' ' and estadoAtual != 23) or caractere == '\n' or caractere == '\t':
                if caractere == '\n':
                    contLinha += 1
                    contColuna = 1
                estadoAtual = funcoes.move(estadoAtual, caractere)
                if funcoes.estadoFinal(estadoAtual):
                    estadoAtual = funcoes.estadoInicial() # Volta para o estado inicial quando le espaços, tabulações e quebras de linha
                    caractere = arquivo.read(1)
                elif estadoAtual != 0:
                    break
            estadoAtual = funcoes.move(estadoAtual, caractere)
            caractere = arquivo.read(1)
            contColuna += 1
            if not caractere:
                estadoAtual = funcoes.move(estadoAtual, caractere)
                break
            

    if funcoes.estadoFinal(estadoAtual):
        return 'Cadeia aceita!', ''
    else:
        return 'Cadeia não aceita.', 'Relatorio de erro: \nErro na linha: ' + str(contLinha) + ' e coluna: ' + str(contColuna)