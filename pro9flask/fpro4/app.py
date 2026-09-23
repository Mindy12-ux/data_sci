from flask import Flask, request, render_template

app = Flask(__name__);

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/condition')
def condition():
    return render_template('condition.html');

@app.route('/loop')
def loop():
    return render_template('loop.html');


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)