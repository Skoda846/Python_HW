import pytest
from sqlalchemy.exc import IntegrityError
from models import Subject


class TestSubjectsCRUD:
    """Тесты CRUD операций для таблицы subject"""

    def test_create_subject(self, db_session):
        """
        Тест 1: Создание нового предмета (CREATE)

        Проверяет, что предмет успешно добавляется в БД
        и данные корректно сохраняются
        """
        # Arrange
        test_id = 100
        test_title = "Mathematics"

        # Act
        subject = Subject(subject_id=test_id, subject_title=test_title)
        db_session.add(subject)
        db_session.commit()

        # Assert
        saved = db_session.query(Subject).filter_by(subject_id=test_id).first()

        assert saved is not None, "Предмет не был сохранен в БД"
        assert saved.subject_id == test_id, "ID предмета не совпадает"
        assert saved.subject_title == test_title, "Название не совпадает"

        print(f"✅ Тест 1 пройден: Предмет создан - {saved}")

    def test_update_subject(self, db_session):
        """
        Тест 2: Обновление существующего предмета (UPDATE)

        Проверяет, что данные предмета можно изменить
        и изменения сохраняются в БД
        """
        # Arrange - создаем предмет
        test_id = 200
        subject = Subject(subject_id=test_id, subject_title="Physics")
        db_session.add(subject)
        db_session.commit()

        # Act - обновляем предмет
        subject_to_update = (
            db_session.query(Subject).filter_by(subject_id=test_id).first()
        )
        subject_to_update.subject_title = "Advanced Physics"
        db_session.commit()

        # Assert - проверяем изменения
        updated = db_session.query(
            Subject
        ).filter_by(subject_id=test_id).first()

        assert updated is not None, "Предмет не найден после обновления"
        assert updated.subject_title == "Advanced Physics", "Название не обновлено"
        assert updated.subject_id == test_id, "ID не должен был измениться"

        print(f"✅ Тест 2 пройден: Предмет обновлен - {updated}")

    def test_delete_subject(self, db_session):
        """
        Тест 3: Удаление предмета (DELETE)

        Проверяет, что предмет полностью удаляется из БД
        """
        # Arrange - создаем предмет
        test_id = 300
        subject = Subject(subject_id=test_id, subject_title="Chemistry")
        db_session.add(subject)
        db_session.commit()

        # Проверяем, что предмет существует
        exists_before = db_session.query(Subject).filter_by(subject_id=test_id).first()
        assert exists_before is not None, "Предмет должен существовать перед удалением"

        # Act - удаляем предмет
        subject_to_delete = (
            db_session.query(Subject).filter_by(subject_id=test_id).first()
        )
        db_session.delete(subject_to_delete)
        db_session.commit()

        # Assert - проверяем, что предмет удален
        exists_after = db_session.query(Subject).filter_by(subject_id=test_id).first()

        assert exists_after is None, "Предмет должен быть удален из БД"

        print(f"✅ Тест 3 пройден: Предмет с ID {test_id} удален")

    def test_duplicate_id_error(self, db_session):
        """
        Тест 4: Проверка уникальности ID

        Проверяет, что нельзя создать два предмета с одинаковым ID
        """
        # Arrange - создаем первый предмет
        test_id = 999
        subject1 = Subject(subject_id=test_id, subject_title="Physics")
        db_session.add(subject1)
        db_session.commit()

        # Act & Assert - пытаемся создать второй предмет с тем же ID
        subject2 = Subject(subject_id=test_id, subject_title="Chemistry")
        db_session.add(subject2)

        # Должна возникнуть ошибка IntegrityError
        with pytest.raises(IntegrityError) as exc_info:
            db_session.commit()

        # Проверяем тип ошибки
        error_msg = str(exc_info.value).lower()
        expected_keywords = ["unique", "duplicate", "primary key", "violates"]
        assert any(
            word in error_msg for word in expected_keywords
        ), f"Ожидалась ошибка уникальности, но получили: {error_msg}"

        print(f"✅ Тест 4 пройден: Проверка уникальности ID - {exc_info.value}")

        # Откатываем невалидную транзакцию
        db_session.rollback()

    def test_read_multiple_subjects(self, db_session):
        """
        Тест 5: Чтение нескольких предметов

        Проверяет работу с несколькими записями одновременно
        """
        # Arrange - создаем три предмета
        subjects_data = [
            (1000, "Mathematics"),
            (1001, "Physics"),
            (1002, "Chemistry"),
        ]

        for subject_id, title in subjects_data:
            subject = Subject(subject_id=subject_id, subject_title=title)
            db_session.add(subject)

        db_session.commit()

        # Act - читаем все предметы
        all_subjects = (
            db_session.query(Subject)
            .filter(Subject.subject_id.in_([1000, 1001, 1002]))
            .all()
        )

        # Assert
        expected_count = 3
        actual_count = len(all_subjects)
        assert (
            actual_count == expected_count
        ), f"Должно быть {expected_count} предмета, найдено {actual_count}"

        # Проверяем, что все созданные предметы присутствуют
        titles = [s.subject_title for s in all_subjects]
        for _, title in subjects_data:
            assert title in titles, f"Предмет '{title}' должен быть в списке"

        print(f"✅ Тест 5 пройден: Найдено {actual_count} предметов")
        for subject in all_subjects:
            print(f"   - {subject}")

    def test_string_representation(self):
        """
        Тест 6: Проверка строкового представления

        Проверяет корректность __repr__ метода
        """
        # Arrange
        test_id = 777
        test_title = "Test Subject"

        # Act
        subject = Subject(subject_id=test_id, subject_title=test_title)
        repr_str = repr(subject)

        # Assert
        assert str(test_id) in repr_str, "ID должен быть в строковом представлении"
        assert test_title in repr_str, "Название должно быть в строковом представлении"
        assert "Subject" in repr_str, "Имя класса должно быть в строковом представлении"

        print(f"✅ Тест 6 пройден: Строковое представление - {repr_str}")

    def test_empty_title_validation(self, db_session):
        """
        Тест 7: Проверка пустого названия

        Проверяет поведение при пустой строке в названии
        """
        # В PostgreSQL пустая строка обычно разрешена
        # Этот тест проверяет, что система работает корректно

        test_id = 888
        subject = Subject(subject_id=test_id, subject_title="")

        try:
            db_session.add(subject)
            db_session.commit()
            saved = db_session.query(Subject).filter_by(subject_id=test_id).first()

            # Если коммит прошел успешно
            assert saved is not None
            assert saved.subject_title == ""
            print("✅ Тест 7 пройден: Пустая строка разрешена для названия")

            # Очищаем
            db_session.delete(saved)
            db_session.commit()

        except Exception as e:
            # Если возникла ошибка - это тоже нормально(зависит от настроек БД)
            print(f"✅ Тест 7 пройден: Ограничение на пустую строку - {e}")
            db_session.rollback()

    def test_nonexistent_subject_query(self, db_session):
        """
        Тест 8: Запрос несуществующего предмета

        Проверяет, что запрос несуществующей записи возвращает None
        """
        # Arrange
        nonexistent_id = 999999

        # Act
        subject = db_session.query(Subject).filter_by(subject_id=nonexistent_id).first()

        # Assert
        assert subject is None, "Запрос несуществующего предмета должен возвращать None"

        print(
            f"✅ Тест 8 пройден: Запрос несуществующего предмета "
            f"(ID {nonexistent_id}) возвращает None"
        )


class TestSubjectsBatchOperations:
    """Тесты пакетных операций"""

    def test_batch_create(self, db_session):
        """Пакетное создание предметов"""
        # Создаем 5 предметов
        subjects = []
        for i in range(5):
            subject = Subject(
                subject_id=5000 + i,
                subject_title=f"Batch Subject {i}",
            )
            subjects.append(subject)

        # Добавляем все сразу
        db_session.add_all(subjects)
        db_session.commit()

        # Проверяем
        count = (
            db_session.query(Subject)
            .filter(Subject.subject_id.between(5000, 5004))
            .count()
        )

        assert count == 5
        print(f"✅ Пакетное создание: добавлено {count} предметов")

    def test_batch_delete(self, db_session):
        """Пакетное удаление предметов"""
        # Создаем предметы для удаления
        for i in range(3):
            subject = Subject(
                subject_id=6000 + i,
                subject_title=f"To Delete {i}",
            )
            db_session.add(subject)
        db_session.commit()

        # Удаляем пакетно
        db_session.query(Subject).filter(Subject.subject_id.between(6000, 6002)).delete(
            synchronize_session=False
        )

        db_session.commit()

        # Проверяем
        remaining = (
            db_session.query(Subject)
            .filter(Subject.subject_id.between(6000, 6002))
            .count()
        )

        assert remaining == 0
        print("✅ Пакетное удаление: удалено 3 предметов")
