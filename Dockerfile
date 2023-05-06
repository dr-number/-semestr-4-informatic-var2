###########
# BUILDER #
###########

# pull official base image
FROM python:3.10-slim as builder

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME
RUN mkdir -p $APP_HOME

RUN apt-get update
RUN apt-get -y install libpq-dev gcc wget


# install pip dependencies
# COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

