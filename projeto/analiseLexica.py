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

    def armazenaTokens(self):
        vetorTokens = []
        with open("code.txt", "r") as arquivo:
            for linha in arquivo:
                stringLinha = linha.split(' ')
                for elementoLinha in stringLinha:
                    for index, (padrao, _) in enumerate(self.padroes):
                        if padrao == elementoLinha:
                            # print(f"Elemento: {padrao}, Índice: {index}")
                            vetorTokens.append(Token(elementoLinha, self.padroes[index][1]))
        return vetorTokens

# Exemplo de uso
lexer = AnalisadorLexico()
tokens = lexer.armazenaTokens()

for token in tokens:
    print(token)