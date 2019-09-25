import time

import bottle
from bottle import redirect
from bottle import view
from bottle import static_file

from scripts.increase_animal import increase_animal
from scripts.list_results import list_result


def create_app():
    app = bottle.Bottle()
    app.config.load_config('sse_server.conf')
    app.config.setdefault('server', 'auto')
    app.config.setdefault('host', 'localhost')
    app.config.setdefault('port', 8000)
    app.config.setdefault('database_path', 'sqlite:///my_db.sqlite')
    return app

app = create_app()
url = 'http://94.103.94.54:' + app.config.port
urlSF = 'https://sf-pyw.mosyag.in'

#приветственная страница
#в навбаре выбор голосовалки (этот сервер или сервер sf)
@app.route('/')
@view('index.tpl')
def index():
    pass

#страница с голосованием на этом сервере
#в шаблон передаем url нашего сервера
@app.route('/vouting')
@view('vouting.tpl')
def vouting():
    return {'url': url}

#страница с голосованием на этом сервере
#в шаблон передаем url сервера SF
@app.route('/sfvouting')
@view('vouting.tpl')
def sfvouting():
    return {'url': urlSF}

#страница с результатами
@app.route('/results')
@view('results.tpl')
def results():
    return {'urlSF': urlSF, 'url': url}

#SSE-стрим с текущими результатами голосования нашего сервера
@app.route('/stats')
def stats():
    bottle.response.content_type = "text/event-stream"
    bottle.response.cache_control = "no-cache"
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    return f'data: {list_result(app.config.database_path)}'

#принимающими POST-запросы с пустым телом
@app.post('/sse/vote/cats')
def increase_cats():
    increase_animal(app.config.database_path, 'cats')
    #return redirect('/stats')

@app.post('/sse/vote/dogs')
def increase_dogs():
    increase_animal(app.config.database_path, 'dogs')
    #return redirect('/stats')

@app.post('/sse/vote/parrots')
def increase_parrots():
    increase_animal(app.config.database_path, 'parrots')
    #return redirect('/stats')

#объект необходим для работы со статикой (CSS, JS)
@app.route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")

#тестовая страница
@app.route('/words')
def word_spammer():
    bottle.response.content_type = "text/event-stream"
    bottle.response.cache_control = "no-cache"
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'

    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    for word in words:
        yield 'data: %s\n\n' % word
        time.sleep(2)


if __name__ == "__main__":
    bottle.run(
        app=app,
        host=app.config.host,
        port=app.config.port,
        server=app.config.server,
    )