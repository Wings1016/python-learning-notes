from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING':True}).testing

def test_hello(client):
    response = client.get('/hello')
    # 测试响应数据是否匹配
    assert response.data == b'Hello World'
