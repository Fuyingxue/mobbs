from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *
from models.mail import Mail


main = Blueprint('mail', __name__)


@main.route("/add", methods=["POST"])
def add():
    u = current_user()
    if u is None:
        abort(403, "Sorry, you don\'t have permission.")
    else:
        form = request.form
        mail = Mail.new(form)
        mail.set_sender(current_user().id)
        return redirect(url_for(".index"))
        ...


@main.route("/", methods=["GET"])
def index():
    u = current_user()
    if u is None:
        # return redirect(url_for('.index'))
        abort(403, "Sorry, you don\'t have permission.")
    else:
        send_mail = Mail.find_all(sender_id=u.id)
        received_mail = Mail.find_all(receiver_id=u.id)
        return render_template("mail/index.html", sends= send_mail, receives = received_mail)


@main.route("/view/<int:id>")
def view(id):
    mail = Mail.find(id)

    if current_user().id == mail.receiver_id:
        mail.mark_read()
    if current_user().id in [mail.receiver_id, mail.sender_id]:
        return render_template("mail/detail.html", mail=mail)
    else:
        return redirect(url_for(".index"))

