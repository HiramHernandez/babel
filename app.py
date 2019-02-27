from datetime import datetime

from flask import Flask
from flask import jsonify
from flask_babel import Babel

import date_helper
import month_helper

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@app.route("/")
def index():
    return '<h2>Bienvenido al index</h2>'

@app.route("/fechas")
def get_dates():
    current_date = datetime.now()
    date_format = date_helper.DateFormat(current_date)
    response = {
        'Fecha en formato corto': date_format.short_date(), 
        'Fecha en formato largo': date_format.long_date(), 
        'Fecha entera': date_format.full_date()
    }
    return jsonify(response), 200

@app.route("/months")
def months():
    return jsonify({'meses': month_helper.get_months()})

  
if __name__ == '__main__': 
    print(dir(date_helper))
    app.run(debug=False, port=5000)