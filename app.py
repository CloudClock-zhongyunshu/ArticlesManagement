
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', "POST"])  # 路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
def login():
    if request.method == 'POST':
        if request.form['password'] == '1234':
            return render_template('data_visualization.html')
        else:
            return 'wrong'
    elif request.method == 'GET':
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=8181)
