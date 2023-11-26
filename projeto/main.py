import erros
import analiseLexica as lex

status, errosRetorno = erros.verificaCadeia()

if status == 'Cadeia aceita!':
    print(status)
        
    lexer = lex.AnalisadorLexico()
    lexer.armazenaTokens()
    lexer.tabelaSimbolos.imprimir_tabela()

    # Imprime os tokens
    print('\nTokens:')
    for token in lexer.vetorTokens:
        print(token)
else:
    print(status)
    print(errosRetorno)