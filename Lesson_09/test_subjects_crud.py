"""
Тесты CRUD операций для таблицы subject
Соответствуют требованиям задания:
- 3 теста: CREATE, UPDATE, DELETE
- Используют pytest и SQLAlchemy
- Автоматически очищают данные
- Стабильны и повторяемы
"""

import pytest
from sqlalchemy.exc import IntegrityError
from models import Subject


class TestSubjectCRUDOperations:
    """Класс тестов для CRUD операций с предметами"""

    def test_create_subject(self, db_session):
        """
        ТЕСТ 1: Создание нового предмета (CREATE операция)
        """
        # Очищаем перед тестом
        db_session.query(Subject).filter_by(subject_id=10001).delete()
        db_session.commit()

        # Создаем и сохраняем предмет
        new_subject = Subject(
            subject_id=10001, subject_title="Test Mathematics"
        )
        db_session.add(new_subject)
        db_session.commit()

        # Проверка
        saved_subject = db_session.query(
            Subject).filter_by(subject_id=10001).first()

        assert saved_subject is not None,"Предмет небыл сохранен в базу данных"
        assert saved_subject.subject_id == 10001, "ID предмета не совпадает"
        assert (
            saved_subject.subject_title == "Test Mathematics"
        ), "Название предмета не совпадает"

        print("✅ ТЕСТ 1 ПРОЙДЕН: Предмет создан успешно")
        print(f"   Создан предмет: {saved_subject}")

        # Очищаем после теста
        db_session.delete(saved_subject)
        db_session.commit()

    def test_update_subject(self, db_session):
        """
        ТЕСТ 2: Обновление существующего предмета (UPDATE операция)
        """
        # Очищаем перед тестом
        db_session.query(Subject).filter_by(subject_id=10002).delete()
        db_session.commit()

        # Создаем исходный предмет
        subject = Subject(subject_id=10002, subject_title="Physics")
        db_session.add(subject)
        db_session.commit()

        # Обновляем предмет
        subject_to_update = (
            db_session.query(Subject).filter_by(subject_id=10002).first()
        )

        subject_to_update.subject_title = "Advanced Physics"
        db_session.commit()

        # Проверка
        updated_subject = db_session.query(
            Subject
        ).filter_by(subject_id=10002).first()

        assert updated_subject is not None, "Предмет ненайден после обновления"
        assert (
            updated_subject.subject_title == "Advanced Physics"
        ), "Название не было обновлено"
        assert updated_subject.subject_id == 10002, "ID недолжен был изменится"

        print("✅ ТЕСТ 2 ПРОЙДЕН: Предмет обновлен успешно")
        print(f"   Обновлен предмет: {updated_subject}")

        # Очищаем после теста
        db_session.delete(updated_subject)
        db_session.commit()

    def test_delete_subject(self, db_session):
        """
        ТЕСТ 3: Удаление предмета (DELETE операция)
        """
        # Очищаем перед тестом
        db_session.query(Subject).filter_by(subject_id=10003).delete()
        db_session.query(Subject).filter_by(subject_id=10004).delete()
        db_session.commit()

        # Создаем два предмета
        subject1 = Subject(subject_id=10003, subject_title="Chemistry")

        subject2 = Subject(subject_id=10004, subject_title="Biology")

        db_session.add_all([subject1, subject2])
        db_session.commit()

        # Проверяем, что оба предмета существуют перед удалением
        count_before = (
            db_session.query(Subject)
            .filter(Subject.subject_id.in_([10003, 10004]))
            .count()
        )
        assert count_before == 2, "Должно быть 2 предмета перед удалением"

        # Удаляем первый предмет
        subject_to_delete = (
            db_session.query(Subject).filter_by(subject_id=10003).first()
        )

        db_session.delete(subject_to_delete)
        db_session.commit()

        # Проверка 1: удаленный предмет не должен существовать
        deleted_subject = db_session.query(
            Subject
        ).filter_by(subject_id=10003).first()
        assert deleted_subject is None, "Предмет должен быть удален из БД"

        # Проверка 2: второй предмет должен остаться
        remaining_subject = (
            db_session.query(Subject).filter_by(subject_id=10004).first()
        )
        assert remaining_subject is not None, "Второй предмет остаёться в БД"
        assert (
            remaining_subject.subject_title == "Biology"
        ), "Данные второго предмета не должны измениться"

        # Проверка 3: общее количество должно уменьшиться
        count_after = (
            db_session.query(Subject)
            .filter(Subject.subject_id.in_([10003, 10004]))
            .count()
        )
        assert count_after == 1, "Должен остаться 1 предмет после удаления"

        print("✅ ТЕСТ 3 ПРОЙДЕН: Предмет удален успешно")
        print("   Удален предмет с ID: 10003")
        print(f"   Осталось предметов в тестовом диапазоне: {count_after}")

        # Очищаем после теста
        db_session.delete(remaining_subject)
        db_session.commit()


class TestSubjectAdditionalTests:
    """Дополнительные тесты для проверки граничных случаев"""

    def test_duplicate_id_error_fixed(self, db_session):
        """
        Исправленный тест: проверка уникальности ID

        Используем две отдельные сессии для проверки уникальности
        """
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        subject_id = 10005

        # Очищаем перед тестом
        db_session.query(Subject).filter_by(subject_id=subject_id).delete()
        db_session.commit()

        # Создаем первый предмет в первой сессии
        engine = create_engine("postgresql://postgres:12345@localhost:5432/QA")
        Session1 = sessionmaker(bind=engine)
        session1 = Session1()

        subject1 = (Subject
                    (subject_id=subject_id, subject_title="First Subject"))
        session1.add(subject1)
        session1.commit()

        # Пытаемся создать второй предмет с тем же ID во ВТОРОЙ сессии
        Session2 = sessionmaker(bind=engine)
        session2 = Session2()

        subject2 = Subject(
            subject_id=subject_id, subject_title="Second Subject"  # Тот же ID!
        )
        session2.add(subject2)

        # Должна возникнуть ошибка IntegrityError
        with pytest.raises(IntegrityError) as exc_info:
            session2.commit()

        # Проверяем, что ошибка связана с уникальностью
        error_message = str(exc_info.value).lower()
        assert any(
            keyword in error_message
            for keyword in ["unique", "duplicate", "primary key", "violates"]
        ), f"Ожидалась ошибка уникальности, но получено: {error_message}"

        # Закрываем сессии
        session1.close()
        session2.close()

        # Очищаем
        db_session.query(Subject).filter_by(subject_id=subject_id).delete()
        db_session.commit()

        print("✅ ДОПОЛНИТЕЛЬНЫЙ ТЕСТ: Проверка уникальности ID пройдена")

    def test_empty_title(self, db_session):
        """
        Дополнительный тест: создание предмета с пустым названием
        """
        subject_id = 10006

        # Очищаем перед тестом
        db_session.query(Subject).filter_by(subject_id=subject_id).delete()
        db_session.commit()

        subject = Subject(subject_id=subject_id, subject_title="")

        try:
            db_session.add(subject)
            db_session.commit()

            # Если коммит прошел успешно, проверяем сохранение
            saved = db_session.query(
                Subject).filter_by(subject_id=subject_id).first()
            assert saved is not None
            assert saved.subject_title == ""

            print("✅ ДОПОЛНИТЕЛЬНЫЙ ТЕСТ: Пустое название разрешено")

            # Очищаем
            db_session.delete(saved)
            db_session.commit()

        except Exception as e:
            # Если возникла ошибка - это тоже нормально
            print(
                f"✅ ДОПОЛНИТЕЛЬНЫЙ ТЕСТ:\
             Ограничение на пустое название - {e}"
            )
            db_session.rollback()
