FROM python:3

RUN mkdir /news-site
COPY . /news-site/
WORKDIR /news-site

RUN pip install --upgrade pip
RUN pip install django

ENTRYPOINT ['python', 'manage.py']
CMD ['runserver', '0.0.0.0.8000']
