class Token:
    def __init__(self, nome, atributo, tipo, linha, coluna):
        self.nome = nome
        self.atributo = atributo
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna

    def __str__(self):
        return f"(Nome: {self.nome}, Atributo: {self.atributo}, Tipo: {self.tipo}, linha/coluna: ({self.linha}, {self.coluna}))"
    
class TabelaSimbolos:
    def __init__(self):
        self.tabelaSimbolos = {}

    def inserir(self, chave, valor):
        self.tabelaSimbolos[chave] = valor

    def buscar_por_chave(self, chave):
        return self.tabelaSimbolos.get(chave, None)

    def buscar_por_valor(self, valor):
        for chave, v in self.tabelaSimbolos.items():
            if v[0] == valor:
                return chave
        return None

    def remover(self, chave):
        if chave in self.tabelaSimbolos:
            del self.tabelaSimbolos[chave]
            return True
        else:
            return False
    
    def imprimir_tabela(self):
        print("Tabela de Símbolos:")
        for chave, valor in self.tabelaSimbolos.items():
            print(f"({chave}, {valor})")

class AnalisadorLexico:
    def __init__(self):
        # Define padroes para os tokens
        self.padroes = [
            ('int', ''),
            ('char', ''),
            ('float', ''),
            ('if', ''),
            ('then', ''),
            ('else', ''),
            ('while', ''),
            ('until', ''),
            ('repeat', ''),
            ('<', 'LT'),
            ('>', 'GT'),
            ('<=', 'LE'),
            ('>=', 'GE'),
            ('=', 'EQ'),
            ('!=', 'DIFF'),
            ('+', 'SUM'),
            ('-', 'SUB'),
            ('*', 'MULT'),
            ('/', 'DIV'),
            ('^', 'POW'),
            ('(', ''),
            (')', ''),
            (':=', '')
        ]

    # Variaveis globais da classe
    vetorTokens = []
    posicaoTabSimbolos = 1
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    tabelaSimbolos = TabelaSimbolos()
    contLinha = 0
    contColuna = 1

    def inserirToken(self, elementoLinha, chave, linha, coluna):
        if elementoLinha[0] in self.numeros:
            if '.' in elementoLinha[0]:
                self.vetorTokens.append(Token('constNum', chave, 'float', linha, coluna))
            else:
                self.vetorTokens.append(Token('constNum', chave, 'int', linha, coluna))
        elif elementoLinha[0] == "'" and elementoLinha[-1] == "'":
            self.vetorTokens.append(Token('constChar', chave, 'char', linha, coluna))
        else:
            self.vetorTokens.append(Token('id', chave, 'id', linha, coluna))

    def calculaColuna(self, elementoLinha, elemento):
        linha = elementoLinha
        substring = elemento

        indices = []
        index = linha.find(substring)

        while index != -1:
            indices.append(index)
            index = linha.find(substring, index + 1)

        return indices
        
    def armazenaTokens(self):
        with open("code.txt", "r") as arquivo:
            for linha in arquivo:
                self.contLinha += 1
                self.contColuna = 1
                # Verificamos se existe um comentario nesta linha.
                # Lembrando que o comentario deve ter uma linha so para ele.
                if linha[0] == '{' and linha[-2] == '}':
                    continue

                stringLinha = linha.split(' ')
                for elementoLinha in stringLinha:
                    if elementoLinha in linha:
                        index = linha.index(elementoLinha)
                    self.contColuna = index + 1
                    # Verifica se o token esta nos padroes de tokens.
                    flag = False
                    for tupla in self.padroes:
                        if elementoLinha == tupla[0]:
                            flag = True
                            break
                    if flag:
                        self.vetorTokens.append(Token(elementoLinha, tupla[1], '', self.contLinha, self.contColuna))
                    else:
                        if '\n' in elementoLinha:
                            elementoLinha = elementoLinha.replace('\n', '')
                        
                        tabelaSimbolosLista = list(self.tabelaSimbolos.tabelaSimbolos.values())
                        # Verifica se o elemento ja esta na tabela de simbolos.
                        flag2 = False
                        for i in range(len(tabelaSimbolosLista)):
                            if elementoLinha in tabelaSimbolosLista[i][0]:
                                flag2 = True
                        if flag2 == False:
                            # Verifica se constNum, constaChar ou id.
                            if elementoLinha[0] in self.numeros:
                                self.tabelaSimbolos.inserir(self.posicaoTabSimbolos, (elementoLinha, 'constNum'))
                                self.inserirToken(elementoLinha, self.posicaoTabSimbolos, self.contLinha, self.contColuna)

                            elif elementoLinha[0] == "'":
                                self.tabelaSimbolos.inserir(self.posicaoTabSimbolos, (elementoLinha, 'constChar'))
                                self.inserirToken(elementoLinha, self.posicaoTabSimbolos, self.contLinha, self.contColuna)
                            else:
                                self.tabelaSimbolos.inserir(self.posicaoTabSimbolos, (elementoLinha, 'id'))
                                self.inserirToken(elementoLinha, self.posicaoTabSimbolos, self.contLinha, self.contColuna)
                            self.posicaoTabSimbolos += 1
                        else:
                            # Se ja existir na tabela de simbolos, busca para repetir no vetorTokens
                            chave = self.tabelaSimbolos.buscar_por_valor(elementoLinha)
                            self.inserirToken(elementoLinha, chave)