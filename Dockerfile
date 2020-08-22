# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
  && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirementsdocker.txt .
RUN pip install -r requirementsdocker.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . ./usr/src/app

# change permission
# RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
RUN python usr/src/app/manage.py migrate