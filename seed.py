from random import randint, choice, sample
from datetime import datetime, timedelta

from faker import Faker
from sqlalchemy import delete

from database import SessionLocal
from models import Group, Teacher, Student, Subject, Grade

fake = Faker("uk_UA")


def seed_database():
    session = SessionLocal()

    try:
        # Очищення таблиць перед новим заповненням
        session.execute(delete(Grade))
        session.execute(delete(Student))
        session.execute(delete(Subject))
        session.execute(delete(Teacher))
        session.execute(delete(Group))
        session.commit()

        # Створення груп
        groups = [
            Group(name="Група-101"),
            Group(name="Група-102"),
            Group(name="Група-103"),
        ]
        session.add_all(groups)
        session.commit()

        # Створення викладачів
        teachers = [Teacher(fullname=fake.name()) for _ in range(randint(3, 5))]
        session.add_all(teachers)
        session.commit()

        # Створення предметів
        subject_names = [
            "Математичний аналіз",
            "Лінійна алгебра",
            "Програмування Python",
            "Бази даних",
            "Алгоритми",
            "Фізика",
            "Англійська мова",
            "Веброзробка",
        ]

        selected_subjects = sample(subject_names, randint(5, 8))
        subjects = [Subject(name=name, teacher_id=choice(teachers).id) for name in selected_subjects]
        session.add_all(subjects)
        session.commit()

        # Створення студентів
        students = [
            Student(fullname=fake.name(), group_id=choice(groups).id)
            for _ in range(randint(30, 50))
        ]
        session.add_all(students)
        session.commit()

        # Створення оцінок
        start_date = datetime(2025, 9, 1)
        grades = []

        for student in students:
            student_subjects = sample(subjects, randint(3, len(subjects)))
            grades_count = randint(10, 20)

            for _ in range(grades_count):
                subject = choice(student_subjects)
                random_days = randint(0, 250)

                grade = Grade(
                    student_id=student.id,
                    subject_id=subject.id,
                    grade=randint(60, 100),
                    grade_date=(start_date + timedelta(days=random_days)).date(),
                )
                grades.append(grade)

        session.add_all(grades)
        session.commit()

        print("Базу даних успішно заповнено випадковими даними")

    except Exception as e:
        session.rollback()
        print(f"Помилка під час заповнення: {e}")
        raise

    finally:
        session.close()


if __name__ == "__main__":
    seed_database()