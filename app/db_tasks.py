import uuid
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///my_db_tasks.sqlite"
Base = declarative_base()

class Tasks(Base):

    __tablename__ = "tasks"

    id = sa.Column(sa.INTEGER, primary_key=True)    # порядковый номер задачи 
    uid = sa.Column(sa.TEXT, unique=True)           # уникальный ID задачи
    desc = sa.Column(sa.TEXT)                       # текст задачи
    user = sa.Column(sa.TEXT)                       # имя владельца задачи
    is_completed = sa.Column(sa.BOOLEAN)            # признак выполненности
    is_deleted = sa.Column(sa.BOOLEAN)              # признак удаления

def connect_db(DB_PATH):
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def find_tasks(user):
    """
    Находит все задачи принадлежащие пользователю
    """
    session = connect_db(DB_PATH)
    tasks = session.query(Tasks).filter(Tasks.user == user, Tasks.is_deleted == False).all()
    return tasks

def get_all_tasks():
    """
    Находит все задачи принадлежащие пользователю
    """
    session = connect_db(DB_PATH)
    tasks = session.query(Tasks).all()
    return tasks

def add_task(user, desc, uid = '', is_completed = False, is_deleted = False):
    """
    Добавление задачи с возможностью генерации UUID
    """
    session = connect_db(DB_PATH)

    if uid == '':
        uid = str(uuid.uuid4())

    task = Tasks(
        user = user,
        desc = desc,
        uid = uid,
        is_completed = is_completed,
        is_deleted = is_deleted
    )

    session.add(task)
    session.commit()
    pass

# def change_task(uid, *args, **kwargs):
def change_task(**kwargs):
    """
    Изменяем задачу по uid
    """
    session = connect_db(DB_PATH)
    uid = kwargs['uid']
    task = session.query(Tasks).\
        filter(Tasks.uid == uid).first()
    
    for key, value in kwargs.items():
        if key == 'description':
            task.desc = value
        if key == 'is_completed':
            task.is_completed = value
        if key == 'is_deleted':
            task.is_deleted = value
        if key == 'user':
            task.user = value
    
    session.add(task)
    session.commit()
    pass

def get_task(uid):
    session = connect_db(DB_PATH)
    task = session.query(Tasks).\
        filter(Tasks.uid == uid).first()
    return task