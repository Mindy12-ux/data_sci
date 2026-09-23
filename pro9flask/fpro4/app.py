from flask import Flask, request, render_template

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/condition')
def condition():
    score = 85;
    return render_template('condition.html',score = score);

@app.route('/loop')
def loop():
    users = ['김찬우','김민채','제임스']
    return render_template('loop.html', users=users);

@app.route('/filter')
def filter():
    message = "hello flask jinja2";
    price = 1234534564534;
    return render_template('filter.html', message = message, price=price);

# jinja2에는 기본적으로 1000 단위 콤마가 없으므로, 직접 구현하거나 format을 사용해야 한다.
@app.template_filter('format')
def format_number(value):
    return format(value, ",")    # 숫자 세 자리마다 콤마가 찍힘

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)