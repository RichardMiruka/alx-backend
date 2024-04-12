from flask import request
#...
from flask_babel import flask_babel

def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # an attribute of Flask's request object called accept_languages

app = Flask(_name_)
# ...
babel = Babel(app, locale_selector=get_locale)
#...
