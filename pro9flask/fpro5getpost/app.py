from flask import Flask, request, render_template, Request

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/get_form')
def get_form():
    return render_template('get_form.html');

@app.route('/post_form')
def post_form():
    return render_template('post_form.html');

@app.route('/get_result')
def get_result():
    name = request.args.get('username');  # get방식 요청 자료 받기, 자료를 받는 주체는 서버
    # get 방식일때는 args로 값을 받는다
    age = request.args.get('age');  # '23'문자 타입으로 받기, 연산을 하고 싶으면 숫자로 바꿔줘야 됨
    age = age + '살';
    return render_template('get_result.html', name = name, age = age);
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)