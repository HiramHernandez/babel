from datetime import date, datetime, time

from babel import Locale
from babel.dates import format_date, format_datetime, format_time

from app import babel

class DateFormat():
    _instance = None
    str_date = None,
    

    def __init__(self, str_date):
        self.str_date = str_date

    def __str__(self):
        return "Hora {}".format(self.str_date)

    @classmethod
    def _date_with_format(cls, date, str_format):
        return format_date(date, str_format, babel.default_locale)

    
    def short_date(self):
        return self._date_with_format(self.str_date, 'short')

    def long_date(self):
        return self._date_with_format(self.str_date, 'long')

    def full_date(self):
        return self._date_with_format(self.str_date, 'full')
