from datetime import date, datetime, time

from babel import Locale

def get_months():
        from app import babel
        locale = babel.default_locale
        month_names = locale.months['format']['wide'].items()
        order = 0
        name = None
        months = [lambda month: order, name in sorted(month_names)]  
        return [name.upper() for idx, name in sorted(month_names)]
     