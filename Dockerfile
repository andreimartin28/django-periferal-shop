FROM python:3.11.9-bookworm
WORKDIR /shop

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update

RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . /shop

ENTRYPOINT ["gunicorn", "shop.wsgi:application"]
