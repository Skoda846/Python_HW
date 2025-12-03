"""
Минимальные тесты для проверки CRUD операций
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Subject(Base):
    __tablename__ = "subject"
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String(100))


# Фикстура сессии
@pytest.fixture
def db_session():
    engine = create_engine("postgresql://postgres:12345@localhost:5432/QA")
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    # Очистка тестовых данных
    session.query(Subject).filter(
        Subject.subject_id.in_([101, 102, 103, 104, 105])
    ).delete(synchronize_session=False)
    session.commit()
    session.close()


def test_create(db_session):
    """Тест создания"""
    # Очистка перед тестом
    db_session.query(Subject).filter_by(subject_id=101).delete()
    db_session.commit()

    # Создание
    subject = Subject(subject_id=101, subject_title="Test Create")
    db_session.add(subject)
    db_session.commit()

    # Проверка
    saved = db_session.query(Subject).filter_by(subject_id=101).first()
    assert saved is not None
    assert saved.subject_title == "Test Create"
    print("✅ CREATE тест пройден")


def test_update(db_session):
    """Тест обновления"""
    # Создаем
    subject = Subject(subject_id=102, subject_title="Before Update")
    db_session.add(subject)
    db_session.commit()

    # Обновляем
    subject.subject_title = "After Update"
    db_session.commit()

    # Проверяем
    updated = db_session.query(Subject).filter_by(subject_id=102).first()
    assert updated.subject_title == "After Update"
    print("✅ UPDATE тест пройден")


def test_delete(db_session):
    """Тест удаления"""
    # Создаем
    subject = Subject(subject_id=103, subject_title="To Delete")
    db_session.add(subject)
    db_session.commit()

    # Удаляем
    db_session.delete(subject)
    db_session.commit()

    # Проверяем
    deleted = db_session.query(Subject).filter_by(subject_id=103).first()
    assert deleted is None
    print("✅ DELETE тест пройден")
