# Use an official Python runtime as the base image
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

# Copy the current directory contents into the container at /app
COPY . /code

# Set the working directory inside the container
WORKDIR /code

# Install the dependencies specified in requirements.txt
RUN pip install -r requirements.txt

COPY . /code