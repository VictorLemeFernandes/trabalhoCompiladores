tabelaSimbolos = [
    # [tipoToken, lexema, valor, tipoDado] -> 2 ultimos serao preenchidos somente quando necessario
    ['relOp', '<', 'LT', None],
    ['relOp', '>', 'GT', None],
    ['relOp', '<=', 'LE', None],
    ['relOp', '>=', 'GE', None],
    ['relOp', '=', 'E', None],
    ['relOp', '!=', 'DIFF', None],
    ['+', '+', None, None],
    ['-', '-', None, None],
    ['*', '*', None, None],
    ['/', '/', None, None],
    [':=', ':=', None, None],
    [';', ';', None, None],
    ['.', '.', None, None],
    ['(', '(', None, None],
    [')', ')', None, None],
    ['{', '{', None, None],
    ['}', '}', None, None],
]


# keywords
keywords = ['int', 'char', 'float', 'if', 'then', 'else', 'while', 'until', 'repeat', 'program', 'begin', 'end']
listaTokens = []
arrayDigitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def consultaTabela(lexema):
    if lexema in keywords:
        listaTokens.append([lexema, None])
        return 
    
    for i in range(len(tabelaSimbolos)):
        if lexema == tabelaSimbolos[i][1]:
            if lexema[0] == "'":
                listaTokens.append(['constChar', i])
            elif lexema[0] in arrayDigitos:
                listaTokens.append(['constNum', i])
            else:
                listaTokens.append(['id', i])
        else:
            if lexema[0] == "'":
                tabelaSimbolos.append(['constChar', lexema, lexema, 'char'])
            elif lexema[0] in arrayDigitos:
                if '.' in lexema:
                    tabelaSimbolos.append(['constNum', lexema, lexema, 'float'])
                else:
                    tabelaSimbolos.append(['constNum', lexema, lexema, 'int'])
            else:
                tabelaSimbolos.append(['id', lexema, lexema, 'variable'])
                

def isKeyword(lexema):
    return lexema in keywords
