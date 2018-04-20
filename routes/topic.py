from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from utils import log
from routes import *

from models.topic import Topic
from models.board import Board
from models.reply import Reply


main = Blueprint('topic', __name__)


import uuid
csrf_tokens = dict()

@main.route("/")
def index():
    # board_id = 2
    board_id = int(request.args.get('board_id', -1))
    log('request.args', request.args)
    log('ms board_id', board_id)
    if board_id == -1:
        ms = Topic.all()
        log('if ms 查看', ms)
    else:
        ms = Topic.find_all(board_id=board_id)
        log('else ms 查看', ms)
    bs = Board.all()
    u = current_user()
    if u is None:
        return render_template("topic/index.html", ms=ms, bs=bs)

    else:
        token = str(uuid.uuid4())
        csrf_tokens[token] = u.id
        return render_template("topic/index.html", ms=ms, token=token, bs=bs)


@main.route('/<int:id>')
def detail(id):
    m = Topic.get(id)
    # 传递 topic 的所有 reply 到 页面中
    return render_template("topic/detail.html", topic=m)


@main.route("/add", methods=["POST"])
def add():
    u = current_user()
    if u is None:
        abort(403, "Sorry, Don\'t have permission.")
    else:
        form = request.form
        m = Topic.new(form, user_id=u.id)
        log('add m type', type(m),m.id, m)
        return redirect(url_for('.detail', id=m.id))


@main.route("/delete")
def delete():
    u = current_user()
    if u is None:
        abort(403, "Sorry, Don\'t have permission.")
    else:
        # m = Topic.get('user_id')
        id = int(request.args.get('id'))
        token = request.args.get('token')
        ms = Topic.find_by(id=id)
        # 判断 token 是否是我们给的
        if token in csrf_tokens and csrf_tokens[token] == ms.user_id:
            csrf_tokens.pop(token)
            t = Topic.find_by(id=id)
            print('mongo t', t)
            t.delete()
            # 删除评论
            delr = Reply.find_all(topic_id=id)
            print('delr mongo', delr)
            for i in range(len(delr)):
                delr[i].delete()
            return redirect(url_for('.index'))
        else:
            abort(404,"Sorry, not you")



@main.route("/new")
def new():
    u = current_user()
    if u is None:
        abort(403, "Sorry, Don\'t have permission.")
    else:
        bs = Board.all()
        return render_template("topic/new.html", bs=bs)
