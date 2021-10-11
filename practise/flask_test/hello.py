#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for, request, render_template, make_response, abort, redirect, jsonify, g
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 默认是GET方法


@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    return '<p>Hello World</p>'

# Variable Rules


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# Redirection


@app.route('/projects/')    # 如果访问的是/projects，flask会自动转到/projecs/
def projects():
    return 'The project page'


@app.route('/about')    # 如果访问/about/，会提示404
def about():
    return 'The about page'


# url_for构建url函数
with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('show_user_profile', username='John Doe'))
    print(url_for('static', filename='style.css'))

# 静态文件,通常存放在static文件夹下，如css和js文件
# url_for('static',filename = 'style.css')

# 使用html模版，templates文件夹下
'''
Case 1: a module:

/application.py
/templates
    /hello.html

Case 2: a package:

/application
    /__init__.py
    /templates
        /hello.html
'''


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# request


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    '''
    if request.method == 'POST':
        pass
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
        '''
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

# 文件上传


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
        # 保存为上传前的文件名
        f.save(f'/var/www/uploads/{secure_filename(f.filename)}')

# Cookies

# Reading cookies:


@app.route('/test')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.

# Storing cookies:


@app.route('/test')
def index1():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

# 重定向和弃用


@app.route('/')
def index2():
    return redirect(url_for('login'))


@app.route('/test1')
def login1():
    abort(401)
    print('this is never executed.')

# 修改response对象的内容


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

# jsonify序列化数据然后打包成response


@app.route("/users/me")
def get_current_user():
    return jsonify(
        username=g.user.username,
        email=g.user.email,
        id=g.user.id,
    )
