import sys
from re import match

from flask import Flask, render_template, request, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class RegxConverters(BaseConverter):
    regex = r'1[3-9]\d{9}$'
app.url_map.converters['regex1'] = RegxConverters

@app.route('/index/<regex1:args>')
def index(args):
    # return render_template('index.html')
    print(args)
    return 'hehe'
@app.route('/',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('manager.html')
    user = request.form.get('user')
    password = request.form.get("pwd")
    if user =='majun' and password =='123456':
        return redirect('https://www.bilibili.com/')
    return render_template('login.html', context={'error': '用户名或者密码错误'})




if __name__ == '__main__':
    app.run(host="0.0.0.0")
print(sys.path)

# from itertools import chain
# def fun1(x):
#     return x +1
# def fun2(x):
#     return x * 2
# new_func = chain([fun1],[fun2])
# for fun in new_func:
#     print(fun(2))
#
#
# result = list(map(fun1,[1,2,3,4]))
# print(result)





