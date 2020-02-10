from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SubmitField, FileField
from wtforms.fields.html5 import URLField, EmailField
from wtforms.validators import DataRequired

# csrf = CSRFProtect()


class UploadFileForm(FlaskForm):
    file = FileField()

    submit = SubmitField('Submit')
