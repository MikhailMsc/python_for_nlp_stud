FROM python:3


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD [ "python", "./run_flask_app.py" ]