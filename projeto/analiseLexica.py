class Token:
    def __init__(self, nome, atributo):
        self.nome = nome
        self.atributo = atributo

    def __str__(self):
        return f"({self.nome}, {self.atributo})"
    
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
            ('{', ''),
            ('}', ''),
            (':=', '')
        ]

    vetorTokens = []
    posicaoTabSimbolos = 1
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    tabelaSimbolos = TabelaSimbolos()

    def inserirToken(self, elementoLinha, chave):
        if elementoLinha[0] in self.numeros:
            self.vetorTokens.append(Token('constNum', chave))
        elif elementoLinha[0] == "'" and elementoLinha[-1] == "'":
            self.vetorTokens.append(Token('constChar', chave))
        else:
            self.vetorTokens.append(Token('id', chave))
        
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
                        
                        tabelaSimbolosLista = list(self.tabelaSimbolos.tabelaSimbolos.values())
                        flag2 = False
                        for i in range(len(tabelaSimbolosLista)):
                            if elementoLinha in tabelaSimbolosLista[i][0]:
                                flag2 = True
                        if flag2 == False:
                            if elementoLinha[0] in self.numeros:
                                self.tabelaSimbolos.inserir(self.posicaoTabSimbolos, (elementoLinha, 'constNum'))
                                self.inserirToken(elementoLinha, self.posicaoTabSimbolos)
                            elif elementoLinha[0] == "'":
                                self.tabelaSimbolos.inserir(self.posicaoTabSimbolos, (elementoLinha, 'constChar'))
                                self.inserirToken(elementoLinha, self.posicaoTabSimbolos)
                            else:
                                self.tabelaSimbolos.inserir(self.posicaoTabSimbolos, (elementoLinha, 'id'))
                                self.inserirToken(elementoLinha, self.posicaoTabSimbolos)
                            self.posicaoTabSimbolos += 1
                        else:
                            chave = self.tabelaSimbolos.buscar_por_valor(elementoLinha)
                            self.inserirToken(elementoLinha, chave)


# Exemplo de uso
lexer = AnalisadorLexico()
lexer.armazenaTokens()
lexer.tabelaSimbolos.imprimir_tabela()
print('\nTokens:')
for token in lexer.vetorTokens:
    print(token)