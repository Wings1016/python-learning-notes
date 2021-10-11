
import os
from flask import Flask

# Application Factory（工厂）函数使得测试和部署更加方便。我们不必将加载的配置写死在某处，而是直接在不同的地方按照需要的配置创建程序实例。
# 通过支持创建多个程序实例，工厂函数提供了很大的灵活性。
def create_app(test_config=None):
    # create the app
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',    # dev是临时key
        DATABASE = os.path.join(app.instance_path,'flaskr.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py',silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello World'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/',endpoint='index')      # 关联/和index，则url_for('blog')和url_for('blog.index')一样

    return app
