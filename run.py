from flask import redirect
from mainapp import creat_app
app = creat_app()
@app.errorhandler(404)
def page_not_found(error):
    return  redirect('/'), 404, {"Refresh": "1; url=/"}