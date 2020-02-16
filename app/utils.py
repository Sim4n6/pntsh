
from pygments import highlight
from pygments.lexers import BashLexer, guess_lexer
from pygments.formatters import TerminalFormatter

from pygments.lexer import RegexLexer
from pygments.token import *

class PntLexer(RegexLexer):
    name = 'Pnt'
    aliases = ['Pnt']

    tokens = {
        'root': [
            (r'^#.*', Comment.Singleline),
            (r'^\w+ ', Name.Builtin),
            (r'-\w ', Operator),
            (r'--\w ', Operator),
        ]
    }

def colorize(text):
    return highlight(text, PntLexer(), TerminalFormatter())