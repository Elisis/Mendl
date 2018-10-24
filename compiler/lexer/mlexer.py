from rply import LexerGenerator

class Lexer():
	def __init__(self):
		self.lexer = LexerGenerator()
		
	def _add_tokens(self):
		
		#Print
		self.lexer.add('OUT', r'out')
		
		#If
		self.lexer.add('IF', r'if')
		
		#Parentheses
		self.lexer.add('OPEN_PAREN', r'\(')
		self.lexer.add('CLOSE_PAREN', r'\)')
		
		#Braces
		self.lexer.add('OPEN_BRACE', r'\{')
		self.lexer.add('CLOSE_BRACE', r'\}')
		
		#Semicolon
		self.lexer.add('SEMI_COLON', r'\;')
		
		#Operators
		self.lexer.add('SUM', r'\+')
		self.lexer.add('SUB', r'\-')
		self.lexer.add('MULTIPLY', r'\*')
		
		#Number
		self.lexer.add('NUMBER', r'\d+')
		
		#Ignore spaces
		self.lexer.ignore('\s+')
		
	def get_lexer(self):
		self._add_tokens()
		return self.lexer.build()
