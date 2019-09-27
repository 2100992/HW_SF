# import time
from time import time, sleep
from configparser import ConfigParser

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
    app.config.setdefault('SSEHost', 'http://localhost')
    app.config.setdefault('SSEPort', 8000)
    #путь к базе данных
    app.config.setdefault('database_path', 'sqlite:///my_db.sqlite')
    return app

app = create_app()

config = ConfigParser()
try:
    config.read('sse_server.conf')
    app.config.SSEHost = config['bottle']['ssehost']
    app.config.SSEPort = config['bottle']['sseport']
except Exception as err:
    print(err)

print(f'server = {app.config.server}')
print(f'host = {app.config.server}')
print(f'port = {app.config.port}')
print(f'SSEHost = {app.config.SSEHost}')
print(f'SSEPort = {app.config.SSEPort}')
print(f'database_path = {app.config.database_path}')


url = str(app.config.SSEHost) + ":" + str(app.config.SSEPort)
urlSF = 'https://sf-pyw.mosyag.in'

#приветственная страница
#выбор голосовалки (этот сервер или сервер sf)
@app.route('/')
@view('index.tpl')
def index():
    print('/')
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
    bottle.response.content_type = "text/event-stream"
    bottle.response.cache_control = "no-cache"
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'
    #result = f'data: {list_result(app.config.database_path)}\n\n'
    #print(result)
    #return result

    # Set client-side auto-reconnect timeout, ms.
    yield 'retry: 100\n\n'
    
    # Keep connection alive no more then... (s)
    end = time() + 60
    while time() < end:
        yield 'data: %i\n\n' % list_result(app.config.database_path)
        sleep(1)


#    now = time()
#    while time() - now > 1:
#         yield f'data: {list_result(app.config.database_path)}'
    #         now = time()
        # result = f'data: {list_result(app.config.database_path)}'
        #print(result)
        # yield result
        #sleep(1)


#принимающими POST-запросы с пустым телом
@app.post('/sse/vote/cats')
def increase_cats():
    print('increase_cats')
    increase_animal(app.config.database_path, 'cats')
    stats()
    #return redirect('/stats')

@app.post('/sse/vote/dogs')
def increase_dogs():
    print('increase_dogs')
    increase_animal(app.config.database_path, 'dogs')
    stats()
    #return redirect('/stats')

@app.post('/sse/vote/parrots')
def increase_parrots():
    print('increase_parrots')
    increase_animal(app.config.database_path, 'parrots')
    stats()
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