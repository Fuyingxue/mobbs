import time
from models import Model


class Reply(Model):
    __fields__ = Model.__fields__ + [
        ('content', str, ''),
        ('topic_id', int, -1),
        ('receiver_id', int, -1),
        ('user_id', int, -1)
    ]

    def user(self):
        from .user import User
        u = User.find(self.user_id)
        return u

    def set_user_id(self, user_id):
        self.user_id = user_id
        self.save()

    def ct(self):
        format = '%Y/%m/%d %H:%M:%S'
        value = time.localtime(self.created_time)
        dt = time.strftime(format, value)
        return dt
