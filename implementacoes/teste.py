import state

tabelaTransicao = state.defineTabelaTransicao()

estadoAtual = state.estadoInicial()

estadoAtual = state.move('+', estadoAtual, tabelaTransicao)

print(estadoAtual.nome)

