from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.getcwd())


@app.route('/')
def index():
    return render_template('index.html', welcome="欢迎来到AmazingCoding官网")


@app.route('/download')
def download():
    return render_template('download.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
