FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define work dir
WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

# Copy reqs
COPY ./requirements.txt requirements.txt
# Install reqs
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app
# add all stuff




## Run python  manage.py
#CMD python manage.py runserver