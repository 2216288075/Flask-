from flask import Flask, redirect, url_for, request, render_template, make_response, jsonify, redirect, url_for, session, abort
from werkzeug.routing import BaseConverter
import json
from datetime import timedelta


#----------------------------------------初始化--------------------------------------------

app = Flask(__name__, 
            template_folder='templates')

#设置应用密钥(用于session的签名处理)
app.secret_key = '1sjJDJ678HuigHJVBHHJwss='
#设置session的有效期
app.permanent_session_lifetime = timedelta(days=7)

class MobileConverter(BaseConverter):
    regex = '1[3-9]\d{9}$'


app.url_map.converters['mobile'] = MobileConverter


#---------------------------------------——-蓝图--—-----------------------------------------

from user import user_blu

#注册蓝图对象
app.register_blueprint(user_blu)






#__________________________________________练习____________________________________________


#@app.route('/',methods=['GET','POST'])
#def index():
#    return 'Hello Worid'

#@app.route('/useruser/<int:id>',methods=['GET','POST'])
#def user(id):
#    id = str(id)
#    return 'Hello'+id

#@app.route('/mobile/<mobile:M>')
#def mobile(M):
#    return 'Hello Worid' + M

#@app.route('/AAA/',methods=['GET','POST'])
#def AAA():
#    file_obj = request.files.get('AAA')
#    file_obj.save('AAA.jpg')	
#    return 'Hello Worid'

#@app.route('/BBB/',methods=['GET','POST'])
#def BBB():
#    obj = request.data	
#    obj = obj.decode('utf-8')
#    return 'Hello Worid'+ obj


#@app.route('/CCC/',methods=['GET','POST'])
#def CCC():
#    obj = request.form
#    obj = obj.get('AAA')	
#    return 'Hello Worid'+ obj


#@app.route('/DDD/',methods=['GET','POST'])
#def DDD():
#    obj = request.json
#    obj = obj.get('AAA')
#    return 'Hello Worid'+ obj


#@app.route('/EEE/',methods=['GET','POST'])
#def EEE():
#    AAA="欢迎来到魔仙堡"
#    BBB="欢迎来到水帘洞"
#    return render_template('index.html',kw=AAA,KW=BBB)


#@app.route('/FFF/',methods=['GET','POST'])
#def FFF():
#    response = make_response('设置响应头')	
#    response.headers['a'] = 100
#    return response 


#@app.route('/GGG/',methods=['GET','POST'])
#def GGG():
#    dict1 = {'AAA':'AAA','BBB':'100'}	
#    return jsonify(dict1)
   

#@app.route('/HHH/',methods=['GET','POST'])
#def HHH():
#    return redirect('http://www.baidu.com')


#@app.route('/LLL/',methods=['GET','POST'])
#def LLL():
#    return redirect(url_for('HHH'))


#@app.route('/JJJ/',methods=['GET','POST'])
#def JJJ():
#    return redirect(url_for('useruser',id=20))


#@app.route('/KKK/',methods=['GET','POST'])
#def KKK():
#    return '设置状态码',222,{'a':100}


#@app.route('/III/',methods=['GET','POST'])
#def III():
#    is_help = request.cookies.get("is_help")
#    if is_help:
#        return '显示'
#    response = make_response("帮助")
#    response.set_cookie("is_help","1",max_age=86400)
#     
#    删除cookie 本质man-age=0
#    response.delete_cookie('is_help')
#    return response


#-----------------------------------------上下文-------------------------------------------


#上下文变量:不是全局变量,是有适用范围的「某次从请求开始到请求结束」
#请求上下文:记录一些和请求有关的数据 request  session
#应用上下文:记录一些和应用有关的数据 current_app g
#current_app 会自动应用创建的app 对象,想要在其他文件中使用app时,应该通过current_app来代替
#g flask给开发者预留的容器,用于储存一些自定义的数据,每次请求后g变量会重置. 应以场景 1> 钩子和视图传递数据  2>视图函数中多层函数传递


#------------------------------------------钩子--------------------------------------------


#@app.before_request
#def prepare():
#    print("视图函数之前调用,一般完成一些请求准备工作,如参数校验,黑名单,数据统计等")


#@app.after_request
#def process(response):
#    print("视图函数之后调用,一般用户对响应进行统一加工,如设置响应头,包装格式等")
#    return response

#@app.before_first_request
#def initial():
#    print("服务器被第一次请求时调用,一般完成初始化处理,如连接数据库")


#@app.teardown_request
#def error_handle(e):
#    print("请求之后调用,是否出现异常都会执行,一般完成请求的收尾工作,如资源回收,异常统计等")


#---------------------------------------------登陆---------------------------------------------

@app.route('/',methods=['GET','POST'])
def index():
    name = session.get('name')
    if name:
        return '欢迎回来,%s' % name
    else:
        return 'Hello Worid'


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET': 
        #会读取静态文件到内容并且根据文件类型自动设置content-type
        return app.send_static_file('login.html')
       # return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zs' and password == '123':
            #开启session的有效机制,默认为31天
            session.permanent = True
	    
            #记录用户的身份信息,使用session状态保持
            session['name'] = 'zs'
   		
            #删除session数据
            #session.pop('name')

            return '登陆成功'
        else:
            return '登陆失败'


#-----------------------------------------异常-------------------------------------------------


@app.errorhandler(404)
def error_404(e):
    return "错误~~~~~~~~~~~~~~~~~~~~~~~~~"


@app.route('/MMM/',methods=['GET','POST'])
def MMM():
   # abort(404)
    return '主动抛出异常'


#----------------------------------------------------------------------------------------------



















if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)

