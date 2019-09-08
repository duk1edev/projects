from flask import Flask, abort, redirect
from flask import render_template, request
from links_db import LinksDB

links = LinksDB()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def create_link():
    """Controller of creating new link"""

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
    return render_template('add_link.html',
                           name=name, url=url,
                           error=error_message,
                           success=success_message)


@app.route('/<name>')
def go_to_link(name):
    """Controller following by the links"""

    try:
        url = links.get_url(name)
    except KeyError:
        abort(404)
    return redirect(url)


if __name__ == '__main__':
    app.run()
