import click
import sqlite3
from flask import current_app,g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            # current_app 是另一个特殊对象，该对象指向处理请求的 Flask 应用。
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()

# 运行schema.sql
def init_db():
    db = get_db()   # 返回一个数据库链接
    # open_resource() 打开一个文件，该文件名是 相对于 flaskr 包的。这样就不需要考虑以后应用具体部署在哪个位置。
    with current_app.open_resource('todolist.sql') as f:
        db.executescript(f.read().decode('utf-8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

# 注册应用实例
def init_app(app):
    # app.teardown_appcontext()告诉Flask在返回响应后进行清理的时候调用此函数。
    app.teardown_appcontext(close_db)
    # # app.cli.add_command() 添加一个新的可以与flask一起工作的命令。
    app.cli.add_command(init_db_command)