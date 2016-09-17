# -*- coding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired


class CommentForm(Form):
    comment = TextAreaField(u"Your book review",
                            validators=[DataRequired(message=u"The content can not be blank"), Length(1, 1024, message=u"Book review length is limited to 1024 characters or fewer")])
    submit = SubmitField(u"Release")
