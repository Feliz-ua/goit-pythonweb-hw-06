from sqlalchemy import func, desc, and_

from database import SessionLocal
from models import Student, Group, Teacher, Subject, Grade


# 1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів
def select_1():
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.fullname,
                func.round(func.avg(Grade.grade), 2).label("avg_grade")
            )
            .join(Grade, Grade.student_id == Student.id)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .limit(5)
            .all()
        )
        return result
    finally:
        session.close()


# 2. Знайти студента із найвищим середнім балом з певного предмета
def select_2(subject_id: int):
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.fullname,
                func.round(func.avg(Grade.grade), 2).label("avg_grade")
            )
            .join(Grade, Grade.student_id == Student.id)
            .filter(Grade.subject_id == subject_id)
            .group_by(Student.id)
            .order_by(desc("avg_grade"))
            .first()
        )
        return result
    finally:
        session.close()


# 3. Знайти середній бал у групах з певного предмета
def select_3(subject_id: int):
    session = SessionLocal()
    try:
        result = (
            session.query(
                Group.name,
                func.round(func.avg(Grade.grade), 2).label("avg_grade")
            )
            .select_from(Group)
            .join(Student, Student.group_id == Group.id)
            .join(Grade, Grade.student_id == Student.id)
            .filter(Grade.subject_id == subject_id)
            .group_by(Group.id)
            .all()
        )
        return result
    finally:
        session.close()


# 4. Знайти середній бал на потоці (по всій таблиці оцінок)
def select_4():
    session = SessionLocal()
    try:
        result = session.query(
            func.round(func.avg(Grade.grade), 2)
        ).scalar()
        return result
    finally:
        session.close()


# 5. Знайти які курси читає певний викладач
def select_5(teacher_id: int):
    session = SessionLocal()
    try:
        result = (
            session.query(Subject.name)
            .filter(Subject.teacher_id == teacher_id)
            .all()
        )
        return result
    finally:
        session.close()


# 6. Знайти список студентів у певній групі
def select_6(group_id: int):
    session = SessionLocal()
    try:
        result = (
            session.query(Student.fullname)
            .filter(Student.group_id == group_id)
            .all()
        )
        return result
    finally:
        session.close()


# 7. Знайти оцінки студентів у окремій групі з певного предмета
def select_7(group_id: int, subject_id: int):
    session = SessionLocal()
    try:
        result = (
            session.query(
                Student.fullname,
                Grade.grade,
                Grade.grade_date
            )
            .join(Grade, Grade.student_id == Student.id)
            .filter(
                and_(
                    Student.group_id == group_id,
                    Grade.subject_id == subject_id
                )
            )
            .order_by(Student.fullname)
            .all()
        )
        return result
    finally:
        session.close()


# 8. Знайти середній бал, який ставить певний викладач зі своїх предметів
def select_8(teacher_id: int):
    session = SessionLocal()
    try:
        result = (
            session.query(
                func.round(func.avg(Grade.grade), 2).label("avg_grade")
            )
            .select_from(Grade)
            .join(Subject, Subject.id == Grade.subject_id)
            .filter(Subject.teacher_id == teacher_id)
            .scalar()
        )
        return result
    finally:
        session.close()


# 9. Знайти список курсів, які відвідує певний студент
def select_9(student_id: int):
    session = SessionLocal()
    try:
        result = (
            session.query(Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .filter(Grade.student_id == student_id)
            .distinct()
            .all()
        )
        return result
    finally:
        session.close()


# 10. Список курсів, які певному студентові читає певний викладач
def select_10(student_id: int, teacher_id: int):
    session = SessionLocal()
    try:
        result = (
            session.query(Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .filter(
                and_(
                    Grade.student_id == student_id,
                    Subject.teacher_id == teacher_id
                )
            )
            .distinct()
            .all()
        )
        return result
    finally:
        session.close()