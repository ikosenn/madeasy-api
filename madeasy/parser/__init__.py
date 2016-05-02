# Instatiate the parser model every time the app is called
import os

from textx.metamodel import metamodel_from_file


PARSER_APP = os.path.dirname(os.path.abspath(__file__))
parser_file = os.path.join(PARSER_APP, 'parser.tx')

parser_mm = metamodel_from_file(parser_file, debug=False, ignore_case=True)
