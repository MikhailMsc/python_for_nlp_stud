## Домашнее задание 4: Краулер

**Дедлайн:**

**212 -- 15 декабря 23:59**


**Важное: работы принимаются строго в ipynb (не скрипт, не скрипт в ячейке ipynb)**

**Задание**

Вам нужно обкачать новости (или статьи) с сайтов газет или аналогичных онлайн-изданий и поместить это в базу. **Точная формулировка по необходимым данным будет от преподавателя в зависимости от информации на выбранном сайте**

**Данные**

Надо записаться в таблицу, чтобы ваши газеты не повторялись: [таблица](https://docs.google.com/spreadsheets/d/124v-PqwLM2UQPjYJtOCgZ48IqRgBxTZlaTzxShHjOB8/edit?usp=sharing)

**Совет по выбору**

Легче всего, если:

- навигация по страницам/выпускам/датам - под/над есть что-то вроде 1, 2, 3, ... 45, 46 по которым переход на страницы (например, Медуза - это плохой вариант, там кнопка "показать еще", The Village хороший вариант - там внизу навигация по страницам)
- в адресной строке будет навигация вроде <адрес>p=2 или  <адрес>page=2 или что-то такое, например, как на фикбуке ("https://ficbook.net/fanfiction/no_fandom/originals?p=2"). Это можно посмотреть, перейдя на вторую страницу интересующей ленты новостей.
- региональная газета - там попроще сайт и будет легче доставать информацию (у топовых газет много всего на скриптах и там сложно или невозможно доставать информацию)

**Схема базы**:

(пример)

- таблица для текстов:
    - id
    - дата (отдельно поля год месяц день)
    - текст новости
    - категория (спорт, политика), если возможно
    - количество просмотров, если возможно
- таблица для какой-то дополнительной информации (уточнит преподаватель по вашему сайту), например как в семинаре: id, текст тега
- таблица связывающая две предыдущие, например: id, id_text, id_tag

**Минимальные требования по объему: 1000 постов/новостей/статей**, если не будет решено, что сайт сложный и можно меньше

**На 6 баллов**:

1. Выполнены требования по кол-ву постов
3. Данные сохраняются в базу данных, есть описание, какие в ней поля и связи
4. Посчитайте статистику:
   - самые популярные теги (или другой параметр в вашей газете)


**На 8 баллов**

1. Код программы разделен на логичные функции (а не все подряд в цикле)
2. Есть обработка ошибок (try-except), куда-то сохраняется информация о том, какие посты не скачались и какая ошибка
4. С помощью TF-IDF выделите ключевые слова для каждой новости

**На 9 баллов**

Используя sklearn.metrics.pairwise.cosine_similarity, посчитайте близость между tf-idf векторами текстов и для каждого текста найдите 3 похожих. Сохраните пары в БД, в тетрадке приведите результаты для 3 текстов (можно вывести только начало текста).

**На 10 баллов**

Посмотрите, как запустить Selenium в конспекте и попробуйте погуглить, как можно скроллить страницу с помощью него [(например, скролл как на этом сайте)](https://openedu.ru/course/). Возьмите любой сайт и напишите код, который будет скроллить его страницу.

**Подсказка** используйте библиотеку tqdm для удобного отслеживания прогресса

**Чек-лист**

1. Тетрадка с кодом
2. **Получившаяся база данных (она должна открываться и быть заполненной!)**, проверьте на адекватность хотя бы по размеру файла - он должен быть как минимм несколько мегабайт.

Если у вас есть вопросы, задавайте в чате или пишите преподавателям

[**Ссылка на GiHub Classroom**](https://classroom.github.com/a/c4H30Uhs)
