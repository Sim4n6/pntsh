from app import app

@app.errorhandler(404)
def page_not_found(error):
    return "Page not found.\n", 404

