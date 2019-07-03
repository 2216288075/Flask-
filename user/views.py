from user import user_blu
from flask import Flask, session, g, abort
import functools

#@user_blu.route('/AAA/')
#def AAA():
#    return 'user蓝图index'


#@user_blu.before_request
#def get_user_info():
#    
#    name=session.get('name')
#    g.name=name


#----------------------------------------认证-----------------------------------------------




def AAA(f):
    @functools.wraps(f)
    def BBB(*args, **kwargs):
        if session.get('name'):
            return f(*args, **kwargs)
        else:
            abort(401)
    return BBB



@user_blu.route('/')
def index():
    name = session.get('name')
    if name == 'ww':
        return '已登陆'
    else:
        return '未登陆'


@user_blu.route('/login/')
def login():
    session['name'] = 'ww'
    return '用户登陆'


@user_blu.route('/info/')
@AAA
def info():
    return '用户登陆'













