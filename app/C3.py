import bottle
from bottle import redirect
from bottle import view
from bottle import static_file

from app.server import create_app

app = create_app()

#приветственная страница по модулю C3
#выбор программы "Ваш город" или "Галочки предпочтений"
@app.route('/C3')
@view('C3.tpl')
def indexC2():
    print('/C3')
    pass