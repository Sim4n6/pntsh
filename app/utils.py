
from pygments import highlight
from pygments.lexers import BashLexer, guess_lexer
from pygments.formatters import TerminalFormatter, TerminalTrueColorFormatter

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *
from pygments.style import Style


class MyStyle(Style):
    #default_style = ""
    styles = {
        Comment:                '#808080', # gray
        Generic:                '#00ff00', # green
    }

class PntLexer(RegexLexer):
    name = 'Pnt'
    aliases = ['Pnt']

    tokens = {
        'root': [
            (r'^# .*', Comment), # captures ---> # nmap xxxxxxx 
            #(r'^\w+ ', Name.Builtin),
            #(r'-\w ', Operator),
            #(r'--\w ', Operator),
            (r'^[^#].*\n$', Generic), # captures ---> nmap -xxxxxx
        ]
    }


def colorize(text):
    return highlight(text, PntLexer(), TerminalTrueColorFormatter(style=MyStyle))


def is_from_cmdline(name_browser):
    print(name_browser)
    if name_browser in ["firefox", "chrome", "edge", "konqueror", "mozilla", "microsoft", "opera", "netscape", "safari"]: # TODO to improve
        return False
    else:
        return True