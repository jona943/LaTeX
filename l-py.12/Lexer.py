import ply.lex as lex

# Lista de tokens
tokens = (
    'VAR', 'NUMBER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EQUALS',
    'IDENTIFIER', 'PRINT', 'IF', 'ELSE', 'FUNCTION', 'RETURN'
)

# Definición de tokens con expresiones regulares
t_VAR = r'\\var'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_PRINT = r'\\print'
t_IF = r'\\ifthenelse'
t_ELSE = r'\{'
t_FUNCTION = r'\\def'
t_RETURN = r'\\return'

# Regla para ignorar caracteres como espacios y tabulaciones
t_ignore = ' \t'

# Regla para identificar identificadores (variables y funciones)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Regla para identificar números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejo de errores
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Creación del analizador léxico
lexer = lex.lex()
