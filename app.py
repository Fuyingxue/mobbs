from flask import Flask

import config


# web framework
# web application
# __main__
app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = config.secret_key


"""
在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
蓝图可以拥有自己的静态资源路径、模板路径
"""
# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
from routes.index import main as index_routes
from routes.topic import main as topic_routes
from routes.reply import main as reply_routes
from routes.board import main as board_routes
from routes.mail import main as mail_routes
app.register_blueprint(index_routes, url_prefix='/py')
app.register_blueprint(topic_routes, url_prefix='/py/topic')
app.register_blueprint(reply_routes, url_prefix='/py/reply')
app.register_blueprint(board_routes, url_prefix='/py/board')
app.register_blueprint(mail_routes, url_prefix='/py/mail')



# 运行代码
if __name__ == '__main__':
    # debug 模式可以自动加载对代码的变动, 不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=2001,
    )
    app.run(**config)