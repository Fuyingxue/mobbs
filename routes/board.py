from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.board import Board


main = Blueprint('board', __name__)

# 这是一个要求管理员权限的函数
def admin_required():
    u = current_user()
    # u 不存在或者不是管理员
    if u is None or not u.is_admin():
        print('现在访问的是', request.url, u)
        abort(403, "Sorry, Don\'t ")

# 一次性给蓝图中的每个路由加上管理权限验证
# 这样就不用手动去给每个函数分别加这个验证了
main.before_request(admin_required)

@main.route("/admin")
def index():
    ms = Board.all()
    return render_template('board/admin_index.html', board=ms)
    ...


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    m = Board.new(form)
    return redirect(url_for('topic.index'))


@main.route("/edit/<int:id>")
def edit(id):
    t = Board.find_by(id=id)
    return render_template('board/admin_edit.html', board=t)

@main.route("/update/<int:id>", methods=["POST"])
def update(id):
    form = request.form
    t = Board.find_by(id=id)
    t.title = form.get('title')
    t.save()
    return redirect(url_for('.index'))

