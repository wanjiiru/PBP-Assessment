from flask_wtf import FlaskForm, CSRFProtect, CsrfProtect
from wtforms import SubmitField, FileField


class UploadFileForm(FlaskForm):
    file = FileField()

    submit = SubmitField('Submit')
