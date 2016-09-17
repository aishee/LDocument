# -*- coding:utf-8 -*-
from app import db
from app.models import User
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(Form):
    email = StringField('Email',
                        validators=[DataRequired(message=u"The forgot to fill in the!"), Length(1, 64), Email(message=u"Are you sure this is Email ?")])
    password = PasswordField(u'Password', validators=[DataRequired(message=u"The forgot to fill in the!"), Length(6, 32)])
    remember_me = BooleanField(u"Keep me signed in", default=True)
    submit = SubmitField(u'Sign in')


class RegistrationForm(Form):
    email = StringField('Email',
                        validators=[DataRequired(message=u"The forgot to fill in the!"), Length(1, 64), Email(message=u"Are you sure this is Email ?")])
    name = StringField(u'Username', validators=[DataRequired(message=u"The forgot to fill in the!"), Length(1, 64)])
    password = PasswordField(u'Password',
                             validators=[DataRequired(message=u"The forgot to fill in the!"), EqualTo('password2', message=u'Passwords must match'),
                                         Length(6, 32)])
    password2 = PasswordField(u'Confirm password again', validators=[DataRequired(message=u"The forgot to fill in the!")])
    submit = SubmitField(u'Register')

    def validate_email(self, filed):
        if User.query.filter(db.func.lower(User.email) == db.func.lower(filed.data)).first():
            raise ValidationError(u'The Email is already registered')


class ChangePasswordForm(Form):
    old_password = PasswordField(u'Old password', validators=[DataRequired(message=u"The forgot to fill in the!")])
    new_password = PasswordField(u'New password', validators=[DataRequired(message=u"The forgot to fill in the!"),
                                                     EqualTo('confirm_password', message=u'Passwords must match'),
                                                     Length(6, 32)])
    confirm_password = PasswordField(u'Confirm the new password', validators=[DataRequired(message=u"The forgot to fill in the!")])
    submit = SubmitField(u"Save Password")

    def validate_old_password(self, filed):
        from flask.ext.login import current_user
        if not current_user.verify_password(filed.data):
            raise ValidationError(u'Old password is wrong')
