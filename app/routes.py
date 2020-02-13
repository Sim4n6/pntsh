from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/<path:cmd>')
def get_cmd(cmd):
    return render_template(cmd)