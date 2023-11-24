class Token:
    def __init__(self, nome, atributo):
        self.nome = nome
        self.atributo = atributo

    def __str__(self):
        return f"({self.nome}, {self.atributo})"

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
            ('{', ''),
            ('}', ''),
            (':=', '')
        ]

    vetorTokens = []
    tabelaSimbolos = {}
    posicaoTabSimbolos = 1
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def addTabelaSimbolos(self, elementoLinha):
        if elementoLinha[0] in self.numeros:
            self.tabelaSimbolos[self.posicaoTabSimbolos] = (elementoLinha, 'constNum')
            self.vetorTokens.append(Token('constNum', self.posicaoTabSimbolos))
        else:
            self.tabelaSimbolos[self.posicaoTabSimbolos] = (elementoLinha, 'id')
            self.vetorTokens.append(Token('id', self.posicaoTabSimbolos))

        self.posicaoTabSimbolos += 1

    def exibeTabelaSimbolos(self):
        print(f"Tabela de símbolos: {self.tabelaSimbolos}")
        
    def armazenaTokens(self):
        with open("code.txt", "r") as arquivo:
            for linha in arquivo:
                stringLinha = linha.split(' ')
                for elementoLinha in stringLinha:
                    flag = False
                    for tupla in self.padroes:
                        if elementoLinha == tupla[0]:
                            flag = True
                            break
                    if flag:
                        self.vetorTokens.append(Token(elementoLinha, tupla[1]))
                    else:
                        if '\n' in elementoLinha:
                            elementoLinha = elementoLinha.replace('\n', '')
                        tabelaSimbolosLista = list(self.tabelaSimbolos.values())
                        flag2 = False
                        for i in range(len(tabelaSimbolosLista)):
                            if elementoLinha in tabelaSimbolosLista[i][0]:
                                flag2 = True
                        if flag2 == False:
                            self.addTabelaSimbolos(elementoLinha)

# Exemplo de uso
lexer = AnalisadorLexico()
lexer.armazenaTokens()
lexer.exibeTabelaSimbolos()
print('Tokens:')
for token in lexer.vetorTokens:
    print(token)