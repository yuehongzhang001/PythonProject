# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response, redirect,flash,get_flashed_messages
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.secret_key='nowcoder'


@app.route('/index')
@app.route('/')
def index():
    res=''
    for msg, cat in get_flashed_messages(with_categories=True):
        res = res + msg + cat+ '<br/>'
    return res + 'hello'

@app.route('/profile/<uid>', methods=['GET','POST'])
def profile(uid):
    colors=('red','green')
    userInfo = {'name':'jay','age':'11','gender':'male'}
    return render_template('profile.html',uid=uid, colors=colors,userInfo=userInfo)

@app.route('/request')
def request_demo():
    key = request.args.get('key','defaultkey')
    res= request.args.get('key','defaultkey') +'<br/>'
    res = res + request.url+"---"+request.path+'<br/>'
    for p in dir(request):
        res = res+str(p) + str(eval('request.'+p))+'<br/>'
    response = make_response(res)
    response.set_cookie('id',key)
    return response

@app.route('/newpath')
def newpath():
    return 'newpath'

@app.route('/re/<int:code>')
def redirect_demo(code):
    return redirect('/newpath',code=301)

@app.errorhandler(404)
def page_not_found(error):
    print error
    return render_template('not_found.html', url=request.url)

@app.route('/admin')
def admin():
    key = request.args.get('key')
    if key=='admin':
        return '<h1>Hello! admin </h1>'
    else:
        raise ValueError()
    return 'xxx'

@app.route('/login')
def login():
    flash('Good!','info')

    return redirect('/index')

@app.route('/log/<level>/<msg>/')
def log(level, msg):
    dict = {'warn':logging.WARN, 'error':logging.ERROR, 'info':logging.INFO}
    if dict.has_key(level):
        app.logger.log(dict[level],msg)
    return 'logged:'+msg

def set_logger():
    info_file_handler= RotatingFileHandler('./logs/info.txt')
    info_file_handler.setLevel(logging.INFO)
    app.logger.addHandler(info_file_handler)
    warn_file_handler= RotatingFileHandler('./logs/warn.txt')
    warn_file_handler.setLevel(logging.WARN)
    app.logger.addHandler(warn_file_handler)
    error_file_handler= RotatingFileHandler('./logs/error.txt')
    error_file_handler.setLevel(logging.ERROR)
    app.logger.addHandler(error_file_handler)


if __name__=='__main__':
    set_logger()
    app.run(debug=True)