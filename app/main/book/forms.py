# -*- coding:utf-8 -*-
from app.models import Book
from flask.ext.pagedown.fields import PageDownField
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Length, DataRequired, Regexp


class EditBookForm(Form):
    isbn = StringField(u"ISBN",
                       validators=[DataRequired(message=u"The forgot to fill in the!"),
                                   Regexp('[0-9]{13,13}', message=u"ISBN must be 13 digits")])
    title = StringField(u"Title",
                        validators=[DataRequired(message=u"The forgot to fill in the!"), Length(1, 128, message=u"A length of 1-128 characters")])
    origin_title = StringField(u"Original name", validators=[Length(0, 128, message=u"A length of 0-128 characters")])
    subtitle = StringField(u"Subtitle", validators=[Length(0, 128, message=u"A length of 0-128 characters")])
    author = StringField(u"Author", validators=[Length(0, 128, message=u"A length of 0-64 characters")])
    translator = StringField(u"Translator",
                             validators=[Length(0, 64, message=u"A length of 0-64 characters")])
    publisher = StringField(u"Public", validators=[Length(0, 64, message=u"A length of 0-64 characters")])
    image = StringField(u"Images address", validators=[Length(0, 128, message=u"A length of 0-128 characters")])
    pubdate = StringField(u"Public Date", validators=[Length(0, 32, message=u"A length of 0-32 characters")])
    tags = StringField(u"Label", validators=[Length(0, 128, message=u"A length of 0-128 characters")])
    pages = IntegerField(u"Pages")
    price = StringField(u"Pricing", validators=[Length(0, 64, message=u"A length of 0-32 characters")])
    binding = StringField(u"Bind", validators=[Length(0, 16, message=u"A length of 0-16 characters")])
    numbers = IntegerField(u"Collection", validators=[DataRequired(message=u"The forgot to fill in the!")])
    summary = PageDownField(u"Introduction")
    catalog = PageDownField(u"Table of Contents")
    submit = SubmitField(u"Save Changes")


class AddBookForm(EditBookForm):
    def validate_isbn(self, filed):
        if Book.query.filter_by(isbn=filed.data).count():
            raise ValidationError(u'Already exists same ISBN,please check carefully whether the book inventory.')


class SearchForm(Form):
    search = StringField(validators=[DataRequired()])
    submit = SubmitField(u"Search")


