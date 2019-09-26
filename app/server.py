# import time
from time import time, sleep

import bottle
from bottle import redirect
from bottle import view
from bottle import static_file

from scripts.increase_animal import increase_animal
from scripts.list_results import list_result


def create_app():
    app = bottle.Bottle()
    #пытаемся загрузить конфигурацию из этого файла
    app.config.load_config('sse_server.conf')
    #в случае отсутствия файла с конфигурацией
    #http сервер по умолчанию gunicorn/nginx/auto/
    app.config.setdefault('server', 'auto')
    #host - ip адрес с которого слушаем запросы (0.0.0.0 - со всех адресов)
    app.config.setdefault('host', 'localhost')
    app.config.setdefault('port', 8000)
    #SSEHost, SSEPort - адрес и порт на котором запущен наш SSE сервер
    app.config.setdefault('SSEHost', 'localhost')
    app.config.setdefault('SSEPort', 8000)
    #путь к базе данных
    app.config.setdefault('database_path', 'sqlite:///my_db.sqlite')
    return app

app = create_app()
print(f'server = {app.config.server}')
print(f'host = {app.config.server}')
print(f'port = {app.config.port}')
print(f'SSEHost = {app.config.SSEHost}')
print(f'SSEPort = {app.config.SSEPort}')
print(f'database_path = {app.config.database_path}')


url = str(app.config.SSEHost) + ":" + str(app.config.SSEPort)
urlSF = 'https://sf-pyw.mosyag.in'

#приветственная страница
#в навбаре выбор голосовалки (этот сервер или сервер sf)
@app.route('/')
@view('index.tpl')
def index():
    pass

#страница с голосованием на этом сервере
#в шаблон передаем url нашего сервера
@app.route('/voting')
@view('voting.tpl')
def vouting():
    return {'url': url}

#страница с голосованием на этом сервере
#в шаблон передаем url сервера SF
@app.route('/sfvoting')
@view('voting.tpl')
def sfvouting():
    return {'url': urlSF}

#страница с результатами
@app.route('/results')
@view('results.tpl')
def results():
    return {'urlSF': urlSF, 'url': url}

#SSE-стрим с текущими результатами голосования нашего сервера
@app.route('/sse/vote/stats')
def stats():
    #now = time()
    bottle.response.content_type = "text/event-stream"
    bottle.response.cache_control = "no-cache"
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    # result = f'data: {list_result(app.config.database_path)}'
    # print(result)
    # return result

    while True:
        # if time() - now > 1:
        #     yield f'data: {list_result(app.config.database_path)}'
        #     now = time()
        result = f'data: {list_result(app.config.database_path)}'
        print(result)
        yield result
        sleep(1)


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
        sleep(1)

#тестовая страница
@app.route('/randoms')
@view('randoms.tpl')
def mosyagin_randoms():
    pass


if __name__ == "__main__":
    bottle.run(
        app=app,
        host=app.config.host,
        port=app.config.port,
        server=app.config.server,
    )