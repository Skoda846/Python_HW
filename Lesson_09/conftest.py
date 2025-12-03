"""
Конфигурация тестов и фикстуры для pytest
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Subject, Base

# Конфигурация подключения к базе данных
DATABASE_URL = "postgresql://postgres:12345@localhost:5432/QA"


@pytest.fixture(scope="session")
def engine():
    """Создание движка базы данных для всей сессии тестов"""
    engine = create_engine(DATABASE_URL, echo=False)

    # Создаем таблицы, если они не существуют
    Base.metadata.create_all(engine)

    return engine


@pytest.fixture(scope="function")
def db_session(engine):
    """
    Создание сессии БД для каждого теста
    Автоматически очищает тестовые данные после теста
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    # Очищаем тестовые данные перед тестом
    cleanup_test_data(session)

    yield session

    # Очищаем тестовые данные после теста
    cleanup_test_data(session)
    session.close()


def cleanup_test_data(session):
    """Удаление тестовых данных из таблицы subject"""
    try:
        # Удаляем записи с тестовыми ID
        session.query(Subject).filter(Subject.subject_id.between(
            10000, 20000)).delete(
            synchronize_session=False
        )
        session.commit()
    except Exception as e:
        session.rollback()
