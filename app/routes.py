from flask import render_template
from pathlib import Path
from app import app

@app.route('/')
@app.route('/index')
def index():
    return get_cmd("index")


@app.route('/<path:cmd>')
def get_cmd(cmd):
    filename = cmd + ".txt"
    path_file = Path.cwd().joinpath("app","cmds",filename)
    if path_file.exists():
        return render_template(filename)
    else :
        return "File not accessible"
