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
digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras = ['a']

def isKeyword(lexema):
    return lexema in keywords


def estadoInicial():
    return 0


def estadoFinal(estado):
    estadosFinais = [2, 4, 7, 11, 100]
    if estado not in estadosFinais:
        return False
    else:
        return True


# Verifica se eh uma letra do alfabeto
def ehAZ(caractere):
    if (ord('a') <= ord(caractere) <= ord('z')) or (ord('A') <= ord(caractere) <= ord('Z')):
        return True
    else:
        return False


# Verifica se eh um digito de 0 a 9
def ehNumero(caractere):
    if ord('0') <= ord(caractere) <= ord('9'):
        return True
    else:
        return False


# Verifica se eh um separador
def ehSeparador(caractere):
    if caractere == '\n' or caractere == ' ' or caractere == '\t' or caractere == '':
        return True
    else:
        return False
    
# Verifica se eh um digito especial p/ numeros (constNum)
def ehEspecialDigito(caractere):
    if caractere == '.':
        return 1
    elif caractere == 'E':
        return 2
    elif caractere == '+':
        return 3
    elif caractere == '-':
        return 4
    else:
        return 0


def move(estado, caractere):
    if caractere == '':
        return 100

    # Para ID's
    if estado == 0 and ehAZ(caractere):
        return 1
    elif estado == 1 and (ehAZ(caractere) or ehNumero(caractere)):
        return 1
    elif estado == 1 and ehSeparador(caractere):
        return 2 # Estado final
    elif estado == 2 and (not ehAZ(caractere) and not ehNumero(caractere)):
        return -1 # Quando for erro


    # Para digitos
    elif estado == 0 and ehNumero(caractere):
        return 3
    elif estado == 3 and not ehNumero(caractere) and not ehSeparador(caractere) and ehEspecialDigito(caractere) == 0:
        return -1 # Quando for erro
    elif estado == 3 and ehNumero(caractere):
        if estado == 3:
            return 3
    elif estado == 3 and ehEspecialDigito(caractere) == 0: # quando eh inteiro
        return 4
    elif estado == 3 and ehEspecialDigito(caractere) == 1: # 1 == '.'
        return 5
    # elif estado > 3 and not ehNumero(caractere) and not ehEspecialDigito(caractere):
    #     return 4 # Estado final
    elif estado == 3 and ehEspecialDigito(caractere) == 2: # 2 == 'E'
        return 8
    elif estado == 5 and ehNumero(caractere):
        return 6
    elif estado == 5 and not ehNumero(caractere) and ehEspecialDigito(caractere) != 0:
        return -1 # Quando for erro
    elif estado == 6:
        if ehNumero(caractere):
            return 6
        elif not ehNumero(caractere) and not ehEspecialDigito(caractere) == 2:
            return 7 # Estado final
        elif ehEspecialDigito(caractere) == 2:
            return 8
    elif estado == 8:
        if ehEspecialDigito(caractere) == 3 or ehEspecialDigito(caractere) == 4:
            return 9
        elif ehNumero(caractere):
            return 10
        else:
            return -1 # Quando for erro
    elif estado == 9 and ehNumero(caractere):
        return 10
    elif estado == 9 and not ehNumero(caractere):
        return -1 # Quando for erro
    elif estado == 10:
        if ehNumero(caractere):
            return 10
        elif not ehNumero(caractere):
            return 11 # Estado final
    