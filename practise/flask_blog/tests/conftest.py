import os
import tempfile
import pytest
from flaskr import create_app
from flaskr.db import get_db,init_db

with open(os.path.join(os.path.dirname(__file__),'data.sql')) as f:
    _data_sql = f.read()

# app 固件会调用工厂并为测试传递 test_config 来配置应用和数据库，而不使用本地的开发配置。
# 每个测试都会用到pytest的fixture函数
@pytest.fixture
def app():
    db_fd,db_path = tempfile.mkstemp()
    # mkstemp:以最安全的方式创建一个临时文件。

    app = create_app({
        'TESTING':True,
        'DATABASE':db_path
    })

    # Use app_context() in a with block, and everything that runs in the block will have access to current_app.
    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)
    
    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

# 用类的方法使用客户端将post请求发给login视图，避免每次测试都写一遍
class AuthActions(object):
    def __init__(self,client):
        self._client = client

    def login(self,username='test',password='test'):
        return self._client.post(
            '/auth/login',
            data={'username':username,'password':password}
        )

    def logout(self):
        return self._client.get('/auth/logout')

@pytest.fixture
def auth(client):
    return AuthActions(client)