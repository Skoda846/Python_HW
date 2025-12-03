"""
Модель данных для таблицы subject
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Subject(Base):
    """Модель предмета/дисциплины"""

    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String(100), nullable=False)

    def __repr__(self):
        return f"Subject(id={self.subject_id}, title='{self.subject_title}')"
