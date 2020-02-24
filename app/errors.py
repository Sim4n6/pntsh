from app import app

@app.errorhandler(404)
def page_not_found(error):
    return "Page not found. Please, feel free to contribute https://github.com/Sim4n6/pntsh .\n", 404

