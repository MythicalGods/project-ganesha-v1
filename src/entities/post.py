from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4

@dataclass
class Post:
    id: UUID
    title: str
    author: str
    content: str
    date_posted: datetime

    @classmethod
    def new(cls, title, author, content, date_posted):
        return cls(uuid4(), title, author, content, date_posted)

    @classmethod
    def from_dict(cls, adict):
        return cls.new(**adict)

    @property
    def data(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'content': self.content,
            'date_posted': self.date_posted
        }