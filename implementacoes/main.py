import variaveisGlobais as funcoes

estadoAtual = funcoes.estadoInicial()

with open("code.txt", "r") as arquivo:
    caractere = arquivo.read(1) # Le 1 caractere do arquivo
    while funcoes.estadoFinal(estadoAtual) == False and estadoAtual != -1:
        estadoAtual = funcoes.move(estadoAtual, caractere)
        caractere = arquivo.read(1)
        if not caractere:
            break

if funcoes.estadoFinal(estadoAtual):
    print('Cadeia aceita!')
else:
    print('Cadeia não aceita.')
