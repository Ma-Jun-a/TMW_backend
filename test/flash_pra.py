from flask import Flask, request, render_template, flash, redirect, get_flashed_messages, session, make_response

app = Flask(__name__)
app.secret_key = 'fuck'

# @app.before_request
# def login_require(*args,**kwargs):
#
#     user = session.get('user')
#     if not user:
#         return render_template('login.html')
#     else: return None

@app.route('/')
def index():

    val = request.args.get('v')
    if val:
        return render_template('index.html')
        # return 'index'
    flash('connect error')
    return redirect('/error')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    user = request.form.get('user')
    password = request.form.get("pwd")
    if user =='majun' and password =='123456':
        session['user'] = 'majun'

        return render_template('manager.html')
    return render_template('login.html', context={'error': '用户名或者密码错误'})

@app.route('/error')
def error():
    data = get_flashed_messages()
    return "错误提示：%s" % data

if __name__ == '__main__':
    """flash 的实现是基于session的所以就和用户相关的操作"""
    app.run()



