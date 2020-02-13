from flask import render_template
from pathlib import Path
from app import app

@app.route('/')
@app.route('/index')
def index():
    cmds_path = Path.cwd().joinpath("app","cmds")
    cmds_available = [ x.stem for x in cmds_path.glob("*.txt") ]
    return render_template("index.txt", cmds_available=cmds_available )


@app.route('/<path:cmd>')
def get_cmd(cmd):
    filename = cmd + ".txt"
    cmds_path = Path.cwd().joinpath("app","cmds")
    filename_path = cmds_path.joinpath(filename)
    if filename_path.exists():
        return render_template(filename)
    else :
        return "File not accessible"
