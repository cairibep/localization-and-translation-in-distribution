import requests
import gettext
import locale
from datetime import datetime
from babel.dates import format_datetime

locale.setlocale(locale.LC_ALL, '')
language, _ = locale.getlocale()

translation = gettext.translation(
    domain='dev_aberto',
    localedir='dev_aberto/locale',
    languages=[language] if language else ['en_US'],
    fallback=True
)
translation.install()
_ = translation.gettext

def hello():
    """Retorna data e nome do último commit do repositório insper/dev-aberto"""
    c = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    info = c.json()
    commit_info = info[0]['commit']['author']
    date = commit_info['date']
    name = commit_info['name']


    dt = datetime.fromisoformat(date.replace('Z', '+00:00'))
    formatted_date = format_datetime(dt, format='full', locale=language or 'en_US')

    return formatted_date, name

def main():
    date, name = hello()
    print(_('Último commit feito em: {date}, por {name}.').format(date=date, name=name))
