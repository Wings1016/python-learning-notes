# config_default.py

configs = {
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'www-data',
        'password': 'www-data123',
        'database': 'awesome'
    },
    'session': {
        'secret': 'AwEsOmE'
    }
}


'''
如果要修改配置信息，通常新建config_override.py
# config_override.py

configs = {
    'db': {
        'host': '192.168.0.100'
    }
}
可以既方便地在本地开发，又可以随时把应用部署到服务器上。

为了统一，合并到config.py
'''