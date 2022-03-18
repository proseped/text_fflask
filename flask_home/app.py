from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/admin/<int:id>')
def admin(id):
    return 'Hello World!,我是后台管理员%s' % id


if __name__ == '__main__':
    app.debug = True
    app.run()
