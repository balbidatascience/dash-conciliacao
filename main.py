from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Pagina inicial'

@app.route('/conciliacao')
def conciliacao():
    return '<h2>Monitor Conciliação</h2>'


if __name__ == '__main__':
    app.run(debug=True)
