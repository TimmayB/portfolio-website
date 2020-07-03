from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.htm')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.htm')

if __name__ == '__main__':
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.run('127.0.0.1', port=5000, debug=True)