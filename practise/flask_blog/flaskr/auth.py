# A view function is the code you write to respond to requests to your application. 
# A Blueprint is a way to organize a group of related views and other code.
# Flaskr will have two blueprints, one for authentication functions and one for the blog posts functions.

import functools
from flask import render_template,Blueprint,g,request,flash,url_for,redirect,session
from werkzeug.security import generate_password_hash,check_password_hash
from flaskr.db import get_db

bp = Blueprint('auth',__name__,url_prefix='/auth')

# The first View:register
@bp.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = '用户名不能为空！'
        elif not password:
            error = '密码不能为空！'
        elif db.execute('SELECT id FROM user WHERE username=?', (username,)).fetchone() is not None:
            error = '该用户名已被注册！'
        
        if error is None:
            db.execute('INSERT INTO user(username,password) values(?,?)',(username,generate_password_hash(password)))
            db.commit()
            return redirect(url_for('auth.login'))
        
        flash(error)
    
    return render_template('auth/register.html')

# Loging登录
@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute('SELECT * FROM user WHERE username=?',(username,)).fetchone()

        if user is None:
            error = "该用户不存在！"
        elif not check_password_hash(user['password'],password):
            error = "密码输入不正确！"
            
        if error is None:
            session.clear()     # session 是一个存储跨请求数据的字典。
            session['user_id']=user['id']
            return redirect(url_for('index'))
            
        flash(error)

    return render_template('auth/login.html')

# bp.before_app_request() registers a function that runs before the view function，检查user_id是否在session中，如果不在则None
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user=None
    else:
        g.user=get_db().execute('SELECT * FROM user WHERE id=?',(user_id,)).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Creating,editing,and deleting blog posts will require a user to be logged in. 
# A decorator can be used to check this for each view it’s applied to.
def login_required(view):
    @functools.wraps(view)
    def wrappered_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrappered_view