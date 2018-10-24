from lexer.mlexer import Lexer

text_input = """
out(4 + 4 - 2);
"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
	print token
