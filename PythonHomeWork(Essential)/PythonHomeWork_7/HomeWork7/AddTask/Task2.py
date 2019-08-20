"""Python homework Essentials
Эмуляция работы сервиса по сокращению ссылок"""

from flask import Flask
from flask import abort
from flask import redirect
from flask import render_template
from flask import request
from urllib.parse import urlparse


class LinksDB(object):
    """Хранилище ссылок.
    Для простоты использутся обычный словарь."""

    def __init__(self):
        # Словарь ссылок
        self._links = {}

    def get_url(self, name):
        # Получение ссылки по имени
        return self._links[name]

    def set_url(self, name, url):
        """Метод добавления новый ссылки"""
        url = self.normalize_url(url)
        if not name:
            raise KeyError('Link name cannot be empty', name)
        if not url:
            raise ValueError('Invalid link URL', url)
        if name in self._links:
            raise KeyError('Link already exist', name)

    def normalize_url(self, url):
        """Метод который добавляет протокол, если он отсутствует,
        и возвращает исправный или исходный URL, если он корректный,
        или None в ином случае"""
        if not urlparse(url).scheme:
            url = 'http://' + url
        if urlparse(url).netloc:
            return url
        else:
            return None


links = LinksDB()  # Создание глобального хранилища
app = Flask(__name__)  # Создание объекта веб-приложения


@app.route('/', methods=['GET', 'POST'])
def create_link():
    """Контроллер создания новой ссылки"""

    error_message = None
    name = ''
    url = 'http://'
    success_message = None

    if request.method == 'POST':
        name = request.form['name']
        url = request.form['url']

        try:
            links.set_url(name, url)
        except (KeyError, ValueError) as error:
            error_message = error.args[0]
        else:
            success_message = 'Link added successfully'
    return render_template('task 2_for_advanced_learners.html',
                           name=name, url=url,
                           error=error_message,
                           success=success_message)


@app.route('/<name>')
def go_to_link(name):
    """Контроллер перехода по ссылке"""

    try:
        url = links.get_url(name)
    except KeyError:
        abort(404)
    return redirect(url)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
