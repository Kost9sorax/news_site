FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /site
COPY . /site/
WORKDIR /site

COPY ./requirements.txt usr/src/requirements/txt

RUN pip install --upgrade pip
RUN pip install -r /usr/src/requirements/txt


ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
