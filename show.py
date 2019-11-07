# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 11:32
# @Author  : Kelly
# @Email   : 289786098@qq.com
# @File    : show.py
# @Description:讲多分类的结果展示出来
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash,jsonify
import setproctitle

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
app = Flask(__name__, instance_path='/Users/henry/Documents/application/newsExtract/instance/folder')
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/show')
def show():
    return render_template('show.html')


@app.route('/bullet.js')
def jsshow():
    return render_template('bullet.js')

@app.route('/bullets.json')
def jsonfile():
    return render_template('bullets.json')

@app.route('/bullets1.json')
def jsonfile1():
    return render_template('bullets1.json')


if __name__ == '__main__':
    setproctitle.setproctitle('bertshow')
    app.run(
        host='0.0.0.0',
        port=9990,
        debug=True#Flask配置文件在开发环境中，在生产线上的代码是绝对不允许使用debug模式，正确的做法应该写在配置文件中，这样我们只需要更改配置文件即可但是你每次修改代码后都要手动重启它。这样并不够优雅，而且 Flask 可以做到更好。如果你启用了调试支持，服务器会在代码修改后自动重新载入，并在发生错误时提供一个相当有用的调试器。
    )
