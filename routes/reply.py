from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *


from models.reply import Reply


main = Blueprint('reply', __name__)


@main.route("/add", methods=["POST"])
def add():
    u = current_user()
    if u is None:
        abort(403, "Sorry, you don\'t have permission.")
    else:
        form = request.form
        m = Reply.new(form, user_id=u.id)
        return redirect(url_for('topic.detail', id=m.topic_id))
