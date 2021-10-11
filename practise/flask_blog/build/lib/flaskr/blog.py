import functools
from flask import render_template,Blueprint,g,request,flash,url_for,redirect
from flaskr.db import get_db
from werkzeug.exceptions import abort
from flaskr.auth import login_required

bp = Blueprint('blog',__name__)

@bp.route('/')
def index():
    db = get_db()
    # posts = db.execute('SELECT p.id,title,content,created,author_id,username FROM post p JOIN user u'
    # 'ON p.author_id=u.id ORDER BY created DESC').fetchall()
    posts = db.execute('SELECT p.id, title, content, createtime, author_id, username FROM post p JOIN user u ON p.author_id = u.id ORDER BY createtime DESC').fetchall()
    return render_template('blog/index.html',posts=posts)

@bp.route('/create',methods=['GET','POST'])
@login_required
def create():
    if request.method=='POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = "标题不能为空！"
            
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('INSERT INTO post(title,content,author_id) values(?,?,?)', (title,content,g.user['id']) )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id,check_author=True):
    db = get_db()
    # post = db.execute('SELECT p.id,title,content,created,author_id,username FROM post p JOIN user u'
    # 'ON p.author_id=u.id WHERE p.id=?',(id,)).fetchone()
    post = get_db().execute(
        'SELECT p.id, title, content, createtime, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404,f'博客id：{id}不存在！')
    
    if check_author and post['id']!=g.user['id']:
        abort(403)
    
    return post

@bp.route('/<int:id>/update',methods=['GET','POST'])
@login_required
def update(id):
    post = get_post(id)
    if request.method=='POST':
        title = request.form['title']
        content = request.form['content']
        error = None

        if not title:
            error = "标题不能为空！"
            
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('UPDATE post SET title=?,content=? WHERE id=?',(title,content,id))
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html',post=post)

@bp.route('/<int:id>/delete',methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id=?',(id,))
    db.commit()
    return redirect(url_for('blog.index'))
