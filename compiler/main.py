from lexer.mlexer import Lexer
from parser.mparser import Parser
from codegen.mcodegen import CodeGen

fname = "input.mend"
with open(fname) as f:
	text_input = f.read()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
outf = codegen.outf

pg = Parser(module, builder, outf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir("output.mlx")
