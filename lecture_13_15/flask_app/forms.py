from flask_wtf import FlaskForm
from wtforms import (
    widgets, StringField, SubmitField, EmailField,
    IntegerField, SelectField, SelectMultipleField, TextAreaField
)
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SurveyForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    education = SelectField('Ваше образование',
                            choices=[('детский сад', 'детский сад'), ('9 классов школы', '9 классов школы'),
                                     ('11 классов школы', '11 классов школы'),
                                     ('среднее специальное', 'среднее специальное'),
                                     ('неоконченное высшее', 'неоконченное высшее'),
                                     ('бакалавриат / специалитет', 'бакалавриат / специалитет'),
                                     ('магистратура', 'магистратура'),
                                     ('аспирантура', 'аспирантура'),
                                     ('кандидат наук', 'кандидат наук'),
                                     ('доктор наук', 'доктор наук'),
                                     ]
                            )
    languages = MultiCheckboxField('Какие языки программирования вы знаете?',
                            choices=[('C', 'C'), ('C++', 'C++'), ('R', 'R'), ('Java', 'Java'), ('py', 'Python'),
                                     ('JavaScript', 'JavaScript Text')]
                            )
    comment = TextAreaField('Комментарий')
    submit = SubmitField('Сохранить')
