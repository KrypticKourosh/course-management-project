from datetime import date, time

from accounts.models import User
from courses.models import Category, Course, Session
from enrollments.models import Enrollment


def user(username, role):
    u, created = User.objects.get_or_create(username=username, defaults={'role': role})
    if created:
        u.set_password('test1234')
        u.save()
    return u


t1, t2 = user('teacher1', 'instructor'), user('teacher2', 'instructor')
s1, s2, s3 = user('student1', 'student'), user('student2', 'student'), user('student3', 'student')

prog, _ = Category.objects.get_or_create(name='برنامه‌نویسی')
lang, _ = Category.objects.get_or_create(name='زبان')
design, _ = Category.objects.get_or_create(name='طراحی')

data = [
    ('آموزش پایتون', prog, t1, 20, 500000),
    ('جنگو مقدماتی', prog, t1, 15, 700000),
    ('انگلیسی مکالمه', lang, t2, 25, 0),
    ('طراحی UI', design, t2, 10, 400000),
]
for title, cat, teacher, cap, price in data:
    c, created = Course.objects.get_or_create(
        title=title,
        defaults=dict(description='توضیحات ' + title, category=cat, instructor=teacher,
                      capacity=cap, price=price, start_date=date(2026, 12, 1), end_date=date(2027, 2, 1)),
    )
    if created:
        for i in range(1, 4):
            Session.objects.create(course=c, title=f'جلسه {i}', date=date(2026, 12, i * 7),
                                   start_time=time(17, 0), end_time=time(19, 0))

python_course = Course.objects.get(title='آموزش پایتون')
for s in (s1, s2):
    Enrollment.objects.get_or_create(student=s, course=python_course)