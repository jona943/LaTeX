import ply.lex as lex

# Lista de tokens
tokens = (
    'VAR', 'NUMBER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EQUALS',
    'IDENTIFIER', 'PRINT', 'IF', 'ELSE', 'FUNCTION', 'RETURN', 
    'BEGIN', 'END', 'ITEM', 'SECTION', 'SUBSECTION', 'TEXT', 
    'GRAPHICS', 'TABLE', 'ROW', 'COLUMN', 'CAPTION', 'LABEL',
    'REF', 'INCLUDE', 'MATH', 'EQUATION', 'BULLET', 'ENUM'
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

#Nuevos -  Inicio
t_BEGIN = r'\\begin'
t_END = r'\\end'
t_ITEM = r'\\item'
t_SECTION = r'\\section'
t_SUBSECTION = r'\\subsection'
t_TEXT = r'\\text'
t_GRAPHICS = r'\\includegraphics'
t_TABLE = r'\\begin\{tabular\}'
t_ROW = r'\\hline'
t_COLUMN = r'&'
t_CAPTION = r'\\caption'
t_LABEL = r'\\label'
t_REF = r'\\ref'
t_INCLUDE = r'\\include'
t_MATH = r'\$'
t_EQUATION = r'\\begin\{equation\}'
t_BULLET = r'\\begin\{itemize\}'
t_ENUM = r'\\begin\{enumerate\}'
# Fin ^

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


# t_VAR: Define una variable en LaTeX (`\var`).
# t_PLUS, t_MINUS, t_MULTIPLY, t_DIVIDE: Operadores aritméticos.
# t_EQUALS: Operador de asignación (`=`).
# t_PRINT: Comando para imprimir (`\print`).
# t_IF: Condicional (`\ifthenelse`).
# t_ELSE: Parte del condicional (`{`).
# t_FUNCTION: Definición de funciones (`\def`).
# t_RETURN: Retorno de funciones (`\return`).
# t_BEGIN, t_END: Inicio y fin de entornos en LaTeX (`\begin` y `\end`).
# t_ITEM: Ítem en una lista (`\item`).
# t_SECTION, t_SUBSECTION: Secciones y subsecciones (`\section` y `\subsection`).
# t_TEXT: Texto en LaTeX (`\text`).
# t_GRAPHICS: Inclusión de gráficos (`\includegraphics`).
# t_TABLE**: Tabla en LaTeX (`\begin{tabular}`).
# t_ROW**: Fila en una tabla (`\hline`).
# t_COLUMN**: Columna en una tabla (`&`).
# t_CAPTION**: Leyenda para tablas o gráficos (`\caption`).
# t_LABEL**: Etiquetas (`\label`).
# t_REF**: Referencias (`\ref`).
# t_INCLUDE**: Inclusión de archivos (`\include`).
# t_MATH**: Matemáticas en modo inline (`$`).
# t_EQUATION**: Ecuación (`\begin{equation}`).
# t_BULLET**: Lista con viñetas (`\begin{itemize}`).
# t_ENUM**: Lista enumerada (`\begin{enumerate}`).
