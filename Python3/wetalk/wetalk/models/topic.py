# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String

from .base import Base
from .base import db


class Topic(Base):
    __tablename__ = 'topic'

    id = Column(Integer, primary_key=True)
    name = Column(String(24), unique=True, index=True, nullable=False)
    description = Column(String(255), default='')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Topic:{}>'.format(self.name)

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description
        }

    @staticmethod
    def fake_test():
        db.session.add_all([Topic('数码', ''),
                            Topic('健身', ''),
                            Topic('编程', ''),
                            Topic('旅游', ''),
                            Topic('工作', '')])
        db.session.commit()