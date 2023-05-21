from flask import Flask

app = Flask(__name__)


@app.route('/')
def test():  # put application's code here
    return 'test,failed!'


if __name__ == '__main__':
    app.run()
