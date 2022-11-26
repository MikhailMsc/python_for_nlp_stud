import pandas as pd
from flask_app import app #, db
from flask import render_template, redirect
# from flask_app.forms import SurveyForm
# from flask_app.models import Anketa
import pretty_html_table


@app.route('/')  # Задаем ответ сервера при входе в корень сайта.
def index():
    return 'Hello, world!'


@app.route('/ru')
def hi_ru():
    return 'Привет мир!'


@app.route('/ukr')
def hi_ukr():
    return 'Привіт світ!'


# @app.route('/')  # Задаем ответ сервера при входе в корень сайта.
# def main():
#     html_code = '''
#     <!doctype html>
#     <html>
#         <head>
#             <title>Главная страница</title>
#         </head>
#         <body>
#             <h1>Добро пожаловать!</h1>
#             <p>Здесь Вы можете пройти опрос или посмотреть результаты.</p>
#             <button type="button">Пройти опрос</button>
#             <button type="button">Посмотреть результаты</button>
#         </body>
#     </html>'''
#     return html_code


@app.route('/')
def main():
    return render_template('main.html')


# @app.route('/anketa')
# def opros():
#     return render_template('tmp_opros_result.html', title='Опрос', text_info='Здесь будет опрос.')


# @app.route('/result')
# def result():
#     return render_template('tmp_opros_result.html', title='Результаты', text_info='Здесь будут результаты опроса.')


# @app.route('/anketa')
# def opros():
#     return render_template('opros.html')


@app.route('/anketa', methods=['POST', 'GET'])
def opros():
    form = SurveyForm()
    if form.validate_on_submit():
        # print('Has DATA')
        new_anketa = Anketa(
            username=form.username.data,
            email=form.email.data,
            age=form.age.data,
            education=form.education.data,
            languages=', '.join(form.languages.data),
            comment=form.comment.data
        )
        db.session.add(new_anketa)
        db.session.commit()
        return redirect('/')
    return render_template('opros2.html', form=form)

# @app.route('/result')
# def result():
#     all_ankets = Anketa.query.all()
#     return render_template('result.html', rows=all_ankets)


@app.route('/result')
def result():
    all_ankets = Anketa.query.all()
    all_ankets = [(v.username, v.email, v.age, v.education, v.languages, v.comment)
                  for v in all_ankets]
    all_ankets = pd.DataFrame(all_ankets,
                              columns=['Имя', 'Email', 'Возраст', 'Образование',
                                       'Языки программирования', 'Комментарий']
                              )
    all_ankets = pretty_html_table.build_table(all_ankets, 'blue_light')
    # return render_template('result2.html', html_table=all_ankets)

    with open('flask_app/templates/result2.html', 'r') as f:
        html_code = f.read()
    html_code = html_code.replace('{{ html_table }}', all_ankets)
    return html_code

