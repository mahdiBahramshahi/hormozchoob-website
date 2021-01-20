from flask_wtf import FlaskForm
from wtforms import FileField , SelectField , StringField
from wtforms.validators import DataRequired


class FileUploadForm(FlaskForm):
    project_name = StringField()
    height =StringField(validators=[DataRequired()])
    width = StringField(validators=[DataRequired()])
    qty = StringField(validators=[DataRequired()])
    pvc = SelectField(u'pvc count', choices=[('pvc بدون', 'pvc بدون'),('یک طول', 'یک طول'), ('دو طول', 'دو طول'), ('چهار طرف', 'چهار طرف') , ('یک عرض', 'یک عرض')])
    file = FileField()

