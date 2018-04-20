import time
from models import Model
from models.user import User
from utils import log


class Topic(Model):
    __fields__ = Model.__fields__ + [
        ('content', str, ''),
        ('title', str, ''),
        ('user_id', int, -1),
        ('board_id', int, -1),
        ('views', int, 0)
    ]

    @classmethod
    def get(cls, id):
        m = cls.find_by(id=id)
        m.views += 1
        m.save()
        return m

    def replies(self):
        from .reply import Reply
        ms = Reply.find_all(topic_id=self.id)
        return ms

    def board(self):
        from .board import Board
        m = Board.find(self.board_id)
        return m

    def user(self):
        u = User.find(id = self.user_id)
        return u

    def ct(self):
        format = '%Y/%m/%d %H:%M:%S'
        value = time.localtime(self.created_time)
        dt = time.strftime(format, value)
        return dt
