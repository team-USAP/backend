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
RUN pip install --upgrade pip --no-cache-dir
COPY ./requirementsdocker.txt .
RUN pip install -r requirementsdocker.txt --no-cache-dir

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
RUN chmod +rwx entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]