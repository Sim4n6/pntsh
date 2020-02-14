
from pygments import highlight
from pygments.lexers import BashLexer, guess_lexer
from pygments.formatters import TerminalFormatter

def colorize(text):
    return highlight(text, guess_lexer(text), TerminalFormatter())