from rply import ParserGenerator
from ast import Number, Sum, Sub, Out, Multiply

class Parser():
	def __init__(self, module, builder, outf):
		self.pg = ParserGenerator(
		#A list of token names accepted by the parser.
		['NUMBER', 'OUT', 'IF', 'OPEN_BRACE', 'CLOSE_BRACE', 'OPEN_PAREN', 'CLOSE_PAREN',
		'SEMI_COLON', 'SUM', 'SUB', 'MULTIPLY'],
		
		precedence = [
			('left', ['SUM', 'SUB']),
			('left', ['MULTIPLY'])
		]
	
		)
		self.module = module
		self.builder = builder
		self.outf = outf
		
	def parse(self):
		@self.pg.production('program : OUT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
		def program(p):
			return Out(self.builder, self.module, self.outf, p[2])
		
		@self.pg.production('expression : expression MULTIPLY expression')	
		@self.pg.production('expression : expression SUM expression')
		@self.pg.production('expression : expression SUB expression')
		def expression(p):
			left = p[0]
			right = p[2]
			operator = p[1]
			
			if operator.gettokentype() == 'SUM':
				return Sum(self.builder, self.module, left, right)
			
			elif operator.gettokentype() == 'SUB':
				return Sub(self.builder, self.module, left, right)
				
			elif operator.gettokentype() == 'MULTIPLY':
				return Multiply(self.builder, self.module, left, right)
		
		@self.pg.production('expression : NUMBER')
		def number(p):
			return Number(self.builder, self.module, p[0].value)
			
		@self.pg.error
		def error_handle(token):
			raise ValueError(token)
			
	def get_parser(self):
		return self.pg.build() 
			
