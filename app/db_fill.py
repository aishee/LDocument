# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Book, Log, Role

app_ctx = app.app_context()
app_ctx.push()
db.create_all()
Role.insert_roles()

admin = User(name=u'aishee', email='aishee@aishee.net', password='24111408', major='administrator',
             headline=u"A temporary administrator", about_me=u"He graduated from the Department of Management,Interested in reading,Therefore, part-time librarian.")
user1 = User(name=u'test1', email='akarin@Gmail.com', password='123456', major='Computer Science', headline=u"Ordinary student")
user2 = User(name=u'test', email='test@test.com', password='123456')
user3 = User(name=u'test2', email='x@a.com', password='123456')
user4 = User(name=u'test3', email='x@yahoo.com', password='123456')

book1 = Book(title=u"Flask Web", subtitle=u"XXX", author=u"Miguel Grinberg", isbn='9787115373991',
             tags_string=u"xx,xx,xxx", image='http://img3.douban.com/lpic/s27906700.jpg',
             summary=u"""
# xx.

* xx;
* xx;
* xx;
* xx;
* xx;
* xx;
* xx;
* xx;
""")
book2 = Book(title=u"xx", subtitle=u"xx xx", author=u"侯捷", isbn='9787560926995',
             tags_string=u"xx,xx,C++", image='http://img3.doubanio.com/lpic/s1092076.jpg',
             summary=u"""* xx
* xx Black xx xx/xx xx""")
book3 = Book(title=u"xx", subtitle=u"xx",
             author="Alfred V. Aho / Monica S.Lam / Ravi Sethi / Jeffrey D. Ullman ", isbn="9787111251217",
             tags_string=u"xx,xx", image='http://img3.douban.com/lpic/s3392161.jpg',
             summary=u"""* xx
* xx""")
book4 = Book(title=u"xx", author="Randal E.Bryant / David O'Hallaron", isbn="9787111321330",
             tags_string=u"xx,xx", image='http://img3.douban.com/lpic/s4510534.jpg',
             summary=u"""* xx/xx
* xx
* xx""")
book5 = Book(title=u"xx#", subtitle=u"C#5.xx", author=u"xx (Joseph Albahari) / xx (Ben Albahari)",
             isbn="9787517010845", tags_string=u"xx,xx,C#", image='http://img3.douban.com/lpic/s28152290.jpg',
             summary=u"""* xx#——c#5.xx.xx.xx#5.xx#4.xx
* xx#——c#5.xx#xx#xx#xx""")
book6 = Book(title=u"xx",
             author="Thomas H.Cormen / Charles E.Leiserson / Ronald L.Rivest / Clifford Stein",
             isbn="9787111187776", tags_string=u"xx,xx", image='http://img3.doubanio.com/lpic/s1959967.jpg',
             summary=u"xx")
logs = [Log(user1, book2), Log(user1, book3), Log(user1, book4), Log(user1, book6),
        Log(user2, book1), Log(user2, book3), Log(user2, book5),
        Log(user3, book2), Log(user3, book5)]

db.session.add_all([admin, user1, user2, user3, user4, book1, book2, book3, book4, book5, book6] + logs)
db.session.commit()

app_ctx.pop()
