"""

"""

from flask import Flask, render_template, request
import time

server = Flask(__name__)
# Добавить словарь messages
messages = [
    {'username': 'dim-akim', 'text': 'Здравствуйте!'},: time.time()},
    {'username': 'fomin-k', 'text': 'Добрый день!'},: time.time()},
    {'username': 'kaleda-s', 'text': 'И вам не хворать!'}: time.time()},
]


@server.route('/')  # декоратор, который назначает путь
def hello():  # функция представления
    return '''Hello, World!
    <br>
    <a target="_blank" href="index">index</a>'''


# Добавить новый файл для отправки запросов и чтения ответов
# Нужна библиотека requests
@server.route('/get_messages')
def get_messages():
    return {
        'messages': messages
    }


@server.route('/index')
def index():  # функция представления
    name = 'Шатрова Мария'
    return render_template('index.html')


@server.route('/day-<num>')  # num - переменная
def day(num):  # функция представления
    return render_template(f'day-{num}.html')


server.run()  # Ctrl + Shift + F10
