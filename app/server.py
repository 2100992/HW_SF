from time import time, sleep
from configparser import ConfigParser

import bottle
from bottle import redirect
from bottle import view
from bottle import static_file
from truckpad.bottle.cors import CorsPlugin, enable_cors

from scripts.increase_animal import increase_animal
from scripts.list_results import list_result

#from http import cookies

import app.db_tasks as db_tasks

#Очень сомнительный кусок кода bottle.Bottle().config.load_config разбирает только часть конфига
#SSEHost, SSEPort, database_path не читаются. Надо бы вынести чтение конфигов базы данных и SSE в отдельные функции
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

#Догружаем нераспознанные параметры в app.config

config = ConfigParser()
try:
    config.read('sse_server.conf')
    app.config.SSEHost = config['bottle']['SSEHost']
    app.config.SSEPort = config['bottle']['SSEPort']
    app.config.database_path = config['bottle']['database_path']
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
@app.route('/')
@view('index.tpl')
def index():
    print('/')
    pass
#-----------------------------------C1-------------------------------------
#приветственная страница по модулю C1
@app.route('/C1')
@view('C1.tpl')
def indexC1():
    print('/C1')
    pass

#-----------------------------------C2-------------------------------------
#приветственная страница по модулю C2
#выбор голосовалки (этот сервер или сервер sf)
@app.route('/C2')
@view('C2.tpl')
def indexC2():
    print('/C2')
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
    
    # # Keep connection alive no more then... (s)
    end = time() + 600
    while time() < end:
        yield 'data: %s\n\n' % list_result(app.config.database_path)
        sleep(1)

    # now = time()
    # while True:
    #     if time() - now > 1:
    #         yield 'data: %s\n\n' % list_result(app.config.database_path)
    #         now = time()


#принимающими POST-запросы с пустым телом
@app.post('/sse/vote/cats')
def increase_cats():
    print('increase_cats')
    increase_animal(app.config.database_path, 'cats')


@app.post('/sse/vote/dogs')
def increase_dogs():
    print('increase_dogs')
    increase_animal(app.config.database_path, 'dogs')


@app.post('/sse/vote/parrots')
def increase_parrots():
    print('increase_parrots')
    increase_animal(app.config.database_path, 'parrots')


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


#-----------------------------------C3-------------------------------------
#приветственная страница по модулю C3
#выбор программы "Ваш город" или "Галочки предпочтений"
@app.route('/C3')
@view('C3.tpl')
def indexC3():
    print('/C3')
    pass

# Такой способ не проходит
# не получается декодировать кирилицу из bottle.request.get_cookie('my_city')
# @app.route('/your_city')
# @view('your_city.tpl')
# def your_city():
#     print('/your_city')
#     city = bottle.request.get_cookie('my_city')
#     print(city)
#     if city:
#         return {'city': city, 'is_known': '', 'is_unknown': 'd-none'}
#     else:
#         return {'city': '', 'is_known': 'd-none', 'is_unknown': ''}


@app.route('/your_city')
@view('your_city.tpl')
def your_city():
    print('/your_city')
    pass


@app.route('/preferences')
@view('preferences.tpl')
def preferences():
    print('/preferences')
    pass


#-----------------------------------C4-------------------------------------
# @enable_cors
# @app.route("/api/tasks/")
# def indexC4():
#     # bottle.response.headers['Access-Control-Allow-Origin'] = '*'
#     tasks = [task.to_dict() for task in tasks_db.values()]
#     return {"tasks": tasks}

# @enable_cors
# @app.post("/api/add-task")
# def add_task():
#     desc = bottle.request.json['description']
#     is_completed = bottle.request.json['is_completed']
#     if len(desc) > 0:
#         new_uid = max(tasks_db.keys()) + 1
#         t = TodoItem(desc, new_uid)
#         t.is_completed = is_completed
#         tasks_db[new_uid] = t
#     return "Ok"

@app.route('/C4')
@view('C4.html')
def indexC4():
    redirect('http://94.103.94.54:5000')

@enable_cors
@app.route("/api/tasks/<userName>", method=["GET", "POST", "PUT"])
def add_task(userName):
    if bottle.request.method == 'GET':
        tasks = []
        for task in db_tasks.find_tasks(userName):
            tasks.append({
                'id': task.id,
                'uid': task.uid,
                'desc': task.desc,
                'user': task.user,
                'is_completed': task.is_completed,
                'is_deleted': task.is_deleted
            })
        return {"tasks": tasks}
    elif bottle.request.method == "POST":
        db_tasks.add_task(userName, bottle.request.json['description'])
        print(bottle.request.json)
        return "OK"
    elif bottle.request.method == "PUT":
        print(bottle.request.json)
        uid = bottle.request.json['uid']
        #db_tasks.change_task(uid, **bottle.request.json)
        db_tasks.change_task(**bottle.request.json)
        #print(bottle.request.json)
        return "OK"
    # elif bottle.request.method == "OPTIONS":
    #     db_tasks.change_task(bottle.request.json['uid'], **bottle.request.json)
    #     print(bottle.request.json)
    #     return "OK"

@app.route("/api/delete/<uid:int>")
def api_delete(uid):
    tasks_db.pop(uid)
    return "Ok"


@app.route("/api/complete/<uid:int>")
def api_complete(uid):
    tasks_db[uid].is_completed = True
    return "Ok"



app.install(CorsPlugin(origins=['http://94.103.94.54:8080']))
#--------------------------------------------------------------------------
if __name__ == "__main__":
    bottle.run(
        app=app,
        host=app.config.host,
        port=app.config.port,
        server=app.config.server,
    )