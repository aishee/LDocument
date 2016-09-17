# -*- coding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, URL
from flask.ext.pagedown.fields import PageDownField
from flask.ext.wtf.file import FileField, FileAllowed
from app import avatars


class EditProfileForm(Form):
    name = StringField(u'Username', validators=[DataRequired(message=u"The forgot to fill in the!"), Length(1, 64, message=u"A length of 1-64 characters")])
    major = StringField(u'Major', validators=[Length(0, 128, message=u"A length of 0-128 characters")])
    headline = StringField(u'Introduce', validators=[Length(0, 32, message=u"A length of 32 characters or less")])
    about_me = PageDownField(u"Personal profile")
    submit = SubmitField(u"Save Changes")


class AvatarEditForm(Form):
    avatar_url = StringField('', validators=[Length(1, 100, message=u"Length limit of 100 characters or less"), URL(message=u"Please fill in the correct URL")])
    submit = SubmitField(u"Save")


class AvatarUploadForm(Form):
    avatar = FileField('', validators=[FileAllowed(avatars, message=u"Only allowed to upload pictures")])
