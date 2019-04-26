from flask import Blueprint, render_template, redirect, request, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from back.models import User, ArticleType, db, Article
from utils.functions import is_login

back_blueprint = Blueprint('back',__name__)


@back_blueprint.route('/index/')
@is_login
def index():
    return render_template('back/index.html')

@back_blueprint.route('/register/',methods=['GET','POST'])

def register():#登入
    if request.method == 'GET':
        return render_template('back/register.html')
    if request.method == 'POST':
            #获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        if username and password:
            # 从数据库取值判断
            user = User.query.filter(User.username == username).first()
            if not user:
                error = '该账号不存在请重新注册'
                return render_template('back/login.html',error=error)
            if not check_password_hash(user.password,password):
                error = '密码错误,请重新输入密码'
                return render_template('back/register.html',error=error)
            #账号密码都正确,返回首页之前给一个标志
            session['user_id'] = user.id
            return redirect(url_for('back.index'))
        else:
            error = '请填写完整的登入信息'
            return render_template('back/register.html',error=error)

@back_blueprint.route('/login/',methods=['GET','POST'])

def login():#注册
    print(request.method )
    if request.method == 'GET':
        return render_template('back/login.html')#注册页面
    # if request.method == 'POST':
    #
    #     return render_template('back/index.html')
@back_blueprint.route('/login1/',methods=['GET','POST'])
def login1():#注册
    if request.method == 'POST':
        # 获取数据
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if username and password:
            #判断该账号是否注册过,这里是从数据库取值
            user = User.query.filter(User.username == username).first()
            if user:
                error = '该账号已经被注册'
                return render_template('back/login.html',error=error)
            else:
                if password == password2:
                    # 保存数据
                    user = User()
                    user.username = username
                    user.password =  generate_password_hash(password)
                    user.save()
                    # return render_template('back/register.html')
                    return redirect(url_for('back.register'))
                else:
                #     密码错误
                    error = '密码不一致'
                    return render_template('back/login.html',error=error)
@back_blueprint.route('/logout/',methods=['GET'])
@is_login
def logout():
    del session['user_id']
    return redirect(url_for('back.register'))

@back_blueprint.route('/type/',methods=['GET','POST'])
@is_login
def type():
    if request.method == 'GET':
        types = ArticleType.query.all()
        return render_template('back/category.html', types=types)
        # return render_template('back/category.html')
    if request.method == 'POST':
        #获取数据
        name = request.form.get('name')
        alias = request.form.get('alias')
        #保存数据
        art_type = ArticleType()
        art_type.name = name
        art_type.alias = alias
        db.session.add(art_type)
        db.session.commit()
        return redirect(url_for('back.type'))

# @back_blueprint.route('/add_type/',methods=['GET','PSOT'])
# def add_type():
#     if request.method == 'GET':
#         types = ArticleType.query.all()
#         return render_template('back/category.html',types=types)
@back_blueprint.route('/del_type/<int:id>/',methods=['GET'])
# @is_login
def del_type(id):
    aid = ArticleType.query.get(id)#aid是一个列表对象
    # print(aid)<ArticleType 15>
    db.session.delete(aid)
    db.session.commit()
    return redirect(url_for('back.type'))
@back_blueprint.route('/update_art/<int:id>',methods=['GET','POST'])
def update_art(id):
    if request.method == 'GET':
        upid = ArticleType.query.get(id)
        return render_template('back/category-change.html',upid=upid)
    if request.method == 'POST':
        uid = ArticleType.query.get(id)
        uid.name = request.form.get('name')
        uid.alias = request.form.get('alias')
        db.session.add(uid)
        db.session.commit()
        return redirect(url_for('back.type'))
@back_blueprint.route('/article/',methods=['GET','POST'])
@is_login
def article():

    if request.method == 'GET':

        arts = Article.query.all()
        return render_template('back/article.html',arts=arts)
@back_blueprint.route('/add-articel/',methods=['GET','POST'])
@is_login
def add_article():
    if request.method == 'GET':
        return render_template('back/add-article.html')
    if request.method == 'POST':
        #获取数据
        title = request.form.get('title')
        content = request.form.get('content')
        tags = request.form.get('tags')
        category = request.form.get('category')
        create_time = request.form.get('create_time')
        #保存数据
        art = Article()
        art.title = title
        art.content = content
        art.category = category
        art.tags = tags
        art.create_time = create_time
        db.session.add(art)
        db.session.commit()
        return redirect(url_for('back.article'))
@back_blueprint.route('/del_article/<int:id>',methods=['GET'])
@is_login
def del_article(id):
    bid = Article.query.get(id)
    db.session.delete(bid)
    db.session.commit()
    return redirect(url_for('back.article'))
@back_blueprint.route('/update_article/<int:id>',methods=['GET','POST'])
@is_login
def update_article(id):
    if request.method == 'GET':
        upid = Article.query.get(id)
        return render_template('back/change-article.html',upid=upid)
    if request.method == 'POST':
        upid = Article.query.get(id)
        upid.title = request.form.get('title')
        upid.content = request.form.get('content')
        upid.category = request.form.get('category')
        upid.tags = request.form.get('tags')
        # upid.create_time = request.form.get('create_time')
        db.session.add(upid)
        db.session.commit()
        return redirect(url_for('back.article'))












