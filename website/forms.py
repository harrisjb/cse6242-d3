import flask
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, DecimalField, SubmitField, BooleanField, IntegerField, HiddenField, PasswordField
from wtforms.validators import DataRequired, Regexp, Optional
from decimal import Decimal
import re
import string
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

